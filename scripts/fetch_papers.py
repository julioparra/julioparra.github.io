#!/usr/bin/env python3
"""Fetch papers from INSPIRE-HEP API and write to _data/papers.yml."""

import json
import os
import re
import urllib.request
import urllib.parse

AUTHOR_BAI = "J.Parra.Martinez.1"
AUTHOR_RECID = 1519679
API_BASE = "https://inspirehep.net/api/literature"
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "_data", "papers.yml")
COAUTHORS_PATH = os.path.join(os.path.dirname(__file__), "..", "_data", "coauthors.yml")
PAGE_SIZE = 100

FIELDS = ",".join([
    "titles",
    "arxiv_eprints",
    "dois",
    "publication_info",
    "authors",
    "preprint_date",
    "texkeys",
    "abstracts",
    "number_of_pages",
])


def fetch_all_papers():
    """Fetch all papers for the author, handling pagination."""
    papers = []
    page = 1
    while True:
        params = urllib.parse.urlencode({
            "sort": "mostrecent",
            "size": PAGE_SIZE,
            "page": page,
            "q": f"a {AUTHOR_BAI}",
            "fields": FIELDS,
        })
        url = f"{API_BASE}?{params}"
        with urllib.request.urlopen(url) as resp:
            data = json.loads(resp.read())

        hits = data.get("hits", {}).get("hits", [])
        if not hits:
            break
        papers.extend(hits)

        total = data.get("hits", {}).get("total", 0)
        if page * PAGE_SIZE >= total:
            break
        page += 1

    return papers


# Words that should keep their capitalization
CAPITALIZED_WORDS = {
    # Proper nouns
    "Einstein", "Feynman", "Minkowskian", "Minkowski", "Flatland",
    "Gliozzi", "Scherk", "Olive", "Raman",
    # Acronyms and initialisms
    "SMEFT", "SYM", "sYM", "IIA", "IIB", "GSO", "SPT", "EFT", "GR",
    "UV", "IR",
}
# Build a lookup: lowercase -> preferred form
_CAPS_LOOKUP = {w.lower(): w for w in CAPITALIZED_WORDS}


def _lowercase_word(word):
    """Lowercase a word, handling hyphenated compounds and exceptions."""
    if "-" in word:
        parts = word.split("-")
        return "-".join(_lowercase_word(p) for p in parts)
    stripped = word.strip(".,;:!?()\"'")
    if stripped.lower() in _CAPS_LOOKUP:
        preferred = _CAPS_LOOKUP[stripped.lower()]
        return word.replace(stripped, preferred)
    if stripped.isupper() and len(stripped) > 1:
        return word
    return word.lower()


def normalize_title_case(title):
    """Convert title to sentence case, preserving exceptions and LaTeX."""
    # Split into LaTeX and non-LaTeX segments
    parts = re.split(r'(\\\(.*?\\\))', title)
    result = []
    is_first_word = True
    after_colon = False

    for part in parts:
        # Don't touch LaTeX segments
        if part.startswith("\\("):
            result.append(part)
            continue

        words = part.split(" ")
        new_words = []
        for word in words:
            if not word:
                new_words.append(word)
                continue

            # Check if this word ends with a colon
            ends_colon = word.endswith(":")

            # Strip punctuation for lookup
            stripped = word.strip(".,;:!?()\"'")

            if is_first_word or after_colon:
                # Keep first word / word after colon, but lowercase after hyphens
                if "-" in word:
                    parts = word.split("-")
                    new_words.append(parts[0] + "-" + "-".join(_lowercase_word(p) for p in parts[1:]))
                else:
                    new_words.append(word)
                is_first_word = False
                after_colon = ends_colon
            else:
                new_words.append(_lowercase_word(word))
                after_colon = ends_colon

        result.append(" ".join(new_words))

    return "".join(result)


def normalize_latex(text):
    """Normalize math markup in titles to \\(...\\) for MathJax."""
    # Strip MathML tags, replacing with plain text content
    text = re.sub(r'<math[^>]*>.*?</math>', lambda m: mathml_to_latex(m.group()), text)
    # Normalize $...$ and $$...$$ to \(...\)
    text = re.sub(r'\$\$(.+?)\$\$', r'\\(\1\\)', text)
    text = re.sub(r'\$(.+?)\$', r'\\(\1\\)', text)
    # Clean up extra spaces inside \(...\)
    text = re.sub(r'\\\(\s+', r'\\(', text)
    text = re.sub(r'\s+\\\)', r'\\)', text)
    # Normalize calligraphic O variants to {\cal O}
    text = text.replace(r'\mathcal{O}', r'{\cal O}')
    text = re.sub(r'\\mathcal\s+O', r'{\\cal O}', text)
    # Replace O(G^n) with {\cal O}(G^n) everywhere
    text = re.sub(r'(?<!\\cal )O\(G\^', r'{\\cal O}(G^', text)
    # Wrap bare {\cal O}(G^n) not already in math delimiters
    text = re.sub(r'(?<!\\[({])\{\\cal O\}\(G\^(\d+)\)', r'\\({\\cal O}(G^\1)\\)', text)
    # Wrap U(1) in math delimiters
    text = re.sub(r'(?<!\\[({])U\(1\)', r'\\(U(1)\\)', text)
    # Strip LaTeX wrapping from R7
    text = text.replace(r'\(\mathrm{R}7\)', 'R7')
    text = text.replace(r'\(R7\)', 'R7')
    # Normalize all N=<number> variants (plain, \cal, \mathcal) to \({\cal N}=<number>\)
    # First, unwrap any already-wrapped variants so we can re-wrap uniformly
    text = re.sub(r'\\\(\\mathcal\s*N\s*=\s*(\d+)\\\)', r'N=\1', text)
    text = re.sub(r'\\\(\{?\\cal N\}?\s*=\s*(\d+)\\\)', r'N=\1', text)
    text = re.sub(r'\\\(N\s*=\s*(\d+)\\\)', r'N=\1', text)
    # Now wrap all plain N=<number> uniformly
    text = re.sub(r'N\s*=\s*(\d+)', r'\\({\\cal N}=\1\\)', text)
    return text


def mathml_to_latex(mathml):
    """Best-effort conversion of simple MathML to LaTeX."""
    # Strip all tags, keeping text content
    text = re.sub(r'<[^>]+>', '', mathml)
    # Wrap in \(...\) if there's any content
    text = text.strip()
    if text:
        return f"\\({text}\\)"
    return ""


def pick_best_title(titles):
    """Pick the best title, preferring arXiv source for clean LaTeX."""
    if not titles:
        return ""
    # Prefer arXiv source
    for t in titles:
        if t.get("source") == "arXiv":
            return normalize_title_case(normalize_latex(t.get("title", "")))
    return normalize_title_case(normalize_latex(titles[0].get("title", "")))


def extract_paper(hit):
    """Extract relevant fields from an API hit."""
    meta = hit.get("metadata", {})
    paper = {}

    # Title — prefer arXiv source for clean LaTeX
    titles = meta.get("titles", [])
    if titles:
        paper["title"] = pick_best_title(titles)

    # Arxiv
    arxiv = meta.get("arxiv_eprints", [])
    if arxiv:
        paper["arxivnumber"] = arxiv[0].get("value", "")
        categories = arxiv[0].get("categories", [])
        if categories:
            paper["arxiv_categories"] = categories

    # DOI
    dois = meta.get("dois", [])
    if dois:
        paper["doi"] = dois[0].get("value", "")

    # Publication info
    pub = meta.get("publication_info", [])
    if pub:
        pub_info = pub[0]
        if "journal_title" in pub_info:
            paper["journal"] = pub_info["journal_title"]
        if "journal_volume" in pub_info:
            paper["journal_volume"] = pub_info["journal_volume"]
        if "artid" in pub_info:
            paper["journal_artid"] = pub_info["artid"]
        if "year" in pub_info:
            paper["publication_year"] = pub_info["year"]

    # Authors
    authors = meta.get("authors", [])
    if authors:
        paper["authors"] = [a.get("full_name", "") for a in authors]

    # Preprint date
    if "preprint_date" in meta:
        paper["preprint_date"] = meta["preprint_date"]

    # INSPIRE texkey
    texkeys = meta.get("texkeys", [])
    if texkeys:
        paper["texkey"] = texkeys[0]

    # Abstract
    abstracts = meta.get("abstracts", [])
    if abstracts:
        paper["abstract"] = abstracts[0].get("value", "")

    # Number of pages
    if "number_of_pages" in meta:
        paper["number_of_pages"] = meta["number_of_pages"]

    return paper


def yaml_escape(s):
    """Escape a string for YAML output."""
    if any(c in s for c in ":{}\n\"\\#[]|>&*!%@`"):
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return s


def write_yaml(papers):
    """Write papers to YAML without external dependencies."""
    lines = []
    for p in papers:
        lines.append(f"- title: {yaml_escape(p.get('title', ''))}")
        if "arxivnumber" in p:
            lines.append(f"  arxivnumber: \"{p['arxivnumber']}\"")
        if "arxiv_categories" in p:
            cats = ", ".join(p["arxiv_categories"])
            lines.append(f"  arxiv_categories: [{cats}]")
        if "doi" in p:
            lines.append(f"  doi: \"{p['doi']}\"")
        if "journal" in p:
            lines.append(f"  journal: \"{p['journal']}\"")
        if "journal_volume" in p:
            lines.append(f"  journal_volume: \"{p['journal_volume']}\"")
        if "journal_artid" in p:
            lines.append(f"  journal_artid: \"{p['journal_artid']}\"")
        if "publication_year" in p:
            lines.append(f"  publication_year: {p['publication_year']}")
        if "authors" in p:
            lines.append("  authors:")
            for author in p["authors"]:
                lines.append(f"    - \"{author}\"")
        if "preprint_date" in p:
            lines.append(f"  preprint_date: \"{p['preprint_date']}\"")
        if "texkey" in p:
            lines.append(f"  texkey: \"{p['texkey']}\"")
        if "abstract" in p:
            lines.append(f"  abstract: {yaml_escape(p['abstract'])}")
        if "number_of_pages" in p:
            lines.append(f"  number_of_pages: {p['number_of_pages']}")

    output = "\n".join(lines) + "\n"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        f.write(output)

    print(f"Wrote {len(papers)} papers to {OUTPUT_PATH}")


def extract_coauthors(raw_papers):
    """Extract unique coauthors from raw API results, excluding self.

    Papers arrive most-recent-first from the API, so the first time we
    encounter a coauthor is their most recent collaboration date.
    Duplicates are handled by only recording each recid once.
    """
    coauthors = {}
    for hit in raw_papers:
        date = hit.get("metadata", {}).get("preprint_date", "")
        for author in hit.get("metadata", {}).get("authors", []):
            recid = author.get("recid")
            if not recid or recid == AUTHOR_RECID:
                continue
            if recid not in coauthors:
                full_name = author.get("full_name", "")
                # Convert "Last, First" to "First Last"
                if ", " in full_name:
                    last, first = full_name.split(", ", 1)
                    full_name = f"{first} {last}"
                coauthors[recid] = {
                    "name": full_name,
                    "recid": recid,
                    "last_active": date,
                }
    # Sort by most recent collaboration date (descending)
    return sorted(coauthors.values(),
                  key=lambda a: a["last_active"], reverse=True)


def write_coauthors_yaml(coauthors):
    """Write coauthors to YAML."""
    lines = []
    for c in coauthors:
        lines.append(f"- name: \"{c['name']}\"")
        lines.append(f"  inspire_url: \"https://inspirehep.net/authors/{c['recid']}\"")
    output = "\n".join(lines) + "\n"

    os.makedirs(os.path.dirname(COAUTHORS_PATH), exist_ok=True)
    with open(COAUTHORS_PATH, "w") as f:
        f.write(output)

    print(f"Wrote {len(coauthors)} coauthors to {COAUTHORS_PATH}")


def main():
    print(f"Fetching papers for {AUTHOR_BAI}...")
    raw_papers = fetch_all_papers()
    print(f"Fetched {len(raw_papers)} papers from INSPIRE-HEP")

    papers = [extract_paper(hit) for hit in raw_papers]
    papers = [p for p in papers if "arxivnumber" in p]
    write_yaml(papers)

    coauthors = extract_coauthors(raw_papers)
    write_coauthors_yaml(coauthors)


if __name__ == "__main__":
    main()

---
layout: default
--- 
<div class="row">
<div class="col-4 col-sm-4 col-md-5">
<img src="/images/julio.jpg">  
</div>
<div class="col-8 col-sm-8 col-md-4">
Julio Parra-Martinez <br> 
Permanent professor <a href="/cv_short.pdf"> (CV) </a> <br>
<a href="https://www.ihes.fr/en/">IHES </a> <br>
<a href="https://www.ihes.fr/en/directions/"> 35 Route de Chartres,  <br>
91440, Bures-sur-Yvette,   <br>
France</a>  <br>
Office: 0N5 <br>
Contact: <a href="mailto:julio@ihes.fr"> julio (at) ihes.fr</a> <br>
<!--

<a href="/contact/index.html">Contact </a>
<D-c>-->
</div>
<div class="col-5 col-sm-5 col-md-3">
<img src="/images/IHES-logo-3-filets.png" class="float-sm-center float-md-right" style="width:100%">  
</div>
</div>
<br>

***




<!--

### My group ###

Jonah Berean-Dutcher (PhD student, UBC) <br>
Rachel Wang (PhD student, UBC) <br>
Vincent He (Masters student, UBC) <br>
<br>
Past members:
Francesco Calisto (Summer student 2023 -> PhD Student at Caltech)
-->


<br>

{% capture datenow %}{{'now' | date: '%s'}}{% endcapture %}

### Research ###

I am a theoretical physicist working on quantum field theory, scattering amplitudes, gravitation, effective field theories and string theory. 


<div style="margin-top: 1.3em"></div>

<h4> Upcoming seminars, talks, lectures, etc </h4>

{% for talk in site.data.talks reversed %}
{% capture talkdate %}{{ talk.date | date: '%s'}}{% endcapture %}
  {% if talkdate > datenow %}
  <div class="row">
     <div class="col-11"> {{ talk.date | date: "%m/%Y" }}: {% if talk.link != nil %} <a href="{{ talk.link }}">{{ talk.name }}</a>{% else %}{{ talk.name }}{% endif %}{% if talk.institution != nil %}, {{ talk.institution }}{% endif %}{% if talk.location != nil %}, {{ talk.location }} {% endif %} </div> 
  </div>
  {% endif %}
{% endfor %}

<div style="margin-top: 1.3em"></div>

  <div class="row">
    <div class="col-md-8 col-0"> <h4> <span id="all-publications-recent">Recent</span> publications {% if site.data.papers.size > 10 %}<small style="font-weight: 300">(<a href="#" onclick="return toggleSection('all-publications', this);">see all</a>)</small>{% endif %}</h4> </div>
    <div class="col-md-4 col-12" style="vertical-align: middle; text-align:right"> (<a href="http://inspirehep.net/author/profile/J.Parra.Martinez.1">INSPIRE</a>, <a href="https://scholar.google.com/citations?user=oASELmIAAAAJ&hl=en&authuser=1">Google Scholar</a>)</div>
  </div>
  {% for paper in site.data.papers %}
  {% if forloop.index == 11 %}<div id="all-publications" style="display:none">{% endif %}
  <div class="row">
    <div class="col-md-10 col-0"> {{ paper.title }} </div>
    <div class="col-md-2 col-12" style="text-align:right"> <a href="http://arxiv.org/abs/{{ paper.arxivnumber }}">arXiv:{{ paper.arxivnumber }}</a> </div>
  </div>
  {% endfor %}
  {% if site.data.papers.size > 10 %}</div>{% endif %}
<br>


<h4> <span id="all-conferences-recent">Recent</span> conference talks {% assign conf_count = 0 %}{% for talk in site.data.talks %}{% capture talkdate %}{{ talk.date | date: '%s'}}{% endcapture %}{% if talk.type == "conference" or talk.type == "workshop" %}{% if talkdate < datenow %}{% assign conf_count = conf_count | plus: 1 %}{% endif %}{% endif %}{% endfor %}{% if conf_count > 10 %}<small style="font-weight: 300">(<a href="#" onclick="return toggleSection('all-conferences', this);">see all</a>)</small>{% endif %}</h4>

{% assign conf_count = 0 %}
{% for talk in site.data.talks %}
{% capture talkdate %}{{ talk.date | date: '%s'}}{% endcapture %}
  {% if talk.type == "conference" or talk.type == "workshop" %}
  {% if talkdate < datenow %}
  {% assign conf_count = conf_count | plus: 1 %}
  {% if conf_count == 11 %}<div id="all-conferences" style="display:none">{% endif %}
  <div class="row">
    <div class="col-11"> {{ talk.date | date: "%m/%Y" }}: {% if talk.link != nil %} <a href="{{ talk.link }}">{{ talk.name }}</a>{% else %}{{ talk.name }}{% endif %}{% if talk.institution != nil %}, {{ talk.institution }}{% endif %}{% if talk.location != nil %}, {{ talk.location }} {% endif %} </div> 
    {% if talk.video != nil %}
    <div class="col-1" style="text-align:right">(<a href="{{ talk.video }}">video</a>)</div>
    {% endif %}
  </div>
  {% endif %}
  {% endif %}
{% endfor %}
{% if conf_count > 10 %}</div>{% endif %}

<br>

<h4> <span id="all-seminars-recent">Recent</span> seminars, colloquia, etc {% assign sem_pre = 0 %}{% for talk in site.data.talks %}{% capture talkdate %}{{ talk.date | date: '%s'}}{% endcapture %}{% if talkdate < datenow and talk.type == "seminar" or talk.type == "colloquium" %}{% assign sem_pre = sem_pre | plus: 1 %}{% endif %}{% endfor %}{% if sem_pre > 10 %}<small style="font-weight: 300">(<a href="#" onclick="return toggleSection('all-seminars', this);">see all</a>)</small>{% endif %}</h4>

{% capture datenow %}{{'now' | date: '%s'}}{% endcapture %}
{% assign sem_count = 0 %}
{% for talk in site.data.talks %}
{% capture talkdate %}{{ talk.date | date: '%s'}}{% endcapture %}
  {% if talkdate < datenow and talk.type == "seminar" or talk.type == "colloquium" %}
  {% assign sem_count = sem_count | plus: 1 %}
  {% if sem_count == 11 %}<div id="all-seminars" style="display:none">{% endif %}
  <div class="row">
     <div class="col-11"> {{ talk.date | date: "%m/%Y" }}: {% if talk.link != nil %} <a href="{{ talk.link }}">{{ talk.name }}</a>{% else %}{{ talk.name }}{% endif %}{% if talk.institution != nil %}, {{ talk.institution }}{% endif %}{% if talk.location != nil %}, {{ talk.location }} {% endif %} </div>  
    {% if talk.video != nil %}
    <div class="col-1" style="text-align:right">(<a href="{{ talk.video }}">video</a>)</div>
    {% endif %}
  </div>
  {% endif %}
{% endfor %}
{% if sem_count > 10 %}</div>{% endif %}

<br>

<h4> <span id="all-lectures-recent">Recent</span> lectures {% assign lect_pre = 0 %}{% for talk in site.data.talks %}{% capture talkdate %}{{ talk.date | date: '%s'}}{% endcapture %}{% if talkdate < datenow and talk.type == "lectures" %}{% assign lect_pre = lect_pre | plus: 1 %}{% endif %}{% endfor %}{% if lect_pre > 10 %}<small style="font-weight: 300">(<a href="#" onclick="return toggleSection('all-lectures', this);">see all</a>)</small>{% endif %}</h4>

{% capture datenow %}{{'now' | date: '%s'}}{% endcapture %}
{% assign lect_count = 0 %}
{% for talk in site.data.talks %}
{% capture talkdate %}{{ talk.date | date: '%s'}}{% endcapture %}
  {% if talkdate < datenow and talk.type == "lectures" %}
  {% assign lect_count = lect_count | plus: 1 %}
  {% if lect_count == 11 %}<div id="all-lectures" style="display:none">{% endif %}
  <div class="row">
    <div class="col-11"> {{ talk.date | date: "%m/%Y" }}: {% if talk.link != nil %} <a href="{{ talk.link }}">{{ talk.name }}</a>{% else %}{{ talk.name }}{% endif %}{% if talk.institution != nil %}, {{ talk.institution }}{% endif %}{% if talk.location != nil %}, {{ talk.location }} {% endif %} </div> 
    {% if talk.video != nil %}
    <div class="col-1" style="text-align:right">(<a href="{{ talk.video }}">video</a>)</div>
    {% endif %}
  </div>
  {% endif %}
{% endfor %}
{% if lect_count > 10 %}</div>{% endif %}

<br>

#### My collaborators ####

{% for coauthor in site.data.coauthors limit:10 %}<a href="{{ coauthor.inspire_url }}">{{ coauthor.name }}</a>, {% endfor %}<a href="#" onclick="document.getElementById('all-coauthors').style.display='inline'; this.style.display='none'; return false;">more...</a><span id="all-coauthors" style="display:none">{% for coauthor in site.data.coauthors offset:10 %}<a href="{{ coauthor.inspire_url }}">{{ coauthor.name }}</a>{% unless forloop.last %}, {% endunless %}{% endfor %}</span>

<br>

<div class="row">
    <div class="col-6">  </div>
    <div class="col-6" style="text-align:right">  Updated: {{ 'now' | date: "%d/%m/%Y"}} </div>
</div>



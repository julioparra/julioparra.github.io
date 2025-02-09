---
layout: default
--- 
<div class="row">
<div class="col-4 col-sm-4 col-md-5">
<img src="/images/julio.jpg">  
</div>
<div class="col-8 col-sm-8 col-md-4">
Julio Parra-Martinez <br> 
Permanent professor <br>
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

I am a theoretical physicist working on quantum field theory, scattering amplitudes, gravitation, effective field theories and string theory. 
<br>

### My group ###

Jonah Berean-Dutcher (PhD student, UBC) <br>
Rachel Wang (PhD student, UBC) <br>
Vincent He (Masters student, UBC) <br>
<br>
Past members:
Francesco Calisto (Summer student 2023 -> PhD Student at Caltech)
-->


<br>

### Research ###

  <div class="row">
    <div class="col-md-8 col-0"> <h4> Publications </h4> </div>
    <div class="col-md-4 col-12" style="vertical-align: middle; text-align:right"> (<a href="http://inspirehep.net/author/profile/J.Parra.Martinez.1">INSPIRE</a>, <a href="https://scholar.google.com/citations?user=oASELmIAAAAJ&hl=en&authuser=1">Google Scholar</a>)</div>
  </div>
  {% for paper in site.data.papers %}
  <div class="row">
    <div class="col-md-10 col-0"> {{ paper.title }} </div>
    <div class="col-md-2 col-12" style="text-align:right"> <a href="http://arxiv.org/abs/{{ paper.arxivnumber }}">arXiv:{{ paper.arxivnumber }}</a> </div>
  </div>
  {% endfor %}
 
<br>


{% capture datenow %}{{'now' | date: '%s'}}{% endcapture %}

#### Upcoming Seminars, Talks, etc ####

{% for talk in site.data.talks reversed %}
{% capture talkdate %}{{ talk.date | date: '%s'}}{% endcapture %}
  {% if talk.type == "conference" or talk.type == "workshop" or talk.type == "seminar" %}
  {% if talkdate > datenow %}
  <div class="row">
     <div class="col-11"> {{ talk.date | date: "%m/%Y" }}: {% if talk.link != nil %} <a href="{{ talk.link }}">{{ talk.name }}</a>{% else %}{{ talk.name }}{% endif %}{% if talk.institution != nil %}, {{ talk.institution }}{% endif %}{% if talk.location != nil %}, {{ talk.location }} {% endif %} </div> 
  </div>
  {% endif %}
  {% endif %}
{% endfor %}

<br>

#### Upcoming Lectures ####

{% for talk in site.data.talks reversed %}
{% capture talkdate %}{{ talk.date | date: '%s'}}{% endcapture %}
  {% if talkdate > datenow and talk.type == "lectures" %}
  <div class="row">
     <div class="col-11"> {{ talk.date | date: "%m/%Y" }}: {% if talk.link != nil %} <a href="{{ talk.link }}">{{ talk.name }}</a>{% else %}{{ talk.name }}{% endif %}{% if talk.institution != nil %}, {{ talk.institution }}{% endif %}{% if talk.location != nil %}, {{ talk.location }} {% endif %} </div> 
  </div>
  {% endif %}
  {% endif %}
{% endfor %}

<br>


#### Conference Talks ####

{% for talk in site.data.talks %}
{% capture talkdate %}{{ talk.date | date: '%s'}}{% endcapture %}
  {% if talk.type == "conference" or talk.type == "workshop" %}
  {% if talkdate < datenow %}
  <div class="row">
    <div class="col-11"> {{ talk.date | date: "%m/%Y" }}: {% if talk.link != nil %} <a href="{{ talk.link }}">{{ talk.name }}</a>{% else %}{{ talk.name }}{% endif %}{% if talk.institution != nil %}, {{ talk.institution }}{% endif %}{% if talk.location != nil %}, {{ talk.location }} {% endif %} </div> 
    {% if talk.video != nil %}
    <div class="col-1" style="text-align:right">(<a href="{{ talk.video }}">video</a>)</div>
    {% endif %}
  </div>
  {% endif %}
  {% endif %}
{% endfor %}

<br>

#### Lectures ####

{% capture datenow %}{{'now' | date: '%s'}}{% endcapture %}
{% for talk in site.data.talks %}
{% capture talkdate %}{{ talk.date | date: '%s'}}{% endcapture %}
  {% if talkdate < datenow and talk.type == "lectures" %}
  <div class="row">
    <div class="col-11"> {{ talk.date | date: "%m/%Y" }}: {% if talk.link != nil %} <a href="{{ talk.link }}">{{ talk.name }}</a>{% else %}{{ talk.name }}{% endif %}{% if talk.institution != nil %}, {{ talk.institution }}{% endif %}{% if talk.location != nil %}, {{ talk.location }} {% endif %} </div> 
    {% if talk.video != nil %}
    <div class="col-1" style="text-align:right">(<a href="{{ talk.video }}">video</a>)</div>
    {% endif %}
  </div>
  {% endif %}
{% endfor %}

<br>

#### Seminars, colloquia, etc ####

{% capture datenow %}{{'now' | date: '%s'}}{% endcapture %}
{% for talk in site.data.talks %}
{% capture talkdate %}{{ talk.date | date: '%s'}}{% endcapture %}
  {% if talkdate < datenow and talk.type == "seminar" %}
  <div class="row">
     <div class="col-11"> {{ talk.date | date: "%m/%Y" }}: {% if talk.link != nil %} <a href="{{ talk.link }}">{{ talk.name }}</a>{% else %}{{ talk.name }}{% endif %}{% if talk.institution != nil %}, {{ talk.institution }}{% endif %}{% if talk.location != nil %}, {{ talk.location }} {% endif %} </div>  
    {% if talk.video != nil %}
    <div class="col-1" style="text-align:right">(<a href="{{ talk.video }}">video</a>)</div>
    {% endif %}
  </div>
  {% endif %}
{% endfor %}

<br>

<div class="row">
    <div class="col-6">  </div>
    <div class="col-6" style="text-align:right">  Updated: {{ 'now' | date: "%d/%m/%Y"}} </div>
</div>



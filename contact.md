---
layout: page
title: Contact
permalink: /contact/
order: 100
---


<form accept-charset="UTF-8" action="http://formspree.io/jparra@physics.ucla.edu" method="POST">
  <div class="row">
    <div class="col-lg-6">
     <div class="form-group">
      <div class="input-group">
        <span class="input-group-addon" id="basic-addon1">
        <span class="glyphicon glyphicon-user" aria-hidden="true"></span></span>
        <input type="text" class="form-control" placeholder="Name" name="name" aria-describedby="basic-addon1">
      </div>
      </div>
    </div>

    <div class="col-lg-6">
     <div class="form-group">
      <div class="input-group">
        <span class="input-group-addon" id="basic-addon1">@</span>
        <input type="text" class="form-control" placeholder="Email" name="_replyto" aria-describedby="basic-addon1">
      </div>
      </div>
    </div>

  </div>

  <div class="form-group">
    <textarea class="form-control" id="exampleTextarea" name="subject" rows="1" placeholder="Subject" style="resize:none"></textarea>
  </div>

  <div class="form-group">
    <textarea class="form-control" id="exampleTextarea" name="body" rows="8"></textarea>
  </div>

  <div class="row">
     <div class="col-xs-12 col-md-10">
       <div class="form-group row">
         <label for="exampleSelect1" class="col-xs-12 col-sm-7 col-md-5 col-form-label"> Your message is concerning:</label>
         <div class="col-xs-12 col-sm-5 col-md-3">
           <select class="form-control" id="exampleSelect1" name="Topic">
	     <option>-----------</option>
             <option>Research</option>
             <option>Teaching</option>
             <option>Other</option>
           </select>
         </div>
      </div>
    </div>
    <div class="col-xs-12 col-md-2">
       <button type="submit" class="btn btn-primary pull-xs-right col-xs-12" value="Send">Send</button>
    </div>
  </div>




</form>

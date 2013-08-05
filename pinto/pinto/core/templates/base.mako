<!DOCTYPE html>
<!--[if IE 8]> <html class="no-js lt-ie9" lang="en" > <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js" lang="en" > <!--<![endif]-->

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Pinto - Because why not.</title>


  <link rel="stylesheet" href="${request.static_url('pinto:static/stylesheets/app.css')}">
  <script src="${request.static_url('pinto:static/javascripts/vendor/jquery.js')}" type="text/javascript" charset="utf-8"></script>
  <script src="${request.static_url('pinto:static/javascripts/vendor/custom.modernizr.js')}"></script>

</head>
<body>
<!-- Nav Bar -->

  <div class="row">
    <div class="large-12 columns">
      <div class="nav-bar right">
       <ul class="button-group">
         <li><a href="#" class="button">Link 1</a></li>
         <li><a href="#" class="button">Link 2</a></li>
         <li><a href="#" class="button">Link 3</a></li>
         <li><a href="#" class="button">Link 4</a></li>
        </ul>
      </div>
      <h1>Blog <small>This is my blog. It's awesome.</small></h1>
      <hr />
    </div>
  </div>

  <!-- End Nav -->

  <!-- Main Page Content and Sidebar -->

  <div class="row">

    <!-- Main Blog Content -->
    <div class="large-9 columns" role="content">

    ${next.body()}

    </div>

 <!-- Sidebar -->

    <aside class="large-3 columns">

      <h5>Categories</h5>
      <ul class="side-nav">
        <li><a href="#">News</a></li>
        <li><a href="#">Code</a></li>
        <li><a href="#">Design</a></li>
        <li><a href="#">Fun</a></li>
        <li><a href="#">Weasels</a></li>
      </ul>

      <div class="panel">
        <h5>Featured</h5>
        <p>Pork drumstick turkey fugiat. Tri-tip elit turducken pork chop in. Swine short ribs meatball irure bacon nulla pork belly cupidatat meatloaf cow.</p>
        <a href="#">Read More &rarr;</a>
      </div>

    </aside>

    <!-- End Sidebar -->
  </div>

  <!-- End Main Content and Sidebar -->

  <!-- Footer -->

  <footer class="row">
    <div class="large-12 columns">
      <hr />
      <div class="row">
        <div class="large-6 columns">
          <p>&copy; Copyright no one at all. Go to town.</p>
        </div>
        <div class="large-6 columns">
          <ul class="inline-list right">
            <li><a href="#">Link 1</a></li>
            <li><a href="#">Link 2</a></li>
            <li><a href="#">Link 3</a></li>
            <li><a href="#">Link 4</a></li>
          </ul>
        </div>
      </div>
    </div>
  </footer>
</body>
</html>

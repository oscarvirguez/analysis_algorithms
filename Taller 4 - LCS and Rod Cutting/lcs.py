
<!DOCTYPE HTML>
<html>

<head>
    <meta charset="utf-8">

    <title>lcs.py (editing)</title>
    <link rel="shortcut icon" type="image/x-icon" href="/user/rajaquep/static/base/images/favicon.ico?v=30780f272ab4aac64aa073a841546240">
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <link rel="stylesheet" href="/user/rajaquep/static/components/jquery-ui/themes/smoothness/jquery-ui.min.css?v=60f0405edd95e7135ec6a0bbc36d1385" type="text/css" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    
<link rel="stylesheet" href="/user/rajaquep/static/components/codemirror/lib/codemirror.css?v=1c26f7d1f30cbcc58982178f588906d5">
<link rel="stylesheet" href="/user/rajaquep/static/components/codemirror/addon/dialog/dialog.css?v=910c1893a275073be1f80f32b77cd5a4">

    <link rel="stylesheet" href="/user/rajaquep/static/style/style.min.css?v=3938f8554ee5d9c06ee2fb644a20bec4" type="text/css"/>
    

    <link rel="stylesheet" href="/user/rajaquep/static/custom/custom.css?v=900035aa0c126bb85df55c5b3e51b6f1" type="text/css" />
    <script src="/user/rajaquep/static/components/es6-promise/promise.min.js?v=f004a16cb856e0ff11781d01ec5ca8fe" type="text/javascript" charset="utf-8"></script>
    <script src="/user/rajaquep/static/components/requirejs/require.js?v=640929dac3c23a448d2eebc37bc32062" type="text/javascript" charset="utf-8"></script>
    <script>
      require.config({
          
          urlArgs: "v=20161219030703",
          
          baseUrl: '/user/rajaquep/static/',
          paths: {
            nbextensions : '/user/rajaquep/nbextensions',
            kernelspecs : '/user/rajaquep/kernelspecs',
            underscore : 'components/underscore/underscore-min',
            backbone : 'components/backbone/backbone-min',
            jquery: 'components/jquery/jquery.min',
            bootstrap: 'components/bootstrap/js/bootstrap.min',
            bootstraptour: 'components/bootstrap-tour/build/js/bootstrap-tour.min',
            jqueryui: 'components/jquery-ui/ui/minified/jquery-ui.min',
            moment: 'components/moment/moment',
            codemirror: 'components/codemirror',
            termjs: 'components/term.js/src/term',
          },
          shim: {
            underscore: {
              exports: '_'
            },
            backbone: {
              deps: ["underscore", "jquery"],
              exports: "Backbone"
            },
            bootstrap: {
              deps: ["jquery"],
              exports: "bootstrap"
            },
            bootstraptour: {
              deps: ["bootstrap"],
              exports: "Tour"
            },
            jqueryui: {
              deps: ["jquery"],
              exports: "$"
            }
          }
      });

      require.config({
          map: {
              '*':{
                'contents': 'services/contents',
              }
          }
      });
    </script>

    
    

</head>

<body class="edit_app " 
data-base-url="/user/rajaquep/"
data-file-path="algorithms/lcs.py"

>

<noscript>
    <div id='noscript'>
      IPython Notebook requires JavaScript.<br>
      Please enable it to proceed.
  </div>
</noscript>

<div id="header">
  <div id="header-container" class="container">
  <div id="ipython_notebook" class="nav navbar-brand pull-left"><a href="/user/rajaquep/tree" title='dashboard'><img src='/user/rajaquep/static/base/images/logo.png?v=7c4597ba713d804995e8f8dad448a397' alt='Jupyter Notebook'/></a></div>

  


  

    <span id="login_widget">
      
        <button id="logout" class="btn btn-sm navbar-btn">Logout</button>
      
    </span>

  

  

<a href='/hub/home'
 class='btn btn-default btn-sm navbar-btn pull-right'
 style='margin-right: 4px; margin-left: 2px;'
>
Control Panel</a>


  

<span id="save_widget" class="pull-left save_widget">
    <span class="filename"></span>
    <span class="last_modified"></span>
</span>


  </div>
  <div class="header-bar"></div>

  

<div id="menubar-container" class="container">
  <div id="menubar">
    <div id="menus" class="navbar navbar-default" role="navigation">
      <div class="container-fluid">
          <p  class="navbar-text indicator_area">
          <span id="current-mode" >current mode</span>
          </p>
        <button type="button" class="btn btn-default navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
          <i class="fa fa-bars"></i>
          <span class="navbar-text">Menu</span>
        </button>
        <ul class="nav navbar-nav navbar-right">
          <li id="notification_area"></li>
        </ul>
        <div class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">File</a>
              <ul id="file-menu" class="dropdown-menu">
                <li id="new-file"><a href="#">New</a></li>
                <li id="save-file"><a href="#">Save</a></li>
                <li id="rename-file"><a href="#">Rename</a></li>
                <li id="download-file"><a href="#">Download</a></li>
              </ul>
            </li>
            <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">Edit</a>
              <ul id="edit-menu" class="dropdown-menu">
                <li id="menu-find"><a href="#">Find</a></li>
                <li id="menu-replace"><a href="#">Find &amp; Replace</a></li>
                <li class="divider"></li>
                <li class="dropdown-header">Key Map</li>
                <li id="menu-keymap-default"><a href="#">Default<i class="fa"></i></a></li>
                <li id="menu-keymap-sublime"><a href="#">Sublime Text<i class="fa"></i></a></li>
                <li id="menu-keymap-vim"><a href="#">Vim<i class="fa"></i></a></li>
                <li id="menu-keymap-emacs"><a href="#">emacs<i class="fa"></i></a></li>
              </ul>
            </li>
            <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">View</a>
              <ul id="view-menu" class="dropdown-menu">
                <li id="menu-line-numbers"><a href="#">Toggle Line Numbers</a></li>
              </ul>
            </li>
            <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">Language</a>
              <ul id="mode-menu" class="dropdown-menu">
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="lower-header-bar"></div>


</div>

<div id="site">


<div id="texteditor-backdrop">
<div id="texteditor-container" class="container"></div>
</div>


</div>






    


<script src="/user/rajaquep/static/edit/js/main.js?v=58955bd704577062447729fec98f6971" type="text/javascript" charset="utf-8"></script>


</body>

</html>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<!-- saved from url=(0044)https://automatetheboringstuff.com/chapter8/ -->
<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xml:lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <link rel="stylesheet" type="text/css" href="./statequiz_files/automate_website.css">
  
  <title>Automate the Boring Stuff with Python</title>
</head>

<body>
  <div class="top_header">
  <a href="https://automatetheboringstuff.com/">Home</a> | <a href="https://www.nostarch.com/automatestuff">Buy on No Starch Press</a> | <a href="http://www.amazon.com/gp/product/1593275994/ref=as_li_tl?ie=UTF8&amp;camp=1789&amp;creative=9325&amp;creativeASIN=1593275994&amp;linkCode=as2&amp;tag=playwithpyth-20&amp;linkId=HDM7V3T6RHC5VVN4">Buy on Amazon</a> | <a href="https://twitter.com/AlSweigart">@AlSweigart</a> | <form action="https://www.paypal.com/cgi-bin/webscr" method="post">
            <input type="hidden" name="cmd" value="_s-xclick"> <input type="hidden" name="encrypted" value="-----BEGIN PKCS7-----MIIHPwYJKoZIhvcNAQcEoIIHMDCCBywCAQExggEwMIIBLAIBADCBlDCBjjELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAkNBMRYwFAYDVQQHEw1Nb3VudGFpbiBWaWV3MRQwEgYDVQQKEwtQYXlQYWwgSW5jLjETMBEGA1UECxQKbGl2ZV9jZXJ0czERMA8GA1UEAxQIbGl2ZV9hcGkxHDAaBgkqhkiG9w0BCQEWDXJlQHBheXBhbC5jb20CAQAwDQYJKoZIhvcNAQEBBQAEgYCgxPYQJv3Obo0bDfmsrZC9NE7NgomnCSQYzv/qoo+SXiFnbdf4mEmccT4S+0nqLTLu/9k3rkoQtk3a/5bIjBrzgO372uHrT8gmkhvF08XSyS2EJ4wzFCkvRJJTcXskj9Wu3Fy5x5WQfiJQBuYvTOBpBdALM1pR4isBk3s4Js3MljELMAkGBSsOAwIaBQAwgbwGCSqGSIb3DQEHATAUBggqhkiG9w0DBwQIeOPj/1/T33qAgZjwQw5CrNvgceyGdLNX3he0m8Z/vB/gZrTN9Fsy1gqd55nsqvF9mz3g4tESgYR1fZ1z4dbp+VWihXs8wDt8+Gf+VFRGbqKBb8Ehf8viIKdwq0oBlJ8PqIZg2BbfgFWtTNiduFUaxikJsI99cmUCGKyMS6YUb9H6RWxs7hdWRLSi5JCBI7JrDKRXh1rQ7Fyul/axzyXbJd3K6qCCA4cwggODMIIC7KADAgECAgEAMA0GCSqGSIb3DQEBBQUAMIGOMQswCQYDVQQGEwJVUzELMAkGA1UECBMCQ0ExFjAUBgNVBAcTDU1vdW50YWluIFZpZXcxFDASBgNVBAoTC1BheVBhbCBJbmMuMRMwEQYDVQQLFApsaXZlX2NlcnRzMREwDwYDVQQDFAhsaXZlX2FwaTEcMBoGCSqGSIb3DQEJARYNcmVAcGF5cGFsLmNvbTAeFw0wNDAyMTMxMDEzMTVaFw0zNTAyMTMxMDEzMTVaMIGOMQswCQYDVQQGEwJVUzELMAkGA1UECBMCQ0ExFjAUBgNVBAcTDU1vdW50YWluIFZpZXcxFDASBgNVBAoTC1BheVBhbCBJbmMuMRMwEQYDVQQLFApsaXZlX2NlcnRzMREwDwYDVQQDFAhsaXZlX2FwaTEcMBoGCSqGSIb3DQEJARYNcmVAcGF5cGFsLmNvbTCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEAwUdO3fxEzEtcnI7ZKZL412XvZPugoni7i7D7prCe0AtaHTc97CYgm7NsAtJyxNLixmhLV8pyIEaiHXWAh8fPKW+R017+EmXrr9EaquPmsVvTywAAE1PMNOKqo2kl4Gxiz9zZqIajOm1fZGWcGS0f5JQ2kBqNbvbg2/Za+GJ/qwUCAwEAAaOB7jCB6zAdBgNVHQ4EFgQUlp98u8ZvF71ZP1LXChvsENZklGswgbsGA1UdIwSBszCBsIAUlp98u8ZvF71ZP1LXChvsENZklGuhgZSkgZEwgY4xCzAJBgNVBAYTAlVTMQswCQYDVQQIEwJDQTEWMBQGA1UEBxMNTW91bnRhaW4gVmlldzEUMBIGA1UEChMLUGF5UGFsIEluYy4xEzARBgNVBAsUCmxpdmVfY2VydHMxETAPBgNVBAMUCGxpdmVfYXBpMRwwGgYJKoZIhvcNAQkBFg1yZUBwYXlwYWwuY29tggEAMAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQEFBQADgYEAgV86VpqAWuXvX6Oro4qJ1tYVIT5DgWpE692Ag422H7yRIr/9j/iKG4Thia/Oflx4TdL+IFJBAyPK9v6zZNZtBgPBynXb048hsP16l2vi0k5Q2JKiPDsEfBhGI+HnxLXEaUWAcVfCsQFvd2A1sxRr67ip5y2wwBelUecP3AjJ+YcxggGaMIIBlgIBATCBlDCBjjELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAkNBMRYwFAYDVQQHEw1Nb3VudGFpbiBWaWV3MRQwEgYDVQQKEwtQYXlQYWwgSW5jLjETMBEGA1UECxQKbGl2ZV9jZXJ0czERMA8GA1UEAxQIbGl2ZV9hcGkxHDAaBgkqhkiG9w0BCQEWDXJlQHBheXBhbC5jb20CAQAwCQYFKw4DAhoFAKBdMBgGCSqGSIb3DQEJAzELBgkqhkiG9w0BBwEwHAYJKoZIhvcNAQkFMQ8XDTA5MTAwODIxMjUzNVowIwYJKoZIhvcNAQkEMRYEFI3IhaXiNtG/+5ZEYOHqSsAgYHXGMA0GCSqGSIb3DQEBAQUABIGAOfyAIJVkJnivbfGpRWAncl+2+4JMV+9OKY+4G+NxDNEYEXlZTgoxRMSgI68s4DwqBt8gnxD2hlUapPccwBSTWLgJRzs/weWaGjx5e/uoylM4cNzvO0HOXKGjqUCV1NySB2uDUgvo/WyS6rupK21TSeljRswRLF4PUMQhkYf1KiM=-----END PKCS7----- "> <input type="image" src="./statequiz_files/btn_donate_LG.gif" border="0" name="submit" alt="PayPal - The safer, easier way to pay online!"> <img alt="" border="0" src="./statequiz_files/pixel.gif" width="1" height="1" hidden="" style="display: none !important;">
          </form></div>

  <div class="main">
	
				
<article id="post-122" class="post-122 page type-page status-publish hentry">
	<header class="entry-header">
		<h1 class="entry-title">Chapter  8 – Reading and Writing Files</h1>	</header><!-- .entry-header -->

	<div class="entry-content">
		<p></p><center><a href="https://automatetheboringstuff.com/chapter7"><img src="./statequiz_files/prev.png"></a><a href="https://automatetheboringstuff.com/#toc"><img src="./statequiz_files/toc.png"></a><a href="https://automatetheboringstuff.com/chapter9"><img src="./statequiz_files/next.png"></a><br>Support the Author: Buy the book on <a href="http://www.amazon.com/gp/product/1593275994/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&amp;camp=1789&amp;creative=9325&amp;creativeASIN=1593275994&amp;linkCode=as2&amp;tag=playwithpyth-20&amp;linkId=2KIYOE7RFLG7D2RJ">Amazon</a> or<br><a href="http://www.nostarch.com/automatestuff">the book/ebook bundle directly from No Starch Press</a>.<br><a href="http://www.nostarch.com/automatestuff"><img class=" size-full wp-image-49 aligncenter" src="./statequiz_files/automate_small_cover.png" alt="small_cover" width="170" height="225"></a><br><a href="https://inventwithpython.com/">Read the author's other free Python books:</a><br><a href="https://inventwithpython.com/chapters"><img src="./statequiz_files/smallcover_invent.png" width="120"></a> <a href="https://inventwithpython.com/pygame/chapters"><img src="./statequiz_files/smallcover_makinggames.png" width="120"></a> <a href="https://inventwithpython.com/hacking/chapters"><img src="./statequiz_files/smallcover_hacking.png" width="120"></a></center><p></p>
<div class="calibre" id="calibre_link-81">
<div class="book" title="Chapter 8. Reading and Writing Files">
<div class="titlepage">
<div class="book">
<div class="book">
<h1 class="title1"><a id="calibre_link-2678" class="firstname"></a>Reading and Writing Files</h1>
</div>
</div>
</div>
<p class="calibre4"><a id="calibre_link-471" class="calibre1"></a><a id="calibre_link-613" class="calibre1"></a><a id="calibre_link-622" class="calibre1"></a><a id="calibre_link-623" class="calibre1"></a><a id="calibre_link-653" class="calibre1"></a><a id="calibre_link-678" class="calibre1"></a><a id="calibre_link-1222" class="calibre1"></a>Variables are a fine way to store data while your program is running, but if you want your data to persist even after your program has finished, you need to save it to a file. You can think of a file’s contents as a single string value, potentially gigabytes in size. In this chapter, you will learn how to use Python to create, read, and save files on the hard drive.</p>
<div class="book" title="Files and File Paths">
<div class="titlepage">
<div class="book">
<div class="book">
<h1 class="title2"><a id="calibre_link-2679" class="firstname"></a>Files and File Paths</h1>
</div>
</div>
</div>
<p class="calibre4">A file has two key properties: a <span class="calibre1"><em class="calibre5">filename</em></span> (usually written as one word) and a <span class="calibre1"><em class="calibre5">path</em></span>. The path specifies the location of a file on the computer. For example, there is a file on my Windows 7 laptop with the filename <span class="calibre1"><em class="calibre5">project.docx</em></span> in the path <span class="calibre1"><em class="calibre5">C:\Users\asweigart\Documents</em></span>. The part of the filename after the last period is called the file’s <span class="calibre1"><em class="calibre5">extension</em></span> and tells you a file’s type. <span class="calibre1"><em class="calibre5">project.docx</em></span> is a Word document, and <span class="calibre1"><em class="calibre5">Users</em></span>, <span class="calibre1"><em class="calibre5">asweigart</em></span>, and <span class="calibre1"><em class="calibre5">Documents</em></span> all refer to <span class="calibre1"><em class="calibre5">folders</em></span> (also <a id="calibre_link-169" class="calibre1"></a><a id="calibre_link-164" class="calibre1"></a><a id="calibre_link-261" class="calibre1"></a><a id="calibre_link-472" class="calibre1"></a><a id="calibre_link-624" class="calibre1"></a><a id="calibre_link-679" class="calibre1"></a><a id="calibre_link-717" class="calibre1"></a><a id="calibre_link-915" class="calibre1"></a><a id="calibre_link-969" class="calibre1"></a><a id="calibre_link-1044" class="calibre1"></a><a id="calibre_link-1092" class="calibre1"></a><a id="calibre_link-1189" class="calibre1"></a><a id="calibre_link-1223" class="calibre1"></a><a id="calibre_link-1796" class="calibre1"></a><a id="calibre_link-1844" class="calibre1"></a>called <span class="calibre1"><em class="calibre5">directories</em></span>). Folders can contain files and other folders. For example, <span class="calibre1"><em class="calibre5">project.docx</em></span> is in the <span class="calibre1"><em class="calibre5">Documents</em></span> folder, which is inside the <span class="calibre1"><em class="calibre5">asweigart</em></span> folder, which is inside the <span class="calibre1"><em class="calibre5">Users</em></span> folder. <a class="ulink" href="https://automatetheboringstuff.com/chapter8/#calibre_link-82" title="Figure 8-1. A file in a hierarchy of folders">Figure&nbsp;8-1</a> shows this folder organization.</p>
<div class="figure"><a id="calibre_link-82" class="calibre1"></a>
<div class="book">
<div class="book"><a id="calibre_link-2680" class="calibre1"></a><img src="./statequiz_files/000027.jpg" alt="A file in a hierarchy of folders" class="calibre8"></div>
</div>
<p class="title4">Figure&nbsp;8-1.&nbsp;A file in a hierarchy of folders</p>
</div>
<p class="calibre4">The <span class="calibre1"><em class="calibre5">C:\</em></span> part of the path is the <span class="calibre1"><em class="calibre5">root folder</em></span>, which contains all other folders. On Windows, the root folder is named <span class="calibre1"><em class="calibre5">C:\</em></span> and is also called the <span class="calibre1"><em class="calibre5">C: drive</em></span>. On OS X and Linux, the root folder is <span class="calibre1"><em class="calibre5">/</em></span>. In this book, I’ll be using the Windows-style root folder, <span class="calibre1"><em class="calibre5">C:\</em></span>. If you are entering the interactive shell examples on OS X or Linux, enter <code class="literal1">/</code> instead.</p>
<p class="calibre4">Additional <span class="calibre1"><em class="calibre5">volumes</em></span>, such as a DVD drive or USB thumb drive, will appear differently on different operating systems. On Windows, they appear as new, lettered root drives, such as <span class="calibre1"><em class="calibre5">D:\</em></span> or <span class="calibre1"><em class="calibre5">E:\</em></span>. On OS X, they appear as new folders under the <span class="calibre1"><em class="calibre5">/Volumes</em></span> folder. On Linux, they appear as new folders under the <span class="calibre1"><em class="calibre5">/mnt</em></span> (“mount”) folder. Also note that while folder names and filenames are not case sensitive on Windows and OS X, they are case sensitive on Linux.</p>
<div class="book" title="Backslash on Windows and Forward Slash on OS X and Linux">
<div class="titlepage">
<div class="book">
<div class="book">
<h2 class="title3"><a id="calibre_link-2681" class="firstname"></a>Backslash on Windows and Forward Slash on OS X and Linux</h2>
</div>
</div>
</div>
<p class="calibre4">On Windows, paths are written using backslashes (<span class="calibre1"><em class="calibre5">\</em></span>) as the separator between folder names. OS X and Linux, however, use the forward slash (<span class="calibre1"><em class="calibre5">/</em></span>) as their path separator. If you want your programs to work on all operating systems, you will have to write your Python scripts to handle both cases.</p>
<p class="calibre4">Fortunately, this is simple to do with the <code class="literal1">os.path.join()</code> function. If you pass it the string values of individual file and folder names in your path, <code class="literal1">os.path.join()</code> will return a string with a file path using the correct path separators. Enter the following into the interactive shell:</p>
<p><a id="calibre_link-2682" class="calibre1"></a>
</p><pre class="programlisting">&gt;&gt;&gt; <span class="calibre1"><strong class="literal">import os</strong></span>
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">os.path.join('usr', 'bin', 'spam')</strong></span>
'usr\\bin\\spam'</pre>
<p class="calibre4">I’m running these interactive shell examples on Windows, so <code class="literal1">os.path.join('usr', 'bin', 'spam')</code> returned <code class="literal1">'usr\\bin\\spam'</code>. (Notice that the backslashes are doubled because each backslash needs to be escaped by another backslash character.) If I had called this function on OS X or Linux, the string would have been <code class="literal1">'usr/bin/spam'</code>.</p>
<p class="calibre4">The os.path.join() function is helpful if you need to create strings for filenames. These strings will be passed to several of the file-related functions introduced in this chapter. For example, the following example joins names from a list of filenames to the end of a folder’s name:</p>
<p><a id="calibre_link-2683" class="calibre1"></a>
</p><pre class="programlisting">&gt;&gt;&gt; <span class="calibre1"><strong class="literal">myFiles = ['accounts.txt', 'details.csv', 'invite.docx']</strong></span>
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">for filename in myFiles:</strong></span>
        print(os.path.join('C:\\Users\\asweigart', filename))
C:\Users\asweigart\accounts.txt
C:\Users\asweigart\details.csv
C:\Users\asweigart\invite.docx</pre>
</div>
<div class="book" title="The Current Working Directory">
<div class="titlepage">
<div class="book">
<div class="book">
<h2 class="title3"><a id="calibre_link-2684" class="firstname"></a>The Current Working Directory</h2>
</div>
</div>
</div>
<p class="calibre4"><a id="calibre_link-157" class="calibre1"></a><a id="calibre_link-219" class="calibre1"></a><a id="calibre_link-321" class="calibre1"></a><a id="calibre_link-402" class="calibre1"></a><a id="calibre_link-473" class="calibre1"></a><a id="calibre_link-474" class="calibre1"></a><a id="calibre_link-497" class="calibre1"></a><a id="calibre_link-625" class="calibre1"></a><a id="calibre_link-626" class="calibre1"></a><a id="calibre_link-680" class="calibre1"></a><a id="calibre_link-681" class="calibre1"></a><a id="calibre_link-739" class="calibre1"></a><a id="calibre_link-1224" class="calibre1"></a><a id="calibre_link-1225" class="calibre1"></a><a id="calibre_link-1476" class="calibre1"></a>Every program that runs on your computer has a <span class="calibre1"><em class="calibre5">current working directory</em></span>, or <span class="calibre1"><em class="calibre5">cwd</em></span>. Any filenames or paths that do not begin with the root folder are assumed to be under the current working directory. You can get the current working directory as a string value with the <code class="literal1">os.getcwd()</code> function and change it with <code class="literal1">os.chdir()</code>. Enter the following into the interactive shell:</p>
<p><a id="calibre_link-2685" class="calibre1"></a>
</p><pre class="programlisting">&gt;&gt;&gt; <span class="calibre1"><strong class="literal">import os</strong></span>
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">os.getcwd()</strong></span>
'C:\\Python34'
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">os.chdir('C:\\Windows\\System32')</strong></span>
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">os.getcwd()</strong></span>
'C:\\Windows\\System32'</pre>
<p class="calibre4">Here, the current working directory is set to <span class="calibre1"><em class="calibre5">C:\Python34</em></span>, so the filename <span class="calibre1"><em class="calibre5">project.docx</em></span> refers to <span class="calibre1"><em class="calibre5">C:\Python34\project.docx</em></span>. When we change the current working directory to <span class="calibre1"><em class="calibre5">C:\Windows</em></span>, <span class="calibre1"><em class="calibre5">project.docx</em></span> is interpreted as <span class="calibre1"><em class="calibre5">C:\ Windows\project.docx</em></span>.</p>
<p class="calibre4">Python will display an error if you try to change to a directory that does not exist.</p>
<p><a id="calibre_link-2686" class="calibre1"></a>
</p><pre class="programlisting">&gt;&gt;&gt; <span class="calibre1"><strong class="literal">os.chdir('C:\\ThisFolderDoesNotExist')</strong></span>
Traceback (most recent call last):
  File "&lt;pyshell#18&gt;", line 1, in &lt;module&gt;
    os.chdir('C:\\ThisFolderDoesNotExist')
FileNotFoundError: [WinError 2] The system cannot find the file specified:
'C:\\ThisFolderDoesNotExist'</pre>
<div class="note" title="Note">
<h3 class="title5"><a id="calibre_link-2687" class="calibre1"></a>Note</h3>
<p class="calibre4"><span class="calibre1"><em class="calibre5">While folder is the more modern name for directory, note that</em></span> current working directory <span class="calibre1"><em class="calibre5">(or just</em></span> working directory<span class="calibre1"><em class="calibre5">) is the standard term, not current working folder.</em></span></p>
</div>
</div>
<div class="book" title="Absolute vs. Relative Paths">
<div class="titlepage">
<div class="book">
<div class="book">
<h2 class="title3"><a id="calibre_link-2688" class="firstname"></a>Absolute vs. Relative Paths</h2>
</div>
</div>
</div>
<p class="calibre4">There are two ways to specify a file path.</p>
<div class="book">
<ul class="itemizedlist">
<li class="listitem">
<p class="calibre4">An <span class="calibre1"><em class="calibre5">absolute path</em></span>, which always begins with the root folder</p>
</li>
<li class="listitem">
<p class="calibre4">A <span class="calibre1"><em class="calibre5">relative path</em></span>, which is relative to the program’s current working directory</p>
</li>
</ul>
</div>
<p class="calibre4">There are also the <span class="calibre1"><em class="calibre5">dot</em></span> (<code class="literal1">.</code>) and <span class="calibre1"><em class="calibre5">dot-dot</em></span> (<code class="literal1">..</code>) folders. These are not real folders but special names that can be used in a path. A single period (“dot”) for a folder name is shorthand for “this directory.” Two periods (“dot-dot”) means “the parent folder.”</p>
<p class="calibre4"><a id="calibre_link-475" class="calibre1"></a><a id="calibre_link-627" class="calibre1"></a><a id="calibre_link-682" class="calibre1"></a><a id="calibre_link-1046" class="calibre1"></a><a class="ulink" href="https://automatetheboringstuff.com/chapter8/#calibre_link-83" title="Figure 8-2. The relative paths for folders and files in the working directory C:\bacon">Figure&nbsp;8-2</a> is an example of some folders and files. When the current working directory is set to <span class="calibre1"><em class="calibre5">C:\bacon</em></span>, the relative paths for the other folders and files are set as they are in the figure.</p>
<div class="figure"><a id="calibre_link-83" class="calibre1"></a>
<div class="book">
<div class="book"><a id="calibre_link-2689" class="calibre1"></a><img src="./statequiz_files/000032.jpg" alt="The relative paths for folders and files in the working directory C:\bacon" class="calibre8"></div>
</div>
<p class="title4">Figure&nbsp;8-2.&nbsp;The relative paths for folders and files in the working directory <span class="calibre1"><em class="calibre5">C:\bacon</em></span></p>
</div>
<p class="calibre4">The <span class="calibre1"><em class="calibre5">.\</em></span> at the start of a relative path is optional. For example, <span class="calibre1"><em class="calibre5">.\spam.txt</em></span> and <span class="calibre1"><em class="calibre5">spam.txt</em></span> refer to the same file.</p>
</div>
<div class="book" title="Creating New Folders with os.makedirs()">
<div class="titlepage">
<div class="book">
<div class="book">
<h2 class="title3"><a id="calibre_link-2690" class="firstname"></a>Creating New Folders with os.makedirs()</h2>
</div>
</div>
</div>
<p class="calibre4">Your programs can create new folders (directories) with the <code class="literal1">os.makedirs()</code> function. Enter the following into the interactive shell:</p>
<p><a id="calibre_link-2691" class="calibre1"></a>
</p><pre class="programlisting">&gt;&gt;&gt; <span class="calibre1"><strong class="literal">import os</strong></span>
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">os.makedirs('C:\\delicious\\walnut\\waffles')</strong></span></pre>
<p class="calibre4">This will create not just the <span class="calibre1"><em class="calibre5">C:\delicious</em></span> folder but also a <span class="calibre1"><em class="calibre5">walnut</em></span> folder inside <span class="calibre1"><em class="calibre5">C:\delicious</em></span> and a <span class="calibre1"><em class="calibre5">waffles</em></span> folder inside <span class="calibre1"><em class="calibre5">C:\delicious\walnut</em></span>. That is, <code class="literal1">os.makedirs()</code> will create any necessary intermediate folders in order to ensure that the full path exists. <a class="ulink" href="https://automatetheboringstuff.com/chapter8/#calibre_link-84" title="Figure 8-3. The result of os.makedirs(&#39;C:\\delicious \\walnut\\waffles&#39;)">Figure&nbsp;8-3</a> shows this hierarchy of folders.</p>
<div class="figure"><a id="calibre_link-84" class="calibre1"></a>
<div class="book">
<div class="book"><a id="calibre_link-2692" class="calibre1"></a><img src="./statequiz_files/000036.jpg" alt="The result of os.makedirs(&#39;C:\\delicious \\walnut\\waffles&#39;)" class="calibre8"></div>
</div>
<p class="title4">Figure&nbsp;8-3.&nbsp;The result of <code class="literal1">os.makedirs('C:\\delicious \\walnut\\waffles')</code></p>
</div>
</div>
</div>
<div class="book" title="The os.path Module">
<div class="titlepage">
<div class="book">
<div class="book">
<h1 class="title2"><a id="calibre_link-2693" class="firstname"></a>The os.path Module</h1>
</div>
</div>
</div>
<p class="calibre4"><a id="calibre_link-220" class="calibre1"></a><a id="calibre_link-476" class="calibre1"></a><a id="calibre_link-477" class="calibre1"></a><a id="calibre_link-478" class="calibre1"></a><a id="calibre_link-628" class="calibre1"></a><a id="calibre_link-629" class="calibre1"></a><a id="calibre_link-630" class="calibre1"></a><a id="calibre_link-683" class="calibre1"></a><a id="calibre_link-684" class="calibre1"></a><a id="calibre_link-685" class="calibre1"></a><a id="calibre_link-897" class="calibre1"></a><a id="calibre_link-916" class="calibre1"></a><a id="calibre_link-1226" class="calibre1"></a><a id="calibre_link-1227" class="calibre1"></a><a id="calibre_link-1228" class="calibre1"></a><a id="calibre_link-1477" class="calibre1"></a>The <code class="literal1">os.path</code> module contains many helpful functions related to filenames and file paths. For instance, you’ve already used <code class="literal1">os.path.join()</code> to build paths in a way that will work on any operating system. Since <code class="literal1">os.path</code> is a module inside the <code class="literal1">os</code> module, you can import it by simply running <code class="literal1">import os</code>. Whenever your programs need to work with files, folders, or file paths, you can refer to the short examples in this section. The full documentation for the <code class="literal1">os.path</code> module is on the Python website at <span class="calibre1"><em class="calibre5"><a class="ulink" href="http://docs.python.org/3/library/os.path.html">http://docs.python.org/3/library/os.path.html</a></em></span>.</p>
<div class="note" title="Note">
<h3 class="title5"><a id="calibre_link-2694" class="calibre1"></a>Note</h3>
<p class="calibre4"><span class="calibre1"><em class="calibre5">Most of the examples that follow in this section will require the</em></span> <code class="literal1">os</code> <span class="calibre1"><em class="calibre5">module, so remember to import it at the beginning of any script you write and any time you restart IDLE. Otherwise, you’ll get a</em></span> <code class="literal1">NameError: name 'os' is not defined</code> <span class="calibre1"><em class="calibre5">error message.</em></span></p>
</div>
<div class="book" title="Handling Absolute and Relative Paths">
<div class="titlepage">
<div class="book">
<div class="book">
<h2 class="title3"><a id="calibre_link-2695" class="firstname"></a>Handling Absolute and Relative Paths</h2>
</div>
</div>
</div>
<p class="calibre4">The <code class="literal1">os.path</code> module provides functions for returning the absolute path of a relative path and for checking whether a given path is an absolute path.</p>
<div class="book">
<ul class="itemizedlist">
<li class="listitem">
<p class="calibre4">Calling <code class="literal1">os.path.abspath(</code><span class="calibre1"><em class="calibre5"><code class="literal3">path</code></em></span><code class="literal1">)</code> will return a string of the absolute path of the argument. This is an easy way to convert a relative path into an absolute one.</p>
</li>
<li class="listitem">
<p class="calibre4">Calling <code class="literal1">os.path.isabs(</code><span class="calibre1"><em class="calibre5"><code class="literal3">path</code></em></span><code class="literal1">)</code> will return <code class="literal1">True</code> if the argument is an absolute path and <code class="literal1">False</code> if it is a relative path.</p>
</li>
<li class="listitem">
<p class="calibre4">Calling <code class="literal1">os.path.relpath(</code><span class="calibre1"><em class="calibre5"><code class="literal3">path, start</code></em></span><code class="literal1">)</code> will return a string of a relative path from the <span class="calibre1"><em class="calibre5"><code class="literal3">start</code></em></span> path to <span class="calibre1"><em class="calibre5"><code class="literal3">path</code></em></span>. If <span class="calibre1"><em class="calibre5"><code class="literal3">start</code></em></span> is not provided, the current working directory is used as the start path.</p>
</li>
</ul>
</div>
<p class="calibre4">Try these functions in the interactive shell:</p>
<p><a id="calibre_link-2696" class="calibre1"></a>
</p><pre class="programlisting">&gt;&gt;&gt; <span class="calibre1"><strong class="literal">os.path.abspath('.')</strong></span>
'C:\\Python34'
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">os.path.abspath('.\\Scripts')</strong></span>
'C:\\Python34\\Scripts'
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">os.path.isabs('.')</strong></span>
False
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">os.path.isabs(os.path.abspath('.'))</strong></span>
True</pre>
<p class="calibre4">Since <span class="calibre1"><em class="calibre5">C:\Python34</em></span> was the working directory when <code class="literal1">os.path.abspath()</code> was called, the “single-dot” folder represents the absolute path <code class="literal1">'C:\\Python34'</code>.</p>
<div class="note" title="Note">
<h3 class="title5"><a id="calibre_link-2697" class="calibre1"></a>Note</h3>
<p class="calibre4"><span class="calibre1"><em class="calibre5">Since your system probably has different files and folders on it than mine, you won’t be able to follow every example in this chapter exactly. Still, try to follow along using folders that exist on your computer.</em></span></p>
</div>
<p class="calibre4"><a id="calibre_link-263" class="calibre1"></a><a id="calibre_link-488" class="calibre1"></a><a id="calibre_link-1478" class="calibre1"></a><a id="calibre_link-1607" class="calibre1"></a>Enter the following calls to <code class="literal1">os.path.relpath()</code> into the interactive shell:</p>
<p><a id="calibre_link-2698" class="calibre1"></a>
</p><pre class="programlisting">&gt;&gt;&gt; <span class="calibre1"><strong class="literal">os.path.relpath('C:\\Windows', 'C:\\')</strong></span>
'Windows'
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">os.path.relpath('C:\\Windows', 'C:\\spam\\eggs')</strong></span>
'..\\..\\Windows'
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">os.getcwd()</strong></span> 'C:\\Python34'</pre>
<p class="calibre4">Calling <code class="literal1">os.path.dirname(</code><span class="calibre1"><em class="calibre5"><code class="literal3">path</code></em></span><code class="literal1">)</code> will return a string of everything that comes before the last slash in the <code class="literal1">path</code> argument. Calling <code class="literal1">os.path.basename(</code><span class="calibre1"><em class="calibre5"><code class="literal3">path</code></em></span><code class="literal1">)</code> will return a string of everything that comes after the last slash in the <code class="literal1">path</code> argument. The dir name and base name of a path are outlined in <a class="ulink" href="https://automatetheboringstuff.com/chapter8/#calibre_link-85" title="Figure 8-4. The base name follows the last slash in a path and is the same as the filename. The dir name is everything before the last slash.">Figure&nbsp;8-4</a>.</p>
<div class="figure"><a id="calibre_link-85" class="calibre1"></a>
<div class="book">
<div class="book"><a id="calibre_link-2699" class="calibre1"></a><img src="./statequiz_files/000041.png" alt="The base name follows the last slash in a path and is the same as the filename. The dir name is everything before the last slash." class="calibre8"></div>
</div>
<p class="title4">Figure&nbsp;8-4.&nbsp;The base name follows the last slash in a path and is the same as the filename. The dir name is everything before the last slash.</p>
</div>
<p class="calibre4">For example, enter the following into the interactive shell:</p>
<p><a id="calibre_link-2700" class="calibre1"></a>
</p><pre class="programlisting">&gt;&gt;&gt; <span class="calibre1"><strong class="literal">path = 'C:\\Windows\\System32\\calc.exe'</strong></span>
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">os.path.basename(path)</strong></span>
'calc.exe'
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">os.path.dirname(path)</strong></span>
'C:\\Windows\\System32'</pre>
<p class="calibre4">If you need a path’s dir name and base name together, you can just call <code class="literal1">os.path.split()</code> to get a tuple value with these two strings, like so:</p>
<p><a id="calibre_link-2701" class="calibre1"></a>
</p><pre class="programlisting">&gt;&gt;&gt; <span class="calibre1"><strong class="literal">calcFilePath = 'C:\\Windows\\System32\\calc.exe'</strong></span>
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">os.path.split(calcFilePath)</strong></span>
('C:\\Windows\\System32', 'calc.exe')</pre>
<p class="calibre4">Notice that you could create the same tuple by calling <code class="literal1">os.path.dirname()</code> and <code class="literal1">os.path.basename()</code> and placing their return values in a tuple.</p>
<p><a id="calibre_link-2702" class="calibre1"></a>
</p><pre class="programlisting">&gt;&gt;&gt; <span class="calibre1"><strong class="literal">(os.path.dirname(calcFilePath), os.path.basename(calcFilePath))</strong></span>
('C:\\Windows\\System32', 'calc.exe')</pre>
<p class="calibre4">But <code class="literal1">os.path.split()</code> is a nice shortcut if you need both values.</p>
<p class="calibre4">Also, note that <code class="literal1">os.path.split()</code> does <span class="calibre1"><em class="calibre5">not</em></span> take a file path and return a list of strings of each folder. For that, use the <code class="literal1">split()</code> string method and split on the string in <code class="literal1">os.sep</code>. Recall from earlier that the <code class="literal1">os.sep</code> variable is set to the correct folder-separating slash for the computer running the program.</p>
<p class="calibre4"><a id="calibre_link-479" class="calibre1"></a><a id="calibre_link-480" class="calibre1"></a><a id="calibre_link-631" class="calibre1"></a><a id="calibre_link-632" class="calibre1"></a><a id="calibre_link-686" class="calibre1"></a><a id="calibre_link-687" class="calibre1"></a><a id="calibre_link-751" class="calibre1"></a><a id="calibre_link-978" class="calibre1"></a><a id="calibre_link-1229" class="calibre1"></a><a id="calibre_link-1230" class="calibre1"></a>For example, enter the following into the interactive shell:</p>
<p><a id="calibre_link-2703" class="calibre1"></a>
</p><pre class="programlisting">&gt;&gt;&gt; <span class="calibre1"><strong class="literal">calcFilePath.split(os.path.sep)</strong></span>
['C:', 'Windows', 'System32', 'calc.exe']</pre>
<p class="calibre4">On OS X and Linux systems, there will be a blank string at the start of the returned list:</p>
<p><a id="calibre_link-2704" class="calibre1"></a>
</p><pre class="programlisting">&gt;&gt;&gt; <span class="calibre1"><strong class="literal">'/usr/bin'.split(os.path.sep)</strong></span>
['', 'usr', 'bin']</pre>
<p class="calibre4">The <code class="literal1">split()</code> string method will work to return a list of each part of the path. It will work on any operating system if you pass it <code class="literal1">os.path.sep</code>.</p>
</div>
<div class="book" title="Finding File Sizes and Folder Contents">
<div class="titlepage">
<div class="book">
<div class="book">
<h2 class="title3"><a id="calibre_link-2705" class="firstname"></a>Finding File Sizes and Folder Contents</h2>
</div>
</div>
</div>
<p class="calibre4">Once you have ways of handling file paths, you can then start gathering information about specific files and folders. The <code class="literal1">os.path</code> module provides functions for finding the size of a file in bytes and the files and folders inside a given folder.</p>
<div class="book">
<ul class="itemizedlist">
<li class="listitem">
<p class="calibre4">Calling <code class="literal1">os.path.getsize(</code><span class="calibre1"><em class="calibre5"><code class="literal3">path</code></em></span><code class="literal1">)</code> will return the size in bytes of the file in the <span class="calibre1"><em class="calibre5"><code class="literal3">path</code></em></span> argument.</p>
</li>
<li class="listitem">
<p class="calibre4">Calling <code class="literal1">os.listdir(</code><span class="calibre1"><em class="calibre5"><code class="literal3">path</code></em></span><code class="literal1">)</code> will return a list of filename strings for each file in the <span class="calibre1"><em class="calibre5"><code class="literal3">path</code></em></span> argument. (Note that this function is in the <code class="literal1">os</code> module, not <code class="literal1">os.path</code>.)</p>
</li>
</ul>
</div>
<p class="calibre4">Here’s what I get when I try these functions in the interactive shell:</p>
<p><a id="calibre_link-2706" class="calibre1"></a>
</p><pre class="programlisting">&gt;&gt;&gt; <span class="calibre1"><strong class="literal">os.path.getsize('C:\\Windows\\System32\\calc.exe')</strong></span>
776192
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">os.listdir('C:\\Windows\\System32')</strong></span>
['0409', '12520437.cpx', '12520850.cpx', '5U877.ax', 'aaclient.dll',
--<span class="calibre1"><em class="literal3">snip</em></span>--
'xwtpdui.dll', 'xwtpw32.dll', 'zh-CN', 'zh-HK', 'zh-TW', 'zipfldr.dll']</pre>
<p class="calibre4">As you can see, the <span class="calibre1"><em class="calibre5">calc.exe</em></span> program on my computer is 776,192 bytes in size, and I have a lot of files in <span class="calibre1"><em class="calibre5">C:\Windows\system32</em></span>. If I want to find the total size of all the files in this directory, I can use <code class="literal1">os.path.getsize()</code> and <code class="literal1">os.listdir()</code> together.</p>
<p><a id="calibre_link-2707" class="calibre1"></a>
</p><pre class="programlisting">&gt;&gt;&gt; <span class="calibre1"><strong class="literal">totalSize = 0</strong></span>
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">for filename in os.listdir('C:\\Windows\\System32'):</strong></span>
      <span class="calibre1"><strong class="literal">totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))</strong></span>

&gt;&gt;&gt; <span class="calibre1"><strong class="literal">print(totalSize)</strong></span>
1117846456</pre>
<p class="calibre4"><a id="calibre_link-268" class="calibre1"></a><a id="calibre_link-481" class="calibre1"></a><a id="calibre_link-606" class="calibre1"></a><a id="calibre_link-633" class="calibre1"></a><a id="calibre_link-634" class="calibre1"></a><a id="calibre_link-688" class="calibre1"></a><a id="calibre_link-901" class="calibre1"></a><a id="calibre_link-904" class="calibre1"></a><a id="calibre_link-1231" class="calibre1"></a><a id="calibre_link-1282" class="calibre1"></a>As I loop over each filename in the <span class="calibre1"><em class="calibre5">C:\Windows\System32</em></span> folder, the <code class="literal1">totalSize</code> variable is incremented by the size of each file. Notice how when I call <code class="literal1">os.path.getsize()</code>, I use <code class="literal1">os.path.join()</code> to join the folder name with the current filename. The integer that <code class="literal1">os.path.getsize()</code> returns is added to the value of <code class="literal1">totalSize</code>. After looping through all the files, I print <code class="literal1">totalSize</code> to see the total size of the <span class="calibre1"><em class="calibre5">C:\Windows\System32</em></span> folder.</p>
</div>
<div class="book" title="Checking Path Validity">
<div class="titlepage">
<div class="book">
<div class="book">
<h2 class="title3"><a id="calibre_link-2708" class="firstname"></a>Checking Path Validity</h2>
</div>
</div>
</div>
<p class="calibre4">Many Python functions will crash with an error if you supply them with a path that does not exist. The <code class="literal1">os.path</code> module provides functions to check whether a given path exists and whether it is a file or folder.</p>
<div class="book">
<ul class="itemizedlist">
<li class="listitem">
<p class="calibre4">Calling <code class="literal1">os.path.exists(</code><span class="calibre1"><em class="calibre5"><code class="literal3">path</code></em></span><code class="literal1">)</code> will return <code class="literal1">True</code> if the file or folder referred to in the argument exists and will return <code class="literal1">False</code> if it does not exist.</p>
</li>
<li class="listitem">
<p class="calibre4">Calling <code class="literal1">os.path.isfile(</code><span class="calibre1"><em class="calibre5"><code class="literal3">path</code></em></span><code class="literal1">)</code> will return <code class="literal1">True</code> if the path argument exists and is a file and will return <code class="literal1">False</code> otherwise.</p>
</li>
<li class="listitem">
<p class="calibre4">Calling <code class="literal1">os.path.isdir(</code><span class="calibre1"><em class="calibre5"><code class="literal3">path</code></em></span><code class="literal1">)</code> will return <code class="literal1">True</code> if the path argument exists and is a folder and will return <code class="literal1">False</code> otherwise.</p>
</li>
</ul>
</div>
<p class="calibre4">Here’s what I get when I try these functions in the interactive shell:</p>
<p><a id="calibre_link-2709" class="calibre1"></a>
</p><pre class="programlisting">&gt;&gt;&gt; <span class="calibre1"><strong class="literal">os.path.exists('C:\\Windows')</strong></span>
True
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">os.path.exists('C:\\some_made_up_folder')</strong></span>
False
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">os.path.isdir('C:\\Windows\\System32')</strong></span>
True
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">os.path.isfile('C:\\Windows\\System32')</strong></span>
False
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">os.path.isdir('C:\\Windows\\System32\\calc.exe')</strong></span>
False
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">os.path.isfile('C:\\Windows\\System32\\calc.exe')</strong></span>
True</pre>
<p class="calibre4">You can determine whether there is a DVD or flash drive currently attached to the computer by checking for it with the <code class="literal1">os.path.exists()</code> function. For instance, if I wanted to check for a flash drive with the volume named <span class="calibre1"><em class="calibre5">D:\</em></span> on my Windows computer, I could do that with the following:</p>
<p><a id="calibre_link-2710" class="calibre1"></a>
</p><pre class="programlisting">&gt;&gt;&gt; <span class="calibre1"><strong class="literal">os.path.exists('D:\\')</strong></span>
False</pre>
<p class="calibre4">Oops! It looks like I forgot to plug in my flash drive.</p>
</div>
</div>
<div class="book" title="The File Reading/Writing Process">
<div class="titlepage">
<div class="book">
<div class="book">
<h1 class="title2"><a id="calibre_link-2711" class="firstname"></a>The File Reading/Writing Process</h1>
</div>
</div>
</div>
<p class="calibre4">Once you are comfortable working with folders and relative paths, you’ll be able to specify the location of files to read and write. The functions covered in the next few sections will apply to plaintext files. <span class="calibre1"><em class="calibre5">Plaintext files</em></span> <a id="calibre_link-635" class="calibre1"></a><a id="calibre_link-1168" class="calibre1"></a><a id="calibre_link-1172" class="calibre1"></a>contain only basic text characters and do not include font, size, or color information. Text files with the <span class="calibre1"><em class="calibre5">.txt</em></span> extension or Python script files with the <span class="calibre1"><em class="calibre5">.py</em></span> extension are examples of plaintext files. These can be opened with Windows’s Notepad or OS X’s TextEdit application. Your programs can easily read the contents of plaintext files and treat them as an ordinary string value.</p>
<p class="calibre4"><span class="calibre1"><em class="calibre5">Binary files</em></span> are all other file types, such as word processing documents, PDFs, images, spreadsheets, and executable programs. If you open a binary file in Notepad or TextEdit, it will look like scrambled nonsense, like in <a class="ulink" href="https://automatetheboringstuff.com/chapter8/#calibre_link-86" title="Figure 8-5. The Windows calc.exe program opened in Notepad">Figure&nbsp;8-5</a>.</p>
<div class="figure"><a id="calibre_link-86" class="calibre1"></a>
<div class="book">
<div class="book"><a id="calibre_link-2712" class="calibre1"></a><img src="./statequiz_files/000046.jpg" alt="The Windows calc.exe program opened in Notepad" class="calibre8"></div>
</div>
<p class="title4">Figure&nbsp;8-5.&nbsp;The Windows <code class="literal1">calc.exe</code> program opened in Notepad</p>
</div>
<p class="calibre4">Since every different type of binary file must be handled in its own way, this book will not go into reading and writing raw binary files directly. Fortunately, many modules make working with binary files easier—you will explore one of them, the <code class="literal1">shelve</code> module, later in this chapter.</p>
<p class="calibre4">There are three steps to reading or writing files in Python.</p>
<div class="book">
<ol class="orderedlist">
<li class="listitem">
<p class="calibre4">Call the <code class="literal1">open()</code> function to return a <code class="literal1">File</code> object.</p>
</li>
<li class="listitem">
<p class="calibre4">Call the <code class="literal1">read()</code> or <code class="literal1">write()</code> method on the <code class="literal1">File</code> object.</p>
</li>
<li class="listitem">
<p class="calibre4">Close the file by calling the <code class="literal1">close()</code> method on the <code class="literal1">File</code> object.</p>
</li>
</ol>
</div>
<div class="book" title="Opening Files with the open() Function">
<div class="titlepage">
<div class="book">
<div class="book">
<h2 class="title3"><a id="calibre_link-2713" class="firstname"></a>Opening Files with the open() Function</h2>
</div>
</div>
</div>
<p class="calibre4">To open a file with the <code class="literal1">open()</code> function, you pass it a string path indicating the file you want to open; it can be either an absolute or relative path. The <code class="literal1">open()</code> function returns a <code class="literal1">File</code> object.</p>
<p class="calibre4">Try it by creating a text file named <span class="calibre1"><em class="calibre5">hello.txt</em></span> using Notepad or TextEdit. Type <span class="calibre1"><strong class="calibre7"><code class="literal">Hello world!</code></strong></span> as the content of this text file and save it in your user home folder. Then, if you’re using Windows, enter the following into the interactive shell:</p>
<p><a id="calibre_link-2714" class="calibre1"></a>
</p><pre class="programlisting">&gt;&gt;&gt; <span class="calibre1"><strong class="literal">helloFile = open('C:\\Users\\</strong></span><span class="calibre1"><em class="literal3"><span class="calibre1"><strong class="calibre27">your_home_folder</strong></span></em></span><span class="calibre1"><strong class="literal">\\hello.txt')</strong></span></pre>
<p class="calibre4">If you’re using OS X, enter the following into the interactive shell instead:</p>
<p><a id="calibre_link-2715" class="calibre1"></a>
</p><pre class="programlisting">&gt;&gt;&gt; <span class="calibre1"><strong class="literal">helloFile = open('/Users/</strong></span><span class="calibre1"><em class="literal3"><span class="calibre1"><strong class="calibre27">your_home_folder</strong></span></em></span><span class="calibre1"><strong class="literal">/hello.txt')</strong></span></pre>
<p class="calibre4"><a id="calibre_link-636" class="calibre1"></a><a id="calibre_link-654" class="calibre1"></a><a id="calibre_link-1439" class="calibre1"></a><a id="calibre_link-1441" class="calibre1"></a><a id="calibre_link-1442" class="calibre1"></a>Make sure to replace <span class="calibre1"><em class="calibre5"><code class="literal3">your_home_folder</code></em></span> with your computer username. For example, my username is <span class="calibre1"><em class="calibre5">asweigart</em></span>, so I’d enter <code class="literal1">'C:\\Users\\asweigart\\ hello.txt'</code> on Windows.</p>
<p class="calibre4">Both these commands will open the file in “reading plaintext” mode, or <span class="calibre1"><em class="calibre5">read mode</em></span> for short. When a file is opened in read mode, Python lets you only read data from the file; you can’t write or modify it in any way. Read mode is the default mode for files you open in Python. But if you don’t want to rely on Python’s defaults, you can explicitly specify the mode by passing the string value <code class="literal1">'r'</code> as a second argument to <code class="literal1">open()</code>. So <code class="literal1">open('/Users/asweigart/ hello.txt', 'r')</code> and <code class="literal1">open('/Users/asweigart/hello.txt')</code> do the same thing.</p>
<p class="calibre4">The call to <code class="literal1">open()</code> returns a <code class="literal1">File</code> object. A <code class="literal1">File</code> object represents a file on your computer; it is simply another type of value in Python, much like the lists and dictionaries you’re already familiar with. In the previous example, you stored the <code class="literal1">File</code> object in the variable <code class="literal1">helloFile</code>. Now, whenever you want to read from or write to the file, you can do so by calling methods on the <code class="literal1">File</code> object in <code class="literal1">helloFile</code>.</p>
</div>
<div class="book" title="Reading the Contents of Files">
<div class="titlepage">
<div class="book">
<div class="book">
<h2 class="title3"><a id="calibre_link-2716" class="firstname"></a>Reading the Contents of Files</h2>
</div>
</div>
</div>
<p class="calibre4">Now that you have a <code class="literal1">File</code> object, you can start reading from it. If you want to read the entire contents of a file as a string value, use the <code class="literal1">File</code> object’s <code class="literal1">read()</code> method. Let’s continue with the <span class="calibre1"><em class="calibre5">hello.txt</em></span> <code class="literal1">File</code> object you stored in <code class="literal1">helloFile</code>. Enter the following into the interactive shell:</p>
<p><a id="calibre_link-2717" class="calibre1"></a>
</p><pre class="programlisting">&gt;&gt;&gt; <span class="calibre1"><strong class="literal">helloContent = helloFile.read()</strong></span>
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">helloContent</strong></span>
'Hello world!'</pre>
<p class="calibre4">If you think of the contents of a file as a single large string value, the <code class="literal1">read()</code> method returns the string that is stored in the file.</p>
<p class="calibre4">Alternatively, you can use the <code class="literal1">readlines()</code> method to get a <span class="calibre1"><em class="calibre5">list</em></span> of string values from the file, one string for each line of text. For example, create a file named <span class="calibre1"><em class="calibre5">sonnet29.txt</em></span> in the same directory as <span class="calibre1"><em class="calibre5">hello.txt</em></span> and write the following text in it:</p>
<p><a id="calibre_link-2718" class="calibre1"></a>
</p><pre class="programlisting">When, in disgrace with fortune and men's eyes,
I all alone beweep my outcast state,
And trouble deaf heaven with my bootless cries,
And look upon myself and curse my fate,</pre>
<p class="calibre4">Make sure to separate the four lines with line breaks. Then enter the following into the interactive shell:</p>
<p><a id="calibre_link-2719" class="calibre1"></a>
</p><pre class="programlisting">&gt;&gt;&gt; <span class="calibre1"><strong class="literal">sonnetFile = open('sonnet29.txt')</strong></span>
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">sonnetFile.readlines()</strong></span>
[When, in disgrace with fortune and men's eyes,\n', ' I all alone beweep my
outcast state,\n', And trouble deaf heaven with my bootless cries,\n', And
look upon myself and curse my fate,']</pre>
<p class="calibre4"><a id="calibre_link-637" class="calibre1"></a><a id="calibre_link-1870" class="calibre1"></a>Note that each of the string values ends with a newline character, <code class="literal1">\n</code>, except for the last line of the file. A list of strings is often easier to work with than a single large string value.</p>
</div>
<div class="book" title="Writing to Files">
<div class="titlepage">
<div class="book">
<div class="book">
<h2 class="title3"><a id="calibre_link-2720" class="firstname"></a>Writing to Files</h2>
</div>
</div>
</div>
<p class="calibre4">Python allows you to write content to a file in a way similar to how the <code class="literal1">print()</code> function “writes” strings to the screen. You can’t write to a file you’ve opened in read mode, though. Instead, you need to open it in “write plaintext” mode or “append plaintext” mode, or <span class="calibre1"><em class="calibre5">write mode</em></span> and <span class="calibre1"><em class="calibre5">append mode</em></span> for short.</p>
<p class="calibre4">Write mode will overwrite the existing file and start from scratch, just like when you overwrite a variable’s value with a new value. Pass <code class="literal1">'w'</code> as the second argument to <code class="literal1">open()</code> to open the file in write mode. Append mode, on the other hand, will append text to the end of the existing file. You can think of this as appending to a list in a variable, rather than overwriting the variable altogether. Pass <code class="literal1">'a'</code> as the second argument to <code class="literal1">open()</code> to open the file in append mode.</p>
<p class="calibre4">If the filename passed to <code class="literal1">open()</code> does not exist, both write and append mode will create a new, blank file. After reading or writing a file, call the <code class="literal1">close()</code> method before opening the file again.</p>
<p class="calibre4">Let’s put these concepts together. Enter the following into the interactive shell:</p>
<p><a id="calibre_link-2721" class="calibre1"></a>
</p><pre class="programlisting">&gt;&gt;&gt; <span class="calibre1"><strong class="literal">baconFile = open('bacon.txt', 'w')</strong></span>
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">baconFile.write('Hello world!\n')</strong></span>
13
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">baconFile.close()</strong></span>
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">baconFile = open('bacon.txt', 'a')</strong></span>
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">baconFile.write('Bacon is not a vegetable.')</strong></span>
25
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">baconFile.close()</strong></span>
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">baconFile = open('bacon.txt')</strong></span>
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">content = baconFile.read()</strong></span>
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">baconFile.close()</strong></span>
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">print(content)</strong></span>
Hello world!
Bacon is not a vegetable.</pre>
<p class="calibre4">First, we open <span class="calibre1"><em class="calibre5">bacon.txt</em></span> in write mode. Since there isn’t a <span class="calibre1"><em class="calibre5">bacon.txt</em></span> yet, Python creates one. Calling <code class="literal1">write()</code> on the opened file and passing <code class="literal1">write()</code> the string argument <code class="literal1">'Hello world! /n'</code> writes the string to the file and returns the number of characters written, including the newline. Then we close the file.</p>
<p class="calibre4">To add text to the existing contents of the file instead of replacing the string we just wrote, we open the file in append mode. We write <code class="literal1">'Bacon is not a vegetable.'</code> to the file and close it. Finally, to print the file contents to the screen, we open the file in its default read mode, call <code class="literal1">read()</code>, store the resulting <code class="literal1">File</code> object in <code class="literal1">content</code>, close the file, and print <code class="literal1">content</code>.</p>
<p class="calibre4"><a id="calibre_link-269" class="calibre1"></a><a id="calibre_link-638" class="calibre1"></a><a id="calibre_link-1573" class="calibre1"></a><a id="calibre_link-1793" class="calibre1"></a>Note that the <code class="literal1">write()</code> method does not automatically add a newline character to the end of the string like the <code class="literal1">print()</code> function does. You will have to add this character yourself.</p>
</div>
</div>
<div class="book" title="Saving Variables with the shelve Module">
<div class="titlepage">
<div class="book">
<div class="book">
<h1 class="title2"><a id="calibre_link-2722" class="firstname"></a>Saving Variables with the shelve Module</h1>
</div>
</div>
</div>
<p class="calibre4">You can save variables in your Python programs to binary shelf files using the <code class="literal1">shelve</code> module. This way, your program can restore data to variables from the hard drive. The <code class="literal1">shelve</code> module will let you add Save and Open features to your program. For example, if you ran a program and entered some configuration settings, you could save those settings to a shelf file and then have the program load them the next time it is run.</p>
<p class="calibre4">Enter the following into the interactive shell:</p>
<p><a id="calibre_link-2723" class="calibre1"></a>
</p><pre class="programlisting">&gt;&gt;&gt; <span class="calibre1"><strong class="literal">import shelve</strong></span>
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">shelfFile = shelve.open('mydata')</strong></span>
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">cats = ['Zophie', 'Pooka', 'Simon']</strong></span>
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">shelfFile['cats'] = cats</strong></span>
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">shelfFile.close()</strong></span></pre>
<p class="calibre4">To read and write data using the <code class="literal1">shelve</code> module, you first import <code class="literal1">shelve</code>. Call <code class="literal1">shelve.open()</code> and pass it a filename, and then store the returned shelf value in a variable. You can make changes to the shelf value as if it were a dictionary. When you’re done, call <code class="literal1">close()</code> on the shelf value. Here, our shelf value is stored in <code class="literal1">shelfFile</code>. We create a list <code class="literal1">cats</code> and write <code class="literal1">shelfFile['cats'] = cats</code> to store the list in <code class="literal1">shelfFile</code> as a value associated with the key <code class="literal1">'cats'</code> (like in a dictionary). Then we call <code class="literal1">close()</code> on <code class="literal1">shelfFile</code>.</p>
<p class="calibre4">After running the previous code on Windows, you will see three new files in the current working directory: <span class="calibre1"><em class="calibre5">mydata.bak</em></span>, <span class="calibre1"><em class="calibre5">mydata.dat</em></span>, and <span class="calibre1"><em class="calibre5">mydata.dir</em></span>. On OS X, only a single <span class="calibre1"><em class="calibre5">mydata.db</em></span> file will be created.</p>
<p class="calibre4">These binary files contain the data you stored in your shelf. The format of these binary files is not important; you only need to know what the <code class="literal1">shelve</code> module does, not how it does it. The module frees you from worrying about how to store your program’s data to a file.</p>
<p class="calibre4">Your programs can use the <code class="literal1">shelve</code> module to later reopen and retrieve the data from these shelf files. Shelf values don’t have to be opened in read or write mode—they can do both once opened. Enter the following into the interactive shell:</p>
<p><a id="calibre_link-2724" class="calibre1"></a>
</p><pre class="programlisting">&gt;&gt;&gt; <span class="calibre1"><strong class="literal">shelfFile = shelve.open('mydata')</strong></span>
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">type(shelfFile)</strong></span>
&lt;class 'shelve.DbfilenameShelf'&gt;
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">shelfFile['cats']</strong></span>
['Zophie', 'Pooka', 'Simon']
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">shelfFile.close()</strong></span></pre>
<p class="calibre4">Here, we open the shelf files to check that our data was stored correctly. Entering <code class="literal1">shelfFile['cats']</code> returns the same list that we stored earlier, so we know that the list is correctly stored, and we call <code class="literal1">close()</code>.</p>
<p class="calibre4"><a id="calibre_link-639" class="calibre1"></a><a id="calibre_link-1251" class="calibre1"></a>Just like dictionaries, shelf values have <code class="literal1">keys()</code> and <code class="literal1">values()</code> methods that will return list-like values of the keys and values in the shelf. Since these methods return list-like values instead of true lists, you should pass them to the <code class="literal1">list()</code> function to get them in list form. Enter the following into the interactive shell:</p>
<p><a id="calibre_link-2725" class="calibre1"></a>
</p><pre class="programlisting">&gt;&gt;&gt; <span class="calibre1"><strong class="literal">shelfFile = shelve.open('mydata')</strong></span>
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">list(shelfFile.keys())</strong></span>
['cats']
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">list(shelfFile.values())</strong></span>
[['Zophie', 'Pooka', 'Simon']]
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">shelfFile.close()</strong></span></pre>
<p class="calibre4">Plaintext is useful for creating files that you’ll read in a text editor such as Notepad or TextEdit, but if you want to save data from your Python programs, use the <code class="literal1">shelve</code> module.</p>
</div>
<div class="book" title="Saving Variables with the pprint.pformat() Function">
<div class="titlepage">
<div class="book">
<div class="book">
<h1 class="title2"><a id="calibre_link-2726" class="firstname"></a>Saving Variables with the pprint.pformat() Function</h1>
</div>
</div>
</div>
<p class="calibre4">Recall from <a class="ulink" href="https://automatetheboringstuff.com/chapter8/#calibre_link-87" title="Pretty Printing">Pretty Printing</a> that the <code class="literal1">pprint.pprint()</code> function will “pretty print” the contents of a list or dictionary to the screen, while the <code class="literal1">pprint.pformat()</code> function will return this same text as a string instead of printing it. Not only is this string formatted to be easy to read, but it is also syntactically correct Python code. Say you have a dictionary stored in a variable and you want to save this variable and its contents for future use. Using <code class="literal1">pprint.pformat()</code> will give you a string that you can write to <span class="calibre1"><em class="calibre5">.py</em></span> file. This file will be your very own module that you can import whenever you want to use the variable stored in it.</p>
<p class="calibre4">For example, enter the following into the interactive shell:</p>
<p><a id="calibre_link-2727" class="calibre1"></a>
</p><pre class="programlisting">&gt;&gt;&gt; <span class="calibre1"><strong class="literal">import pprint</strong></span>
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]</strong></span>
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">pprint.pformat(cats)</strong></span>
"[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]"
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">fileObj = open('myCats.py', 'w')</strong></span>
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">fileObj.write('cats = ' + pprint.pformat(cats) + '\n')</strong></span>
83
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">fileObj.close()</strong></span></pre>
<p class="calibre4">Here, we import <code class="literal1">pprint</code> to let us use <code class="literal1">pprint.pformat()</code>. We have a list of dictionaries, stored in a variable <code class="literal1">cats</code>. To keep the list in <code class="literal1">cats</code> available even after we close the shell, we use <code class="literal1">pprint.pformat()</code> to return it as a string. Once we have the data in <code class="literal1">cats</code> as a string, it’s easy to write the string to a file, which we’ll call <span class="calibre1"><em class="calibre5">myCats.py</em></span>.</p>
<p class="calibre4">The modules that an <code class="literal1">import</code> statement imports are themselves just Python scripts. When the string from <code class="literal1">pprint.pformat()</code> is saved to a <span class="calibre1"><em class="calibre5">.py</em></span> file, the file is a module that can be imported just like any other.</p>
<p class="calibre4"><a id="calibre_link-1330" class="calibre1"></a><a id="calibre_link-1425" class="calibre1"></a><a id="calibre_link-1426" class="calibre1"></a>And since Python scripts are themselves just text files with the <span class="calibre1"><em class="calibre5">.py</em></span> file extension, your Python programs can even generate other Python programs. You can then import these files into scripts.</p>
<p><a id="calibre_link-2728" class="calibre1"></a>
</p><pre class="programlisting">&gt;&gt;&gt; <span class="calibre1"><strong class="literal">import myCats</strong></span>
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">myCats.cats</strong></span>
[{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">myCats.cats[0]</strong></span>
{'name': 'Zophie', 'desc': 'chubby'}
&gt;&gt;&gt; <span class="calibre1"><strong class="literal">myCats.cats[0]['name']</strong></span>
'Zophie'</pre>
<p class="calibre4">The benefit of creating a <span class="calibre1"><em class="calibre5">.py</em></span> file (as opposed to saving variables with the <code class="literal1">shelve</code> module) is that because it is a text file, the contents of the file can be read and modified by anyone with a simple text editor. For most applications, however, saving data using the <code class="literal1">shelve</code> module is the preferred way to save variables to a file. Only basic data types such as integers, floats, strings, lists, and dictionaries can be written to a file as simple text. <code class="literal1">File</code> objects, for example, cannot be encoded as text.</p>
</div>
<div class="book" title="Project: Generating Random Quiz Files">
<div class="titlepage">
<div class="book">
<div class="book">
<h1 class="title2"><a id="calibre_link-2729" class="firstname"></a>Project: Generating Random Quiz Files</h1>
</div>
</div>
</div>
<p class="calibre4">Say you’re a geography teacher with 35 students in your class and you want to give a pop quiz on US state capitals. Alas, your class has a few bad eggs in it, and you can’t trust the students not to cheat. You’d like to randomize the order of questions so that each quiz is unique, making it impossible for anyone to crib answers from anyone else. Of course, doing this by hand would be a lengthy and boring affair. Fortunately, you know some Python.</p>
<p class="calibre4">Here is what the program does:</p>
<div class="book">
<ul class="itemizedlist">
<li class="listitem">
<p class="calibre4">Creates 35 different quizzes.</p>
</li>
<li class="listitem">
<p class="calibre4">Creates 50 multiple-choice questions for each quiz, in random order.</p>
</li>
<li class="listitem">
<p class="calibre4">Provides the correct answer and three random wrong answers for each question, in random order.</p>
</li>
<li class="listitem">
<p class="calibre4">Writes the quizzes to 35 text files.</p>
</li>
<li class="listitem">
<p class="calibre4">Writes the answer keys to 35 text files.</p>
</li>
</ul>
</div>
<p class="calibre4">This means the code will need to do the following:</p>
<div class="book">
<ul class="itemizedlist">
<li class="listitem">
<p class="calibre4">Store the states and their capitals in a dictionary.</p>
</li>
<li class="listitem">
<p class="calibre4">Call <code class="literal1">open()</code>, <code class="literal1">write()</code>, and <code class="literal1">close()</code> for the quiz and answer key text files.</p>
</li>
<li class="listitem">
<p class="calibre4">Use <code class="literal1">random.shuffle()</code> to randomize the order of the questions and multiple-choice options.</p>
</li>
</ul>
</div>
<div class="book" title="Step 1: Store the Quiz Data in a Dictionary">
<div class="titlepage">
<div class="book">
<div class="book">
<h2 class="title3"><a id="calibre_link-2730" class="firstname"></a>Step 1: Store the Quiz Data in a Dictionary</h2>
</div>
</div>
</div>
<p class="calibre4"><a id="calibre_link-1427" class="calibre1"></a>The first step is to create a skeleton script and fill it with your quiz data. Create a file named <span class="calibre1"><em class="calibre5">randomQuizGenerator.py</em></span>, and make it look like the following:</p>
<p><a id="calibre_link-2731" class="calibre1"></a>
</p><pre class="programlisting">   #! python3
   # randomQuizGenerator.py - Creates quizzes with questions and answers in
   # random order, along with the answer key.

❶ import random

   # The quiz data. Keys are states and values are their capitals.
❷ capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New
   Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West
   Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

   # Generate 35 quiz files.
❸ for quizNum in range(35):
       # TODO: Create the quiz and answer key files.

       # TODO: Write out the header for the quiz.

       # TODO: Shuffle the order of the states.

       # TODO: Loop through all 50 states, making a question for each.</pre>
<p class="calibre4">Since this program will be randomly ordering the questions and answers, you’ll need to import the <code class="literal1">random</code> module ❶ to make use of its functions. The <code class="literal1">capitals</code> variable ❷ contains a dictionary with US states as keys and their capitals as values. And since you want to create 35 quizzes, the code that actually generates the quiz and answer key files (marked with <code class="literal1">TODO</code> comments for now) will go inside a <code class="literal1">for</code> loop that loops 35 times ❸. (This number can be changed to generate any number of quiz files.)</p>
</div>
<div class="book" title="Step 2: Create the Quiz File and Shuffle the Question Order">
<div class="titlepage">
<div class="book">
<div class="book">
<h2 class="title3"><a id="calibre_link-2732" class="firstname"></a>Step 2: Create the Quiz File and Shuffle the Question Order</h2>
</div>
</div>
</div>
<p class="calibre4"><a id="calibre_link-1428" class="calibre1"></a><a id="calibre_link-1429" class="calibre1"></a>Now it’s time to start filling in those <code class="literal1">TODO</code>s.</p>
<p class="calibre4">The code in the loop will be repeated 35 times—once for each quiz—so you have to worry about only one quiz at a time within the loop. First you’ll create the actual quiz file. It needs to have a unique filename and should also have some kind of standard header in it, with places for the student to fill in a name, date, and class period. Then you’ll need to get a list of states in randomized order, which can be used later to create the questions and answers for the quiz.</p>
<p class="calibre4">Add the following lines of code to <span class="calibre1"><em class="calibre5">randomQuizGenerator.py</em></span>:</p>
<p><a id="calibre_link-2733" class="calibre1"></a>
</p><pre class="programlisting">   #! python3
   # randomQuizGenerator.py - Creates quizzes with questions and answers in
   # random order, along with the answer key.

   --<span class="calibre1"><em class="literal3">snip</em></span>--

   # Generate 35 quiz files.
   for quizNum in range(35):
       <span class="calibre1"><strong class="literal"># Create the quiz and answer key files.</strong></span>
❶     <span class="calibre1"><strong class="literal">quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')</strong></span>
❷     <span class="calibre1"><strong class="literal">answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')</strong></span>

       <span class="calibre1"><strong class="literal"># Write out the header for the quiz.</strong></span>
❸     <span class="calibre1"><strong class="literal">quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')</strong></span>
       <span class="calibre1"><strong class="literal">quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))</strong></span>
       <span class="calibre1"><strong class="literal">quizFile.write('\n\n')</strong></span>

       <span class="calibre1"><strong class="literal"># Shuffle the order of the states.</strong></span>
       <span class="calibre1"><strong class="literal">states = list(capitals.keys())</strong></span>
❹     <span class="calibre1"><strong class="literal">random.shuffle(states)</strong></span>

       # TODO: Loop through all 50 states, making a question for each.</pre>
<p class="calibre4">The filenames for the quizzes will be <span class="calibre1"><em class="calibre5">capitalsquiz&lt;N&gt;.txt</em></span>, where <span class="calibre1"><em class="calibre5">&lt;N&gt;</em></span> is a unique number for the quiz that comes from <code class="literal1">quizNum</code>, the <code class="literal1">for</code> loop’s counter. The answer key for <span class="calibre1"><em class="calibre5">capitalsquiz&lt;N&gt;.txt</em></span> will be stored in a text file named <span class="calibre1"><em class="calibre5">capitalsquiz_answers&lt;N&gt;.txt</em></span>. Each time through the loop, the <code class="literal1">%s</code> placeholder in <code class="literal1">'capitalsquiz%s.txt'</code> and <code class="literal1">'capitalsquiz_answers%s.txt'</code> will be replaced by <code class="literal1">(quizNum + 1)</code>, so the first quiz and answer key created will be <span class="calibre1"><em class="calibre5">capitalsquiz1.txt</em></span> and <span class="calibre1"><em class="calibre5">capitalsquiz_answers1.txt</em></span>. These files will be created with calls to the <code class="literal1">open()</code> function at ❶ and ❷, with <code class="literal1">'w'</code> as the second argument to open them in write mode.</p>
<p class="calibre4">The <code class="literal1">write()</code> statements at ❸ create a quiz header for the student to fill out. Finally, a randomized list of US states is created with the help of the <code class="literal1">random.shuffle()</code> function ❹, which randomly reorders the values in any list that is passed to it.</p>
</div>
<div class="book" title="Step 3: Create the Answer Options">
<div class="titlepage">
<div class="book">
<div class="book">
<h2 class="title3"><a id="calibre_link-2734" class="firstname"></a>Step 3: Create the Answer Options</h2>
</div>
</div>
</div>
<p class="calibre4"><a id="calibre_link-1430" class="calibre1"></a><a id="calibre_link-1431" class="calibre1"></a>Now you need to generate the answer options for each question, which will be multiple choice from A to D. You’ll need to create another <code class="literal1">for</code> loop—this one to generate the content for each of the 50 questions on the quiz. Then there will be a third <code class="literal1">for</code> loop nested inside to generate the multiple-choice options for each question. Make your code look like the following:</p>
<p><a id="calibre_link-2735" class="calibre1"></a>
</p><pre class="programlisting">   #! python3
   # randomQuizGenerator.py - Creates quizzes with questions and answers in
   # random order, along with the answer key.

   --<span class="calibre1"><em class="literal3">snip</em></span>--

       <span class="calibre1"><strong class="literal"># Loop through all 50 states, making a question for each.</strong></span>
       <span class="calibre1"><strong class="literal">for questionNum in range(50):</strong></span>

           <span class="calibre1"><strong class="literal"># Get right and wrong answers.</strong></span>
❶         <span class="calibre1"><strong class="literal">correctAnswer = capitals[states[questionNum]]</strong></span>
❷         <span class="calibre1"><strong class="literal">wrongAnswers = list(capitals.values())</strong></span>
❸         <span class="calibre1"><strong class="literal">del wrongAnswers[wrongAnswers.index(correctAnswer)]</strong></span>
❹         <span class="calibre1"><strong class="literal">wrongAnswers = random.sample(wrongAnswers, 3)</strong></span>
❺         <span class="calibre1"><strong class="literal">answerOptions = wrongAnswers + [correctAnswer]</strong></span>
❻         <span class="calibre1"><strong class="literal">random.shuffle(answerOptions)</strong></span>

           <span class="calibre1"><strong class="literal"># TODO: Write the question and answer options to the quiz file.</strong></span>

           <span class="calibre1"><strong class="literal"># TODO: Write the answer key to a file.</strong></span></pre>
<p class="calibre4">The correct answer is easy to get—it’s stored as a value in the <code class="literal1">capitals</code> dictionary ❶. This loop will loop through the states in the shuffled <code class="literal1">states</code> list, from <code class="literal1">states[0]</code> to <code class="literal1">states[49]</code>, find each state in <code class="literal1">capitals</code>, and store that state’s corresponding capital in <code class="literal1">correctAnswer</code>.</p>
<p class="calibre4">The list of possible wrong answers is trickier. You can get it by duplicating <span class="calibre1"><em class="calibre5">all</em></span> the values in the <code class="literal1">capitals</code> dictionary ❷, deleting the correct answer ❸, and selecting three random values from this list ❹. The <code class="literal1">random.sample()</code> function makes it easy to do this selection. Its first argument is the list you want to select from; the second argument is the number of values you want to select. The full list of answer options is the combination of these three wrong answers with the correct answers ❺. Finally, the answers need to be randomized ❻ so that the correct response isn’t always choice D.</p>
</div>
<div class="book" title="Step 4: Write Content to the Quiz and Answer Key Files">
<div class="titlepage">
<div class="book">
<div class="book">
<h2 class="title3"><a id="calibre_link-2736" class="firstname"></a>Step 4: Write Content to the Quiz and Answer Key Files</h2>
</div>
</div>
</div>
<p class="calibre4">All that is left is to write the question to the quiz file and the answer to the answer key file. Make your code look like the following:</p>
<p><a id="calibre_link-2737" class="calibre1"></a>
</p><pre class="programlisting">   #! python3
   # randomQuizGenerator.py - Creates quizzes with questions and answers in
   # random order, along with the answer key.

   --<span class="calibre1"><em class="literal3">snip</em></span>--
       # Loop through all 50 states, making a question for each.
       for questionNum in range(50):
           --<span class="calibre1"><em class="literal3">snip</em></span>--

           <span class="calibre1"><strong class="literal"># Write the question and the answer options to the quiz file.</strong></span>
           <span class="calibre1"><strong class="literal">quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1,</strong></span>
               <span class="calibre1"><strong class="literal">states[questionNum]))</strong></span>
❶         <span class="calibre1"><strong class="literal">for i in range(4):</strong></span>
❷             <span class="calibre1"><strong class="literal">quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))</strong></span>
           <span class="calibre1"><strong class="literal">quizFile.write('\n')</strong></span>

           <span class="calibre1"><strong class="literal"># Write the answer key to a file.</strong></span>
❸         <span class="calibre1"><strong class="literal">answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[</strong></span>
              <span class="calibre1"><strong class="literal">answerOptions.index(correctAnswer)]))</strong></span>
       <span class="calibre1"><strong class="literal">quizFile.close()</strong></span>
       <span class="calibre1"><strong class="literal">answerKeyFile.close()</strong></span></pre>
<p class="calibre4">A <code class="literal1">for</code> loop that goes through integers <code class="literal1">0</code> to <code class="literal1">3</code> will write the answer options in the <code class="literal1">answerOptions</code> list ❶. The expression <code class="literal1">'ABCD'[i]</code> at ❷ treats the string <code class="literal1">'ABCD'</code> as an array and will evaluate to <code class="literal1">'A'</code>,<code class="literal1">'B'</code>, <code class="literal1">'C'</code>, and then <code class="literal1">'D'</code> on each respective iteration through the loop.</p>
<p class="calibre4">In the final line ❸, the expression <code class="literal1">answerOptions.index(correctAnswer)</code> will find the integer index of the correct answer in the randomly ordered answer options, and <code class="literal1">'ABCD'[answerOptions.index(correctAnswer)]</code> will evaluate to the correct answer’s letter to be written to the answer key file.</p>
<p class="calibre4">After you run the program, this is how your <span class="calibre1"><em class="calibre5">capitalsquiz1.txt</em></span> file will look, though of course your questions and answer options may be different from those shown here, depending on the outcome of your <code class="literal1">random.shuffle()</code> calls:</p>
<p><a id="calibre_link-2738" class="calibre1"></a>
</p><pre class="programlisting">Name:

Date:

Period:

                    State Capitals Quiz (Form 1)

1. What is the capital of West Virginia?
    A. Hartford
    B. Santa Fe
    C. Harrisburg
    D. Charleston

2. What is the capital of Colorado?
    A. Raleigh
    B. Harrisburg
    C. Denver
    D. Lincoln

--<span class="calibre1"><em class="literal3">snip</em></span>--</pre>
<p class="calibre4"><a id="calibre_link-640" class="calibre1"></a><a id="calibre_link-1126" class="calibre1"></a><a id="calibre_link-1127" class="calibre1"></a><a id="calibre_link-1331" class="calibre1"></a>The corresponding <span class="calibre1"><em class="calibre5">capitalsquiz_answers1.txt</em></span> text file will look like this:</p>
<p><a id="calibre_link-2739" class="calibre1"></a>
</p><pre class="programlisting">1. D
2. C
3. A
4. C
--<span class="calibre1"><em class="literal3">snip</em></span>--</pre>
</div>
</div>
<div class="book" title="Project: Multiclipboard">
<div class="titlepage">
<div class="book">
<div class="book">
<h1 class="title2"><a id="calibre_link-2740" class="firstname"></a>Project: Multiclipboard</h1>
</div>
</div>
</div>
<p class="calibre4">Say you have the boring task of filling out many forms in a web page or software with several text fields. The clipboard saves you from typing the same text over and over again. But only one thing can be on the clipboard at a time. If you have several different pieces of text that you need to copy and paste, you have to keep highlighting and copying the same few things over and over again.</p>
<p class="calibre4">You can write a Python program to keep track of multiple pieces of text. This “multiclipboard” will be named <span class="calibre1"><em class="calibre5">mcb.pyw</em></span> (since “mcb” is shorter to type than “multiclipboard”). The <span class="calibre1"><em class="calibre5">.pyw</em></span> extension means that Python won’t show a Terminal window when it runs this program. (See Appendix B for more details.)</p>
<p class="calibre4">The program will save each piece of clipboard text under a keyword. For example, when you run <code class="literal1">py mcb.pyw save spam</code>, the current contents of the clipboard will be saved with the keyword <span class="calibre1"><em class="calibre5">spam</em></span>. This text can later be loaded to the clipboard again by running <code class="literal1">py mcb.pyw spam</code>. And if the user forgets what keywords they have, they can run <code class="literal1">py mcb.pyw list</code> to copy a list of all keywords to the clipboard.</p>
<p class="calibre4">Here’s what the program does:</p>
<div class="book">
<ul class="itemizedlist">
<li class="listitem">
<p class="calibre4">The command line argument for the keyword is checked.</p>
</li>
<li class="listitem">
<p class="calibre4">If the argument is <code class="literal1">save</code>, then the clipboard contents are saved to the keyword.</p>
</li>
<li class="listitem">
<p class="calibre4">If the argument is <code class="literal1">list</code>, then all the keywords are copied to the clipboard.</p>
</li>
<li class="listitem">
<p class="calibre4">Otherwise, the text for the keyword is copied to the clipboard.</p>
</li>
</ul>
</div>
<p class="calibre4">This means the code will need to do the following:</p>
<div class="book">
<ul class="itemizedlist">
<li class="listitem">
<p class="calibre4">Read the command line arguments from <code class="literal1">sys.argv</code>.</p>
</li>
<li class="listitem">
<p class="calibre4">Read and write to the clipboard.</p>
</li>
<li class="listitem">
<p class="calibre4">Save and load to a shelf file.</p>
</li>
</ul>
</div>
<p class="calibre4">If you use Windows, you can easily run this script from the Run... window by creating a batch file named <span class="calibre1"><em class="calibre5">mcb.bat</em></span> with the following content:</p>
<p><a id="calibre_link-2741" class="calibre1"></a>
</p><pre class="programlisting">@pyw.exe C:\Python34\mcb.pyw %*</pre>
<div class="book" title="Step 1: Comments and Shelf Setup">
<div class="titlepage">
<div class="book">
<div class="book">
<h2 class="title3"><a id="calibre_link-2742" class="firstname"></a>Step 1: Comments and Shelf Setup</h2>
</div>
</div>
</div>
<p class="calibre4"><a id="calibre_link-1128" class="calibre1"></a><a id="calibre_link-1129" class="calibre1"></a>Let’s start by making a skeleton script with some comments and basic setup. Make your code look like the following:</p>
<p><a id="calibre_link-2743" class="calibre1"></a>
</p><pre class="programlisting">   #! python3
   # mcb.pyw - Saves and loads pieces of text to the clipboard.
❶ # Usage: py.exe mcb.pyw save &lt;keyword&gt; - Saves clipboard to keyword.
   #        py.exe mcb.pyw &lt;keyword&gt; - Loads keyword to clipboard.
   #        py.exe mcb.pyw list - Loads all keywords to clipboard.

❷ import shelve, pyperclip, sys

❸ mcbShelf = shelve.open('mcb')

   # TODO: Save clipboard content.

   # TODO: List keywords and load content.

   mcbShelf.close()</pre>
<p class="calibre4">It’s common practice to put general usage information in comments at the top of the file ❶. If you ever forget how to run your script, you can always look at these comments for a reminder. Then you import your modules ❷. Copying and pasting will require the <code class="literal1">pyperclip</code> module, and reading the command line arguments will require the <code class="literal1">sys</code> module. The <code class="literal1">shelve</code> module will also come in handy: Whenever the user wants to save a new piece of clipboard text, you’ll save it to a shelf file. Then, when the user wants to paste the text back to their clipboard, you’ll open the shelf file and load it back into your program. The shelf file will be named with the prefix <span class="calibre1"><em class="calibre5">mcb</em></span> ❸.</p>
</div>
<div class="book" title="Step 2: Save Clipboard Content with a Keyword">
<div class="titlepage">
<div class="book">
<div class="book">
<h2 class="title3"><a id="calibre_link-2744" class="firstname"></a>Step 2: Save Clipboard Content with a Keyword</h2>
</div>
</div>
</div>
<p class="calibre4">The program does different things depending on whether the user wants to save text to a keyword, load text into the clipboard, or list all the existing keywords. Let’s deal with that first case. Make your code look like the following:</p>
<p><a id="calibre_link-2745" class="calibre1"></a>
</p><pre class="programlisting">   #! python3
   # mcb.pyw - Saves and loads pieces of text to the clipboard.
   --<span class="calibre1"><em class="literal3">snip</em></span>--

   <span class="calibre1"><strong class="literal"># Save clipboard content.</strong></span>
❶ <span class="calibre1"><strong class="literal">if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':</strong></span>
❷         <span class="calibre1"><strong class="literal">mcbShelf[sys.argv[2]] = pyperclip.paste()</strong></span>
   <span class="calibre1"><strong class="literal">elif len(sys.argv) == 2:</strong></span>
❸    # TODO: List keywords and load content.

   mcbShelf.close()</pre>
<p class="calibre4"><a id="calibre_link-1130" class="calibre1"></a><a id="calibre_link-1131" class="calibre1"></a>If the first command line argument (which will always be at index <code class="literal1">1</code> of the <code class="literal1">sys.argv</code> list) is <code class="literal1">'save'</code> ❶, the second command line argument is the keyword for the current content of the clipboard. The keyword will be used as the key for <code class="literal1">mcbShelf</code>, and the value will be the text currently on the clipboard ❷.</p>
<p class="calibre4">If there is only one command line argument, you will assume it is either <code class="literal1">'list'</code> or a keyword to load content onto the clipboard. You will implement that code later. For now, just put a <code class="literal1">TODO</code> comment there ❸.</p>
</div>
<div class="book" title="Step 3: List Keywords and Load a Keyword’s Content">
<div class="titlepage">
<div class="book">
<div class="book">
<h2 class="title3"><a id="calibre_link-2746" class="firstname"></a>Step 3: List Keywords and Load a Keyword’s Content</h2>
</div>
</div>
</div>
<p class="calibre4">Finally, let’s implement the two remaining cases: The user wants to load clipboard text in from a keyword, or they want a list of all available keywords. Make your code look like the following:</p>
<p><a id="calibre_link-2747" class="calibre1"></a>
</p><pre class="programlisting">   #! python3
   # mcb.pyw - Saves and loads pieces of text to the clipboard.
   --<span class="calibre1"><em class="literal3">snip</em></span>--

   # Save clipboard content.
   if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
           mcbShelf[sys.argv[2]] = pyperclip.paste()
   elif len(sys.argv) == 2:
       <span class="calibre1"><strong class="literal"># List keywords and load content.</strong></span>
❶     <span class="calibre1"><strong class="literal">if sys.argv[1].lower() == 'list':</strong></span>
❷         <span class="calibre1"><strong class="literal">pyperclip.copy(str(list(mcbShelf.keys())))</strong></span>
       <span class="calibre1"><strong class="literal">elif sys.argv[1] in mcbShelf:</strong></span>
❸         <span class="calibre1"><strong class="literal">pyperclip.copy(mcbShelf[sys.argv[1]])</strong></span>

   mcbShelf.close()</pre>
<p class="calibre4">If there is only one command line argument, first let’s check whether it’s <code class="literal1">'list'</code> ❶. If so, a string representation of the list of shelf keys will be copied to the clipboard ❷. The user can paste this list into an open text editor to read it.</p>
<p class="calibre4">Otherwise, you can assume the command line argument is a keyword. If this keyword exists in the <code class="literal1">mcbShelf</code> shelf as a key, you can load the value onto the clipboard ❸.</p>
<p class="calibre4">And that’s it! Launching this program has different steps depending on what operating system your computer uses. See Appendix B for details for your operating system.</p>
<p class="calibre4">Recall the password locker program you created in <a class="ulink" href="https://automatetheboringstuff.com/chapter6" title="Chapter 6. Manipulating Strings">Chapter&nbsp;6</a> that stored the passwords in a dictionary. Updating the passwords required changing the source code of the program. This isn’t ideal because average users don’t feel comfortable changing source code to update their software. Also, every time you modify the source code to a program, you run the risk of accidentally introducing new bugs. By storing the data for a program in a different place than the code, you can make your programs easier for others to use and more resistant to bugs.</p>
</div>
</div>
<div class="book" title="Summary">
<div class="titlepage">
<div class="book">
<div class="book">
<h1 class="title2"><a id="calibre_link-2748" class="firstname"></a>Summary</h1>
</div>
</div>
</div>
<p class="calibre4">Files are organized into folders (also called directories), and a path describes the location of a file. Every program running on your computer has a current working directory, which allows you to specify file paths relative to the current location instead of always typing the full (or absolute) path. The <code class="literal1">os.path</code> module has many functions for manipulating file paths.</p>
<p class="calibre4">Your programs can also directly interact with the contents of text files. The <code class="literal1">open()</code> function can open these files to read in their contents as one large string (with the <code class="literal1">read()</code> method) or as a list of strings (with the <code class="literal1">readlines()</code> method). The <code class="literal1">open()</code> function can open files in write or append mode to create new text files or add to existing text files, respectively.</p>
<p class="calibre4">In previous chapters, you used the clipboard as a way of getting large amounts of text into a program, rather than typing it all in. Now you can have your programs read files directly from the hard drive, which is a big improvement, since files are much less volatile than the clipboard.</p>
<p class="calibre4">In the next chapter, you will learn how to handle the files themselves, by copying them, deleting them, renaming them, moving them, and more.</p>
</div>
<div class="book" title="Practice Questions">
<div class="titlepage">
<div class="book">
<div class="book">
<h1 class="title2"><a id="calibre_link-2749" class="firstname"></a>Practice Questions</h1>
</div>
</div>
</div>
<div class="book" title="Frequently Asked Questions"><a id="calibre_link-2750" class="calibre1"></a><br>
<table border="0" width="100%" summary="Q and A Set" class="calibre22">
<colgroup><col width="1%" class="calibre23">
<col class="calibre11">
</colgroup><tbody class="calibre16">
<tr class="calibre13" title="Q:">
<td valign="top" class="calibre21"><a id="calibre_link-2751" class="calibre1"></a><a id="calibre_link-2752" class="calibre1"></a>
<p class="calibre4">Q:</p>
</td>
<td valign="top" class="calibre21">
<p class="calibre4">1. What is a relative path relative to?</p>
</td>
</tr>
<tr class="calibre19" title="Q:">
<td valign="top" class="calibre21"><a id="calibre_link-2753" class="calibre1"></a><a id="calibre_link-2754" class="calibre1"></a>
<p class="calibre4">Q:</p>
</td>
<td valign="top" class="calibre21">
<p class="calibre4">2. What does an absolute path start with?</p>
</td>
</tr>
<tr class="calibre13" title="Q:">
<td valign="top" class="calibre21"><a id="calibre_link-2755" class="calibre1"></a><a id="calibre_link-2756" class="calibre1"></a>
<p class="calibre4">Q:</p>
</td>
<td valign="top" class="calibre21">
<p class="calibre4">3. What do the <code class="literal2">os.getcwd()</code> and <code class="literal2">os.chdir()</code> functions do?</p>
</td>
</tr>
<tr class="calibre19" title="Q:">
<td valign="top" class="calibre21"><a id="calibre_link-2757" class="calibre1"></a><a id="calibre_link-2758" class="calibre1"></a>
<p class="calibre4">Q:</p>
</td>
<td valign="top" class="calibre21">
<p class="calibre4">4. What are the <code class="literal2">.</code> and <code class="literal2">..</code> folders?</p>
</td>
</tr>
<tr class="calibre13" title="Q:">
<td valign="top" class="calibre21"><a id="calibre_link-2759" class="calibre1"></a><a id="calibre_link-2760" class="calibre1"></a>
<p class="calibre4">Q:</p>
</td>
<td valign="top" class="calibre21">
<p class="calibre4">5. In <span class="calibre1"><em class="calibre5">C:\bacon\eggs\spam.txt</em></span>, which part is the dir name, and which part is the base name?</p>
</td>
</tr>
<tr class="calibre19" title="Q:">
<td valign="top" class="calibre21"><a id="calibre_link-2761" class="calibre1"></a><a id="calibre_link-2762" class="calibre1"></a>
<p class="calibre4">Q:</p>
</td>
<td valign="top" class="calibre21">
<p class="calibre4">6. What are the three “mode” arguments that can be passed to the <code class="literal2">open()</code> function?</p>
</td>
</tr>
<tr class="calibre13" title="Q:">
<td valign="top" class="calibre21"><a id="calibre_link-2763" class="calibre1"></a><a id="calibre_link-2764" class="calibre1"></a>
<p class="calibre4">Q:</p>
</td>
<td valign="top" class="calibre21">
<p class="calibre4">7. What happens if an existing file is opened in write mode?</p>
</td>
</tr>
<tr class="calibre19" title="Q:">
<td valign="top" class="calibre21"><a id="calibre_link-2765" class="calibre1"></a><a id="calibre_link-2766" class="calibre1"></a>
<p class="calibre4">Q:</p>
</td>
<td valign="top" class="calibre21">
<p class="calibre4">8. What is the difference between the <code class="literal2">read()</code> and <code class="literal2">readlines()</code> methods?</p>
</td>
</tr>
<tr class="calibre13" title="Q:">
<td valign="top" class="calibre21"><a id="calibre_link-2767" class="calibre1"></a><a id="calibre_link-2768" class="calibre1"></a>
<p class="calibre4">Q:</p>
</td>
<td valign="top" class="calibre21">
<p class="calibre4">9. What data structure does a shelf value resemble?</p>
</td>
</tr>
</tbody>
</table>
</div>
</div>
<div class="book" title="Practice Projects">
<div class="titlepage">
<div class="book">
<div class="book">
<h1 class="title2"><a id="calibre_link-2769" class="firstname"></a>Practice Projects</h1>
</div>
</div>
</div>
<p class="calibre4">For practice, design and write the following programs.</p>
<div class="book" title="Extending the Multiclipboard">
<div class="titlepage">
<div class="book">
<div class="book">
<h2 class="title3"><a id="calibre_link-2770" class="firstname"></a>Extending the Multiclipboard</h2>
</div>
</div>
</div>
<p class="calibre4">Extend the multiclipboard program in this chapter so that it has a <code class="literal1">delete &lt;keyword&gt;</code> command line argument that will delete a keyword from the shelf. Then add a <code class="literal1">delete</code> command line argument that will delete <span class="calibre1"><em class="calibre5">all</em></span> keywords.</p>
</div>
<div class="book" title="Mad Libs">
<div class="titlepage">
<div class="book">
<div class="book">
<h2 class="title3"><a id="calibre_link-2771" class="firstname"></a>Mad Libs</h2>
</div>
</div>
</div>
<p class="calibre4">Create a Mad Libs program that reads in text files and lets the user add their own text anywhere the word <span class="calibre1"><em class="calibre5">ADJECTIVE</em></span>, <span class="calibre1"><em class="calibre5">NOUN</em></span>, <span class="calibre1"><em class="calibre5">ADVERB</em></span>, or <span class="calibre1"><em class="calibre5">VERB</em></span> appears in the text file. For example, a text file may look like this:</p>
<p><a id="calibre_link-2772" class="calibre1"></a>
</p><pre class="programlisting">The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.</pre>
<p class="calibre4">The program would find these occurrences and prompt the user to replace them.</p>
<p><a id="calibre_link-2773" class="calibre1"></a>
</p><pre class="programlisting">Enter an adjective:
<span class="calibre1"><strong class="literal">silly</strong></span>
Enter a noun:
<span class="calibre1"><strong class="literal">chandelier</strong></span>
Enter a verb:
<span class="calibre1"><strong class="literal">screamed</strong></span>
Enter a noun:
<span class="calibre1"><strong class="literal">pickup truck</strong></span></pre>
<p class="calibre4">The following text file would then be created:</p>
<p><a id="calibre_link-2774" class="calibre1"></a>
</p><pre class="programlisting">The silly panda walked to the chandelier and then screamed. A nearby pickup
truck was unaffected by these events.</pre>
<p class="calibre4">The results should be printed to the screen and saved to a new text file.</p>
</div>
<div class="book" title="Regex Search">
<div class="titlepage">
<div class="book">
<div class="book">
<h2 class="title3"><a id="calibre_link-2775" class="firstname"></a>Regex Search</h2>
</div>
</div>
</div>
<p class="calibre4">Write a program that opens all .<span class="calibre1"><em class="calibre5">txt</em></span> files in a folder and searches for any line that matches a user-supplied regular expression. The results should be printed to the screen.</p>
</div>
</div>
</div>
</div>
<p></p><center><a href="https://automatetheboringstuff.com/chapter7"><img src="./statequiz_files/prev.png"></a><a href="https://automatetheboringstuff.com/#toc"><img src="./statequiz_files/toc.png"></a><a href="https://automatetheboringstuff.com/chapter9"><img src="./statequiz_files/next.png"></a><p></p>
			</center></div><!-- .entry-content -->
</article><!-- #post-## -->

				


	<div><center>Support the author by purchasing the print/ebook bundle from <a href="https://www.nostarch.com/automatestuff">No Starch Press</a> or separately on <a href="http://www.amazon.com/gp/product/1593275994/ref=as_li_tl?ie=UTF8&amp;camp=1789&amp;creative=9325&amp;creativeASIN=1593275994&amp;linkCode=as2&amp;tag=playwithpyth-20&amp;linkId=HDM7V3T6RHC5VVN4">Amazon</a>.</center></div>

	<div><center><a href="http://www.amazon.com/gp/product/1593275994/ref=as_li_tl?ie=UTF8&amp;camp=1789&amp;creative=9325&amp;creativeASIN=1593275994&amp;linkCode=as2&amp;tag=playwithpyth-20&amp;linkId=HDM7V3T6RHC5VVN4"><img src="./statequiz_files/automate_small_cover.png" alt="Automate the Boring Stuff book cover thumbnail"></a></center></div>

	<div><center>Read the author's other Creative Commons licensed Python books.</center></div>

	<div><center>
		<a href="https://turtleappstore.com/book"><img src="./statequiz_files/cover_codingwithminecraft_thumb.png" alt="Coding with Minecraft book cover thumbnail" style="width: 150px"></a>

        <a href="https://inventwithpython.com/cracking/"><img src="./statequiz_files/cover_crackingcodes_thumb.png" alt="Cracking Codes with Python book cover thumbnail" style="width: 150px"></a>

        <a href="https://inventwithpython.com/invent4thed"><img src="./statequiz_files/cover_invent4th_thumb.png" alt="Invent with Python book cover thumbnail" style="width: 150px"></a>

        <a href="https://inventwithscratch.com/book/"><img src="./statequiz_files/cover_scratchprogrammingplayground_thumb.jpg" alt="Scratch Programming Playground book cover thumbnail" style="width: 150px"></a>

		<a href="https://inventwithpython.com/pygame/"><img src="./statequiz_files/cover_makinggames_thumb.png" alt="Making Games with Python and Pygame book cover thumbnail" style="width: 150px"></a>

		</center>
	</div>

  </div>


</body></html>
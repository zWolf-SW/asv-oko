#!/usr/bin/haserl
<%in _common.cgi %>
<%
get_system_info
page_title="$tPageTitlePreviewHelp"
%>
<%in _header.cgi %>
<p class="small">&#1044;&#1086;&#1089;&#1090;&#1091;&#1087;&#1085;&#1072; &#1087;&#1086;&#1076;&#1088;&#1086;&#1073;&#1085;&#1072;&#1103; &#1080;&#1085;&#1092;&#1086;&#1088;&#1084;&#1072;&#1094;&#1080;&#1103;<a href="https://github.com/OpenIPC/wiki/blob/master/en/majestic-streamer.md">in the wiki</a>.</p>
<div class="row row-cols-1 row-cols-md-2 g-4">
  <div class="col">
    <div class="card h-100 mb-3">
      <div class="card-header">&#1042;&#1077;&#1073;-&#1089;&#1090;&#1088;&#1072;&#1085;&#1080;&#1094;&#1072;</div>
      <div class="card-body small">
        <dl>
          <dt>http://<%= $ipaddr %>/</dt>
          <dd>&#1055;&#1088;&#1103;&#1084;&#1072;&#1103; &#1090;&#1088;&#1072;&#1085;&#1089;&#1083;&#1103;&#1094;&#1080;&#1103; HLS &#8212; &#1074; &#1074;&#1077;&#1073;-&#1073;&#1088;&#1072;&#1091;&#1079;&#1077;&#1088;.</dd>
          <dt>http://<%= $ipaddr %>/mjpeg.html</dt>
          <dd>MJPEG & MP3  &#8212; &#1074; &#1074;&#1077;&#1073;-&#1073;&#1088;&#1072;&#1091;&#1079;&#1077;&#1088;.</dd>
        </dl>
      </div>
    </div>
  </div>
  <div class="col">
    <div class="card h-100 mb-3">
      <div class="card-header">&#1042;&#1080;&#1076;&#1077;&#1086;&#1087;&#1086;&#1090;&#1086;&#1082;&#1080;</div>
      <div class="card-body small">
        <dl>
          <dt>http://<%= $ipaddr %>/mjpeg</dt>
          <dd>MJPEG &#1042;&#1080;&#1076;&#1077;&#1086;&#1087;&#1086;&#1090;&#1086;&#1082;</dd>
          <dt>http://<%= $ipaddr %>/video.mp4</dt>
          <dd>fMP4 &#1042;&#1080;&#1076;&#1077;&#1086;&#1087;&#1086;&#1090;&#1086;&#1082;</dd>
          <dt>rtsp://<%= $ipaddr %>/stream=0</dt>
          <dd>RTSP &#1086;&#1089;&#1085;&#1086;&#1074;&#1085;&#1086;&#1081; &#1042;&#1080;&#1076;&#1077;&#1086;&#1087;&#1086;&#1090;&#1086;&#1082; ("video0").</dd>
          <dt>rtsp://<%= $ipaddr %>/stream=1</dt>
          <dd>RTSP &#1074;&#1090;&#1086;&#1088;&#1080;&#1095;&#1085;&#1099;&#1081; &#1042;&#1080;&#1076;&#1077;&#1086;&#1087;&#1086;&#1090;&#1086;&#1082; ("video1").</dd>
        </dl>
      </div>
    </div>
  </div>
  <div class="col">
    <div class="card h-100 mb-3">
      <div class="card-header">&#1050;&#1072;&#1076;&#1088;&#1099;</div>
      <div class="card-body small">
        <dl>
          <dt>http://<%= $ipaddr %>/image.jpg</dt>
          <dd>&#1057;&#1085;&#1080;&#1084;&#1086;&#1082; &#1074; &#1092;&#1086;&#1088;&#1084;&#1072;&#1090;&#1077; JPEG.<br>
            &#1044;&#1086;&#1087;&#1086;&#1083;&#1085;&#1080;&#1090;&#1077;&#1083;&#1100;&#1085;&#1099;&#1077; &#1087;&#1072;&#1088;&#1072;&#1084;&#1077;&#1090;&#1088;&#1099;:
            <ul class="small">
              <li>width, height - &#1088;&#1072;&#1079;&#1084;&#1077;&#1088; &#1088;&#1077;&#1079;&#1091;&#1083;&#1100;&#1090;&#1080;&#1088;&#1091;&#1102;&#1097;&#1077;&#1075;&#1086; &#1080;&#1079;&#1086;&#1073;&#1088;&#1072;&#1078;&#1077;&#1085;&#1080;&#1103;</li>
              <li>qfactor - JPEG &#1092;&#1072;&#1082;&#1090;&#1086;&#1088; &#1082;&#1072;&#1095;&#1077;&#1089;&#1090;&#1074;&#1072; (1-99)</li>
              <li>color2gray - &#1087;&#1088;&#1077;&#1086;&#1073;&#1088;&#1072;&#1079;&#1086;&#1074;&#1072;&#1090;&#1100; &#1074; &#1086;&#1090;&#1090;&#1077;&#1085;&#1082;&#1080; &#1089;&#1077;&#1088;&#1086;&#1075;&#1086;</li>
              <li>crop - &#1086;&#1073;&#1088;&#1077;&#1079;&#1072;&#1090;&#1100; &#1087;&#1086;&#1083;&#1091;&#1095;&#1077;&#1085;&#1085;&#1086;&#1077; &#1080;&#1079;&#1086;&#1073;&#1088;&#1072;&#1078;&#1077;&#1085;&#1080;&#1077; &#1082;&#1072;&#1082; 16x16x320x320</li>
            </ul>
          </dd>
          <dt>http://<%= $ipaddr %>/image.heif</dt>
          <dd>&#1057;&#1085;&#1080;&#1084;&#1086;&#1082; &#1074; &#1092;&#1086;&#1088;&#1084;&#1072;&#1090;&#1077; HEIF.</dd>
          <dt>http://<%= $ipaddr %>/image.yuv</dt>
          <dd>&#1057;&#1085;&#1080;&#1084;&#1086;&#1082; &#1074; &#1092;&#1086;&#1088;&#1084;&#1072;&#1090;&#1077; YUV420.</dd>
          <dt>http://<%= $ipaddr %>/image.dng</dt>
          <dd>&#1057;&#1085;&#1080;&#1084;&#1086;&#1082; &#1074; &#1092;&#1086;&#1088;&#1084;&#1072;&#1090;&#1077;  Adobe DNG (raw)<br>
            (&#1090;&#1086;&#1083;&#1100;&#1082;&#1086; &#1076;&#1083;&#1103; v>=2 &#1087;&#1088;&#1086;&#1094;&#1077;&#1089;&#1089;&#1086;&#1088;&#1086;&#1074; HiSilicon).</dd>
        </dl>
      </div>
    </div>
  </div>
  <div class="col">
    <div class="card h-100 mb-3">
      <div class="card-header">&#1040;&#1091;&#1076;&#1080;&#1086;&#1087;&#1086;&#1090;&#1086;&#1082;&#1080;</div>
      <div class="card-body small">
        <dl>
          <dt>http://<%= $ipaddr %>/audio.opus</dt>
          <dd>Opus &#1072;&#1091;&#1076;&#1080;&#1086;&#1087;&#1086;&#1090;&#1086;&#1082;.</dd>
          <dt>http://<%= $ipaddr %>/audio.pcm</dt>
          <dd>Raw PCM &#1072;&#1091;&#1076;&#1080;&#1086;&#1087;&#1086;&#1090;&#1086;&#1082;.</dd>
          <dt>http://<%= $ipaddr %>/audio.m4a</dt>
          <dd>AAC &#1072;&#1091;&#1076;&#1080;&#1086;&#1087;&#1086;&#1090;&#1086;&#1082;.</dd>
          <dt>http://<%= $ipaddr %>/audio.mp3</dt>
          <dd>MP3 &#1072;&#1091;&#1076;&#1080;&#1086;&#1087;&#1086;&#1090;&#1086;&#1082;.</dd>
          <dt>http://<%= $ipaddr %>/audio.alaw</dt>
          <dd>A-law &#1089;&#1078;&#1072;&#1090;&#1099;&#1081; &#1072;&#1091;&#1076;&#1080;&#1086;&#1087;&#1086;&#1090;&#1086;&#1082;.</dd>
          <dt>http://<%= $ipaddr %>/audio.ulaw</dt>
          <dd>μ-law &#1089;&#1078;&#1072;&#1090;&#1099;&#1081; &#1072;&#1091;&#1076;&#1080;&#1086;&#1087;&#1086;&#1090;&#1086;&#1082;.</dd>
          <dt>http://<%= $ipaddr %>/audio.g711a</dt>
          <dd>G.711 A-law &#1072;&#1091;&#1076;&#1080;&#1086;&#1087;&#1086;&#1090;&#1086;&#1082;.</dd>
        </dl>
      </div>
    </div>
  </div>
  <div class="col">
    <div class="card h-100">
      <div class="card-header">&#1053;&#1086;&#1095;&#1085;&#1086;&#1081; API</div>
      <div class="card-body small">
        <dl>
          <dt>http://<%= $ipaddr %>/night/on</dt>
          <dd>&#1042;&#1082;&#1083;&#1102;&#1095;&#1080;&#1090;&#1100; &#1085;&#1086;&#1095;&#1085;&#1086;&#1081; &#1088;&#1077;&#1078;&#1080;&#1084;..</dd>
          <dt>http://<%= $ipaddr %>/night/off</dt>
          <dd>&#1042;&#1099;&#1082;&#1083;&#1102;&#1095;&#1080;&#1090;&#1100; &#1085;&#1086;&#1095;&#1085;&#1086;&#1081; &#1088;&#1077;&#1078;&#1080;&#1084;.</dd>
          <dt>http://<%= $ipaddr %>/night/toggle</dt>
          <dd>&#1055;&#1077;&#1088;&#1077;&#1082;&#1083;&#1102;&#1095;&#1080;&#1090;&#1100; &#1090;&#1077;&#1082;&#1091;&#1097;&#1080;&#1081; &#1085;&#1086;&#1095;&#1085;&#1086;&#1081; &#1088;&#1077;&#1078;&#1080;&#1084;.</dd>
        </dl>
      </div>
    </div>
  </div>
  <div class="col">
    <div class="card h-100">
      <div class="card-header">&#1052;&#1086;&#1085;&#1080;&#1090;&#1086;&#1088;&#1080;&#1085;&#1075;</div>
      <div class="card-body small">
        <dl>
          <dt>http://<%= $ipaddr %>/metrics</dt>
          <dd>&#1057;&#1086;&#1074;&#1084;&#1077;&#1089;&#1090;&#1080;&#1084;&#1086;&#1089;&#1090;&#1100; &#1089;&#1086; &#1089;&#1090;&#1072;&#1085;&#1076;&#1072;&#1088;&#1090;&#1085;&#1099;&#1084; &#1101;&#1082;&#1089;&#1087;&#1086;&#1088;&#1090;&#1077;&#1088;&#1086;&#1084; Node &#1080; &#1089;&#1087;&#1077;&#1094;&#1080;&#1092;&#1080;&#1095;&#1085;&#1099;&#1077; &#1076;&#1083;&#1103; &#1087;&#1088;&#1080;&#1083;&#1086;&#1078;&#1077;&#1085;&#1080;&#1103; &#1084;&#1077;&#1090;&#1088;&#1080;&#1082;&#1080; &#1076;&#1083;&#1103; Prometheus. </dd>
        </dl>
      </div>
    </div>
  </div>
</div>
<%in _footer.cgi %>

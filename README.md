<title>Mario Vaccaro - Final exam</title>

<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>



<style type="text/css">
    /*!
*
* Twitter Bootstrap
*
*/
/*!
 * Bootstrap v3.3.7 (http://getbootstrap.com)
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */
/*! normalize.css v3.0.3 | MIT License | github.com/necolas/normalize.css */
html {
  font-family: sans-serif;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
}
body {
  margin: 0;
}
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
main,
menu,
nav,
section,
summary {
  display: block;
}
audio,
canvas,
progress,
video {
  display: inline-block;
  vertical-align: baseline;
}
audio:not([controls]) {
  display: none;
  height: 0;
}
[hidden],
template {
  display: none;
}
a {
  background-color: transparent;
}
a:active,
a:hover {
  outline: 0;
}
abbr[title] {
  border-bottom: 1px dotted;
}
b,
strong {
  font-weight: bold;
}
dfn {
  font-style: italic;
}
h1 {
  font-size: 2em;
  margin: 0.67em 0;
}
mark {
  background: #ff0;
  color: #000;
}
small {
  font-size: 80%;
}
sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}
sup {
  top: -0.5em;
}
sub {
  bottom: -0.25em;
}
img {
  border: 0;
}
svg:not(:root) {
  overflow: hidden;
}
figure {
  margin: 1em 40px;
}
hr {
  box-sizing: content-box;
  height: 0;
}
pre {
  overflow: auto;
}
code,
kbd,
pre,
samp {
  font-family: monospace, monospace;
  font-size: 1em;
}
button,
input,
optgroup,
select,
textarea {
  color: inherit;
  font: inherit;
  margin: 0;
}
button {
  overflow: visible;
}
button,
select {
  text-transform: none;
}
button,
html input[type="button"],
input[type="reset"],
input[type="submit"] {
  -webkit-appearance: button;
  cursor: pointer;
}
button[disabled],
html input[disabled] {
  cursor: default;
}
button::-moz-focus-inner,
input::-moz-focus-inner {
  border: 0;
  padding: 0;
}
input {
  line-height: normal;
}
input[type="checkbox"],
input[type="radio"] {
  box-sizing: border-box;
  padding: 0;
}
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: textfield;
  box-sizing: content-box;
}
input[type="search"]::-webkit-search-cancel-button,
input[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}
fieldset {
  border: 1px solid #c0c0c0;
  margin: 0 2px;
  padding: 0.35em 0.625em 0.75em;
}
legend {
  border: 0;
  padding: 0;
}
textarea {
  overflow: auto;
}
optgroup {
  font-weight: bold;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
td,
th {
  padding: 0;
}
/*! Source: https://github.com/h5bp/html5-boilerplate/blob/master/src/css/main.css */
@media print {
  *,
  *:before,
  *:after {
    background: transparent !important;
    box-shadow: none !important;
    text-shadow: none !important;
  }
  a,
  a:visited {
    text-decoration: underline;
  }
  a[href]:after {
    content: " (" attr(href) ")";
  }
  abbr[title]:after {
    content: " (" attr(title) ")";
  }
  a[href^="#"]:after,
  a[href^="javascript:"]:after {
    content: "";
  }
  pre,
  blockquote {
    border: 1px solid #999;
    page-break-inside: avoid;
  }
  thead {
    display: table-header-group;
  }
  tr,
  img {
    page-break-inside: avoid;
  }
  img {
    max-width: 100% !important;
  }
  p,
  h2,
  h3 {
    orphans: 3;
    widows: 3;
  }
  h2,
  h3 {
    page-break-after: avoid;
  }
  .navbar {
    display: none;
  }
  .btn > .caret,
  .dropup > .btn > .caret {
    border-top-color: #000 !important;
  }
  .label {
    border: 1px solid #000;
  }
  .table {
    border-collapse: collapse !important;
  }
  .table td,
  .table th {
    background-color: #fff !important;
  }
  .table-bordered th,
  .table-bordered td {
    border: 1px solid #ddd !important;
  }
}
@font-face {
  font-family: 'Glyphicons Halflings';
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot');
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot?#iefix') format('embedded-opentype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff2') format('woff2'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff') format('woff'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.ttf') format('truetype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.svg#glyphicons_halflingsregular') format('svg');
}
.glyphicon {
  position: relative;
  top: 1px;
  display: inline-block;
  font-family: 'Glyphicons Halflings';
  font-style: normal;
  font-weight: normal;
  line-height: 1;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.glyphicon-asterisk:before {
  content: "\002a";
}
.glyphicon-plus:before {
  content: "\002b";
}
.glyphicon-euro:before,
.glyphicon-eur:before {
  content: "\20ac";
}
.glyphicon-minus:before {
  content: "\2212";
}
.glyphicon-cloud:before {
  content: "\2601";
}
.glyphicon-envelope:before {
  content: "\2709";
}
.glyphicon-pencil:before {
  content: "\270f";
}
.glyphicon-glass:before {
  content: "\e001";
}
.glyphicon-music:before {
  content: "\e002";
}
.glyphicon-search:before {
  content: "\e003";
}
.glyphicon-heart:before {
  content: "\e005";
}
.glyphicon-star:before {
  content: "\e006";
}
.glyphicon-star-empty:before {
  content: "\e007";
}
.glyphicon-user:before {
  content: "\e008";
}
.glyphicon-film:before {
  content: "\e009";
}
.glyphicon-th-large:before {
  content: "\e010";
}
.glyphicon-th:before {
  content: "\e011";
}
.glyphicon-th-list:before {
  content: "\e012";
}
.glyphicon-ok:before {
  content: "\e013";
}
.glyphicon-remove:before {
  content: "\e014";
}
.glyphicon-zoom-in:before {
  content: "\e015";
}
.glyphicon-zoom-out:before {
  content: "\e016";
}
.glyphicon-off:before {
  content: "\e017";
}
.glyphicon-signal:before {
  content: "\e018";
}
.glyphicon-cog:before {
  content: "\e019";
}
.glyphicon-trash:before {
  content: "\e020";
}
.glyphicon-home:before {
  content: "\e021";
}
.glyphicon-file:before {
  content: "\e022";
}
.glyphicon-time:before {
  content: "\e023";
}
.glyphicon-road:before {
  content: "\e024";
}
.glyphicon-download-alt:before {
  content: "\e025";
}
.glyphicon-download:before {
  content: "\e026";
}
.glyphicon-upload:before {
  content: "\e027";
}
.glyphicon-inbox:before {
  content: "\e028";
}
.glyphicon-play-circle:before {
  content: "\e029";
}
.glyphicon-repeat:before {
  content: "\e030";
}
.glyphicon-refresh:before {
  content: "\e031";
}
.glyphicon-list-alt:before {
  content: "\e032";
}
.glyphicon-lock:before {
  content: "\e033";
}
.glyphicon-flag:before {
  content: "\e034";
}
.glyphicon-headphones:before {
  content: "\e035";
}
.glyphicon-volume-off:before {
  content: "\e036";
}
.glyphicon-volume-down:before {
  content: "\e037";
}
.glyphicon-volume-up:before {
  content: "\e038";
}
.glyphicon-qrcode:before {
  content: "\e039";
}
.glyphicon-barcode:before {
  content: "\e040";
}
.glyphicon-tag:before {
  content: "\e041";
}
.glyphicon-tags:before {
  content: "\e042";
}
.glyphicon-book:before {
  content: "\e043";
}
.glyphicon-bookmark:before {
  content: "\e044";
}
.glyphicon-print:before {
  content: "\e045";
}
.glyphicon-camera:before {
  content: "\e046";
}
.glyphicon-font:before {
  content: "\e047";
}
.glyphicon-bold:before {
  content: "\e048";
}
.glyphicon-italic:before {
  content: "\e049";
}
.glyphicon-text-height:before {
  content: "\e050";
}
.glyphicon-text-width:before {
  content: "\e051";
}
.glyphicon-align-left:before {
  content: "\e052";
}
.glyphicon-align-center:before {
  content: "\e053";
}
.glyphicon-align-right:before {
  content: "\e054";
}
.glyphicon-align-justify:before {
  content: "\e055";
}
.glyphicon-list:before {
  content: "\e056";
}
.glyphicon-indent-left:before {
  content: "\e057";
}
.glyphicon-indent-right:before {
  content: "\e058";
}
.glyphicon-facetime-video:before {
  content: "\e059";
}
.glyphicon-picture:before {
  content: "\e060";
}
.glyphicon-map-marker:before {
  content: "\e062";
}
.glyphicon-adjust:before {
  content: "\e063";
}
.glyphicon-tint:before {
  content: "\e064";
}
.glyphicon-edit:before {
  content: "\e065";
}
.glyphicon-share:before {
  content: "\e066";
}
.glyphicon-check:before {
  content: "\e067";
}
.glyphicon-move:before {
  content: "\e068";
}
.glyphicon-step-backward:before {
  content: "\e069";
}
.glyphicon-fast-backward:before {
  content: "\e070";
}
.glyphicon-backward:before {
  content: "\e071";
}
.glyphicon-play:before {
  content: "\e072";
}
.glyphicon-pause:before {
  content: "\e073";
}
.glyphicon-stop:before {
  content: "\e074";
}
.glyphicon-forward:before {
  content: "\e075";
}
.glyphicon-fast-forward:before {
  content: "\e076";
}
.glyphicon-step-forward:before {
  content: "\e077";
}
.glyphicon-eject:before {
  content: "\e078";
}
.glyphicon-chevron-left:before {
  content: "\e079";
}
.glyphicon-chevron-right:before {
  content: "\e080";
}
.glyphicon-plus-sign:before {
  content: "\e081";
}
.glyphicon-minus-sign:before {
  content: "\e082";
}
.glyphicon-remove-sign:before {
  content: "\e083";
}
.glyphicon-ok-sign:before {
  content: "\e084";
}
.glyphicon-question-sign:before {
  content: "\e085";
}
.glyphicon-info-sign:before {
  content: "\e086";
}
.glyphicon-screenshot:before {
  content: "\e087";
}
.glyphicon-remove-circle:before {
  content: "\e088";
}
.glyphicon-ok-circle:before {
  content: "\e089";
}
.glyphicon-ban-circle:before {
  content: "\e090";
}
.glyphicon-arrow-left:before {
  content: "\e091";
}
.glyphicon-arrow-right:before {
  content: "\e092";
}
.glyphicon-arrow-up:before {
  content: "\e093";
}
.glyphicon-arrow-down:before {
  content: "\e094";
}
.glyphicon-share-alt:before {
  content: "\e095";
}
.glyphicon-resize-full:before {
  content: "\e096";
}
.glyphicon-resize-small:before {
  content: "\e097";
}
.glyphicon-exclamation-sign:before {
  content: "\e101";
}
.glyphicon-gift:before {
  content: "\e102";
}
.glyphicon-leaf:before {
  content: "\e103";
}
.glyphicon-fire:before {
  content: "\e104";
}
.glyphicon-eye-open:before {
  content: "\e105";
}
.glyphicon-eye-close:before {
  content: "\e106";
}
.glyphicon-warning-sign:before {
  content: "\e107";
}
.glyphicon-plane:before {
  content: "\e108";
}
.glyphicon-calendar:before {
  content: "\e109";
}
.glyphicon-random:before {
  content: "\e110";
}
.glyphicon-comment:before {
  content: "\e111";
}
.glyphicon-magnet:before {
  content: "\e112";
}
.glyphicon-chevron-up:before {
  content: "\e113";
}
.glyphicon-chevron-down:before {
  content: "\e114";
}
.glyphicon-retweet:before {
  content: "\e115";
}
.glyphicon-shopping-cart:before {
  content: "\e116";
}
.glyphicon-folder-close:before {
  content: "\e117";
}
.glyphicon-folder-open:before {
  content: "\e118";
}
.glyphicon-resize-vertical:before {
  content: "\e119";
}
.glyphicon-resize-horizontal:before {
  content: "\e120";
}
.glyphicon-hdd:before {
  content: "\e121";
}
.glyphicon-bullhorn:before {
  content: "\e122";
}
.glyphicon-bell:before {
  content: "\e123";
}
.glyphicon-certificate:before {
  content: "\e124";
}
.glyphicon-thumbs-up:before {
  content: "\e125";
}
.glyphicon-thumbs-down:before {
  content: "\e126";
}
.glyphicon-hand-right:before {
  content: "\e127";
}
.glyphicon-hand-left:before {
  content: "\e128";
}
.glyphicon-hand-up:before {
  content: "\e129";
}
.glyphicon-hand-down:before {
  content: "\e130";
}
.glyphicon-circle-arrow-right:before {
  content: "\e131";
}
.glyphicon-circle-arrow-left:before {
  content: "\e132";
}
.glyphicon-circle-arrow-up:before {
  content: "\e133";
}
.glyphicon-circle-arrow-down:before {
  content: "\e134";
}
.glyphicon-globe:before {
  content: "\e135";
}
.glyphicon-wrench:before {
  content: "\e136";
}
.glyphicon-tasks:before {
  content: "\e137";
}
.glyphicon-filter:before {
  content: "\e138";
}
.glyphicon-briefcase:before {
  content: "\e139";
}
.glyphicon-fullscreen:before {
  content: "\e140";
}
.glyphicon-dashboard:before {
  content: "\e141";
}
.glyphicon-paperclip:before {
  content: "\e142";
}
.glyphicon-heart-empty:before {
  content: "\e143";
}
.glyphicon-link:before {
  content: "\e144";
}
.glyphicon-phone:before {
  content: "\e145";
}
.glyphicon-pushpin:before {
  content: "\e146";
}
.glyphicon-usd:before {
  content: "\e148";
}
.glyphicon-gbp:before {
  content: "\e149";
}
.glyphicon-sort:before {
  content: "\e150";
}
.glyphicon-sort-by-alphabet:before {
  content: "\e151";
}
.glyphicon-sort-by-alphabet-alt:before {
  content: "\e152";
}
.glyphicon-sort-by-order:before {
  content: "\e153";
}
.glyphicon-sort-by-order-alt:before {
  content: "\e154";
}
.glyphicon-sort-by-attributes:before {
  content: "\e155";
}
.glyphicon-sort-by-attributes-alt:before {
  content: "\e156";
}
.glyphicon-unchecked:before {
  content: "\e157";
}
.glyphicon-expand:before {
  content: "\e158";
}
.glyphicon-collapse-down:before {
  content: "\e159";
}
.glyphicon-collapse-up:before {
  content: "\e160";
}
.glyphicon-log-in:before {
  content: "\e161";
}
.glyphicon-flash:before {
  content: "\e162";
}
.glyphicon-log-out:before {
  content: "\e163";
}
.glyphicon-new-window:before {
  content: "\e164";
}
.glyphicon-record:before {
  content: "\e165";
}
.glyphicon-save:before {
  content: "\e166";
}
.glyphicon-open:before {
  content: "\e167";
}
.glyphicon-saved:before {
  content: "\e168";
}
.glyphicon-import:before {
  content: "\e169";
}
.glyphicon-export:before {
  content: "\e170";
}
.glyphicon-send:before {
  content: "\e171";
}
.glyphicon-floppy-disk:before {
  content: "\e172";
}
.glyphicon-floppy-saved:before {
  content: "\e173";
}
.glyphicon-floppy-remove:before {
  content: "\e174";
}
.glyphicon-floppy-save:before {
  content: "\e175";
}
.glyphicon-floppy-open:before {
  content: "\e176";
}
.glyphicon-credit-card:before {
  content: "\e177";
}
.glyphicon-transfer:before {
  content: "\e178";
}
.glyphicon-cutlery:before {
  content: "\e179";
}
.glyphicon-header:before {
  content: "\e180";
}
.glyphicon-compressed:before {
  content: "\e181";
}
.glyphicon-earphone:before {
  content: "\e182";
}
.glyphicon-phone-alt:before {
  content: "\e183";
}
.glyphicon-tower:before {
  content: "\e184";
}
.glyphicon-stats:before {
  content: "\e185";
}
.glyphicon-sd-video:before {
  content: "\e186";
}
.glyphicon-hd-video:before {
  content: "\e187";
}
.glyphicon-subtitles:before {
  content: "\e188";
}
.glyphicon-sound-stereo:before {
  content: "\e189";
}
.glyphicon-sound-dolby:before {
  content: "\e190";
}
.glyphicon-sound-5-1:before {
  content: "\e191";
}
.glyphicon-sound-6-1:before {
  content: "\e192";
}
.glyphicon-sound-7-1:before {
  content: "\e193";
}
.glyphicon-copyright-mark:before {
  content: "\e194";
}
.glyphicon-registration-mark:before {
  content: "\e195";
}
.glyphicon-cloud-download:before {
  content: "\e197";
}
.glyphicon-cloud-upload:before {
  content: "\e198";
}
.glyphicon-tree-conifer:before {
  content: "\e199";
}
.glyphicon-tree-deciduous:before {
  content: "\e200";
}
.glyphicon-cd:before {
  content: "\e201";
}
.glyphicon-save-file:before {
  content: "\e202";
}
.glyphicon-open-file:before {
  content: "\e203";
}
.glyphicon-level-up:before {
  content: "\e204";
}
.glyphicon-copy:before {
  content: "\e205";
}
.glyphicon-paste:before {
  content: "\e206";
}
.glyphicon-alert:before {
  content: "\e209";
}
.glyphicon-equalizer:before {
  content: "\e210";
}
.glyphicon-king:before {
  content: "\e211";
}
.glyphicon-queen:before {
  content: "\e212";
}
.glyphicon-pawn:before {
  content: "\e213";
}
.glyphicon-bishop:before {
  content: "\e214";
}
.glyphicon-knight:before {
  content: "\e215";
}
.glyphicon-baby-formula:before {
  content: "\e216";
}
.glyphicon-tent:before {
  content: "\26fa";
}
.glyphicon-blackboard:before {
  content: "\e218";
}
.glyphicon-bed:before {
  content: "\e219";
}
.glyphicon-apple:before {
  content: "\f8ff";
}
.glyphicon-erase:before {
  content: "\e221";
}
.glyphicon-hourglass:before {
  content: "\231b";
}
.glyphicon-lamp:before {
  content: "\e223";
}
.glyphicon-duplicate:before {
  content: "\e224";
}
.glyphicon-piggy-bank:before {
  content: "\e225";
}
.glyphicon-scissors:before {
  content: "\e226";
}
.glyphicon-bitcoin:before {
  content: "\e227";
}
.glyphicon-btc:before {
  content: "\e227";
}
.glyphicon-xbt:before {
  content: "\e227";
}
.glyphicon-yen:before {
  content: "\00a5";
}
.glyphicon-jpy:before {
  content: "\00a5";
}
.glyphicon-ruble:before {
  content: "\20bd";
}
.glyphicon-rub:before {
  content: "\20bd";
}
.glyphicon-scale:before {
  content: "\e230";
}
.glyphicon-ice-lolly:before {
  content: "\e231";
}
.glyphicon-ice-lolly-tasted:before {
  content: "\e232";
}
.glyphicon-education:before {
  content: "\e233";
}
.glyphicon-option-horizontal:before {
  content: "\e234";
}
.glyphicon-option-vertical:before {
  content: "\e235";
}
.glyphicon-menu-hamburger:before {
  content: "\e236";
}
.glyphicon-modal-window:before {
  content: "\e237";
}
.glyphicon-oil:before {
  content: "\e238";
}
.glyphicon-grain:before {
  content: "\e239";
}
.glyphicon-sunglasses:before {
  content: "\e240";
}
.glyphicon-text-size:before {
  content: "\e241";
}
.glyphicon-text-color:before {
  content: "\e242";
}
.glyphicon-text-background:before {
  content: "\e243";
}
.glyphicon-object-align-top:before {
  content: "\e244";
}
.glyphicon-object-align-bottom:before {
  content: "\e245";
}
.glyphicon-object-align-horizontal:before {
  content: "\e246";
}
.glyphicon-object-align-left:before {
  content: "\e247";
}
.glyphicon-object-align-vertical:before {
  content: "\e248";
}
.glyphicon-object-align-right:before {
  content: "\e249";
}
.glyphicon-triangle-right:before {
  content: "\e250";
}
.glyphicon-triangle-left:before {
  content: "\e251";
}
.glyphicon-triangle-bottom:before {
  content: "\e252";
}
.glyphicon-triangle-top:before {
  content: "\e253";
}
.glyphicon-console:before {
  content: "\e254";
}
.glyphicon-superscript:before {
  content: "\e255";
}
.glyphicon-subscript:before {
  content: "\e256";
}
.glyphicon-menu-left:before {
  content: "\e257";
}
.glyphicon-menu-right:before {
  content: "\e258";
}
.glyphicon-menu-down:before {
  content: "\e259";
}
.glyphicon-menu-up:before {
  content: "\e260";
}
* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
*:before,
*:after {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
html {
  font-size: 10px;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 13px;
  line-height: 1.42857143;
  color: #000;
  background-color: #fff;
}
input,
button,
select,
textarea {
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
}
a {
  color: #337ab7;
  text-decoration: none;
}
a:hover,
a:focus {
  color: #23527c;
  text-decoration: underline;
}
a:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
figure {
  margin: 0;
}
img {
  vertical-align: middle;
}
.img-responsive,
.thumbnail > img,
.thumbnail a > img,
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  display: block;
  max-width: 100%;
  height: auto;
}
.img-rounded {
  border-radius: 3px;
}
.img-thumbnail {
  padding: 4px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: all 0.2s ease-in-out;
  -o-transition: all 0.2s ease-in-out;
  transition: all 0.2s ease-in-out;
  display: inline-block;
  max-width: 100%;
  height: auto;
}
.img-circle {
  border-radius: 50%;
}
hr {
  margin-top: 18px;
  margin-bottom: 18px;
  border: 0;
  border-top: 1px solid #eeeeee;
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
[role="button"] {
  cursor: pointer;
}
h1,
h2,
h3,
h4,
h5,
h6,
.h1,
.h2,
.h3,
.h4,
.h5,
.h6 {
  font-family: inherit;
  font-weight: 500;
  line-height: 1.1;
  color: inherit;
}
h1 small,
h2 small,
h3 small,
h4 small,
h5 small,
h6 small,
.h1 small,
.h2 small,
.h3 small,
.h4 small,
.h5 small,
.h6 small,
h1 .small,
h2 .small,
h3 .small,
h4 .small,
h5 .small,
h6 .small,
.h1 .small,
.h2 .small,
.h3 .small,
.h4 .small,
.h5 .small,
.h6 .small {
  font-weight: normal;
  line-height: 1;
  color: #777777;
}
h1,
.h1,
h2,
.h2,
h3,
.h3 {
  margin-top: 18px;
  margin-bottom: 9px;
}
h1 small,
.h1 small,
h2 small,
.h2 small,
h3 small,
.h3 small,
h1 .small,
.h1 .small,
h2 .small,
.h2 .small,
h3 .small,
.h3 .small {
  font-size: 65%;
}
h4,
.h4,
h5,
.h5,
h6,
.h6 {
  margin-top: 9px;
  margin-bottom: 9px;
}
h4 small,
.h4 small,
h5 small,
.h5 small,
h6 small,
.h6 small,
h4 .small,
.h4 .small,
h5 .small,
.h5 .small,
h6 .small,
.h6 .small {
  font-size: 75%;
}
h1,
.h1 {
  font-size: 33px;
}
h2,
.h2 {
  font-size: 27px;
}
h3,
.h3 {
  font-size: 23px;
}
h4,
.h4 {
  font-size: 17px;
}
h5,
.h5 {
  font-size: 13px;
}
h6,
.h6 {
  font-size: 12px;
}
p {
  margin: 0 0 9px;
}
.lead {
  margin-bottom: 18px;
  font-size: 14px;
  font-weight: 300;
  line-height: 1.4;
}
@media (min-width: 768px) {
  .lead {
    font-size: 19.5px;
  }
}
small,
.small {
  font-size: 92%;
}
mark,
.mark {
  background-color: #fcf8e3;
  padding: .2em;
}
.text-left {
  text-align: left;
}
.text-right {
  text-align: right;
}
.text-center {
  text-align: center;
}
.text-justify {
  text-align: justify;
}
.text-nowrap {
  white-space: nowrap;
}
.text-lowercase {
  text-transform: lowercase;
}
.text-uppercase {
  text-transform: uppercase;
}
.text-capitalize {
  text-transform: capitalize;
}
.text-muted {
  color: #777777;
}
.text-primary {
  color: #337ab7;
}
a.text-primary:hover,
a.text-primary:focus {
  color: #286090;
}
.text-success {
  color: #3c763d;
}
a.text-success:hover,
a.text-success:focus {
  color: #2b542c;
}
.text-info {
  color: #31708f;
}
a.text-info:hover,
a.text-info:focus {
  color: #245269;
}
.text-warning {
  color: #8a6d3b;
}
a.text-warning:hover,
a.text-warning:focus {
  color: #66512c;
}
.text-danger {
  color: #a94442;
}
a.text-danger:hover,
a.text-danger:focus {
  color: #843534;
}
.bg-primary {
  color: #fff;
  background-color: #337ab7;
}
a.bg-primary:hover,
a.bg-primary:focus {
  background-color: #286090;
}
.bg-success {
  background-color: #dff0d8;
}
a.bg-success:hover,
a.bg-success:focus {
  background-color: #c1e2b3;
}
.bg-info {
  background-color: #d9edf7;
}
a.bg-info:hover,
a.bg-info:focus {
  background-color: #afd9ee;
}
.bg-warning {
  background-color: #fcf8e3;
}
a.bg-warning:hover,
a.bg-warning:focus {
  background-color: #f7ecb5;
}
.bg-danger {
  background-color: #f2dede;
}
a.bg-danger:hover,
a.bg-danger:focus {
  background-color: #e4b9b9;
}
.page-header {
  padding-bottom: 8px;
  margin: 36px 0 18px;
  border-bottom: 1px solid #eeeeee;
}
ul,
ol {
  margin-top: 0;
  margin-bottom: 9px;
}
ul ul,
ol ul,
ul ol,
ol ol {
  margin-bottom: 0;
}
.list-unstyled {
  padding-left: 0;
  list-style: none;
}
.list-inline {
  padding-left: 0;
  list-style: none;
  margin-left: -5px;
}
.list-inline > li {
  display: inline-block;
  padding-left: 5px;
  padding-right: 5px;
}
dl {
  margin-top: 0;
  margin-bottom: 18px;
}
dt,
dd {
  line-height: 1.42857143;
}
dt {
  font-weight: bold;
}
dd {
  margin-left: 0;
}
@media (min-width: 541px) {
  .dl-horizontal dt {
    float: left;
    width: 160px;
    clear: left;
    text-align: right;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .dl-horizontal dd {
    margin-left: 180px;
  }
}
abbr[title],
abbr[data-original-title] {
  cursor: help;
  border-bottom: 1px dotted #777777;
}
.initialism {
  font-size: 90%;
  text-transform: uppercase;
}
blockquote {
  padding: 9px 18px;
  margin: 0 0 18px;
  font-size: inherit;
  border-left: 5px solid #eeeeee;
}
blockquote p:last-child,
blockquote ul:last-child,
blockquote ol:last-child {
  margin-bottom: 0;
}
blockquote footer,
blockquote small,
blockquote .small {
  display: block;
  font-size: 80%;
  line-height: 1.42857143;
  color: #777777;
}
blockquote footer:before,
blockquote small:before,
blockquote .small:before {
  content: '\2014 \00A0';
}
.blockquote-reverse,
blockquote.pull-right {
  padding-right: 15px;
  padding-left: 0;
  border-right: 5px solid #eeeeee;
  border-left: 0;
  text-align: right;
}
.blockquote-reverse footer:before,
blockquote.pull-right footer:before,
.blockquote-reverse small:before,
blockquote.pull-right small:before,
.blockquote-reverse .small:before,
blockquote.pull-right .small:before {
  content: '';
}
.blockquote-reverse footer:after,
blockquote.pull-right footer:after,
.blockquote-reverse small:after,
blockquote.pull-right small:after,
.blockquote-reverse .small:after,
blockquote.pull-right .small:after {
  content: '\00A0 \2014';
}
address {
  margin-bottom: 18px;
  font-style: normal;
  line-height: 1.42857143;
}
code,
kbd,
pre,
samp {
  font-family: monospace;
}
code {
  padding: 2px 4px;
  font-size: 90%;
  color: #c7254e;
  background-color: #f9f2f4;
  border-radius: 2px;
}
kbd {
  padding: 2px 4px;
  font-size: 90%;
  color: #888;
  background-color: transparent;
  border-radius: 1px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
}
kbd kbd {
  padding: 0;
  font-size: 100%;
  font-weight: bold;
  box-shadow: none;
}
pre {
  display: block;
  padding: 8.5px;
  margin: 0 0 9px;
  font-size: 12px;
  line-height: 1.42857143;
  word-break: break-all;
  word-wrap: break-word;
  color: #333333;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 2px;
}
pre code {
  padding: 0;
  font-size: inherit;
  color: inherit;
  white-space: pre-wrap;
  background-color: transparent;
  border-radius: 0;
}
.pre-scrollable {
  max-height: 340px;
  overflow-y: scroll;
}
.container {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
@media (min-width: 768px) {
  .container {
    width: 768px;
  }
}
@media (min-width: 992px) {
  .container {
    width: 940px;
  }
}
@media (min-width: 1200px) {
  .container {
    width: 1140px;
  }
}
.container-fluid {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
.row {
  margin-left: 0px;
  margin-right: 0px;
}
.col-xs-1, .col-sm-1, .col-md-1, .col-lg-1, .col-xs-2, .col-sm-2, .col-md-2, .col-lg-2, .col-xs-3, .col-sm-3, .col-md-3, .col-lg-3, .col-xs-4, .col-sm-4, .col-md-4, .col-lg-4, .col-xs-5, .col-sm-5, .col-md-5, .col-lg-5, .col-xs-6, .col-sm-6, .col-md-6, .col-lg-6, .col-xs-7, .col-sm-7, .col-md-7, .col-lg-7, .col-xs-8, .col-sm-8, .col-md-8, .col-lg-8, .col-xs-9, .col-sm-9, .col-md-9, .col-lg-9, .col-xs-10, .col-sm-10, .col-md-10, .col-lg-10, .col-xs-11, .col-sm-11, .col-md-11, .col-lg-11, .col-xs-12, .col-sm-12, .col-md-12, .col-lg-12 {
  position: relative;
  min-height: 1px;
  padding-left: 0px;
  padding-right: 0px;
}
.col-xs-1, .col-xs-2, .col-xs-3, .col-xs-4, .col-xs-5, .col-xs-6, .col-xs-7, .col-xs-8, .col-xs-9, .col-xs-10, .col-xs-11, .col-xs-12 {
  float: left;
}
.col-xs-12 {
  width: 100%;
}
.col-xs-11 {
  width: 91.66666667%;
}
.col-xs-10 {
  width: 83.33333333%;
}
.col-xs-9 {
  width: 75%;
}
.col-xs-8 {
  width: 66.66666667%;
}
.col-xs-7 {
  width: 58.33333333%;
}
.col-xs-6 {
  width: 50%;
}
.col-xs-5 {
  width: 41.66666667%;
}
.col-xs-4 {
  width: 33.33333333%;
}
.col-xs-3 {
  width: 25%;
}
.col-xs-2 {
  width: 16.66666667%;
}
.col-xs-1 {
  width: 8.33333333%;
}
.col-xs-pull-12 {
  right: 100%;
}
.col-xs-pull-11 {
  right: 91.66666667%;
}
.col-xs-pull-10 {
  right: 83.33333333%;
}
.col-xs-pull-9 {
  right: 75%;
}
.col-xs-pull-8 {
  right: 66.66666667%;
}
.col-xs-pull-7 {
  right: 58.33333333%;
}
.col-xs-pull-6 {
  right: 50%;
}
.col-xs-pull-5 {
  right: 41.66666667%;
}
.col-xs-pull-4 {
  right: 33.33333333%;
}
.col-xs-pull-3 {
  right: 25%;
}
.col-xs-pull-2 {
  right: 16.66666667%;
}
.col-xs-pull-1 {
  right: 8.33333333%;
}
.col-xs-pull-0 {
  right: auto;
}
.col-xs-push-12 {
  left: 100%;
}
.col-xs-push-11 {
  left: 91.66666667%;
}
.col-xs-push-10 {
  left: 83.33333333%;
}
.col-xs-push-9 {
  left: 75%;
}
.col-xs-push-8 {
  left: 66.66666667%;
}
.col-xs-push-7 {
  left: 58.33333333%;
}
.col-xs-push-6 {
  left: 50%;
}
.col-xs-push-5 {
  left: 41.66666667%;
}
.col-xs-push-4 {
  left: 33.33333333%;
}
.col-xs-push-3 {
  left: 25%;
}
.col-xs-push-2 {
  left: 16.66666667%;
}
.col-xs-push-1 {
  left: 8.33333333%;
}
.col-xs-push-0 {
  left: auto;
}
.col-xs-offset-12 {
  margin-left: 100%;
}
.col-xs-offset-11 {
  margin-left: 91.66666667%;
}
.col-xs-offset-10 {
  margin-left: 83.33333333%;
}
.col-xs-offset-9 {
  margin-left: 75%;
}
.col-xs-offset-8 {
  margin-left: 66.66666667%;
}
.col-xs-offset-7 {
  margin-left: 58.33333333%;
}
.col-xs-offset-6 {
  margin-left: 50%;
}
.col-xs-offset-5 {
  margin-left: 41.66666667%;
}
.col-xs-offset-4 {
  margin-left: 33.33333333%;
}
.col-xs-offset-3 {
  margin-left: 25%;
}
.col-xs-offset-2 {
  margin-left: 16.66666667%;
}
.col-xs-offset-1 {
  margin-left: 8.33333333%;
}
.col-xs-offset-0 {
  margin-left: 0%;
}
@media (min-width: 768px) {
  .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12 {
    float: left;
  }
  .col-sm-12 {
    width: 100%;
  }
  .col-sm-11 {
    width: 91.66666667%;
  }
  .col-sm-10 {
    width: 83.33333333%;
  }
  .col-sm-9 {
    width: 75%;
  }
  .col-sm-8 {
    width: 66.66666667%;
  }
  .col-sm-7 {
    width: 58.33333333%;
  }
  .col-sm-6 {
    width: 50%;
  }
  .col-sm-5 {
    width: 41.66666667%;
  }
  .col-sm-4 {
    width: 33.33333333%;
  }
  .col-sm-3 {
    width: 25%;
  }
  .col-sm-2 {
    width: 16.66666667%;
  }
  .col-sm-1 {
    width: 8.33333333%;
  }
  .col-sm-pull-12 {
    right: 100%;
  }
  .col-sm-pull-11 {
    right: 91.66666667%;
  }
  .col-sm-pull-10 {
    right: 83.33333333%;
  }
  .col-sm-pull-9 {
    right: 75%;
  }
  .col-sm-pull-8 {
    right: 66.66666667%;
  }
  .col-sm-pull-7 {
    right: 58.33333333%;
  }
  .col-sm-pull-6 {
    right: 50%;
  }
  .col-sm-pull-5 {
    right: 41.66666667%;
  }
  .col-sm-pull-4 {
    right: 33.33333333%;
  }
  .col-sm-pull-3 {
    right: 25%;
  }
  .col-sm-pull-2 {
    right: 16.66666667%;
  }
  .col-sm-pull-1 {
    right: 8.33333333%;
  }
  .col-sm-pull-0 {
    right: auto;
  }
  .col-sm-push-12 {
    left: 100%;
  }
  .col-sm-push-11 {
    left: 91.66666667%;
  }
  .col-sm-push-10 {
    left: 83.33333333%;
  }
  .col-sm-push-9 {
    left: 75%;
  }
  .col-sm-push-8 {
    left: 66.66666667%;
  }
  .col-sm-push-7 {
    left: 58.33333333%;
  }
  .col-sm-push-6 {
    left: 50%;
  }
  .col-sm-push-5 {
    left: 41.66666667%;
  }
  .col-sm-push-4 {
    left: 33.33333333%;
  }
  .col-sm-push-3 {
    left: 25%;
  }
  .col-sm-push-2 {
    left: 16.66666667%;
  }
  .col-sm-push-1 {
    left: 8.33333333%;
  }
  .col-sm-push-0 {
    left: auto;
  }
  .col-sm-offset-12 {
    margin-left: 100%;
  }
  .col-sm-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-sm-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-sm-offset-9 {
    margin-left: 75%;
  }
  .col-sm-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-sm-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-sm-offset-6 {
    margin-left: 50%;
  }
  .col-sm-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-sm-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-sm-offset-3 {
    margin-left: 25%;
  }
  .col-sm-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-sm-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-sm-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 992px) {
  .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12 {
    float: left;
  }
  .col-md-12 {
    width: 100%;
  }
  .col-md-11 {
    width: 91.66666667%;
  }
  .col-md-10 {
    width: 83.33333333%;
  }
  .col-md-9 {
    width: 75%;
  }
  .col-md-8 {
    width: 66.66666667%;
  }
  .col-md-7 {
    width: 58.33333333%;
  }
  .col-md-6 {
    width: 50%;
  }
  .col-md-5 {
    width: 41.66666667%;
  }
  .col-md-4 {
    width: 33.33333333%;
  }
  .col-md-3 {
    width: 25%;
  }
  .col-md-2 {
    width: 16.66666667%;
  }
  .col-md-1 {
    width: 8.33333333%;
  }
  .col-md-pull-12 {
    right: 100%;
  }
  .col-md-pull-11 {
    right: 91.66666667%;
  }
  .col-md-pull-10 {
    right: 83.33333333%;
  }
  .col-md-pull-9 {
    right: 75%;
  }
  .col-md-pull-8 {
    right: 66.66666667%;
  }
  .col-md-pull-7 {
    right: 58.33333333%;
  }
  .col-md-pull-6 {
    right: 50%;
  }
  .col-md-pull-5 {
    right: 41.66666667%;
  }
  .col-md-pull-4 {
    right: 33.33333333%;
  }
  .col-md-pull-3 {
    right: 25%;
  }
  .col-md-pull-2 {
    right: 16.66666667%;
  }
  .col-md-pull-1 {
    right: 8.33333333%;
  }
  .col-md-pull-0 {
    right: auto;
  }
  .col-md-push-12 {
    left: 100%;
  }
  .col-md-push-11 {
    left: 91.66666667%;
  }
  .col-md-push-10 {
    left: 83.33333333%;
  }
  .col-md-push-9 {
    left: 75%;
  }
  .col-md-push-8 {
    left: 66.66666667%;
  }
  .col-md-push-7 {
    left: 58.33333333%;
  }
  .col-md-push-6 {
    left: 50%;
  }
  .col-md-push-5 {
    left: 41.66666667%;
  }
  .col-md-push-4 {
    left: 33.33333333%;
  }
  .col-md-push-3 {
    left: 25%;
  }
  .col-md-push-2 {
    left: 16.66666667%;
  }
  .col-md-push-1 {
    left: 8.33333333%;
  }
  .col-md-push-0 {
    left: auto;
  }
  .col-md-offset-12 {
    margin-left: 100%;
  }
  .col-md-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-md-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-md-offset-9 {
    margin-left: 75%;
  }
  .col-md-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-md-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-md-offset-6 {
    margin-left: 50%;
  }
  .col-md-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-md-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-md-offset-3 {
    margin-left: 25%;
  }
  .col-md-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-md-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-md-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 1200px) {
  .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12 {
    float: left;
  }
  .col-lg-12 {
    width: 100%;
  }
  .col-lg-11 {
    width: 91.66666667%;
  }
  .col-lg-10 {
    width: 83.33333333%;
  }
  .col-lg-9 {
    width: 75%;
  }
  .col-lg-8 {
    width: 66.66666667%;
  }
  .col-lg-7 {
    width: 58.33333333%;
  }
  .col-lg-6 {
    width: 50%;
  }
  .col-lg-5 {
    width: 41.66666667%;
  }
  .col-lg-4 {
    width: 33.33333333%;
  }
  .col-lg-3 {
    width: 25%;
  }
  .col-lg-2 {
    width: 16.66666667%;
  }
  .col-lg-1 {
    width: 8.33333333%;
  }
  .col-lg-pull-12 {
    right: 100%;
  }
  .col-lg-pull-11 {
    right: 91.66666667%;
  }
  .col-lg-pull-10 {
    right: 83.33333333%;
  }
  .col-lg-pull-9 {
    right: 75%;
  }
  .col-lg-pull-8 {
    right: 66.66666667%;
  }
  .col-lg-pull-7 {
    right: 58.33333333%;
  }
  .col-lg-pull-6 {
    right: 50%;
  }
  .col-lg-pull-5 {
    right: 41.66666667%;
  }
  .col-lg-pull-4 {
    right: 33.33333333%;
  }
  .col-lg-pull-3 {
    right: 25%;
  }
  .col-lg-pull-2 {
    right: 16.66666667%;
  }
  .col-lg-pull-1 {
    right: 8.33333333%;
  }
  .col-lg-pull-0 {
    right: auto;
  }
  .col-lg-push-12 {
    left: 100%;
  }
  .col-lg-push-11 {
    left: 91.66666667%;
  }
  .col-lg-push-10 {
    left: 83.33333333%;
  }
  .col-lg-push-9 {
    left: 75%;
  }
  .col-lg-push-8 {
    left: 66.66666667%;
  }
  .col-lg-push-7 {
    left: 58.33333333%;
  }
  .col-lg-push-6 {
    left: 50%;
  }
  .col-lg-push-5 {
    left: 41.66666667%;
  }
  .col-lg-push-4 {
    left: 33.33333333%;
  }
  .col-lg-push-3 {
    left: 25%;
  }
  .col-lg-push-2 {
    left: 16.66666667%;
  }
  .col-lg-push-1 {
    left: 8.33333333%;
  }
  .col-lg-push-0 {
    left: auto;
  }
  .col-lg-offset-12 {
    margin-left: 100%;
  }
  .col-lg-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-lg-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-lg-offset-9 {
    margin-left: 75%;
  }
  .col-lg-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-lg-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-lg-offset-6 {
    margin-left: 50%;
  }
  .col-lg-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-lg-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-lg-offset-3 {
    margin-left: 25%;
  }
  .col-lg-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-lg-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-lg-offset-0 {
    margin-left: 0%;
  }
}
table {
  background-color: transparent;
}
caption {
  padding-top: 8px;
  padding-bottom: 8px;
  color: #777777;
  text-align: left;
}
th {
  text-align: left;
}
.table {
  width: 100%;
  max-width: 100%;
  margin-bottom: 18px;
}
.table > thead > tr > th,
.table > tbody > tr > th,
.table > tfoot > tr > th,
.table > thead > tr > td,
.table > tbody > tr > td,
.table > tfoot > tr > td {
  padding: 8px;
  line-height: 1.42857143;
  vertical-align: top;
  border-top: 1px solid #ddd;
}
.table > thead > tr > th {
  vertical-align: bottom;
  border-bottom: 2px solid #ddd;
}
.table > caption + thead > tr:first-child > th,
.table > colgroup + thead > tr:first-child > th,
.table > thead:first-child > tr:first-child > th,
.table > caption + thead > tr:first-child > td,
.table > colgroup + thead > tr:first-child > td,
.table > thead:first-child > tr:first-child > td {
  border-top: 0;
}
.table > tbody + tbody {
  border-top: 2px solid #ddd;
}
.table .table {
  background-color: #fff;
}
.table-condensed > thead > tr > th,
.table-condensed > tbody > tr > th,
.table-condensed > tfoot > tr > th,
.table-condensed > thead > tr > td,
.table-condensed > tbody > tr > td,
.table-condensed > tfoot > tr > td {
  padding: 5px;
}
.table-bordered {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > tbody > tr > th,
.table-bordered > tfoot > tr > th,
.table-bordered > thead > tr > td,
.table-bordered > tbody > tr > td,
.table-bordered > tfoot > tr > td {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > thead > tr > td {
  border-bottom-width: 2px;
}
.table-striped > tbody > tr:nth-of-type(odd) {
  background-color: #f9f9f9;
}
.table-hover > tbody > tr:hover {
  background-color: #f5f5f5;
}
table col[class*="col-"] {
  position: static;
  float: none;
  display: table-column;
}
table td[class*="col-"],
table th[class*="col-"] {
  position: static;
  float: none;
  display: table-cell;
}
.table > thead > tr > td.active,
.table > tbody > tr > td.active,
.table > tfoot > tr > td.active,
.table > thead > tr > th.active,
.table > tbody > tr > th.active,
.table > tfoot > tr > th.active,
.table > thead > tr.active > td,
.table > tbody > tr.active > td,
.table > tfoot > tr.active > td,
.table > thead > tr.active > th,
.table > tbody > tr.active > th,
.table > tfoot > tr.active > th {
  background-color: #f5f5f5;
}
.table-hover > tbody > tr > td.active:hover,
.table-hover > tbody > tr > th.active:hover,
.table-hover > tbody > tr.active:hover > td,
.table-hover > tbody > tr:hover > .active,
.table-hover > tbody > tr.active:hover > th {
  background-color: #e8e8e8;
}
.table > thead > tr > td.success,
.table > tbody > tr > td.success,
.table > tfoot > tr > td.success,
.table > thead > tr > th.success,
.table > tbody > tr > th.success,
.table > tfoot > tr > th.success,
.table > thead > tr.success > td,
.table > tbody > tr.success > td,
.table > tfoot > tr.success > td,
.table > thead > tr.success > th,
.table > tbody > tr.success > th,
.table > tfoot > tr.success > th {
  background-color: #dff0d8;
}
.table-hover > tbody > tr > td.success:hover,
.table-hover > tbody > tr > th.success:hover,
.table-hover > tbody > tr.success:hover > td,
.table-hover > tbody > tr:hover > .success,
.table-hover > tbody > tr.success:hover > th {
  background-color: #d0e9c6;
}
.table > thead > tr > td.info,
.table > tbody > tr > td.info,
.table > tfoot > tr > td.info,
.table > thead > tr > th.info,
.table > tbody > tr > th.info,
.table > tfoot > tr > th.info,
.table > thead > tr.info > td,
.table > tbody > tr.info > td,
.table > tfoot > tr.info > td,
.table > thead > tr.info > th,
.table > tbody > tr.info > th,
.table > tfoot > tr.info > th {
  background-color: #d9edf7;
}
.table-hover > tbody > tr > td.info:hover,
.table-hover > tbody > tr > th.info:hover,
.table-hover > tbody > tr.info:hover > td,
.table-hover > tbody > tr:hover > .info,
.table-hover > tbody > tr.info:hover > th {
  background-color: #c4e3f3;
}
.table > thead > tr > td.warning,
.table > tbody > tr > td.warning,
.table > tfoot > tr > td.warning,
.table > thead > tr > th.warning,
.table > tbody > tr > th.warning,
.table > tfoot > tr > th.warning,
.table > thead > tr.warning > td,
.table > tbody > tr.warning > td,
.table > tfoot > tr.warning > td,
.table > thead > tr.warning > th,
.table > tbody > tr.warning > th,
.table > tfoot > tr.warning > th {
  background-color: #fcf8e3;
}
.table-hover > tbody > tr > td.warning:hover,
.table-hover > tbody > tr > th.warning:hover,
.table-hover > tbody > tr.warning:hover > td,
.table-hover > tbody > tr:hover > .warning,
.table-hover > tbody > tr.warning:hover > th {
  background-color: #faf2cc;
}
.table > thead > tr > td.danger,
.table > tbody > tr > td.danger,
.table > tfoot > tr > td.danger,
.table > thead > tr > th.danger,
.table > tbody > tr > th.danger,
.table > tfoot > tr > th.danger,
.table > thead > tr.danger > td,
.table > tbody > tr.danger > td,
.table > tfoot > tr.danger > td,
.table > thead > tr.danger > th,
.table > tbody > tr.danger > th,
.table > tfoot > tr.danger > th {
  background-color: #f2dede;
}
.table-hover > tbody > tr > td.danger:hover,
.table-hover > tbody > tr > th.danger:hover,
.table-hover > tbody > tr.danger:hover > td,
.table-hover > tbody > tr:hover > .danger,
.table-hover > tbody > tr.danger:hover > th {
  background-color: #ebcccc;
}
.table-responsive {
  overflow-x: auto;
  min-height: 0.01%;
}
@media screen and (max-width: 767px) {
  .table-responsive {
    width: 100%;
    margin-bottom: 13.5px;
    overflow-y: hidden;
    -ms-overflow-style: -ms-autohiding-scrollbar;
    border: 1px solid #ddd;
  }
  .table-responsive > .table {
    margin-bottom: 0;
  }
  .table-responsive > .table > thead > tr > th,
  .table-responsive > .table > tbody > tr > th,
  .table-responsive > .table > tfoot > tr > th,
  .table-responsive > .table > thead > tr > td,
  .table-responsive > .table > tbody > tr > td,
  .table-responsive > .table > tfoot > tr > td {
    white-space: nowrap;
  }
  .table-responsive > .table-bordered {
    border: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:first-child,
  .table-responsive > .table-bordered > tbody > tr > th:first-child,
  .table-responsive > .table-bordered > tfoot > tr > th:first-child,
  .table-responsive > .table-bordered > thead > tr > td:first-child,
  .table-responsive > .table-bordered > tbody > tr > td:first-child,
  .table-responsive > .table-bordered > tfoot > tr > td:first-child {
    border-left: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:last-child,
  .table-responsive > .table-bordered > tbody > tr > th:last-child,
  .table-responsive > .table-bordered > tfoot > tr > th:last-child,
  .table-responsive > .table-bordered > thead > tr > td:last-child,
  .table-responsive > .table-bordered > tbody > tr > td:last-child,
  .table-responsive > .table-bordered > tfoot > tr > td:last-child {
    border-right: 0;
  }
  .table-responsive > .table-bordered > tbody > tr:last-child > th,
  .table-responsive > .table-bordered > tfoot > tr:last-child > th,
  .table-responsive > .table-bordered > tbody > tr:last-child > td,
  .table-responsive > .table-bordered > tfoot > tr:last-child > td {
    border-bottom: 0;
  }
}
fieldset {
  padding: 0;
  margin: 0;
  border: 0;
  min-width: 0;
}
legend {
  display: block;
  width: 100%;
  padding: 0;
  margin-bottom: 18px;
  font-size: 19.5px;
  line-height: inherit;
  color: #333333;
  border: 0;
  border-bottom: 1px solid #e5e5e5;
}
label {
  display: inline-block;
  max-width: 100%;
  margin-bottom: 5px;
  font-weight: bold;
}
input[type="search"] {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
input[type="radio"],
input[type="checkbox"] {
  margin: 4px 0 0;
  margin-top: 1px \9;
  line-height: normal;
}
input[type="file"] {
  display: block;
}
input[type="range"] {
  display: block;
  width: 100%;
}
select[multiple],
select[size] {
  height: auto;
}
input[type="file"]:focus,
input[type="radio"]:focus,
input[type="checkbox"]:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
output {
  display: block;
  padding-top: 7px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
}
.form-control {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
}
.form-control:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.form-control::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.form-control:-ms-input-placeholder {
  color: #999;
}
.form-control::-webkit-input-placeholder {
  color: #999;
}
.form-control::-ms-expand {
  border: 0;
  background-color: transparent;
}
.form-control[disabled],
.form-control[readonly],
fieldset[disabled] .form-control {
  background-color: #eeeeee;
  opacity: 1;
}
.form-control[disabled],
fieldset[disabled] .form-control {
  cursor: not-allowed;
}
textarea.form-control {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: none;
}
@media screen and (-webkit-min-device-pixel-ratio: 0) {
  input[type="date"].form-control,
  input[type="time"].form-control,
  input[type="datetime-local"].form-control,
  input[type="month"].form-control {
    line-height: 32px;
  }
  input[type="date"].input-sm,
  input[type="time"].input-sm,
  input[type="datetime-local"].input-sm,
  input[type="month"].input-sm,
  .input-group-sm input[type="date"],
  .input-group-sm input[type="time"],
  .input-group-sm input[type="datetime-local"],
  .input-group-sm input[type="month"] {
    line-height: 30px;
  }
  input[type="date"].input-lg,
  input[type="time"].input-lg,
  input[type="datetime-local"].input-lg,
  input[type="month"].input-lg,
  .input-group-lg input[type="date"],
  .input-group-lg input[type="time"],
  .input-group-lg input[type="datetime-local"],
  .input-group-lg input[type="month"] {
    line-height: 45px;
  }
}
.form-group {
  margin-bottom: 15px;
}
.radio,
.checkbox {
  position: relative;
  display: block;
  margin-top: 10px;
  margin-bottom: 10px;
}
.radio label,
.checkbox label {
  min-height: 18px;
  padding-left: 20px;
  margin-bottom: 0;
  font-weight: normal;
  cursor: pointer;
}
.radio input[type="radio"],
.radio-inline input[type="radio"],
.checkbox input[type="checkbox"],
.checkbox-inline input[type="checkbox"] {
  position: absolute;
  margin-left: -20px;
  margin-top: 4px \9;
}
.radio + .radio,
.checkbox + .checkbox {
  margin-top: -5px;
}
.radio-inline,
.checkbox-inline {
  position: relative;
  display: inline-block;
  padding-left: 20px;
  margin-bottom: 0;
  vertical-align: middle;
  font-weight: normal;
  cursor: pointer;
}
.radio-inline + .radio-inline,
.checkbox-inline + .checkbox-inline {
  margin-top: 0;
  margin-left: 10px;
}
input[type="radio"][disabled],
input[type="checkbox"][disabled],
input[type="radio"].disabled,
input[type="checkbox"].disabled,
fieldset[disabled] input[type="radio"],
fieldset[disabled] input[type="checkbox"] {
  cursor: not-allowed;
}
.radio-inline.disabled,
.checkbox-inline.disabled,
fieldset[disabled] .radio-inline,
fieldset[disabled] .checkbox-inline {
  cursor: not-allowed;
}
.radio.disabled label,
.checkbox.disabled label,
fieldset[disabled] .radio label,
fieldset[disabled] .checkbox label {
  cursor: not-allowed;
}
.form-control-static {
  padding-top: 7px;
  padding-bottom: 7px;
  margin-bottom: 0;
  min-height: 31px;
}
.form-control-static.input-lg,
.form-control-static.input-sm {
  padding-left: 0;
  padding-right: 0;
}
.input-sm {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-sm {
  height: 30px;
  line-height: 30px;
}
textarea.input-sm,
select[multiple].input-sm {
  height: auto;
}
.form-group-sm .form-control {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.form-group-sm select.form-control {
  height: 30px;
  line-height: 30px;
}
.form-group-sm textarea.form-control,
.form-group-sm select[multiple].form-control {
  height: auto;
}
.form-group-sm .form-control-static {
  height: 30px;
  min-height: 30px;
  padding: 6px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.input-lg {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-lg {
  height: 45px;
  line-height: 45px;
}
textarea.input-lg,
select[multiple].input-lg {
  height: auto;
}
.form-group-lg .form-control {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.form-group-lg select.form-control {
  height: 45px;
  line-height: 45px;
}
.form-group-lg textarea.form-control,
.form-group-lg select[multiple].form-control {
  height: auto;
}
.form-group-lg .form-control-static {
  height: 45px;
  min-height: 35px;
  padding: 11px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.has-feedback {
  position: relative;
}
.has-feedback .form-control {
  padding-right: 40px;
}
.form-control-feedback {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 2;
  display: block;
  width: 32px;
  height: 32px;
  line-height: 32px;
  text-align: center;
  pointer-events: none;
}
.input-lg + .form-control-feedback,
.input-group-lg + .form-control-feedback,
.form-group-lg .form-control + .form-control-feedback {
  width: 45px;
  height: 45px;
  line-height: 45px;
}
.input-sm + .form-control-feedback,
.input-group-sm + .form-control-feedback,
.form-group-sm .form-control + .form-control-feedback {
  width: 30px;
  height: 30px;
  line-height: 30px;
}
.has-success .help-block,
.has-success .control-label,
.has-success .radio,
.has-success .checkbox,
.has-success .radio-inline,
.has-success .checkbox-inline,
.has-success.radio label,
.has-success.checkbox label,
.has-success.radio-inline label,
.has-success.checkbox-inline label {
  color: #3c763d;
}
.has-success .form-control {
  border-color: #3c763d;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-success .form-control:focus {
  border-color: #2b542c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
}
.has-success .input-group-addon {
  color: #3c763d;
  border-color: #3c763d;
  background-color: #dff0d8;
}
.has-success .form-control-feedback {
  color: #3c763d;
}
.has-warning .help-block,
.has-warning .control-label,
.has-warning .radio,
.has-warning .checkbox,
.has-warning .radio-inline,
.has-warning .checkbox-inline,
.has-warning.radio label,
.has-warning.checkbox label,
.has-warning.radio-inline label,
.has-warning.checkbox-inline label {
  color: #8a6d3b;
}
.has-warning .form-control {
  border-color: #8a6d3b;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-warning .form-control:focus {
  border-color: #66512c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
}
.has-warning .input-group-addon {
  color: #8a6d3b;
  border-color: #8a6d3b;
  background-color: #fcf8e3;
}
.has-warning .form-control-feedback {
  color: #8a6d3b;
}
.has-error .help-block,
.has-error .control-label,
.has-error .radio,
.has-error .checkbox,
.has-error .radio-inline,
.has-error .checkbox-inline,
.has-error.radio label,
.has-error.checkbox label,
.has-error.radio-inline label,
.has-error.checkbox-inline label {
  color: #a94442;
}
.has-error .form-control {
  border-color: #a94442;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-error .form-control:focus {
  border-color: #843534;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
}
.has-error .input-group-addon {
  color: #a94442;
  border-color: #a94442;
  background-color: #f2dede;
}
.has-error .form-control-feedback {
  color: #a94442;
}
.has-feedback label ~ .form-control-feedback {
  top: 23px;
}
.has-feedback label.sr-only ~ .form-control-feedback {
  top: 0;
}
.help-block {
  display: block;
  margin-top: 5px;
  margin-bottom: 10px;
  color: #404040;
}
@media (min-width: 768px) {
  .form-inline .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .form-inline .form-control-static {
    display: inline-block;
  }
  .form-inline .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .form-inline .input-group .input-group-addon,
  .form-inline .input-group .input-group-btn,
  .form-inline .input-group .form-control {
    width: auto;
  }
  .form-inline .input-group > .form-control {
    width: 100%;
  }
  .form-inline .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio,
  .form-inline .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio label,
  .form-inline .checkbox label {
    padding-left: 0;
  }
  .form-inline .radio input[type="radio"],
  .form-inline .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .form-inline .has-feedback .form-control-feedback {
    top: 0;
  }
}
.form-horizontal .radio,
.form-horizontal .checkbox,
.form-horizontal .radio-inline,
.form-horizontal .checkbox-inline {
  margin-top: 0;
  margin-bottom: 0;
  padding-top: 7px;
}
.form-horizontal .radio,
.form-horizontal .checkbox {
  min-height: 25px;
}
.form-horizontal .form-group {
  margin-left: 0px;
  margin-right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .control-label {
    text-align: right;
    margin-bottom: 0;
    padding-top: 7px;
  }
}
.form-horizontal .has-feedback .form-control-feedback {
  right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .form-group-lg .control-label {
    padding-top: 11px;
    font-size: 17px;
  }
}
@media (min-width: 768px) {
  .form-horizontal .form-group-sm .control-label {
    padding-top: 6px;
    font-size: 12px;
  }
}
.btn {
  display: inline-block;
  margin-bottom: 0;
  font-weight: normal;
  text-align: center;
  vertical-align: middle;
  touch-action: manipulation;
  cursor: pointer;
  background-image: none;
  border: 1px solid transparent;
  white-space: nowrap;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  border-radius: 2px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.btn:focus,
.btn:active:focus,
.btn.active:focus,
.btn.focus,
.btn:active.focus,
.btn.active.focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
.btn:hover,
.btn:focus,
.btn.focus {
  color: #333;
  text-decoration: none;
}
.btn:active,
.btn.active {
  outline: 0;
  background-image: none;
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn.disabled,
.btn[disabled],
fieldset[disabled] .btn {
  cursor: not-allowed;
  opacity: 0.65;
  filter: alpha(opacity=65);
  -webkit-box-shadow: none;
  box-shadow: none;
}
a.btn.disabled,
fieldset[disabled] a.btn {
  pointer-events: none;
}
.btn-default {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.btn-default:focus,
.btn-default.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.btn-default:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active:hover,
.btn-default.active:hover,
.open > .dropdown-toggle.btn-default:hover,
.btn-default:active:focus,
.btn-default.active:focus,
.open > .dropdown-toggle.btn-default:focus,
.btn-default:active.focus,
.btn-default.active.focus,
.open > .dropdown-toggle.btn-default.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  background-image: none;
}
.btn-default.disabled:hover,
.btn-default[disabled]:hover,
fieldset[disabled] .btn-default:hover,
.btn-default.disabled:focus,
.btn-default[disabled]:focus,
fieldset[disabled] .btn-default:focus,
.btn-default.disabled.focus,
.btn-default[disabled].focus,
fieldset[disabled] .btn-default.focus {
  background-color: #fff;
  border-color: #ccc;
}
.btn-default .badge {
  color: #fff;
  background-color: #333;
}
.btn-primary {
  color: #fff;
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary:focus,
.btn-primary.focus {
  color: #fff;
  background-color: #286090;
  border-color: #122b40;
}
.btn-primary:hover {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active:hover,
.btn-primary.active:hover,
.open > .dropdown-toggle.btn-primary:hover,
.btn-primary:active:focus,
.btn-primary.active:focus,
.open > .dropdown-toggle.btn-primary:focus,
.btn-primary:active.focus,
.btn-primary.active.focus,
.open > .dropdown-toggle.btn-primary.focus {
  color: #fff;
  background-color: #204d74;
  border-color: #122b40;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  background-image: none;
}
.btn-primary.disabled:hover,
.btn-primary[disabled]:hover,
fieldset[disabled] .btn-primary:hover,
.btn-primary.disabled:focus,
.btn-primary[disabled]:focus,
fieldset[disabled] .btn-primary:focus,
.btn-primary.disabled.focus,
.btn-primary[disabled].focus,
fieldset[disabled] .btn-primary.focus {
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary .badge {
  color: #337ab7;
  background-color: #fff;
}
.btn-success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success:focus,
.btn-success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.btn-success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active:hover,
.btn-success.active:hover,
.open > .dropdown-toggle.btn-success:hover,
.btn-success:active:focus,
.btn-success.active:focus,
.open > .dropdown-toggle.btn-success:focus,
.btn-success:active.focus,
.btn-success.active.focus,
.open > .dropdown-toggle.btn-success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  background-image: none;
}
.btn-success.disabled:hover,
.btn-success[disabled]:hover,
fieldset[disabled] .btn-success:hover,
.btn-success.disabled:focus,
.btn-success[disabled]:focus,
fieldset[disabled] .btn-success:focus,
.btn-success.disabled.focus,
.btn-success[disabled].focus,
fieldset[disabled] .btn-success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.btn-info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info:focus,
.btn-info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.btn-info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active:hover,
.btn-info.active:hover,
.open > .dropdown-toggle.btn-info:hover,
.btn-info:active:focus,
.btn-info.active:focus,
.open > .dropdown-toggle.btn-info:focus,
.btn-info:active.focus,
.btn-info.active.focus,
.open > .dropdown-toggle.btn-info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  background-image: none;
}
.btn-info.disabled:hover,
.btn-info[disabled]:hover,
fieldset[disabled] .btn-info:hover,
.btn-info.disabled:focus,
.btn-info[disabled]:focus,
fieldset[disabled] .btn-info:focus,
.btn-info.disabled.focus,
.btn-info[disabled].focus,
fieldset[disabled] .btn-info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.btn-warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning:focus,
.btn-warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.btn-warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active:hover,
.btn-warning.active:hover,
.open > .dropdown-toggle.btn-warning:hover,
.btn-warning:active:focus,
.btn-warning.active:focus,
.open > .dropdown-toggle.btn-warning:focus,
.btn-warning:active.focus,
.btn-warning.active.focus,
.open > .dropdown-toggle.btn-warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  background-image: none;
}
.btn-warning.disabled:hover,
.btn-warning[disabled]:hover,
fieldset[disabled] .btn-warning:hover,
.btn-warning.disabled:focus,
.btn-warning[disabled]:focus,
fieldset[disabled] .btn-warning:focus,
.btn-warning.disabled.focus,
.btn-warning[disabled].focus,
fieldset[disabled] .btn-warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.btn-danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger:focus,
.btn-danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.btn-danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active:hover,
.btn-danger.active:hover,
.open > .dropdown-toggle.btn-danger:hover,
.btn-danger:active:focus,
.btn-danger.active:focus,
.open > .dropdown-toggle.btn-danger:focus,
.btn-danger:active.focus,
.btn-danger.active.focus,
.open > .dropdown-toggle.btn-danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  background-image: none;
}
.btn-danger.disabled:hover,
.btn-danger[disabled]:hover,
fieldset[disabled] .btn-danger:hover,
.btn-danger.disabled:focus,
.btn-danger[disabled]:focus,
fieldset[disabled] .btn-danger:focus,
.btn-danger.disabled.focus,
.btn-danger[disabled].focus,
fieldset[disabled] .btn-danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger .badge {
  color: #d9534f;
  background-color: #fff;
}
.btn-link {
  color: #337ab7;
  font-weight: normal;
  border-radius: 0;
}
.btn-link,
.btn-link:active,
.btn-link.active,
.btn-link[disabled],
fieldset[disabled] .btn-link {
  background-color: transparent;
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn-link,
.btn-link:hover,
.btn-link:focus,
.btn-link:active {
  border-color: transparent;
}
.btn-link:hover,
.btn-link:focus {
  color: #23527c;
  text-decoration: underline;
  background-color: transparent;
}
.btn-link[disabled]:hover,
fieldset[disabled] .btn-link:hover,
.btn-link[disabled]:focus,
fieldset[disabled] .btn-link:focus {
  color: #777777;
  text-decoration: none;
}
.btn-lg,
.btn-group-lg > .btn {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.btn-sm,
.btn-group-sm > .btn {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-xs,
.btn-group-xs > .btn {
  padding: 1px 5px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-block {
  display: block;
  width: 100%;
}
.btn-block + .btn-block {
  margin-top: 5px;
}
input[type="submit"].btn-block,
input[type="reset"].btn-block,
input[type="button"].btn-block {
  width: 100%;
}
.fade {
  opacity: 0;
  -webkit-transition: opacity 0.15s linear;
  -o-transition: opacity 0.15s linear;
  transition: opacity 0.15s linear;
}
.fade.in {
  opacity: 1;
}
.collapse {
  display: none;
}
.collapse.in {
  display: block;
}
tr.collapse.in {
  display: table-row;
}
tbody.collapse.in {
  display: table-row-group;
}
.collapsing {
  position: relative;
  height: 0;
  overflow: hidden;
  -webkit-transition-property: height, visibility;
  transition-property: height, visibility;
  -webkit-transition-duration: 0.35s;
  transition-duration: 0.35s;
  -webkit-transition-timing-function: ease;
  transition-timing-function: ease;
}
.caret {
  display: inline-block;
  width: 0;
  height: 0;
  margin-left: 2px;
  vertical-align: middle;
  border-top: 4px dashed;
  border-top: 4px solid \9;
  border-right: 4px solid transparent;
  border-left: 4px solid transparent;
}
.dropup,
.dropdown {
  position: relative;
}
.dropdown-toggle:focus {
  outline: 0;
}
.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  display: none;
  float: left;
  min-width: 160px;
  padding: 5px 0;
  margin: 2px 0 0;
  list-style: none;
  font-size: 13px;
  text-align: left;
  background-color: #fff;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.15);
  border-radius: 2px;
  -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  background-clip: padding-box;
}
.dropdown-menu.pull-right {
  right: 0;
  left: auto;
}
.dropdown-menu .divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.dropdown-menu > li > a {
  display: block;
  padding: 3px 20px;
  clear: both;
  font-weight: normal;
  line-height: 1.42857143;
  color: #333333;
  white-space: nowrap;
}
.dropdown-menu > li > a:hover,
.dropdown-menu > li > a:focus {
  text-decoration: none;
  color: #262626;
  background-color: #f5f5f5;
}
.dropdown-menu > .active > a,
.dropdown-menu > .active > a:hover,
.dropdown-menu > .active > a:focus {
  color: #fff;
  text-decoration: none;
  outline: 0;
  background-color: #337ab7;
}
.dropdown-menu > .disabled > a,
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  color: #777777;
}
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  text-decoration: none;
  background-color: transparent;
  background-image: none;
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  cursor: not-allowed;
}
.open > .dropdown-menu {
  display: block;
}
.open > a {
  outline: 0;
}
.dropdown-menu-right {
  left: auto;
  right: 0;
}
.dropdown-menu-left {
  left: 0;
  right: auto;
}
.dropdown-header {
  display: block;
  padding: 3px 20px;
  font-size: 12px;
  line-height: 1.42857143;
  color: #777777;
  white-space: nowrap;
}
.dropdown-backdrop {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  z-index: 990;
}
.pull-right > .dropdown-menu {
  right: 0;
  left: auto;
}
.dropup .caret,
.navbar-fixed-bottom .dropdown .caret {
  border-top: 0;
  border-bottom: 4px dashed;
  border-bottom: 4px solid \9;
  content: "";
}
.dropup .dropdown-menu,
.navbar-fixed-bottom .dropdown .dropdown-menu {
  top: auto;
  bottom: 100%;
  margin-bottom: 2px;
}
@media (min-width: 541px) {
  .navbar-right .dropdown-menu {
    left: auto;
    right: 0;
  }
  .navbar-right .dropdown-menu-left {
    left: 0;
    right: auto;
  }
}
.btn-group,
.btn-group-vertical {
  position: relative;
  display: inline-block;
  vertical-align: middle;
}
.btn-group > .btn,
.btn-group-vertical > .btn {
  position: relative;
  float: left;
}
.btn-group > .btn:hover,
.btn-group-vertical > .btn:hover,
.btn-group > .btn:focus,
.btn-group-vertical > .btn:focus,
.btn-group > .btn:active,
.btn-group-vertical > .btn:active,
.btn-group > .btn.active,
.btn-group-vertical > .btn.active {
  z-index: 2;
}
.btn-group .btn + .btn,
.btn-group .btn + .btn-group,
.btn-group .btn-group + .btn,
.btn-group .btn-group + .btn-group {
  margin-left: -1px;
}
.btn-toolbar {
  margin-left: -5px;
}
.btn-toolbar .btn,
.btn-toolbar .btn-group,
.btn-toolbar .input-group {
  float: left;
}
.btn-toolbar > .btn,
.btn-toolbar > .btn-group,
.btn-toolbar > .input-group {
  margin-left: 5px;
}
.btn-group > .btn:not(:first-child):not(:last-child):not(.dropdown-toggle) {
  border-radius: 0;
}
.btn-group > .btn:first-child {
  margin-left: 0;
}
.btn-group > .btn:first-child:not(:last-child):not(.dropdown-toggle) {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn:last-child:not(:first-child),
.btn-group > .dropdown-toggle:not(:first-child) {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group > .btn-group {
  float: left;
}
.btn-group > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group .dropdown-toggle:active,
.btn-group.open .dropdown-toggle {
  outline: 0;
}
.btn-group > .btn + .dropdown-toggle {
  padding-left: 8px;
  padding-right: 8px;
}
.btn-group > .btn-lg + .dropdown-toggle {
  padding-left: 12px;
  padding-right: 12px;
}
.btn-group.open .dropdown-toggle {
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn-group.open .dropdown-toggle.btn-link {
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn .caret {
  margin-left: 0;
}
.btn-lg .caret {
  border-width: 5px 5px 0;
  border-bottom-width: 0;
}
.dropup .btn-lg .caret {
  border-width: 0 5px 5px;
}
.btn-group-vertical > .btn,
.btn-group-vertical > .btn-group,
.btn-group-vertical > .btn-group > .btn {
  display: block;
  float: none;
  width: 100%;
  max-width: 100%;
}
.btn-group-vertical > .btn-group > .btn {
  float: none;
}
.btn-group-vertical > .btn + .btn,
.btn-group-vertical > .btn + .btn-group,
.btn-group-vertical > .btn-group + .btn,
.btn-group-vertical > .btn-group + .btn-group {
  margin-top: -1px;
  margin-left: 0;
}
.btn-group-vertical > .btn:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.btn-group-vertical > .btn:first-child:not(:last-child) {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn:last-child:not(:first-child) {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
.btn-group-vertical > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.btn-group-justified {
  display: table;
  width: 100%;
  table-layout: fixed;
  border-collapse: separate;
}
.btn-group-justified > .btn,
.btn-group-justified > .btn-group {
  float: none;
  display: table-cell;
  width: 1%;
}
.btn-group-justified > .btn-group .btn {
  width: 100%;
}
.btn-group-justified > .btn-group .dropdown-menu {
  left: auto;
}
[data-toggle="buttons"] > .btn input[type="radio"],
[data-toggle="buttons"] > .btn-group > .btn input[type="radio"],
[data-toggle="buttons"] > .btn input[type="checkbox"],
[data-toggle="buttons"] > .btn-group > .btn input[type="checkbox"] {
  position: absolute;
  clip: rect(0, 0, 0, 0);
  pointer-events: none;
}
.input-group {
  position: relative;
  display: table;
  border-collapse: separate;
}
.input-group[class*="col-"] {
  float: none;
  padding-left: 0;
  padding-right: 0;
}
.input-group .form-control {
  position: relative;
  z-index: 2;
  float: left;
  width: 100%;
  margin-bottom: 0;
}
.input-group .form-control:focus {
  z-index: 3;
}
.input-group-lg > .form-control,
.input-group-lg > .input-group-addon,
.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-group-lg > .form-control,
select.input-group-lg > .input-group-addon,
select.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  line-height: 45px;
}
textarea.input-group-lg > .form-control,
textarea.input-group-lg > .input-group-addon,
textarea.input-group-lg > .input-group-btn > .btn,
select[multiple].input-group-lg > .form-control,
select[multiple].input-group-lg > .input-group-addon,
select[multiple].input-group-lg > .input-group-btn > .btn {
  height: auto;
}
.input-group-sm > .form-control,
.input-group-sm > .input-group-addon,
.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-group-sm > .form-control,
select.input-group-sm > .input-group-addon,
select.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  line-height: 30px;
}
textarea.input-group-sm > .form-control,
textarea.input-group-sm > .input-group-addon,
textarea.input-group-sm > .input-group-btn > .btn,
select[multiple].input-group-sm > .form-control,
select[multiple].input-group-sm > .input-group-addon,
select[multiple].input-group-sm > .input-group-btn > .btn {
  height: auto;
}
.input-group-addon,
.input-group-btn,
.input-group .form-control {
  display: table-cell;
}
.input-group-addon:not(:first-child):not(:last-child),
.input-group-btn:not(:first-child):not(:last-child),
.input-group .form-control:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.input-group-addon,
.input-group-btn {
  width: 1%;
  white-space: nowrap;
  vertical-align: middle;
}
.input-group-addon {
  padding: 6px 12px;
  font-size: 13px;
  font-weight: normal;
  line-height: 1;
  color: #555555;
  text-align: center;
  background-color: #eeeeee;
  border: 1px solid #ccc;
  border-radius: 2px;
}
.input-group-addon.input-sm {
  padding: 5px 10px;
  font-size: 12px;
  border-radius: 1px;
}
.input-group-addon.input-lg {
  padding: 10px 16px;
  font-size: 17px;
  border-radius: 3px;
}
.input-group-addon input[type="radio"],
.input-group-addon input[type="checkbox"] {
  margin-top: 0;
}
.input-group .form-control:first-child,
.input-group-addon:first-child,
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group > .btn,
.input-group-btn:first-child > .dropdown-toggle,
.input-group-btn:last-child > .btn:not(:last-child):not(.dropdown-toggle),
.input-group-btn:last-child > .btn-group:not(:last-child) > .btn {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.input-group-addon:first-child {
  border-right: 0;
}
.input-group .form-control:last-child,
.input-group-addon:last-child,
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group > .btn,
.input-group-btn:last-child > .dropdown-toggle,
.input-group-btn:first-child > .btn:not(:first-child),
.input-group-btn:first-child > .btn-group:not(:first-child) > .btn {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.input-group-addon:last-child {
  border-left: 0;
}
.input-group-btn {
  position: relative;
  font-size: 0;
  white-space: nowrap;
}
.input-group-btn > .btn {
  position: relative;
}
.input-group-btn > .btn + .btn {
  margin-left: -1px;
}
.input-group-btn > .btn:hover,
.input-group-btn > .btn:focus,
.input-group-btn > .btn:active {
  z-index: 2;
}
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group {
  margin-right: -1px;
}
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group {
  z-index: 2;
  margin-left: -1px;
}
.nav {
  margin-bottom: 0;
  padding-left: 0;
  list-style: none;
}
.nav > li {
  position: relative;
  display: block;
}
.nav > li > a {
  position: relative;
  display: block;
  padding: 10px 15px;
}
.nav > li > a:hover,
.nav > li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.nav > li.disabled > a {
  color: #777777;
}
.nav > li.disabled > a:hover,
.nav > li.disabled > a:focus {
  color: #777777;
  text-decoration: none;
  background-color: transparent;
  cursor: not-allowed;
}
.nav .open > a,
.nav .open > a:hover,
.nav .open > a:focus {
  background-color: #eeeeee;
  border-color: #337ab7;
}
.nav .nav-divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.nav > li > a > img {
  max-width: none;
}
.nav-tabs {
  border-bottom: 1px solid #ddd;
}
.nav-tabs > li {
  float: left;
  margin-bottom: -1px;
}
.nav-tabs > li > a {
  margin-right: 2px;
  line-height: 1.42857143;
  border: 1px solid transparent;
  border-radius: 2px 2px 0 0;
}
.nav-tabs > li > a:hover {
  border-color: #eeeeee #eeeeee #ddd;
}
.nav-tabs > li.active > a,
.nav-tabs > li.active > a:hover,
.nav-tabs > li.active > a:focus {
  color: #555555;
  background-color: #fff;
  border: 1px solid #ddd;
  border-bottom-color: transparent;
  cursor: default;
}
.nav-tabs.nav-justified {
  width: 100%;
  border-bottom: 0;
}
.nav-tabs.nav-justified > li {
  float: none;
}
.nav-tabs.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-tabs.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-tabs.nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs.nav-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs.nav-justified > .active > a,
.nav-tabs.nav-justified > .active > a:hover,
.nav-tabs.nav-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs.nav-justified > .active > a,
  .nav-tabs.nav-justified > .active > a:hover,
  .nav-tabs.nav-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.nav-pills > li {
  float: left;
}
.nav-pills > li > a {
  border-radius: 2px;
}
.nav-pills > li + li {
  margin-left: 2px;
}
.nav-pills > li.active > a,
.nav-pills > li.active > a:hover,
.nav-pills > li.active > a:focus {
  color: #fff;
  background-color: #337ab7;
}
.nav-stacked > li {
  float: none;
}
.nav-stacked > li + li {
  margin-top: 2px;
  margin-left: 0;
}
.nav-justified {
  width: 100%;
}
.nav-justified > li {
  float: none;
}
.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs-justified {
  border-bottom: 0;
}
.nav-tabs-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs-justified > .active > a,
.nav-tabs-justified > .active > a:hover,
.nav-tabs-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs-justified > .active > a,
  .nav-tabs-justified > .active > a:hover,
  .nav-tabs-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.tab-content > .tab-pane {
  display: none;
}
.tab-content > .active {
  display: block;
}
.nav-tabs .dropdown-menu {
  margin-top: -1px;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar {
  position: relative;
  min-height: 30px;
  margin-bottom: 18px;
  border: 1px solid transparent;
}
@media (min-width: 541px) {
  .navbar {
    border-radius: 2px;
  }
}
@media (min-width: 541px) {
  .navbar-header {
    float: left;
  }
}
.navbar-collapse {
  overflow-x: visible;
  padding-right: 0px;
  padding-left: 0px;
  border-top: 1px solid transparent;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1);
  -webkit-overflow-scrolling: touch;
}
.navbar-collapse.in {
  overflow-y: auto;
}
@media (min-width: 541px) {
  .navbar-collapse {
    width: auto;
    border-top: 0;
    box-shadow: none;
  }
  .navbar-collapse.collapse {
    display: block !important;
    height: auto !important;
    padding-bottom: 0;
    overflow: visible !important;
  }
  .navbar-collapse.in {
    overflow-y: visible;
  }
  .navbar-fixed-top .navbar-collapse,
  .navbar-static-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    padding-left: 0;
    padding-right: 0;
  }
}
.navbar-fixed-top .navbar-collapse,
.navbar-fixed-bottom .navbar-collapse {
  max-height: 340px;
}
@media (max-device-width: 540px) and (orientation: landscape) {
  .navbar-fixed-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    max-height: 200px;
  }
}
.container > .navbar-header,
.container-fluid > .navbar-header,
.container > .navbar-collapse,
.container-fluid > .navbar-collapse {
  margin-right: 0px;
  margin-left: 0px;
}
@media (min-width: 541px) {
  .container > .navbar-header,
  .container-fluid > .navbar-header,
  .container > .navbar-collapse,
  .container-fluid > .navbar-collapse {
    margin-right: 0;
    margin-left: 0;
  }
}
.navbar-static-top {
  z-index: 1000;
  border-width: 0 0 1px;
}
@media (min-width: 541px) {
  .navbar-static-top {
    border-radius: 0;
  }
}
.navbar-fixed-top,
.navbar-fixed-bottom {
  position: fixed;
  right: 0;
  left: 0;
  z-index: 1030;
}
@media (min-width: 541px) {
  .navbar-fixed-top,
  .navbar-fixed-bottom {
    border-radius: 0;
  }
}
.navbar-fixed-top {
  top: 0;
  border-width: 0 0 1px;
}
.navbar-fixed-bottom {
  bottom: 0;
  margin-bottom: 0;
  border-width: 1px 0 0;
}
.navbar-brand {
  float: left;
  padding: 6px 0px;
  font-size: 17px;
  line-height: 18px;
  height: 30px;
}
.navbar-brand:hover,
.navbar-brand:focus {
  text-decoration: none;
}
.navbar-brand > img {
  display: block;
}
@media (min-width: 541px) {
  .navbar > .container .navbar-brand,
  .navbar > .container-fluid .navbar-brand {
    margin-left: 0px;
  }
}
.navbar-toggle {
  position: relative;
  float: right;
  margin-right: 0px;
  padding: 9px 10px;
  margin-top: -2px;
  margin-bottom: -2px;
  background-color: transparent;
  background-image: none;
  border: 1px solid transparent;
  border-radius: 2px;
}
.navbar-toggle:focus {
  outline: 0;
}
.navbar-toggle .icon-bar {
  display: block;
  width: 22px;
  height: 2px;
  border-radius: 1px;
}
.navbar-toggle .icon-bar + .icon-bar {
  margin-top: 4px;
}
@media (min-width: 541px) {
  .navbar-toggle {
    display: none;
  }
}
.navbar-nav {
  margin: 3px 0px;
}
.navbar-nav > li > a {
  padding-top: 10px;
  padding-bottom: 10px;
  line-height: 18px;
}
@media (max-width: 540px) {
  .navbar-nav .open .dropdown-menu {
    position: static;
    float: none;
    width: auto;
    margin-top: 0;
    background-color: transparent;
    border: 0;
    box-shadow: none;
  }
  .navbar-nav .open .dropdown-menu > li > a,
  .navbar-nav .open .dropdown-menu .dropdown-header {
    padding: 5px 15px 5px 25px;
  }
  .navbar-nav .open .dropdown-menu > li > a {
    line-height: 18px;
  }
  .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-nav .open .dropdown-menu > li > a:focus {
    background-image: none;
  }
}
@media (min-width: 541px) {
  .navbar-nav {
    float: left;
    margin: 0;
  }
  .navbar-nav > li {
    float: left;
  }
  .navbar-nav > li > a {
    padding-top: 6px;
    padding-bottom: 6px;
  }
}
.navbar-form {
  margin-left: 0px;
  margin-right: 0px;
  padding: 10px 0px;
  border-top: 1px solid transparent;
  border-bottom: 1px solid transparent;
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  margin-top: -1px;
  margin-bottom: -1px;
}
@media (min-width: 768px) {
  .navbar-form .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .navbar-form .form-control-static {
    display: inline-block;
  }
  .navbar-form .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .navbar-form .input-group .input-group-addon,
  .navbar-form .input-group .input-group-btn,
  .navbar-form .input-group .form-control {
    width: auto;
  }
  .navbar-form .input-group > .form-control {
    width: 100%;
  }
  .navbar-form .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio,
  .navbar-form .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio label,
  .navbar-form .checkbox label {
    padding-left: 0;
  }
  .navbar-form .radio input[type="radio"],
  .navbar-form .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .navbar-form .has-feedback .form-control-feedback {
    top: 0;
  }
}
@media (max-width: 540px) {
  .navbar-form .form-group {
    margin-bottom: 5px;
  }
  .navbar-form .form-group:last-child {
    margin-bottom: 0;
  }
}
@media (min-width: 541px) {
  .navbar-form {
    width: auto;
    border: 0;
    margin-left: 0;
    margin-right: 0;
    padding-top: 0;
    padding-bottom: 0;
    -webkit-box-shadow: none;
    box-shadow: none;
  }
}
.navbar-nav > li > .dropdown-menu {
  margin-top: 0;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar-fixed-bottom .navbar-nav > li > .dropdown-menu {
  margin-bottom: 0;
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.navbar-btn {
  margin-top: -1px;
  margin-bottom: -1px;
}
.navbar-btn.btn-sm {
  margin-top: 0px;
  margin-bottom: 0px;
}
.navbar-btn.btn-xs {
  margin-top: 4px;
  margin-bottom: 4px;
}
.navbar-text {
  margin-top: 6px;
  margin-bottom: 6px;
}
@media (min-width: 541px) {
  .navbar-text {
    float: left;
    margin-left: 0px;
    margin-right: 0px;
  }
}
@media (min-width: 541px) {
  .navbar-left {
    float: left !important;
    float: left;
  }
  .navbar-right {
    float: right !important;
    float: right;
    margin-right: 0px;
  }
  .navbar-right ~ .navbar-right {
    margin-right: 0;
  }
}
.navbar-default {
  background-color: #f8f8f8;
  border-color: #e7e7e7;
}
.navbar-default .navbar-brand {
  color: #777;
}
.navbar-default .navbar-brand:hover,
.navbar-default .navbar-brand:focus {
  color: #5e5e5e;
  background-color: transparent;
}
.navbar-default .navbar-text {
  color: #777;
}
.navbar-default .navbar-nav > li > a {
  color: #777;
}
.navbar-default .navbar-nav > li > a:hover,
.navbar-default .navbar-nav > li > a:focus {
  color: #333;
  background-color: transparent;
}
.navbar-default .navbar-nav > .active > a,
.navbar-default .navbar-nav > .active > a:hover,
.navbar-default .navbar-nav > .active > a:focus {
  color: #555;
  background-color: #e7e7e7;
}
.navbar-default .navbar-nav > .disabled > a,
.navbar-default .navbar-nav > .disabled > a:hover,
.navbar-default .navbar-nav > .disabled > a:focus {
  color: #ccc;
  background-color: transparent;
}
.navbar-default .navbar-toggle {
  border-color: #ddd;
}
.navbar-default .navbar-toggle:hover,
.navbar-default .navbar-toggle:focus {
  background-color: #ddd;
}
.navbar-default .navbar-toggle .icon-bar {
  background-color: #888;
}
.navbar-default .navbar-collapse,
.navbar-default .navbar-form {
  border-color: #e7e7e7;
}
.navbar-default .navbar-nav > .open > a,
.navbar-default .navbar-nav > .open > a:hover,
.navbar-default .navbar-nav > .open > a:focus {
  background-color: #e7e7e7;
  color: #555;
}
@media (max-width: 540px) {
  .navbar-default .navbar-nav .open .dropdown-menu > li > a {
    color: #777;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #333;
    background-color: transparent;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #555;
    background-color: #e7e7e7;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #ccc;
    background-color: transparent;
  }
}
.navbar-default .navbar-link {
  color: #777;
}
.navbar-default .navbar-link:hover {
  color: #333;
}
.navbar-default .btn-link {
  color: #777;
}
.navbar-default .btn-link:hover,
.navbar-default .btn-link:focus {
  color: #333;
}
.navbar-default .btn-link[disabled]:hover,
fieldset[disabled] .navbar-default .btn-link:hover,
.navbar-default .btn-link[disabled]:focus,
fieldset[disabled] .navbar-default .btn-link:focus {
  color: #ccc;
}
.navbar-inverse {
  background-color: #222;
  border-color: #080808;
}
.navbar-inverse .navbar-brand {
  color: #9d9d9d;
}
.navbar-inverse .navbar-brand:hover,
.navbar-inverse .navbar-brand:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-text {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a:hover,
.navbar-inverse .navbar-nav > li > a:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-nav > .active > a,
.navbar-inverse .navbar-nav > .active > a:hover,
.navbar-inverse .navbar-nav > .active > a:focus {
  color: #fff;
  background-color: #080808;
}
.navbar-inverse .navbar-nav > .disabled > a,
.navbar-inverse .navbar-nav > .disabled > a:hover,
.navbar-inverse .navbar-nav > .disabled > a:focus {
  color: #444;
  background-color: transparent;
}
.navbar-inverse .navbar-toggle {
  border-color: #333;
}
.navbar-inverse .navbar-toggle:hover,
.navbar-inverse .navbar-toggle:focus {
  background-color: #333;
}
.navbar-inverse .navbar-toggle .icon-bar {
  background-color: #fff;
}
.navbar-inverse .navbar-collapse,
.navbar-inverse .navbar-form {
  border-color: #101010;
}
.navbar-inverse .navbar-nav > .open > a,
.navbar-inverse .navbar-nav > .open > a:hover,
.navbar-inverse .navbar-nav > .open > a:focus {
  background-color: #080808;
  color: #fff;
}
@media (max-width: 540px) {
  .navbar-inverse .navbar-nav .open .dropdown-menu > .dropdown-header {
    border-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu .divider {
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a {
    color: #9d9d9d;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #fff;
    background-color: transparent;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #fff;
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #444;
    background-color: transparent;
  }
}
.navbar-inverse .navbar-link {
  color: #9d9d9d;
}
.navbar-inverse .navbar-link:hover {
  color: #fff;
}
.navbar-inverse .btn-link {
  color: #9d9d9d;
}
.navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link:focus {
  color: #fff;
}
.navbar-inverse .btn-link[disabled]:hover,
fieldset[disabled] .navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link[disabled]:focus,
fieldset[disabled] .navbar-inverse .btn-link:focus {
  color: #444;
}
.breadcrumb {
  padding: 8px 15px;
  margin-bottom: 18px;
  list-style: none;
  background-color: #f5f5f5;
  border-radius: 2px;
}
.breadcrumb > li {
  display: inline-block;
}
.breadcrumb > li + li:before {
  content: "/\00a0";
  padding: 0 5px;
  color: #5e5e5e;
}
.breadcrumb > .active {
  color: #777777;
}
.pagination {
  display: inline-block;
  padding-left: 0;
  margin: 18px 0;
  border-radius: 2px;
}
.pagination > li {
  display: inline;
}
.pagination > li > a,
.pagination > li > span {
  position: relative;
  float: left;
  padding: 6px 12px;
  line-height: 1.42857143;
  text-decoration: none;
  color: #337ab7;
  background-color: #fff;
  border: 1px solid #ddd;
  margin-left: -1px;
}
.pagination > li:first-child > a,
.pagination > li:first-child > span {
  margin-left: 0;
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.pagination > li:last-child > a,
.pagination > li:last-child > span {
  border-bottom-right-radius: 2px;
  border-top-right-radius: 2px;
}
.pagination > li > a:hover,
.pagination > li > span:hover,
.pagination > li > a:focus,
.pagination > li > span:focus {
  z-index: 2;
  color: #23527c;
  background-color: #eeeeee;
  border-color: #ddd;
}
.pagination > .active > a,
.pagination > .active > span,
.pagination > .active > a:hover,
.pagination > .active > span:hover,
.pagination > .active > a:focus,
.pagination > .active > span:focus {
  z-index: 3;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
  cursor: default;
}
.pagination > .disabled > span,
.pagination > .disabled > span:hover,
.pagination > .disabled > span:focus,
.pagination > .disabled > a,
.pagination > .disabled > a:hover,
.pagination > .disabled > a:focus {
  color: #777777;
  background-color: #fff;
  border-color: #ddd;
  cursor: not-allowed;
}
.pagination-lg > li > a,
.pagination-lg > li > span {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.pagination-lg > li:first-child > a,
.pagination-lg > li:first-child > span {
  border-bottom-left-radius: 3px;
  border-top-left-radius: 3px;
}
.pagination-lg > li:last-child > a,
.pagination-lg > li:last-child > span {
  border-bottom-right-radius: 3px;
  border-top-right-radius: 3px;
}
.pagination-sm > li > a,
.pagination-sm > li > span {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.pagination-sm > li:first-child > a,
.pagination-sm > li:first-child > span {
  border-bottom-left-radius: 1px;
  border-top-left-radius: 1px;
}
.pagination-sm > li:last-child > a,
.pagination-sm > li:last-child > span {
  border-bottom-right-radius: 1px;
  border-top-right-radius: 1px;
}
.pager {
  padding-left: 0;
  margin: 18px 0;
  list-style: none;
  text-align: center;
}
.pager li {
  display: inline;
}
.pager li > a,
.pager li > span {
  display: inline-block;
  padding: 5px 14px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 15px;
}
.pager li > a:hover,
.pager li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.pager .next > a,
.pager .next > span {
  float: right;
}
.pager .previous > a,
.pager .previous > span {
  float: left;
}
.pager .disabled > a,
.pager .disabled > a:hover,
.pager .disabled > a:focus,
.pager .disabled > span {
  color: #777777;
  background-color: #fff;
  cursor: not-allowed;
}
.label {
  display: inline;
  padding: .2em .6em .3em;
  font-size: 75%;
  font-weight: bold;
  line-height: 1;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: .25em;
}
a.label:hover,
a.label:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.label:empty {
  display: none;
}
.btn .label {
  position: relative;
  top: -1px;
}
.label-default {
  background-color: #777777;
}
.label-default[href]:hover,
.label-default[href]:focus {
  background-color: #5e5e5e;
}
.label-primary {
  background-color: #337ab7;
}
.label-primary[href]:hover,
.label-primary[href]:focus {
  background-color: #286090;
}
.label-success {
  background-color: #5cb85c;
}
.label-success[href]:hover,
.label-success[href]:focus {
  background-color: #449d44;
}
.label-info {
  background-color: #5bc0de;
}
.label-info[href]:hover,
.label-info[href]:focus {
  background-color: #31b0d5;
}
.label-warning {
  background-color: #f0ad4e;
}
.label-warning[href]:hover,
.label-warning[href]:focus {
  background-color: #ec971f;
}
.label-danger {
  background-color: #d9534f;
}
.label-danger[href]:hover,
.label-danger[href]:focus {
  background-color: #c9302c;
}
.badge {
  display: inline-block;
  min-width: 10px;
  padding: 3px 7px;
  font-size: 12px;
  font-weight: bold;
  color: #fff;
  line-height: 1;
  vertical-align: middle;
  white-space: nowrap;
  text-align: center;
  background-color: #777777;
  border-radius: 10px;
}
.badge:empty {
  display: none;
}
.btn .badge {
  position: relative;
  top: -1px;
}
.btn-xs .badge,
.btn-group-xs > .btn .badge {
  top: 0;
  padding: 1px 5px;
}
a.badge:hover,
a.badge:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.list-group-item.active > .badge,
.nav-pills > .active > a > .badge {
  color: #337ab7;
  background-color: #fff;
}
.list-group-item > .badge {
  float: right;
}
.list-group-item > .badge + .badge {
  margin-right: 5px;
}
.nav-pills > li > a > .badge {
  margin-left: 3px;
}
.jumbotron {
  padding-top: 30px;
  padding-bottom: 30px;
  margin-bottom: 30px;
  color: inherit;
  background-color: #eeeeee;
}
.jumbotron h1,
.jumbotron .h1 {
  color: inherit;
}
.jumbotron p {
  margin-bottom: 15px;
  font-size: 20px;
  font-weight: 200;
}
.jumbotron > hr {
  border-top-color: #d5d5d5;
}
.container .jumbotron,
.container-fluid .jumbotron {
  border-radius: 3px;
  padding-left: 0px;
  padding-right: 0px;
}
.jumbotron .container {
  max-width: 100%;
}
@media screen and (min-width: 768px) {
  .jumbotron {
    padding-top: 48px;
    padding-bottom: 48px;
  }
  .container .jumbotron,
  .container-fluid .jumbotron {
    padding-left: 60px;
    padding-right: 60px;
  }
  .jumbotron h1,
  .jumbotron .h1 {
    font-size: 59px;
  }
}
.thumbnail {
  display: block;
  padding: 4px;
  margin-bottom: 18px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: border 0.2s ease-in-out;
  -o-transition: border 0.2s ease-in-out;
  transition: border 0.2s ease-in-out;
}
.thumbnail > img,
.thumbnail a > img {
  margin-left: auto;
  margin-right: auto;
}
a.thumbnail:hover,
a.thumbnail:focus,
a.thumbnail.active {
  border-color: #337ab7;
}
.thumbnail .caption {
  padding: 9px;
  color: #000;
}
.alert {
  padding: 15px;
  margin-bottom: 18px;
  border: 1px solid transparent;
  border-radius: 2px;
}
.alert h4 {
  margin-top: 0;
  color: inherit;
}
.alert .alert-link {
  font-weight: bold;
}
.alert > p,
.alert > ul {
  margin-bottom: 0;
}
.alert > p + p {
  margin-top: 5px;
}
.alert-dismissable,
.alert-dismissible {
  padding-right: 35px;
}
.alert-dismissable .close,
.alert-dismissible .close {
  position: relative;
  top: -2px;
  right: -21px;
  color: inherit;
}
.alert-success {
  background-color: #dff0d8;
  border-color: #d6e9c6;
  color: #3c763d;
}
.alert-success hr {
  border-top-color: #c9e2b3;
}
.alert-success .alert-link {
  color: #2b542c;
}
.alert-info {
  background-color: #d9edf7;
  border-color: #bce8f1;
  color: #31708f;
}
.alert-info hr {
  border-top-color: #a6e1ec;
}
.alert-info .alert-link {
  color: #245269;
}
.alert-warning {
  background-color: #fcf8e3;
  border-color: #faebcc;
  color: #8a6d3b;
}
.alert-warning hr {
  border-top-color: #f7e1b5;
}
.alert-warning .alert-link {
  color: #66512c;
}
.alert-danger {
  background-color: #f2dede;
  border-color: #ebccd1;
  color: #a94442;
}
.alert-danger hr {
  border-top-color: #e4b9c0;
}
.alert-danger .alert-link {
  color: #843534;
}
@-webkit-keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
@keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
.progress {
  overflow: hidden;
  height: 18px;
  margin-bottom: 18px;
  background-color: #f5f5f5;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
}
.progress-bar {
  float: left;
  width: 0%;
  height: 100%;
  font-size: 12px;
  line-height: 18px;
  color: #fff;
  text-align: center;
  background-color: #337ab7;
  -webkit-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  -webkit-transition: width 0.6s ease;
  -o-transition: width 0.6s ease;
  transition: width 0.6s ease;
}
.progress-striped .progress-bar,
.progress-bar-striped {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-size: 40px 40px;
}
.progress.active .progress-bar,
.progress-bar.active {
  -webkit-animation: progress-bar-stripes 2s linear infinite;
  -o-animation: progress-bar-stripes 2s linear infinite;
  animation: progress-bar-stripes 2s linear infinite;
}
.progress-bar-success {
  background-color: #5cb85c;
}
.progress-striped .progress-bar-success {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-info {
  background-color: #5bc0de;
}
.progress-striped .progress-bar-info {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-warning {
  background-color: #f0ad4e;
}
.progress-striped .progress-bar-warning {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-danger {
  background-color: #d9534f;
}
.progress-striped .progress-bar-danger {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.media {
  margin-top: 15px;
}
.media:first-child {
  margin-top: 0;
}
.media,
.media-body {
  zoom: 1;
  overflow: hidden;
}
.media-body {
  width: 10000px;
}
.media-object {
  display: block;
}
.media-object.img-thumbnail {
  max-width: none;
}
.media-right,
.media > .pull-right {
  padding-left: 10px;
}
.media-left,
.media > .pull-left {
  padding-right: 10px;
}
.media-left,
.media-right,
.media-body {
  display: table-cell;
  vertical-align: top;
}
.media-middle {
  vertical-align: middle;
}
.media-bottom {
  vertical-align: bottom;
}
.media-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.media-list {
  padding-left: 0;
  list-style: none;
}
.list-group {
  margin-bottom: 20px;
  padding-left: 0;
}
.list-group-item {
  position: relative;
  display: block;
  padding: 10px 15px;
  margin-bottom: -1px;
  background-color: #fff;
  border: 1px solid #ddd;
}
.list-group-item:first-child {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
}
.list-group-item:last-child {
  margin-bottom: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
a.list-group-item,
button.list-group-item {
  color: #555;
}
a.list-group-item .list-group-item-heading,
button.list-group-item .list-group-item-heading {
  color: #333;
}
a.list-group-item:hover,
button.list-group-item:hover,
a.list-group-item:focus,
button.list-group-item:focus {
  text-decoration: none;
  color: #555;
  background-color: #f5f5f5;
}
button.list-group-item {
  width: 100%;
  text-align: left;
}
.list-group-item.disabled,
.list-group-item.disabled:hover,
.list-group-item.disabled:focus {
  background-color: #eeeeee;
  color: #777777;
  cursor: not-allowed;
}
.list-group-item.disabled .list-group-item-heading,
.list-group-item.disabled:hover .list-group-item-heading,
.list-group-item.disabled:focus .list-group-item-heading {
  color: inherit;
}
.list-group-item.disabled .list-group-item-text,
.list-group-item.disabled:hover .list-group-item-text,
.list-group-item.disabled:focus .list-group-item-text {
  color: #777777;
}
.list-group-item.active,
.list-group-item.active:hover,
.list-group-item.active:focus {
  z-index: 2;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.list-group-item.active .list-group-item-heading,
.list-group-item.active:hover .list-group-item-heading,
.list-group-item.active:focus .list-group-item-heading,
.list-group-item.active .list-group-item-heading > small,
.list-group-item.active:hover .list-group-item-heading > small,
.list-group-item.active:focus .list-group-item-heading > small,
.list-group-item.active .list-group-item-heading > .small,
.list-group-item.active:hover .list-group-item-heading > .small,
.list-group-item.active:focus .list-group-item-heading > .small {
  color: inherit;
}
.list-group-item.active .list-group-item-text,
.list-group-item.active:hover .list-group-item-text,
.list-group-item.active:focus .list-group-item-text {
  color: #c7ddef;
}
.list-group-item-success {
  color: #3c763d;
  background-color: #dff0d8;
}
a.list-group-item-success,
button.list-group-item-success {
  color: #3c763d;
}
a.list-group-item-success .list-group-item-heading,
button.list-group-item-success .list-group-item-heading {
  color: inherit;
}
a.list-group-item-success:hover,
button.list-group-item-success:hover,
a.list-group-item-success:focus,
button.list-group-item-success:focus {
  color: #3c763d;
  background-color: #d0e9c6;
}
a.list-group-item-success.active,
button.list-group-item-success.active,
a.list-group-item-success.active:hover,
button.list-group-item-success.active:hover,
a.list-group-item-success.active:focus,
button.list-group-item-success.active:focus {
  color: #fff;
  background-color: #3c763d;
  border-color: #3c763d;
}
.list-group-item-info {
  color: #31708f;
  background-color: #d9edf7;
}
a.list-group-item-info,
button.list-group-item-info {
  color: #31708f;
}
a.list-group-item-info .list-group-item-heading,
button.list-group-item-info .list-group-item-heading {
  color: inherit;
}
a.list-group-item-info:hover,
button.list-group-item-info:hover,
a.list-group-item-info:focus,
button.list-group-item-info:focus {
  color: #31708f;
  background-color: #c4e3f3;
}
a.list-group-item-info.active,
button.list-group-item-info.active,
a.list-group-item-info.active:hover,
button.list-group-item-info.active:hover,
a.list-group-item-info.active:focus,
button.list-group-item-info.active:focus {
  color: #fff;
  background-color: #31708f;
  border-color: #31708f;
}
.list-group-item-warning {
  color: #8a6d3b;
  background-color: #fcf8e3;
}
a.list-group-item-warning,
button.list-group-item-warning {
  color: #8a6d3b;
}
a.list-group-item-warning .list-group-item-heading,
button.list-group-item-warning .list-group-item-heading {
  color: inherit;
}
a.list-group-item-warning:hover,
button.list-group-item-warning:hover,
a.list-group-item-warning:focus,
button.list-group-item-warning:focus {
  color: #8a6d3b;
  background-color: #faf2cc;
}
a.list-group-item-warning.active,
button.list-group-item-warning.active,
a.list-group-item-warning.active:hover,
button.list-group-item-warning.active:hover,
a.list-group-item-warning.active:focus,
button.list-group-item-warning.active:focus {
  color: #fff;
  background-color: #8a6d3b;
  border-color: #8a6d3b;
}
.list-group-item-danger {
  color: #a94442;
  background-color: #f2dede;
}
a.list-group-item-danger,
button.list-group-item-danger {
  color: #a94442;
}
a.list-group-item-danger .list-group-item-heading,
button.list-group-item-danger .list-group-item-heading {
  color: inherit;
}
a.list-group-item-danger:hover,
button.list-group-item-danger:hover,
a.list-group-item-danger:focus,
button.list-group-item-danger:focus {
  color: #a94442;
  background-color: #ebcccc;
}
a.list-group-item-danger.active,
button.list-group-item-danger.active,
a.list-group-item-danger.active:hover,
button.list-group-item-danger.active:hover,
a.list-group-item-danger.active:focus,
button.list-group-item-danger.active:focus {
  color: #fff;
  background-color: #a94442;
  border-color: #a94442;
}
.list-group-item-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.list-group-item-text {
  margin-bottom: 0;
  line-height: 1.3;
}
.panel {
  margin-bottom: 18px;
  background-color: #fff;
  border: 1px solid transparent;
  border-radius: 2px;
  -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
}
.panel-body {
  padding: 15px;
}
.panel-heading {
  padding: 10px 15px;
  border-bottom: 1px solid transparent;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel-heading > .dropdown .dropdown-toggle {
  color: inherit;
}
.panel-title {
  margin-top: 0;
  margin-bottom: 0;
  font-size: 15px;
  color: inherit;
}
.panel-title > a,
.panel-title > small,
.panel-title > .small,
.panel-title > small > a,
.panel-title > .small > a {
  color: inherit;
}
.panel-footer {
  padding: 10px 15px;
  background-color: #f5f5f5;
  border-top: 1px solid #ddd;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .list-group,
.panel > .panel-collapse > .list-group {
  margin-bottom: 0;
}
.panel > .list-group .list-group-item,
.panel > .panel-collapse > .list-group .list-group-item {
  border-width: 1px 0;
  border-radius: 0;
}
.panel > .list-group:first-child .list-group-item:first-child,
.panel > .panel-collapse > .list-group:first-child .list-group-item:first-child {
  border-top: 0;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .list-group:last-child .list-group-item:last-child,
.panel > .panel-collapse > .list-group:last-child .list-group-item:last-child {
  border-bottom: 0;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .panel-heading + .panel-collapse > .list-group .list-group-item:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.panel-heading + .list-group .list-group-item:first-child {
  border-top-width: 0;
}
.list-group + .panel-footer {
  border-top-width: 0;
}
.panel > .table,
.panel > .table-responsive > .table,
.panel > .panel-collapse > .table {
  margin-bottom: 0;
}
.panel > .table caption,
.panel > .table-responsive > .table caption,
.panel > .panel-collapse > .table caption {
  padding-left: 15px;
  padding-right: 15px;
}
.panel > .table:first-child,
.panel > .table-responsive:first-child > .table:first-child {
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child {
  border-top-left-radius: 1px;
  border-top-right-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:first-child {
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:last-child {
  border-top-right-radius: 1px;
}
.panel > .table:last-child,
.panel > .table-responsive:last-child > .table:last-child {
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child {
  border-bottom-left-radius: 1px;
  border-bottom-right-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:first-child {
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:last-child {
  border-bottom-right-radius: 1px;
}
.panel > .panel-body + .table,
.panel > .panel-body + .table-responsive,
.panel > .table + .panel-body,
.panel > .table-responsive + .panel-body {
  border-top: 1px solid #ddd;
}
.panel > .table > tbody:first-child > tr:first-child th,
.panel > .table > tbody:first-child > tr:first-child td {
  border-top: 0;
}
.panel > .table-bordered,
.panel > .table-responsive > .table-bordered {
  border: 0;
}
.panel > .table-bordered > thead > tr > th:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:first-child,
.panel > .table-bordered > tbody > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:first-child,
.panel > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-bordered > thead > tr > td:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:first-child,
.panel > .table-bordered > tbody > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:first-child,
.panel > .table-bordered > tfoot > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:first-child {
  border-left: 0;
}
.panel > .table-bordered > thead > tr > th:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:last-child,
.panel > .table-bordered > tbody > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:last-child,
.panel > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-bordered > thead > tr > td:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:last-child,
.panel > .table-bordered > tbody > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:last-child,
.panel > .table-bordered > tfoot > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:last-child {
  border-right: 0;
}
.panel > .table-bordered > thead > tr:first-child > td,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > td,
.panel > .table-bordered > tbody > tr:first-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > td,
.panel > .table-bordered > thead > tr:first-child > th,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > th,
.panel > .table-bordered > tbody > tr:first-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > th {
  border-bottom: 0;
}
.panel > .table-bordered > tbody > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > td,
.panel > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-bordered > tbody > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > th,
.panel > .table-bordered > tfoot > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > th {
  border-bottom: 0;
}
.panel > .table-responsive {
  border: 0;
  margin-bottom: 0;
}
.panel-group {
  margin-bottom: 18px;
}
.panel-group .panel {
  margin-bottom: 0;
  border-radius: 2px;
}
.panel-group .panel + .panel {
  margin-top: 5px;
}
.panel-group .panel-heading {
  border-bottom: 0;
}
.panel-group .panel-heading + .panel-collapse > .panel-body,
.panel-group .panel-heading + .panel-collapse > .list-group {
  border-top: 1px solid #ddd;
}
.panel-group .panel-footer {
  border-top: 0;
}
.panel-group .panel-footer + .panel-collapse .panel-body {
  border-bottom: 1px solid #ddd;
}
.panel-default {
  border-color: #ddd;
}
.panel-default > .panel-heading {
  color: #333333;
  background-color: #f5f5f5;
  border-color: #ddd;
}
.panel-default > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ddd;
}
.panel-default > .panel-heading .badge {
  color: #f5f5f5;
  background-color: #333333;
}
.panel-default > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ddd;
}
.panel-primary {
  border-color: #337ab7;
}
.panel-primary > .panel-heading {
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.panel-primary > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #337ab7;
}
.panel-primary > .panel-heading .badge {
  color: #337ab7;
  background-color: #fff;
}
.panel-primary > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #337ab7;
}
.panel-success {
  border-color: #d6e9c6;
}
.panel-success > .panel-heading {
  color: #3c763d;
  background-color: #dff0d8;
  border-color: #d6e9c6;
}
.panel-success > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #d6e9c6;
}
.panel-success > .panel-heading .badge {
  color: #dff0d8;
  background-color: #3c763d;
}
.panel-success > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #d6e9c6;
}
.panel-info {
  border-color: #bce8f1;
}
.panel-info > .panel-heading {
  color: #31708f;
  background-color: #d9edf7;
  border-color: #bce8f1;
}
.panel-info > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #bce8f1;
}
.panel-info > .panel-heading .badge {
  color: #d9edf7;
  background-color: #31708f;
}
.panel-info > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #bce8f1;
}
.panel-warning {
  border-color: #faebcc;
}
.panel-warning > .panel-heading {
  color: #8a6d3b;
  background-color: #fcf8e3;
  border-color: #faebcc;
}
.panel-warning > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #faebcc;
}
.panel-warning > .panel-heading .badge {
  color: #fcf8e3;
  background-color: #8a6d3b;
}
.panel-warning > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #faebcc;
}
.panel-danger {
  border-color: #ebccd1;
}
.panel-danger > .panel-heading {
  color: #a94442;
  background-color: #f2dede;
  border-color: #ebccd1;
}
.panel-danger > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ebccd1;
}
.panel-danger > .panel-heading .badge {
  color: #f2dede;
  background-color: #a94442;
}
.panel-danger > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ebccd1;
}
.embed-responsive {
  position: relative;
  display: block;
  height: 0;
  padding: 0;
  overflow: hidden;
}
.embed-responsive .embed-responsive-item,
.embed-responsive iframe,
.embed-responsive embed,
.embed-responsive object,
.embed-responsive video {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  height: 100%;
  width: 100%;
  border: 0;
}
.embed-responsive-16by9 {
  padding-bottom: 56.25%;
}
.embed-responsive-4by3 {
  padding-bottom: 75%;
}
.well {
  min-height: 20px;
  padding: 19px;
  margin-bottom: 20px;
  background-color: #f5f5f5;
  border: 1px solid #e3e3e3;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
}
.well blockquote {
  border-color: #ddd;
  border-color: rgba(0, 0, 0, 0.15);
}
.well-lg {
  padding: 24px;
  border-radius: 3px;
}
.well-sm {
  padding: 9px;
  border-radius: 1px;
}
.close {
  float: right;
  font-size: 19.5px;
  font-weight: bold;
  line-height: 1;
  color: #000;
  text-shadow: 0 1px 0 #fff;
  opacity: 0.2;
  filter: alpha(opacity=20);
}
.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
  opacity: 0.5;
  filter: alpha(opacity=50);
}
button.close {
  padding: 0;
  cursor: pointer;
  background: transparent;
  border: 0;
  -webkit-appearance: none;
}
.modal-open {
  overflow: hidden;
}
.modal {
  display: none;
  overflow: hidden;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1050;
  -webkit-overflow-scrolling: touch;
  outline: 0;
}
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, -25%);
  -ms-transform: translate(0, -25%);
  -o-transform: translate(0, -25%);
  transform: translate(0, -25%);
  -webkit-transition: -webkit-transform 0.3s ease-out;
  -moz-transition: -moz-transform 0.3s ease-out;
  -o-transition: -o-transform 0.3s ease-out;
  transition: transform 0.3s ease-out;
}
.modal.in .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
.modal-open .modal {
  overflow-x: hidden;
  overflow-y: auto;
}
.modal-dialog {
  position: relative;
  width: auto;
  margin: 10px;
}
.modal-content {
  position: relative;
  background-color: #fff;
  border: 1px solid #999;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  background-clip: padding-box;
  outline: 0;
}
.modal-backdrop {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1040;
  background-color: #000;
}
.modal-backdrop.fade {
  opacity: 0;
  filter: alpha(opacity=0);
}
.modal-backdrop.in {
  opacity: 0.5;
  filter: alpha(opacity=50);
}
.modal-header {
  padding: 15px;
  border-bottom: 1px solid #e5e5e5;
}
.modal-header .close {
  margin-top: -2px;
}
.modal-title {
  margin: 0;
  line-height: 1.42857143;
}
.modal-body {
  position: relative;
  padding: 15px;
}
.modal-footer {
  padding: 15px;
  text-align: right;
  border-top: 1px solid #e5e5e5;
}
.modal-footer .btn + .btn {
  margin-left: 5px;
  margin-bottom: 0;
}
.modal-footer .btn-group .btn + .btn {
  margin-left: -1px;
}
.modal-footer .btn-block + .btn-block {
  margin-left: 0;
}
.modal-scrollbar-measure {
  position: absolute;
  top: -9999px;
  width: 50px;
  height: 50px;
  overflow: scroll;
}
@media (min-width: 768px) {
  .modal-dialog {
    width: 600px;
    margin: 30px auto;
  }
  .modal-content {
    -webkit-box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  }
  .modal-sm {
    width: 300px;
  }
}
@media (min-width: 992px) {
  .modal-lg {
    width: 900px;
  }
}
.tooltip {
  position: absolute;
  z-index: 1070;
  display: block;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 12px;
  opacity: 0;
  filter: alpha(opacity=0);
}
.tooltip.in {
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.tooltip.top {
  margin-top: -3px;
  padding: 5px 0;
}
.tooltip.right {
  margin-left: 3px;
  padding: 0 5px;
}
.tooltip.bottom {
  margin-top: 3px;
  padding: 5px 0;
}
.tooltip.left {
  margin-left: -3px;
  padding: 0 5px;
}
.tooltip-inner {
  max-width: 200px;
  padding: 3px 8px;
  color: #fff;
  text-align: center;
  background-color: #000;
  border-radius: 2px;
}
.tooltip-arrow {
  position: absolute;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.tooltip.top .tooltip-arrow {
  bottom: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-left .tooltip-arrow {
  bottom: 0;
  right: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-right .tooltip-arrow {
  bottom: 0;
  left: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.right .tooltip-arrow {
  top: 50%;
  left: 0;
  margin-top: -5px;
  border-width: 5px 5px 5px 0;
  border-right-color: #000;
}
.tooltip.left .tooltip-arrow {
  top: 50%;
  right: 0;
  margin-top: -5px;
  border-width: 5px 0 5px 5px;
  border-left-color: #000;
}
.tooltip.bottom .tooltip-arrow {
  top: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-left .tooltip-arrow {
  top: 0;
  right: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-right .tooltip-arrow {
  top: 0;
  left: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.popover {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1060;
  display: none;
  max-width: 276px;
  padding: 1px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 13px;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}
.popover.top {
  margin-top: -10px;
}
.popover.right {
  margin-left: 10px;
}
.popover.bottom {
  margin-top: 10px;
}
.popover.left {
  margin-left: -10px;
}
.popover-title {
  margin: 0;
  padding: 8px 14px;
  font-size: 13px;
  background-color: #f7f7f7;
  border-bottom: 1px solid #ebebeb;
  border-radius: 2px 2px 0 0;
}
.popover-content {
  padding: 9px 14px;
}
.popover > .arrow,
.popover > .arrow:after {
  position: absolute;
  display: block;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.popover > .arrow {
  border-width: 11px;
}
.popover > .arrow:after {
  border-width: 10px;
  content: "";
}
.popover.top > .arrow {
  left: 50%;
  margin-left: -11px;
  border-bottom-width: 0;
  border-top-color: #999999;
  border-top-color: rgba(0, 0, 0, 0.25);
  bottom: -11px;
}
.popover.top > .arrow:after {
  content: " ";
  bottom: 1px;
  margin-left: -10px;
  border-bottom-width: 0;
  border-top-color: #fff;
}
.popover.right > .arrow {
  top: 50%;
  left: -11px;
  margin-top: -11px;
  border-left-width: 0;
  border-right-color: #999999;
  border-right-color: rgba(0, 0, 0, 0.25);
}
.popover.right > .arrow:after {
  content: " ";
  left: 1px;
  bottom: -10px;
  border-left-width: 0;
  border-right-color: #fff;
}
.popover.bottom > .arrow {
  left: 50%;
  margin-left: -11px;
  border-top-width: 0;
  border-bottom-color: #999999;
  border-bottom-color: rgba(0, 0, 0, 0.25);
  top: -11px;
}
.popover.bottom > .arrow:after {
  content: " ";
  top: 1px;
  margin-left: -10px;
  border-top-width: 0;
  border-bottom-color: #fff;
}
.popover.left > .arrow {
  top: 50%;
  right: -11px;
  margin-top: -11px;
  border-right-width: 0;
  border-left-color: #999999;
  border-left-color: rgba(0, 0, 0, 0.25);
}
.popover.left > .arrow:after {
  content: " ";
  right: 1px;
  border-right-width: 0;
  border-left-color: #fff;
  bottom: -10px;
}
.carousel {
  position: relative;
}
.carousel-inner {
  position: relative;
  overflow: hidden;
  width: 100%;
}
.carousel-inner > .item {
  display: none;
  position: relative;
  -webkit-transition: 0.6s ease-in-out left;
  -o-transition: 0.6s ease-in-out left;
  transition: 0.6s ease-in-out left;
}
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  line-height: 1;
}
@media all and (transform-3d), (-webkit-transform-3d) {
  .carousel-inner > .item {
    -webkit-transition: -webkit-transform 0.6s ease-in-out;
    -moz-transition: -moz-transform 0.6s ease-in-out;
    -o-transition: -o-transform 0.6s ease-in-out;
    transition: transform 0.6s ease-in-out;
    -webkit-backface-visibility: hidden;
    -moz-backface-visibility: hidden;
    backface-visibility: hidden;
    -webkit-perspective: 1000px;
    -moz-perspective: 1000px;
    perspective: 1000px;
  }
  .carousel-inner > .item.next,
  .carousel-inner > .item.active.right {
    -webkit-transform: translate3d(100%, 0, 0);
    transform: translate3d(100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.prev,
  .carousel-inner > .item.active.left {
    -webkit-transform: translate3d(-100%, 0, 0);
    transform: translate3d(-100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.next.left,
  .carousel-inner > .item.prev.right,
  .carousel-inner > .item.active {
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
    left: 0;
  }
}
.carousel-inner > .active,
.carousel-inner > .next,
.carousel-inner > .prev {
  display: block;
}
.carousel-inner > .active {
  left: 0;
}
.carousel-inner > .next,
.carousel-inner > .prev {
  position: absolute;
  top: 0;
  width: 100%;
}
.carousel-inner > .next {
  left: 100%;
}
.carousel-inner > .prev {
  left: -100%;
}
.carousel-inner > .next.left,
.carousel-inner > .prev.right {
  left: 0;
}
.carousel-inner > .active.left {
  left: -100%;
}
.carousel-inner > .active.right {
  left: 100%;
}
.carousel-control {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 15%;
  opacity: 0.5;
  filter: alpha(opacity=50);
  font-size: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
  background-color: rgba(0, 0, 0, 0);
}
.carousel-control.left {
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#80000000', endColorstr='#00000000', GradientType=1);
}
.carousel-control.right {
  left: auto;
  right: 0;
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#00000000', endColorstr='#80000000', GradientType=1);
}
.carousel-control:hover,
.carousel-control:focus {
  outline: 0;
  color: #fff;
  text-decoration: none;
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.carousel-control .icon-prev,
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-left,
.carousel-control .glyphicon-chevron-right {
  position: absolute;
  top: 50%;
  margin-top: -10px;
  z-index: 5;
  display: inline-block;
}
.carousel-control .icon-prev,
.carousel-control .glyphicon-chevron-left {
  left: 50%;
  margin-left: -10px;
}
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-right {
  right: 50%;
  margin-right: -10px;
}
.carousel-control .icon-prev,
.carousel-control .icon-next {
  width: 20px;
  height: 20px;
  line-height: 1;
  font-family: serif;
}
.carousel-control .icon-prev:before {
  content: '\2039';
}
.carousel-control .icon-next:before {
  content: '\203a';
}
.carousel-indicators {
  position: absolute;
  bottom: 10px;
  left: 50%;
  z-index: 15;
  width: 60%;
  margin-left: -30%;
  padding-left: 0;
  list-style: none;
  text-align: center;
}
.carousel-indicators li {
  display: inline-block;
  width: 10px;
  height: 10px;
  margin: 1px;
  text-indent: -999px;
  border: 1px solid #fff;
  border-radius: 10px;
  cursor: pointer;
  background-color: #000 \9;
  background-color: rgba(0, 0, 0, 0);
}
.carousel-indicators .active {
  margin: 0;
  width: 12px;
  height: 12px;
  background-color: #fff;
}
.carousel-caption {
  position: absolute;
  left: 15%;
  right: 15%;
  bottom: 20px;
  z-index: 10;
  padding-top: 20px;
  padding-bottom: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
}
.carousel-caption .btn {
  text-shadow: none;
}
@media screen and (min-width: 768px) {
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-prev,
  .carousel-control .icon-next {
    width: 30px;
    height: 30px;
    margin-top: -10px;
    font-size: 30px;
  }
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .icon-prev {
    margin-left: -10px;
  }
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-next {
    margin-right: -10px;
  }
  .carousel-caption {
    left: 20%;
    right: 20%;
    padding-bottom: 30px;
  }
  .carousel-indicators {
    bottom: 20px;
  }
}
.clearfix:before,
.clearfix:after,
.dl-horizontal dd:before,
.dl-horizontal dd:after,
.container:before,
.container:after,
.container-fluid:before,
.container-fluid:after,
.row:before,
.row:after,
.form-horizontal .form-group:before,
.form-horizontal .form-group:after,
.btn-toolbar:before,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:before,
.btn-group-vertical > .btn-group:after,
.nav:before,
.nav:after,
.navbar:before,
.navbar:after,
.navbar-header:before,
.navbar-header:after,
.navbar-collapse:before,
.navbar-collapse:after,
.pager:before,
.pager:after,
.panel-body:before,
.panel-body:after,
.modal-header:before,
.modal-header:after,
.modal-footer:before,
.modal-footer:after,
.item_buttons:before,
.item_buttons:after {
  content: " ";
  display: table;
}
.clearfix:after,
.dl-horizontal dd:after,
.container:after,
.container-fluid:after,
.row:after,
.form-horizontal .form-group:after,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:after,
.nav:after,
.navbar:after,
.navbar-header:after,
.navbar-collapse:after,
.pager:after,
.panel-body:after,
.modal-header:after,
.modal-footer:after,
.item_buttons:after {
  clear: both;
}
.center-block {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.pull-right {
  float: right !important;
}
.pull-left {
  float: left !important;
}
.hide {
  display: none !important;
}
.show {
  display: block !important;
}
.invisible {
  visibility: hidden;
}
.text-hide {
  font: 0/0 a;
  color: transparent;
  text-shadow: none;
  background-color: transparent;
  border: 0;
}
.hidden {
  display: none !important;
}
.affix {
  position: fixed;
}
@-ms-viewport {
  width: device-width;
}
.visible-xs,
.visible-sm,
.visible-md,
.visible-lg {
  display: none !important;
}
.visible-xs-block,
.visible-xs-inline,
.visible-xs-inline-block,
.visible-sm-block,
.visible-sm-inline,
.visible-sm-inline-block,
.visible-md-block,
.visible-md-inline,
.visible-md-inline-block,
.visible-lg-block,
.visible-lg-inline,
.visible-lg-inline-block {
  display: none !important;
}
@media (max-width: 767px) {
  .visible-xs {
    display: block !important;
  }
  table.visible-xs {
    display: table !important;
  }
  tr.visible-xs {
    display: table-row !important;
  }
  th.visible-xs,
  td.visible-xs {
    display: table-cell !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-block {
    display: block !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline {
    display: inline !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm {
    display: block !important;
  }
  table.visible-sm {
    display: table !important;
  }
  tr.visible-sm {
    display: table-row !important;
  }
  th.visible-sm,
  td.visible-sm {
    display: table-cell !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-block {
    display: block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline {
    display: inline !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md {
    display: block !important;
  }
  table.visible-md {
    display: table !important;
  }
  tr.visible-md {
    display: table-row !important;
  }
  th.visible-md,
  td.visible-md {
    display: table-cell !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-block {
    display: block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline {
    display: inline !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg {
    display: block !important;
  }
  table.visible-lg {
    display: table !important;
  }
  tr.visible-lg {
    display: table-row !important;
  }
  th.visible-lg,
  td.visible-lg {
    display: table-cell !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-block {
    display: block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline {
    display: inline !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline-block {
    display: inline-block !important;
  }
}
@media (max-width: 767px) {
  .hidden-xs {
    display: none !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .hidden-sm {
    display: none !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .hidden-md {
    display: none !important;
  }
}
@media (min-width: 1200px) {
  .hidden-lg {
    display: none !important;
  }
}
.visible-print {
  display: none !important;
}
@media print {
  .visible-print {
    display: block !important;
  }
  table.visible-print {
    display: table !important;
  }
  tr.visible-print {
    display: table-row !important;
  }
  th.visible-print,
  td.visible-print {
    display: table-cell !important;
  }
}
.visible-print-block {
  display: none !important;
}
@media print {
  .visible-print-block {
    display: block !important;
  }
}
.visible-print-inline {
  display: none !important;
}
@media print {
  .visible-print-inline {
    display: inline !important;
  }
}
.visible-print-inline-block {
  display: none !important;
}
@media print {
  .visible-print-inline-block {
    display: inline-block !important;
  }
}
@media print {
  .hidden-print {
    display: none !important;
  }
}
/*!
*
* Font Awesome
*
*/
/*!
 *  Font Awesome 4.7.0 by @davegandy - http://fontawesome.io - @fontawesome
 *  License - http://fontawesome.io/license (Font: SIL OFL 1.1, CSS: MIT License)
 */
/* FONT PATH
 * -------------------------- */
@font-face {
  font-family: 'FontAwesome';
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?v=4.7.0');
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?#iefix&v=4.7.0') format('embedded-opentype'), url('../components/font-awesome/fonts/fontawesome-webfont.woff2?v=4.7.0') format('woff2'), url('../components/font-awesome/fonts/fontawesome-webfont.woff?v=4.7.0') format('woff'), url('../components/font-awesome/fonts/fontawesome-webfont.ttf?v=4.7.0') format('truetype'), url('../components/font-awesome/fonts/fontawesome-webfont.svg?v=4.7.0#fontawesomeregular') format('svg');
  font-weight: normal;
  font-style: normal;
}
.fa {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
/* makes the font 33% larger relative to the icon container */
.fa-lg {
  font-size: 1.33333333em;
  line-height: 0.75em;
  vertical-align: -15%;
}
.fa-2x {
  font-size: 2em;
}
.fa-3x {
  font-size: 3em;
}
.fa-4x {
  font-size: 4em;
}
.fa-5x {
  font-size: 5em;
}
.fa-fw {
  width: 1.28571429em;
  text-align: center;
}
.fa-ul {
  padding-left: 0;
  margin-left: 2.14285714em;
  list-style-type: none;
}
.fa-ul > li {
  position: relative;
}
.fa-li {
  position: absolute;
  left: -2.14285714em;
  width: 2.14285714em;
  top: 0.14285714em;
  text-align: center;
}
.fa-li.fa-lg {
  left: -1.85714286em;
}
.fa-border {
  padding: .2em .25em .15em;
  border: solid 0.08em #eee;
  border-radius: .1em;
}
.fa-pull-left {
  float: left;
}
.fa-pull-right {
  float: right;
}
.fa.fa-pull-left {
  margin-right: .3em;
}
.fa.fa-pull-right {
  margin-left: .3em;
}
/* Deprecated as of 4.4.0 */
.pull-right {
  float: right;
}
.pull-left {
  float: left;
}
.fa.pull-left {
  margin-right: .3em;
}
.fa.pull-right {
  margin-left: .3em;
}
.fa-spin {
  -webkit-animation: fa-spin 2s infinite linear;
  animation: fa-spin 2s infinite linear;
}
.fa-pulse {
  -webkit-animation: fa-spin 1s infinite steps(8);
  animation: fa-spin 1s infinite steps(8);
}
@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
.fa-rotate-90 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=1)";
  -webkit-transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transform: rotate(90deg);
}
.fa-rotate-180 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2)";
  -webkit-transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  transform: rotate(180deg);
}
.fa-rotate-270 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=3)";
  -webkit-transform: rotate(270deg);
  -ms-transform: rotate(270deg);
  transform: rotate(270deg);
}
.fa-flip-horizontal {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1)";
  -webkit-transform: scale(-1, 1);
  -ms-transform: scale(-1, 1);
  transform: scale(-1, 1);
}
.fa-flip-vertical {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1)";
  -webkit-transform: scale(1, -1);
  -ms-transform: scale(1, -1);
  transform: scale(1, -1);
}
:root .fa-rotate-90,
:root .fa-rotate-180,
:root .fa-rotate-270,
:root .fa-flip-horizontal,
:root .fa-flip-vertical {
  filter: none;
}
.fa-stack {
  position: relative;
  display: inline-block;
  width: 2em;
  height: 2em;
  line-height: 2em;
  vertical-align: middle;
}
.fa-stack-1x,
.fa-stack-2x {
  position: absolute;
  left: 0;
  width: 100%;
  text-align: center;
}
.fa-stack-1x {
  line-height: inherit;
}
.fa-stack-2x {
  font-size: 2em;
}
.fa-inverse {
  color: #fff;
}
/* Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
   readers do not read off random characters that represent icons */
.fa-glass:before {
  content: "\f000";
}
.fa-music:before {
  content: "\f001";
}
.fa-search:before {
  content: "\f002";
}
.fa-envelope-o:before {
  content: "\f003";
}
.fa-heart:before {
  content: "\f004";
}
.fa-star:before {
  content: "\f005";
}
.fa-star-o:before {
  content: "\f006";
}
.fa-user:before {
  content: "\f007";
}
.fa-film:before {
  content: "\f008";
}
.fa-th-large:before {
  content: "\f009";
}
.fa-th:before {
  content: "\f00a";
}
.fa-th-list:before {
  content: "\f00b";
}
.fa-check:before {
  content: "\f00c";
}
.fa-remove:before,
.fa-close:before,
.fa-times:before {
  content: "\f00d";
}
.fa-search-plus:before {
  content: "\f00e";
}
.fa-search-minus:before {
  content: "\f010";
}
.fa-power-off:before {
  content: "\f011";
}
.fa-signal:before {
  content: "\f012";
}
.fa-gear:before,
.fa-cog:before {
  content: "\f013";
}
.fa-trash-o:before {
  content: "\f014";
}
.fa-home:before {
  content: "\f015";
}
.fa-file-o:before {
  content: "\f016";
}
.fa-clock-o:before {
  content: "\f017";
}
.fa-road:before {
  content: "\f018";
}
.fa-download:before {
  content: "\f019";
}
.fa-arrow-circle-o-down:before {
  content: "\f01a";
}
.fa-arrow-circle-o-up:before {
  content: "\f01b";
}
.fa-inbox:before {
  content: "\f01c";
}
.fa-play-circle-o:before {
  content: "\f01d";
}
.fa-rotate-right:before,
.fa-repeat:before {
  content: "\f01e";
}
.fa-refresh:before {
  content: "\f021";
}
.fa-list-alt:before {
  content: "\f022";
}
.fa-lock:before {
  content: "\f023";
}
.fa-flag:before {
  content: "\f024";
}
.fa-headphones:before {
  content: "\f025";
}
.fa-volume-off:before {
  content: "\f026";
}
.fa-volume-down:before {
  content: "\f027";
}
.fa-volume-up:before {
  content: "\f028";
}
.fa-qrcode:before {
  content: "\f029";
}
.fa-barcode:before {
  content: "\f02a";
}
.fa-tag:before {
  content: "\f02b";
}
.fa-tags:before {
  content: "\f02c";
}
.fa-book:before {
  content: "\f02d";
}
.fa-bookmark:before {
  content: "\f02e";
}
.fa-print:before {
  content: "\f02f";
}
.fa-camera:before {
  content: "\f030";
}
.fa-font:before {
  content: "\f031";
}
.fa-bold:before {
  content: "\f032";
}
.fa-italic:before {
  content: "\f033";
}
.fa-text-height:before {
  content: "\f034";
}
.fa-text-width:before {
  content: "\f035";
}
.fa-align-left:before {
  content: "\f036";
}
.fa-align-center:before {
  content: "\f037";
}
.fa-align-right:before {
  content: "\f038";
}
.fa-align-justify:before {
  content: "\f039";
}
.fa-list:before {
  content: "\f03a";
}
.fa-dedent:before,
.fa-outdent:before {
  content: "\f03b";
}
.fa-indent:before {
  content: "\f03c";
}
.fa-video-camera:before {
  content: "\f03d";
}
.fa-photo:before,
.fa-image:before,
.fa-picture-o:before {
  content: "\f03e";
}
.fa-pencil:before {
  content: "\f040";
}
.fa-map-marker:before {
  content: "\f041";
}
.fa-adjust:before {
  content: "\f042";
}
.fa-tint:before {
  content: "\f043";
}
.fa-edit:before,
.fa-pencil-square-o:before {
  content: "\f044";
}
.fa-share-square-o:before {
  content: "\f045";
}
.fa-check-square-o:before {
  content: "\f046";
}
.fa-arrows:before {
  content: "\f047";
}
.fa-step-backward:before {
  content: "\f048";
}
.fa-fast-backward:before {
  content: "\f049";
}
.fa-backward:before {
  content: "\f04a";
}
.fa-play:before {
  content: "\f04b";
}
.fa-pause:before {
  content: "\f04c";
}
.fa-stop:before {
  content: "\f04d";
}
.fa-forward:before {
  content: "\f04e";
}
.fa-fast-forward:before {
  content: "\f050";
}
.fa-step-forward:before {
  content: "\f051";
}
.fa-eject:before {
  content: "\f052";
}
.fa-chevron-left:before {
  content: "\f053";
}
.fa-chevron-right:before {
  content: "\f054";
}
.fa-plus-circle:before {
  content: "\f055";
}
.fa-minus-circle:before {
  content: "\f056";
}
.fa-times-circle:before {
  content: "\f057";
}
.fa-check-circle:before {
  content: "\f058";
}
.fa-question-circle:before {
  content: "\f059";
}
.fa-info-circle:before {
  content: "\f05a";
}
.fa-crosshairs:before {
  content: "\f05b";
}
.fa-times-circle-o:before {
  content: "\f05c";
}
.fa-check-circle-o:before {
  content: "\f05d";
}
.fa-ban:before {
  content: "\f05e";
}
.fa-arrow-left:before {
  content: "\f060";
}
.fa-arrow-right:before {
  content: "\f061";
}
.fa-arrow-up:before {
  content: "\f062";
}
.fa-arrow-down:before {
  content: "\f063";
}
.fa-mail-forward:before,
.fa-share:before {
  content: "\f064";
}
.fa-expand:before {
  content: "\f065";
}
.fa-compress:before {
  content: "\f066";
}
.fa-plus:before {
  content: "\f067";
}
.fa-minus:before {
  content: "\f068";
}
.fa-asterisk:before {
  content: "\f069";
}
.fa-exclamation-circle:before {
  content: "\f06a";
}
.fa-gift:before {
  content: "\f06b";
}
.fa-leaf:before {
  content: "\f06c";
}
.fa-fire:before {
  content: "\f06d";
}
.fa-eye:before {
  content: "\f06e";
}
.fa-eye-slash:before {
  content: "\f070";
}
.fa-warning:before,
.fa-exclamation-triangle:before {
  content: "\f071";
}
.fa-plane:before {
  content: "\f072";
}
.fa-calendar:before {
  content: "\f073";
}
.fa-random:before {
  content: "\f074";
}
.fa-comment:before {
  content: "\f075";
}
.fa-magnet:before {
  content: "\f076";
}
.fa-chevron-up:before {
  content: "\f077";
}
.fa-chevron-down:before {
  content: "\f078";
}
.fa-retweet:before {
  content: "\f079";
}
.fa-shopping-cart:before {
  content: "\f07a";
}
.fa-folder:before {
  content: "\f07b";
}
.fa-folder-open:before {
  content: "\f07c";
}
.fa-arrows-v:before {
  content: "\f07d";
}
.fa-arrows-h:before {
  content: "\f07e";
}
.fa-bar-chart-o:before,
.fa-bar-chart:before {
  content: "\f080";
}
.fa-twitter-square:before {
  content: "\f081";
}
.fa-facebook-square:before {
  content: "\f082";
}
.fa-camera-retro:before {
  content: "\f083";
}
.fa-key:before {
  content: "\f084";
}
.fa-gears:before,
.fa-cogs:before {
  content: "\f085";
}
.fa-comments:before {
  content: "\f086";
}
.fa-thumbs-o-up:before {
  content: "\f087";
}
.fa-thumbs-o-down:before {
  content: "\f088";
}
.fa-star-half:before {
  content: "\f089";
}
.fa-heart-o:before {
  content: "\f08a";
}
.fa-sign-out:before {
  content: "\f08b";
}
.fa-linkedin-square:before {
  content: "\f08c";
}
.fa-thumb-tack:before {
  content: "\f08d";
}
.fa-external-link:before {
  content: "\f08e";
}
.fa-sign-in:before {
  content: "\f090";
}
.fa-trophy:before {
  content: "\f091";
}
.fa-github-square:before {
  content: "\f092";
}
.fa-upload:before {
  content: "\f093";
}
.fa-lemon-o:before {
  content: "\f094";
}
.fa-phone:before {
  content: "\f095";
}
.fa-square-o:before {
  content: "\f096";
}
.fa-bookmark-o:before {
  content: "\f097";
}
.fa-phone-square:before {
  content: "\f098";
}
.fa-twitter:before {
  content: "\f099";
}
.fa-facebook-f:before,
.fa-facebook:before {
  content: "\f09a";
}
.fa-github:before {
  content: "\f09b";
}
.fa-unlock:before {
  content: "\f09c";
}
.fa-credit-card:before {
  content: "\f09d";
}
.fa-feed:before,
.fa-rss:before {
  content: "\f09e";
}
.fa-hdd-o:before {
  content: "\f0a0";
}
.fa-bullhorn:before {
  content: "\f0a1";
}
.fa-bell:before {
  content: "\f0f3";
}
.fa-certificate:before {
  content: "\f0a3";
}
.fa-hand-o-right:before {
  content: "\f0a4";
}
.fa-hand-o-left:before {
  content: "\f0a5";
}
.fa-hand-o-up:before {
  content: "\f0a6";
}
.fa-hand-o-down:before {
  content: "\f0a7";
}
.fa-arrow-circle-left:before {
  content: "\f0a8";
}
.fa-arrow-circle-right:before {
  content: "\f0a9";
}
.fa-arrow-circle-up:before {
  content: "\f0aa";
}
.fa-arrow-circle-down:before {
  content: "\f0ab";
}
.fa-globe:before {
  content: "\f0ac";
}
.fa-wrench:before {
  content: "\f0ad";
}
.fa-tasks:before {
  content: "\f0ae";
}
.fa-filter:before {
  content: "\f0b0";
}
.fa-briefcase:before {
  content: "\f0b1";
}
.fa-arrows-alt:before {
  content: "\f0b2";
}
.fa-group:before,
.fa-users:before {
  content: "\f0c0";
}
.fa-chain:before,
.fa-link:before {
  content: "\f0c1";
}
.fa-cloud:before {
  content: "\f0c2";
}
.fa-flask:before {
  content: "\f0c3";
}
.fa-cut:before,
.fa-scissors:before {
  content: "\f0c4";
}
.fa-copy:before,
.fa-files-o:before {
  content: "\f0c5";
}
.fa-paperclip:before {
  content: "\f0c6";
}
.fa-save:before,
.fa-floppy-o:before {
  content: "\f0c7";
}
.fa-square:before {
  content: "\f0c8";
}
.fa-navicon:before,
.fa-reorder:before,
.fa-bars:before {
  content: "\f0c9";
}
.fa-list-ul:before {
  content: "\f0ca";
}
.fa-list-ol:before {
  content: "\f0cb";
}
.fa-strikethrough:before {
  content: "\f0cc";
}
.fa-underline:before {
  content: "\f0cd";
}
.fa-table:before {
  content: "\f0ce";
}
.fa-magic:before {
  content: "\f0d0";
}
.fa-truck:before {
  content: "\f0d1";
}
.fa-pinterest:before {
  content: "\f0d2";
}
.fa-pinterest-square:before {
  content: "\f0d3";
}
.fa-google-plus-square:before {
  content: "\f0d4";
}
.fa-google-plus:before {
  content: "\f0d5";
}
.fa-money:before {
  content: "\f0d6";
}
.fa-caret-down:before {
  content: "\f0d7";
}
.fa-caret-up:before {
  content: "\f0d8";
}
.fa-caret-left:before {
  content: "\f0d9";
}
.fa-caret-right:before {
  content: "\f0da";
}
.fa-columns:before {
  content: "\f0db";
}
.fa-unsorted:before,
.fa-sort:before {
  content: "\f0dc";
}
.fa-sort-down:before,
.fa-sort-desc:before {
  content: "\f0dd";
}
.fa-sort-up:before,
.fa-sort-asc:before {
  content: "\f0de";
}
.fa-envelope:before {
  content: "\f0e0";
}
.fa-linkedin:before {
  content: "\f0e1";
}
.fa-rotate-left:before,
.fa-undo:before {
  content: "\f0e2";
}
.fa-legal:before,
.fa-gavel:before {
  content: "\f0e3";
}
.fa-dashboard:before,
.fa-tachometer:before {
  content: "\f0e4";
}
.fa-comment-o:before {
  content: "\f0e5";
}
.fa-comments-o:before {
  content: "\f0e6";
}
.fa-flash:before,
.fa-bolt:before {
  content: "\f0e7";
}
.fa-sitemap:before {
  content: "\f0e8";
}
.fa-umbrella:before {
  content: "\f0e9";
}
.fa-paste:before,
.fa-clipboard:before {
  content: "\f0ea";
}
.fa-lightbulb-o:before {
  content: "\f0eb";
}
.fa-exchange:before {
  content: "\f0ec";
}
.fa-cloud-download:before {
  content: "\f0ed";
}
.fa-cloud-upload:before {
  content: "\f0ee";
}
.fa-user-md:before {
  content: "\f0f0";
}
.fa-stethoscope:before {
  content: "\f0f1";
}
.fa-suitcase:before {
  content: "\f0f2";
}
.fa-bell-o:before {
  content: "\f0a2";
}
.fa-coffee:before {
  content: "\f0f4";
}
.fa-cutlery:before {
  content: "\f0f5";
}
.fa-file-text-o:before {
  content: "\f0f6";
}
.fa-building-o:before {
  content: "\f0f7";
}
.fa-hospital-o:before {
  content: "\f0f8";
}
.fa-ambulance:before {
  content: "\f0f9";
}
.fa-medkit:before {
  content: "\f0fa";
}
.fa-fighter-jet:before {
  content: "\f0fb";
}
.fa-beer:before {
  content: "\f0fc";
}
.fa-h-square:before {
  content: "\f0fd";
}
.fa-plus-square:before {
  content: "\f0fe";
}
.fa-angle-double-left:before {
  content: "\f100";
}
.fa-angle-double-right:before {
  content: "\f101";
}
.fa-angle-double-up:before {
  content: "\f102";
}
.fa-angle-double-down:before {
  content: "\f103";
}
.fa-angle-left:before {
  content: "\f104";
}
.fa-angle-right:before {
  content: "\f105";
}
.fa-angle-up:before {
  content: "\f106";
}
.fa-angle-down:before {
  content: "\f107";
}
.fa-desktop:before {
  content: "\f108";
}
.fa-laptop:before {
  content: "\f109";
}
.fa-tablet:before {
  content: "\f10a";
}
.fa-mobile-phone:before,
.fa-mobile:before {
  content: "\f10b";
}
.fa-circle-o:before {
  content: "\f10c";
}
.fa-quote-left:before {
  content: "\f10d";
}
.fa-quote-right:before {
  content: "\f10e";
}
.fa-spinner:before {
  content: "\f110";
}
.fa-circle:before {
  content: "\f111";
}
.fa-mail-reply:before,
.fa-reply:before {
  content: "\f112";
}
.fa-github-alt:before {
  content: "\f113";
}
.fa-folder-o:before {
  content: "\f114";
}
.fa-folder-open-o:before {
  content: "\f115";
}
.fa-smile-o:before {
  content: "\f118";
}
.fa-frown-o:before {
  content: "\f119";
}
.fa-meh-o:before {
  content: "\f11a";
}
.fa-gamepad:before {
  content: "\f11b";
}
.fa-keyboard-o:before {
  content: "\f11c";
}
.fa-flag-o:before {
  content: "\f11d";
}
.fa-flag-checkered:before {
  content: "\f11e";
}
.fa-terminal:before {
  content: "\f120";
}
.fa-code:before {
  content: "\f121";
}
.fa-mail-reply-all:before,
.fa-reply-all:before {
  content: "\f122";
}
.fa-star-half-empty:before,
.fa-star-half-full:before,
.fa-star-half-o:before {
  content: "\f123";
}
.fa-location-arrow:before {
  content: "\f124";
}
.fa-crop:before {
  content: "\f125";
}
.fa-code-fork:before {
  content: "\f126";
}
.fa-unlink:before,
.fa-chain-broken:before {
  content: "\f127";
}
.fa-question:before {
  content: "\f128";
}
.fa-info:before {
  content: "\f129";
}
.fa-exclamation:before {
  content: "\f12a";
}
.fa-superscript:before {
  content: "\f12b";
}
.fa-subscript:before {
  content: "\f12c";
}
.fa-eraser:before {
  content: "\f12d";
}
.fa-puzzle-piece:before {
  content: "\f12e";
}
.fa-microphone:before {
  content: "\f130";
}
.fa-microphone-slash:before {
  content: "\f131";
}
.fa-shield:before {
  content: "\f132";
}
.fa-calendar-o:before {
  content: "\f133";
}
.fa-fire-extinguisher:before {
  content: "\f134";
}
.fa-rocket:before {
  content: "\f135";
}
.fa-maxcdn:before {
  content: "\f136";
}
.fa-chevron-circle-left:before {
  content: "\f137";
}
.fa-chevron-circle-right:before {
  content: "\f138";
}
.fa-chevron-circle-up:before {
  content: "\f139";
}
.fa-chevron-circle-down:before {
  content: "\f13a";
}
.fa-html5:before {
  content: "\f13b";
}
.fa-css3:before {
  content: "\f13c";
}
.fa-anchor:before {
  content: "\f13d";
}
.fa-unlock-alt:before {
  content: "\f13e";
}
.fa-bullseye:before {
  content: "\f140";
}
.fa-ellipsis-h:before {
  content: "\f141";
}
.fa-ellipsis-v:before {
  content: "\f142";
}
.fa-rss-square:before {
  content: "\f143";
}
.fa-play-circle:before {
  content: "\f144";
}
.fa-ticket:before {
  content: "\f145";
}
.fa-minus-square:before {
  content: "\f146";
}
.fa-minus-square-o:before {
  content: "\f147";
}
.fa-level-up:before {
  content: "\f148";
}
.fa-level-down:before {
  content: "\f149";
}
.fa-check-square:before {
  content: "\f14a";
}
.fa-pencil-square:before {
  content: "\f14b";
}
.fa-external-link-square:before {
  content: "\f14c";
}
.fa-share-square:before {
  content: "\f14d";
}
.fa-compass:before {
  content: "\f14e";
}
.fa-toggle-down:before,
.fa-caret-square-o-down:before {
  content: "\f150";
}
.fa-toggle-up:before,
.fa-caret-square-o-up:before {
  content: "\f151";
}
.fa-toggle-right:before,
.fa-caret-square-o-right:before {
  content: "\f152";
}
.fa-euro:before,
.fa-eur:before {
  content: "\f153";
}
.fa-gbp:before {
  content: "\f154";
}
.fa-dollar:before,
.fa-usd:before {
  content: "\f155";
}
.fa-rupee:before,
.fa-inr:before {
  content: "\f156";
}
.fa-cny:before,
.fa-rmb:before,
.fa-yen:before,
.fa-jpy:before {
  content: "\f157";
}
.fa-ruble:before,
.fa-rouble:before,
.fa-rub:before {
  content: "\f158";
}
.fa-won:before,
.fa-krw:before {
  content: "\f159";
}
.fa-bitcoin:before,
.fa-btc:before {
  content: "\f15a";
}
.fa-file:before {
  content: "\f15b";
}
.fa-file-text:before {
  content: "\f15c";
}
.fa-sort-alpha-asc:before {
  content: "\f15d";
}
.fa-sort-alpha-desc:before {
  content: "\f15e";
}
.fa-sort-amount-asc:before {
  content: "\f160";
}
.fa-sort-amount-desc:before {
  content: "\f161";
}
.fa-sort-numeric-asc:before {
  content: "\f162";
}
.fa-sort-numeric-desc:before {
  content: "\f163";
}
.fa-thumbs-up:before {
  content: "\f164";
}
.fa-thumbs-down:before {
  content: "\f165";
}
.fa-youtube-square:before {
  content: "\f166";
}
.fa-youtube:before {
  content: "\f167";
}
.fa-xing:before {
  content: "\f168";
}
.fa-xing-square:before {
  content: "\f169";
}
.fa-youtube-play:before {
  content: "\f16a";
}
.fa-dropbox:before {
  content: "\f16b";
}
.fa-stack-overflow:before {
  content: "\f16c";
}
.fa-instagram:before {
  content: "\f16d";
}
.fa-flickr:before {
  content: "\f16e";
}
.fa-adn:before {
  content: "\f170";
}
.fa-bitbucket:before {
  content: "\f171";
}
.fa-bitbucket-square:before {
  content: "\f172";
}
.fa-tumblr:before {
  content: "\f173";
}
.fa-tumblr-square:before {
  content: "\f174";
}
.fa-long-arrow-down:before {
  content: "\f175";
}
.fa-long-arrow-up:before {
  content: "\f176";
}
.fa-long-arrow-left:before {
  content: "\f177";
}
.fa-long-arrow-right:before {
  content: "\f178";
}
.fa-apple:before {
  content: "\f179";
}
.fa-windows:before {
  content: "\f17a";
}
.fa-android:before {
  content: "\f17b";
}
.fa-linux:before {
  content: "\f17c";
}
.fa-dribbble:before {
  content: "\f17d";
}
.fa-skype:before {
  content: "\f17e";
}
.fa-foursquare:before {
  content: "\f180";
}
.fa-trello:before {
  content: "\f181";
}
.fa-female:before {
  content: "\f182";
}
.fa-male:before {
  content: "\f183";
}
.fa-gittip:before,
.fa-gratipay:before {
  content: "\f184";
}
.fa-sun-o:before {
  content: "\f185";
}
.fa-moon-o:before {
  content: "\f186";
}
.fa-archive:before {
  content: "\f187";
}
.fa-bug:before {
  content: "\f188";
}
.fa-vk:before {
  content: "\f189";
}
.fa-weibo:before {
  content: "\f18a";
}
.fa-renren:before {
  content: "\f18b";
}
.fa-pagelines:before {
  content: "\f18c";
}
.fa-stack-exchange:before {
  content: "\f18d";
}
.fa-arrow-circle-o-right:before {
  content: "\f18e";
}
.fa-arrow-circle-o-left:before {
  content: "\f190";
}
.fa-toggle-left:before,
.fa-caret-square-o-left:before {
  content: "\f191";
}
.fa-dot-circle-o:before {
  content: "\f192";
}
.fa-wheelchair:before {
  content: "\f193";
}
.fa-vimeo-square:before {
  content: "\f194";
}
.fa-turkish-lira:before,
.fa-try:before {
  content: "\f195";
}
.fa-plus-square-o:before {
  content: "\f196";
}
.fa-space-shuttle:before {
  content: "\f197";
}
.fa-slack:before {
  content: "\f198";
}
.fa-envelope-square:before {
  content: "\f199";
}
.fa-wordpress:before {
  content: "\f19a";
}
.fa-openid:before {
  content: "\f19b";
}
.fa-institution:before,
.fa-bank:before,
.fa-university:before {
  content: "\f19c";
}
.fa-mortar-board:before,
.fa-graduation-cap:before {
  content: "\f19d";
}
.fa-yahoo:before {
  content: "\f19e";
}
.fa-google:before {
  content: "\f1a0";
}
.fa-reddit:before {
  content: "\f1a1";
}
.fa-reddit-square:before {
  content: "\f1a2";
}
.fa-stumbleupon-circle:before {
  content: "\f1a3";
}
.fa-stumbleupon:before {
  content: "\f1a4";
}
.fa-delicious:before {
  content: "\f1a5";
}
.fa-digg:before {
  content: "\f1a6";
}
.fa-pied-piper-pp:before {
  content: "\f1a7";
}
.fa-pied-piper-alt:before {
  content: "\f1a8";
}
.fa-drupal:before {
  content: "\f1a9";
}
.fa-joomla:before {
  content: "\f1aa";
}
.fa-language:before {
  content: "\f1ab";
}
.fa-fax:before {
  content: "\f1ac";
}
.fa-building:before {
  content: "\f1ad";
}
.fa-child:before {
  content: "\f1ae";
}
.fa-paw:before {
  content: "\f1b0";
}
.fa-spoon:before {
  content: "\f1b1";
}
.fa-cube:before {
  content: "\f1b2";
}
.fa-cubes:before {
  content: "\f1b3";
}
.fa-behance:before {
  content: "\f1b4";
}
.fa-behance-square:before {
  content: "\f1b5";
}
.fa-steam:before {
  content: "\f1b6";
}
.fa-steam-square:before {
  content: "\f1b7";
}
.fa-recycle:before {
  content: "\f1b8";
}
.fa-automobile:before,
.fa-car:before {
  content: "\f1b9";
}
.fa-cab:before,
.fa-taxi:before {
  content: "\f1ba";
}
.fa-tree:before {
  content: "\f1bb";
}
.fa-spotify:before {
  content: "\f1bc";
}
.fa-deviantart:before {
  content: "\f1bd";
}
.fa-soundcloud:before {
  content: "\f1be";
}
.fa-database:before {
  content: "\f1c0";
}
.fa-file-pdf-o:before {
  content: "\f1c1";
}
.fa-file-word-o:before {
  content: "\f1c2";
}
.fa-file-excel-o:before {
  content: "\f1c3";
}
.fa-file-powerpoint-o:before {
  content: "\f1c4";
}
.fa-file-photo-o:before,
.fa-file-picture-o:before,
.fa-file-image-o:before {
  content: "\f1c5";
}
.fa-file-zip-o:before,
.fa-file-archive-o:before {
  content: "\f1c6";
}
.fa-file-sound-o:before,
.fa-file-audio-o:before {
  content: "\f1c7";
}
.fa-file-movie-o:before,
.fa-file-video-o:before {
  content: "\f1c8";
}
.fa-file-code-o:before {
  content: "\f1c9";
}
.fa-vine:before {
  content: "\f1ca";
}
.fa-codepen:before {
  content: "\f1cb";
}
.fa-jsfiddle:before {
  content: "\f1cc";
}
.fa-life-bouy:before,
.fa-life-buoy:before,
.fa-life-saver:before,
.fa-support:before,
.fa-life-ring:before {
  content: "\f1cd";
}
.fa-circle-o-notch:before {
  content: "\f1ce";
}
.fa-ra:before,
.fa-resistance:before,
.fa-rebel:before {
  content: "\f1d0";
}
.fa-ge:before,
.fa-empire:before {
  content: "\f1d1";
}
.fa-git-square:before {
  content: "\f1d2";
}
.fa-git:before {
  content: "\f1d3";
}
.fa-y-combinator-square:before,
.fa-yc-square:before,
.fa-hacker-news:before {
  content: "\f1d4";
}
.fa-tencent-weibo:before {
  content: "\f1d5";
}
.fa-qq:before {
  content: "\f1d6";
}
.fa-wechat:before,
.fa-weixin:before {
  content: "\f1d7";
}
.fa-send:before,
.fa-paper-plane:before {
  content: "\f1d8";
}
.fa-send-o:before,
.fa-paper-plane-o:before {
  content: "\f1d9";
}
.fa-history:before {
  content: "\f1da";
}
.fa-circle-thin:before {
  content: "\f1db";
}
.fa-header:before {
  content: "\f1dc";
}
.fa-paragraph:before {
  content: "\f1dd";
}
.fa-sliders:before {
  content: "\f1de";
}
.fa-share-alt:before {
  content: "\f1e0";
}
.fa-share-alt-square:before {
  content: "\f1e1";
}
.fa-bomb:before {
  content: "\f1e2";
}
.fa-soccer-ball-o:before,
.fa-futbol-o:before {
  content: "\f1e3";
}
.fa-tty:before {
  content: "\f1e4";
}
.fa-binoculars:before {
  content: "\f1e5";
}
.fa-plug:before {
  content: "\f1e6";
}
.fa-slideshare:before {
  content: "\f1e7";
}
.fa-twitch:before {
  content: "\f1e8";
}
.fa-yelp:before {
  content: "\f1e9";
}
.fa-newspaper-o:before {
  content: "\f1ea";
}
.fa-wifi:before {
  content: "\f1eb";
}
.fa-calculator:before {
  content: "\f1ec";
}
.fa-paypal:before {
  content: "\f1ed";
}
.fa-google-wallet:before {
  content: "\f1ee";
}
.fa-cc-visa:before {
  content: "\f1f0";
}
.fa-cc-mastercard:before {
  content: "\f1f1";
}
.fa-cc-discover:before {
  content: "\f1f2";
}
.fa-cc-amex:before {
  content: "\f1f3";
}
.fa-cc-paypal:before {
  content: "\f1f4";
}
.fa-cc-stripe:before {
  content: "\f1f5";
}
.fa-bell-slash:before {
  content: "\f1f6";
}
.fa-bell-slash-o:before {
  content: "\f1f7";
}
.fa-trash:before {
  content: "\f1f8";
}
.fa-copyright:before {
  content: "\f1f9";
}
.fa-at:before {
  content: "\f1fa";
}
.fa-eyedropper:before {
  content: "\f1fb";
}
.fa-paint-brush:before {
  content: "\f1fc";
}
.fa-birthday-cake:before {
  content: "\f1fd";
}
.fa-area-chart:before {
  content: "\f1fe";
}
.fa-pie-chart:before {
  content: "\f200";
}
.fa-line-chart:before {
  content: "\f201";
}
.fa-lastfm:before {
  content: "\f202";
}
.fa-lastfm-square:before {
  content: "\f203";
}
.fa-toggle-off:before {
  content: "\f204";
}
.fa-toggle-on:before {
  content: "\f205";
}
.fa-bicycle:before {
  content: "\f206";
}
.fa-bus:before {
  content: "\f207";
}
.fa-ioxhost:before {
  content: "\f208";
}
.fa-angellist:before {
  content: "\f209";
}
.fa-cc:before {
  content: "\f20a";
}
.fa-shekel:before,
.fa-sheqel:before,
.fa-ils:before {
  content: "\f20b";
}
.fa-meanpath:before {
  content: "\f20c";
}
.fa-buysellads:before {
  content: "\f20d";
}
.fa-connectdevelop:before {
  content: "\f20e";
}
.fa-dashcube:before {
  content: "\f210";
}
.fa-forumbee:before {
  content: "\f211";
}
.fa-leanpub:before {
  content: "\f212";
}
.fa-sellsy:before {
  content: "\f213";
}
.fa-shirtsinbulk:before {
  content: "\f214";
}
.fa-simplybuilt:before {
  content: "\f215";
}
.fa-skyatlas:before {
  content: "\f216";
}
.fa-cart-plus:before {
  content: "\f217";
}
.fa-cart-arrow-down:before {
  content: "\f218";
}
.fa-diamond:before {
  content: "\f219";
}
.fa-ship:before {
  content: "\f21a";
}
.fa-user-secret:before {
  content: "\f21b";
}
.fa-motorcycle:before {
  content: "\f21c";
}
.fa-street-view:before {
  content: "\f21d";
}
.fa-heartbeat:before {
  content: "\f21e";
}
.fa-venus:before {
  content: "\f221";
}
.fa-mars:before {
  content: "\f222";
}
.fa-mercury:before {
  content: "\f223";
}
.fa-intersex:before,
.fa-transgender:before {
  content: "\f224";
}
.fa-transgender-alt:before {
  content: "\f225";
}
.fa-venus-double:before {
  content: "\f226";
}
.fa-mars-double:before {
  content: "\f227";
}
.fa-venus-mars:before {
  content: "\f228";
}
.fa-mars-stroke:before {
  content: "\f229";
}
.fa-mars-stroke-v:before {
  content: "\f22a";
}
.fa-mars-stroke-h:before {
  content: "\f22b";
}
.fa-neuter:before {
  content: "\f22c";
}
.fa-genderless:before {
  content: "\f22d";
}
.fa-facebook-official:before {
  content: "\f230";
}
.fa-pinterest-p:before {
  content: "\f231";
}
.fa-whatsapp:before {
  content: "\f232";
}
.fa-server:before {
  content: "\f233";
}
.fa-user-plus:before {
  content: "\f234";
}
.fa-user-times:before {
  content: "\f235";
}
.fa-hotel:before,
.fa-bed:before {
  content: "\f236";
}
.fa-viacoin:before {
  content: "\f237";
}
.fa-train:before {
  content: "\f238";
}
.fa-subway:before {
  content: "\f239";
}
.fa-medium:before {
  content: "\f23a";
}
.fa-yc:before,
.fa-y-combinator:before {
  content: "\f23b";
}
.fa-optin-monster:before {
  content: "\f23c";
}
.fa-opencart:before {
  content: "\f23d";
}
.fa-expeditedssl:before {
  content: "\f23e";
}
.fa-battery-4:before,
.fa-battery:before,
.fa-battery-full:before {
  content: "\f240";
}
.fa-battery-3:before,
.fa-battery-three-quarters:before {
  content: "\f241";
}
.fa-battery-2:before,
.fa-battery-half:before {
  content: "\f242";
}
.fa-battery-1:before,
.fa-battery-quarter:before {
  content: "\f243";
}
.fa-battery-0:before,
.fa-battery-empty:before {
  content: "\f244";
}
.fa-mouse-pointer:before {
  content: "\f245";
}
.fa-i-cursor:before {
  content: "\f246";
}
.fa-object-group:before {
  content: "\f247";
}
.fa-object-ungroup:before {
  content: "\f248";
}
.fa-sticky-note:before {
  content: "\f249";
}
.fa-sticky-note-o:before {
  content: "\f24a";
}
.fa-cc-jcb:before {
  content: "\f24b";
}
.fa-cc-diners-club:before {
  content: "\f24c";
}
.fa-clone:before {
  content: "\f24d";
}
.fa-balance-scale:before {
  content: "\f24e";
}
.fa-hourglass-o:before {
  content: "\f250";
}
.fa-hourglass-1:before,
.fa-hourglass-start:before {
  content: "\f251";
}
.fa-hourglass-2:before,
.fa-hourglass-half:before {
  content: "\f252";
}
.fa-hourglass-3:before,
.fa-hourglass-end:before {
  content: "\f253";
}
.fa-hourglass:before {
  content: "\f254";
}
.fa-hand-grab-o:before,
.fa-hand-rock-o:before {
  content: "\f255";
}
.fa-hand-stop-o:before,
.fa-hand-paper-o:before {
  content: "\f256";
}
.fa-hand-scissors-o:before {
  content: "\f257";
}
.fa-hand-lizard-o:before {
  content: "\f258";
}
.fa-hand-spock-o:before {
  content: "\f259";
}
.fa-hand-pointer-o:before {
  content: "\f25a";
}
.fa-hand-peace-o:before {
  content: "\f25b";
}
.fa-trademark:before {
  content: "\f25c";
}
.fa-registered:before {
  content: "\f25d";
}
.fa-creative-commons:before {
  content: "\f25e";
}
.fa-gg:before {
  content: "\f260";
}
.fa-gg-circle:before {
  content: "\f261";
}
.fa-tripadvisor:before {
  content: "\f262";
}
.fa-odnoklassniki:before {
  content: "\f263";
}
.fa-odnoklassniki-square:before {
  content: "\f264";
}
.fa-get-pocket:before {
  content: "\f265";
}
.fa-wikipedia-w:before {
  content: "\f266";
}
.fa-safari:before {
  content: "\f267";
}
.fa-chrome:before {
  content: "\f268";
}
.fa-firefox:before {
  content: "\f269";
}
.fa-opera:before {
  content: "\f26a";
}
.fa-internet-explorer:before {
  content: "\f26b";
}
.fa-tv:before,
.fa-television:before {
  content: "\f26c";
}
.fa-contao:before {
  content: "\f26d";
}
.fa-500px:before {
  content: "\f26e";
}
.fa-amazon:before {
  content: "\f270";
}
.fa-calendar-plus-o:before {
  content: "\f271";
}
.fa-calendar-minus-o:before {
  content: "\f272";
}
.fa-calendar-times-o:before {
  content: "\f273";
}
.fa-calendar-check-o:before {
  content: "\f274";
}
.fa-industry:before {
  content: "\f275";
}
.fa-map-pin:before {
  content: "\f276";
}
.fa-map-signs:before {
  content: "\f277";
}
.fa-map-o:before {
  content: "\f278";
}
.fa-map:before {
  content: "\f279";
}
.fa-commenting:before {
  content: "\f27a";
}
.fa-commenting-o:before {
  content: "\f27b";
}
.fa-houzz:before {
  content: "\f27c";
}
.fa-vimeo:before {
  content: "\f27d";
}
.fa-black-tie:before {
  content: "\f27e";
}
.fa-fonticons:before {
  content: "\f280";
}
.fa-reddit-alien:before {
  content: "\f281";
}
.fa-edge:before {
  content: "\f282";
}
.fa-credit-card-alt:before {
  content: "\f283";
}
.fa-codiepie:before {
  content: "\f284";
}
.fa-modx:before {
  content: "\f285";
}
.fa-fort-awesome:before {
  content: "\f286";
}
.fa-usb:before {
  content: "\f287";
}
.fa-product-hunt:before {
  content: "\f288";
}
.fa-mixcloud:before {
  content: "\f289";
}
.fa-scribd:before {
  content: "\f28a";
}
.fa-pause-circle:before {
  content: "\f28b";
}
.fa-pause-circle-o:before {
  content: "\f28c";
}
.fa-stop-circle:before {
  content: "\f28d";
}
.fa-stop-circle-o:before {
  content: "\f28e";
}
.fa-shopping-bag:before {
  content: "\f290";
}
.fa-shopping-basket:before {
  content: "\f291";
}
.fa-hashtag:before {
  content: "\f292";
}
.fa-bluetooth:before {
  content: "\f293";
}
.fa-bluetooth-b:before {
  content: "\f294";
}
.fa-percent:before {
  content: "\f295";
}
.fa-gitlab:before {
  content: "\f296";
}
.fa-wpbeginner:before {
  content: "\f297";
}
.fa-wpforms:before {
  content: "\f298";
}
.fa-envira:before {
  content: "\f299";
}
.fa-universal-access:before {
  content: "\f29a";
}
.fa-wheelchair-alt:before {
  content: "\f29b";
}
.fa-question-circle-o:before {
  content: "\f29c";
}
.fa-blind:before {
  content: "\f29d";
}
.fa-audio-description:before {
  content: "\f29e";
}
.fa-volume-control-phone:before {
  content: "\f2a0";
}
.fa-braille:before {
  content: "\f2a1";
}
.fa-assistive-listening-systems:before {
  content: "\f2a2";
}
.fa-asl-interpreting:before,
.fa-american-sign-language-interpreting:before {
  content: "\f2a3";
}
.fa-deafness:before,
.fa-hard-of-hearing:before,
.fa-deaf:before {
  content: "\f2a4";
}
.fa-glide:before {
  content: "\f2a5";
}
.fa-glide-g:before {
  content: "\f2a6";
}
.fa-signing:before,
.fa-sign-language:before {
  content: "\f2a7";
}
.fa-low-vision:before {
  content: "\f2a8";
}
.fa-viadeo:before {
  content: "\f2a9";
}
.fa-viadeo-square:before {
  content: "\f2aa";
}
.fa-snapchat:before {
  content: "\f2ab";
}
.fa-snapchat-ghost:before {
  content: "\f2ac";
}
.fa-snapchat-square:before {
  content: "\f2ad";
}
.fa-pied-piper:before {
  content: "\f2ae";
}
.fa-first-order:before {
  content: "\f2b0";
}
.fa-yoast:before {
  content: "\f2b1";
}
.fa-themeisle:before {
  content: "\f2b2";
}
.fa-google-plus-circle:before,
.fa-google-plus-official:before {
  content: "\f2b3";
}
.fa-fa:before,
.fa-font-awesome:before {
  content: "\f2b4";
}
.fa-handshake-o:before {
  content: "\f2b5";
}
.fa-envelope-open:before {
  content: "\f2b6";
}
.fa-envelope-open-o:before {
  content: "\f2b7";
}
.fa-linode:before {
  content: "\f2b8";
}
.fa-address-book:before {
  content: "\f2b9";
}
.fa-address-book-o:before {
  content: "\f2ba";
}
.fa-vcard:before,
.fa-address-card:before {
  content: "\f2bb";
}
.fa-vcard-o:before,
.fa-address-card-o:before {
  content: "\f2bc";
}
.fa-user-circle:before {
  content: "\f2bd";
}
.fa-user-circle-o:before {
  content: "\f2be";
}
.fa-user-o:before {
  content: "\f2c0";
}
.fa-id-badge:before {
  content: "\f2c1";
}
.fa-drivers-license:before,
.fa-id-card:before {
  content: "\f2c2";
}
.fa-drivers-license-o:before,
.fa-id-card-o:before {
  content: "\f2c3";
}
.fa-quora:before {
  content: "\f2c4";
}
.fa-free-code-camp:before {
  content: "\f2c5";
}
.fa-telegram:before {
  content: "\f2c6";
}
.fa-thermometer-4:before,
.fa-thermometer:before,
.fa-thermometer-full:before {
  content: "\f2c7";
}
.fa-thermometer-3:before,
.fa-thermometer-three-quarters:before {
  content: "\f2c8";
}
.fa-thermometer-2:before,
.fa-thermometer-half:before {
  content: "\f2c9";
}
.fa-thermometer-1:before,
.fa-thermometer-quarter:before {
  content: "\f2ca";
}
.fa-thermometer-0:before,
.fa-thermometer-empty:before {
  content: "\f2cb";
}
.fa-shower:before {
  content: "\f2cc";
}
.fa-bathtub:before,
.fa-s15:before,
.fa-bath:before {
  content: "\f2cd";
}
.fa-podcast:before {
  content: "\f2ce";
}
.fa-window-maximize:before {
  content: "\f2d0";
}
.fa-window-minimize:before {
  content: "\f2d1";
}
.fa-window-restore:before {
  content: "\f2d2";
}
.fa-times-rectangle:before,
.fa-window-close:before {
  content: "\f2d3";
}
.fa-times-rectangle-o:before,
.fa-window-close-o:before {
  content: "\f2d4";
}
.fa-bandcamp:before {
  content: "\f2d5";
}
.fa-grav:before {
  content: "\f2d6";
}
.fa-etsy:before {
  content: "\f2d7";
}
.fa-imdb:before {
  content: "\f2d8";
}
.fa-ravelry:before {
  content: "\f2d9";
}
.fa-eercast:before {
  content: "\f2da";
}
.fa-microchip:before {
  content: "\f2db";
}
.fa-snowflake-o:before {
  content: "\f2dc";
}
.fa-superpowers:before {
  content: "\f2dd";
}
.fa-wpexplorer:before {
  content: "\f2de";
}
.fa-meetup:before {
  content: "\f2e0";
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
/*!
*
* IPython base
*
*/
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
code {
  color: #000;
}
pre {
  font-size: inherit;
  line-height: inherit;
}
label {
  font-weight: normal;
}
/* Make the page background atleast 100% the height of the view port */
/* Make the page itself atleast 70% the height of the view port */
.border-box-sizing {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.corner-all {
  border-radius: 2px;
}
.no-padding {
  padding: 0px;
}
/* Flexible box model classes */
/* Taken from Alex Russell http://infrequently.org/2009/08/css-3-progress/ */
/* This file is a compatability layer.  It allows the usage of flexible box 
model layouts accross multiple browsers, including older browsers.  The newest,
universal implementation of the flexible box model is used when available (see
`Modern browsers` comments below).  Browsers that are known to implement this 
new spec completely include:

    Firefox 28.0+
    Chrome 29.0+
    Internet Explorer 11+ 
    Opera 17.0+

Browsers not listed, including Safari, are supported via the styling under the
`Old browsers` comments below.
*/
.hbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
.hbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.vbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.vbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.hbox.reverse,
.vbox.reverse,
.reverse {
  /* Old browsers */
  -webkit-box-direction: reverse;
  -moz-box-direction: reverse;
  box-direction: reverse;
  /* Modern browsers */
  flex-direction: row-reverse;
}
.hbox.box-flex0,
.vbox.box-flex0,
.box-flex0 {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
  width: auto;
}
.hbox.box-flex1,
.vbox.box-flex1,
.box-flex1 {
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex,
.vbox.box-flex,
.box-flex {
  /* Old browsers */
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex2,
.vbox.box-flex2,
.box-flex2 {
  /* Old browsers */
  -webkit-box-flex: 2;
  -moz-box-flex: 2;
  box-flex: 2;
  /* Modern browsers */
  flex: 2;
}
.box-group1 {
  /*  Deprecated */
  -webkit-box-flex-group: 1;
  -moz-box-flex-group: 1;
  box-flex-group: 1;
}
.box-group2 {
  /* Deprecated */
  -webkit-box-flex-group: 2;
  -moz-box-flex-group: 2;
  box-flex-group: 2;
}
.hbox.start,
.vbox.start,
.start {
  /* Old browsers */
  -webkit-box-pack: start;
  -moz-box-pack: start;
  box-pack: start;
  /* Modern browsers */
  justify-content: flex-start;
}
.hbox.end,
.vbox.end,
.end {
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
}
.hbox.center,
.vbox.center,
.center {
  /* Old browsers */
  -webkit-box-pack: center;
  -moz-box-pack: center;
  box-pack: center;
  /* Modern browsers */
  justify-content: center;
}
.hbox.baseline,
.vbox.baseline,
.baseline {
  /* Old browsers */
  -webkit-box-pack: baseline;
  -moz-box-pack: baseline;
  box-pack: baseline;
  /* Modern browsers */
  justify-content: baseline;
}
.hbox.stretch,
.vbox.stretch,
.stretch {
  /* Old browsers */
  -webkit-box-pack: stretch;
  -moz-box-pack: stretch;
  box-pack: stretch;
  /* Modern browsers */
  justify-content: stretch;
}
.hbox.align-start,
.vbox.align-start,
.align-start {
  /* Old browsers */
  -webkit-box-align: start;
  -moz-box-align: start;
  box-align: start;
  /* Modern browsers */
  align-items: flex-start;
}
.hbox.align-end,
.vbox.align-end,
.align-end {
  /* Old browsers */
  -webkit-box-align: end;
  -moz-box-align: end;
  box-align: end;
  /* Modern browsers */
  align-items: flex-end;
}
.hbox.align-center,
.vbox.align-center,
.align-center {
  /* Old browsers */
  -webkit-box-align: center;
  -moz-box-align: center;
  box-align: center;
  /* Modern browsers */
  align-items: center;
}
.hbox.align-baseline,
.vbox.align-baseline,
.align-baseline {
  /* Old browsers */
  -webkit-box-align: baseline;
  -moz-box-align: baseline;
  box-align: baseline;
  /* Modern browsers */
  align-items: baseline;
}
.hbox.align-stretch,
.vbox.align-stretch,
.align-stretch {
  /* Old browsers */
  -webkit-box-align: stretch;
  -moz-box-align: stretch;
  box-align: stretch;
  /* Modern browsers */
  align-items: stretch;
}
div.error {
  margin: 2em;
  text-align: center;
}
div.error > h1 {
  font-size: 500%;
  line-height: normal;
}
div.error > p {
  font-size: 200%;
  line-height: normal;
}
div.traceback-wrapper {
  text-align: left;
  max-width: 800px;
  margin: auto;
}
div.traceback-wrapper pre.traceback {
  max-height: 600px;
  overflow: auto;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
body {
  background-color: #fff;
  /* This makes sure that the body covers the entire window and needs to
       be in a different element than the display: box in wrapper below */
  position: absolute;
  left: 0px;
  right: 0px;
  top: 0px;
  bottom: 0px;
  overflow: visible;
}
body > #header {
  /* Initially hidden to prevent FLOUC */
  display: none;
  background-color: #fff;
  /* Display over codemirror */
  position: relative;
  z-index: 100;
}
body > #header #header-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 5px;
  padding-bottom: 5px;
  padding-top: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
body > #header .header-bar {
  width: 100%;
  height: 1px;
  background: #e7e7e7;
  margin-bottom: -1px;
}
@media print {
  body > #header {
    display: none !important;
  }
}
#header-spacer {
  width: 100%;
  visibility: hidden;
}
@media print {
  #header-spacer {
    display: none;
  }
}
#ipython_notebook {
  padding-left: 0px;
  padding-top: 1px;
  padding-bottom: 1px;
}
[dir="rtl"] #ipython_notebook {
  margin-right: 10px;
  margin-left: 0;
}
[dir="rtl"] #ipython_notebook.pull-left {
  float: right !important;
  float: right;
}
.flex-spacer {
  flex: 1;
}
#noscript {
  width: auto;
  padding-top: 16px;
  padding-bottom: 16px;
  text-align: center;
  font-size: 22px;
  color: red;
  font-weight: bold;
}
#ipython_notebook img {
  height: 28px;
}
#site {
  width: 100%;
  display: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  overflow: auto;
}
@media print {
  #site {
    height: auto !important;
  }
}
/* Smaller buttons */
.ui-button .ui-button-text {
  padding: 0.2em 0.8em;
  font-size: 77%;
}
input.ui-button {
  padding: 0.3em 0.9em;
}
span#kernel_logo_widget {
  margin: 0 10px;
}
span#login_widget {
  float: right;
}
[dir="rtl"] span#login_widget {
  float: left;
}
span#login_widget > .button,
#logout {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button:focus,
#logout:focus,
span#login_widget > .button.focus,
#logout.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
span#login_widget > .button:hover,
#logout:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active:hover,
#logout:active:hover,
span#login_widget > .button.active:hover,
#logout.active:hover,
.open > .dropdown-togglespan#login_widget > .button:hover,
.open > .dropdown-toggle#logout:hover,
span#login_widget > .button:active:focus,
#logout:active:focus,
span#login_widget > .button.active:focus,
#logout.active:focus,
.open > .dropdown-togglespan#login_widget > .button:focus,
.open > .dropdown-toggle#logout:focus,
span#login_widget > .button:active.focus,
#logout:active.focus,
span#login_widget > .button.active.focus,
#logout.active.focus,
.open > .dropdown-togglespan#login_widget > .button.focus,
.open > .dropdown-toggle#logout.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  background-image: none;
}
span#login_widget > .button.disabled:hover,
#logout.disabled:hover,
span#login_widget > .button[disabled]:hover,
#logout[disabled]:hover,
fieldset[disabled] span#login_widget > .button:hover,
fieldset[disabled] #logout:hover,
span#login_widget > .button.disabled:focus,
#logout.disabled:focus,
span#login_widget > .button[disabled]:focus,
#logout[disabled]:focus,
fieldset[disabled] span#login_widget > .button:focus,
fieldset[disabled] #logout:focus,
span#login_widget > .button.disabled.focus,
#logout.disabled.focus,
span#login_widget > .button[disabled].focus,
#logout[disabled].focus,
fieldset[disabled] span#login_widget > .button.focus,
fieldset[disabled] #logout.focus {
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button .badge,
#logout .badge {
  color: #fff;
  background-color: #333;
}
.nav-header {
  text-transform: none;
}
#header > span {
  margin-top: 10px;
}
.modal_stretch .modal-dialog {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  min-height: 80vh;
}
.modal_stretch .modal-dialog .modal-body {
  max-height: calc(100vh - 200px);
  overflow: auto;
  flex: 1;
}
.modal-header {
  cursor: move;
}
@media (min-width: 768px) {
  .modal .modal-dialog {
    width: 700px;
  }
}
@media (min-width: 768px) {
  select.form-control {
    margin-left: 12px;
    margin-right: 12px;
  }
}
/*!
*
* IPython auth
*
*/
.center-nav {
  display: inline-block;
  margin-bottom: -4px;
}
[dir="rtl"] .center-nav form.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] .center-nav .navbar-text {
  float: right;
}
[dir="rtl"] .navbar-inner {
  text-align: right;
}
[dir="rtl"] div.text-left {
  text-align: right;
}
/*!
*
* IPython tree view
*
*/
/* We need an invisible input field on top of the sentense*/
/* "Drag file onto the list ..." */
.alternate_upload {
  background-color: none;
  display: inline;
}
.alternate_upload.form {
  padding: 0;
  margin: 0;
}
.alternate_upload input.fileinput {
  position: absolute;
  display: block;
  width: 100%;
  height: 100%;
  overflow: hidden;
  cursor: pointer;
  opacity: 0;
  z-index: 2;
}
.alternate_upload .btn-xs > input.fileinput {
  margin: -1px -5px;
}
.alternate_upload .btn-upload {
  position: relative;
  height: 22px;
}
::-webkit-file-upload-button {
  cursor: pointer;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
ul#tabs {
  margin-bottom: 4px;
}
ul#tabs a {
  padding-top: 6px;
  padding-bottom: 4px;
}
[dir="rtl"] ul#tabs.nav-tabs > li {
  float: right;
}
[dir="rtl"] ul#tabs.nav.nav-tabs {
  padding-right: 0;
}
ul.breadcrumb a:focus,
ul.breadcrumb a:hover {
  text-decoration: none;
}
ul.breadcrumb i.icon-home {
  font-size: 16px;
  margin-right: 4px;
}
ul.breadcrumb span {
  color: #5e5e5e;
}
.list_toolbar {
  padding: 4px 0 4px 0;
  vertical-align: middle;
}
.list_toolbar .tree-buttons {
  padding-top: 1px;
}
[dir="rtl"] .list_toolbar .tree-buttons .pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .list_toolbar .col-sm-4,
[dir="rtl"] .list_toolbar .col-sm-8 {
  float: right;
}
.dynamic-buttons {
  padding-top: 3px;
  display: inline-block;
}
.list_toolbar [class*="span"] {
  min-height: 24px;
}
.list_header {
  font-weight: bold;
  background-color: #EEE;
}
.list_placeholder {
  font-weight: bold;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
}
.list_container {
  margin-top: 4px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 2px;
}
.list_container > div {
  border-bottom: 1px solid #ddd;
}
.list_container > div:hover .list-item {
  background-color: red;
}
.list_container > div:last-child {
  border: none;
}
.list_item:hover .list_item {
  background-color: #ddd;
}
.list_item a {
  text-decoration: none;
}
.list_item:hover {
  background-color: #fafafa;
}
.list_header > div,
.list_item > div {
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
.list_header > div input,
.list_item > div input {
  margin-right: 7px;
  margin-left: 14px;
  vertical-align: text-bottom;
  line-height: 22px;
  position: relative;
  top: -1px;
}
.list_header > div .item_link,
.list_item > div .item_link {
  margin-left: -1px;
  vertical-align: baseline;
  line-height: 22px;
}
[dir="rtl"] .list_item > div input {
  margin-right: 0;
}
.new-file input[type=checkbox] {
  visibility: hidden;
}
.item_name {
  line-height: 22px;
  height: 24px;
}
.item_icon {
  font-size: 14px;
  color: #5e5e5e;
  margin-right: 7px;
  margin-left: 7px;
  line-height: 22px;
  vertical-align: baseline;
}
.item_modified {
  margin-right: 7px;
  margin-left: 7px;
}
[dir="rtl"] .item_modified.pull-right {
  float: left !important;
  float: left;
}
.item_buttons {
  line-height: 1em;
  margin-left: -5px;
}
.item_buttons .btn,
.item_buttons .btn-group,
.item_buttons .input-group {
  float: left;
}
.item_buttons > .btn,
.item_buttons > .btn-group,
.item_buttons > .input-group {
  margin-left: 5px;
}
.item_buttons .btn {
  min-width: 13ex;
}
.item_buttons .running-indicator {
  padding-top: 4px;
  color: #5cb85c;
}
.item_buttons .kernel-name {
  padding-top: 4px;
  color: #5bc0de;
  margin-right: 7px;
  float: left;
}
[dir="rtl"] .item_buttons.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .item_buttons .kernel-name {
  margin-left: 7px;
  float: right;
}
.toolbar_info {
  height: 24px;
  line-height: 24px;
}
.list_item input:not([type=checkbox]) {
  padding-top: 3px;
  padding-bottom: 3px;
  height: 22px;
  line-height: 14px;
  margin: 0px;
}
.highlight_text {
  color: blue;
}
#project_name {
  display: inline-block;
  padding-left: 7px;
  margin-left: -2px;
}
#project_name > .breadcrumb {
  padding: 0px;
  margin-bottom: 0px;
  background-color: transparent;
  font-weight: bold;
}
.sort_button {
  display: inline-block;
  padding-left: 7px;
}
[dir="rtl"] .sort_button.pull-right {
  float: left !important;
  float: left;
}
#tree-selector {
  padding-right: 0px;
}
#button-select-all {
  min-width: 50px;
}
[dir="rtl"] #button-select-all.btn {
  float: right ;
}
#select-all {
  margin-left: 7px;
  margin-right: 2px;
  margin-top: 2px;
  height: 16px;
}
[dir="rtl"] #select-all.pull-left {
  float: right !important;
  float: right;
}
.menu_icon {
  margin-right: 2px;
}
.tab-content .row {
  margin-left: 0px;
  margin-right: 0px;
}
.folder_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f114";
}
.folder_icon:before.fa-pull-left {
  margin-right: .3em;
}
.folder_icon:before.fa-pull-right {
  margin-left: .3em;
}
.folder_icon:before.pull-left {
  margin-right: .3em;
}
.folder_icon:before.pull-right {
  margin-left: .3em;
}
.notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
}
.notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.notebook_icon:before.pull-left {
  margin-right: .3em;
}
.notebook_icon:before.pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
  color: #5cb85c;
}
.running_notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before.pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.pull-right {
  margin-left: .3em;
}
.file_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f016";
  position: relative;
  top: -2px;
}
.file_icon:before.fa-pull-left {
  margin-right: .3em;
}
.file_icon:before.fa-pull-right {
  margin-left: .3em;
}
.file_icon:before.pull-left {
  margin-right: .3em;
}
.file_icon:before.pull-right {
  margin-left: .3em;
}
#notebook_toolbar .pull-right {
  padding-top: 0px;
  margin-right: -1px;
}
ul#new-menu {
  left: auto;
  right: 0;
}
#new-menu .dropdown-header {
  font-size: 10px;
  border-bottom: 1px solid #e5e5e5;
  padding: 0 0 3px;
  margin: -3px 20px 0;
}
.kernel-menu-icon {
  padding-right: 12px;
  width: 24px;
  content: "\f096";
}
.kernel-menu-icon:before {
  content: "\f096";
}
.kernel-menu-icon-current:before {
  content: "\f00c";
}
#tab_content {
  padding-top: 20px;
}
#running .panel-group .panel {
  margin-top: 3px;
  margin-bottom: 1em;
}
#running .panel-group .panel .panel-heading {
  background-color: #EEE;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
#running .panel-group .panel .panel-heading a:focus,
#running .panel-group .panel .panel-heading a:hover {
  text-decoration: none;
}
#running .panel-group .panel .panel-body {
  padding: 0px;
}
#running .panel-group .panel .panel-body .list_container {
  margin-top: 0px;
  margin-bottom: 0px;
  border: 0px;
  border-radius: 0px;
}
#running .panel-group .panel .panel-body .list_container .list_item {
  border-bottom: 1px solid #ddd;
}
#running .panel-group .panel .panel-body .list_container .list_item:last-child {
  border-bottom: 0px;
}
.delete-button {
  display: none;
}
.duplicate-button {
  display: none;
}
.rename-button {
  display: none;
}
.move-button {
  display: none;
}
.download-button {
  display: none;
}
.shutdown-button {
  display: none;
}
.dynamic-instructions {
  display: inline-block;
  padding-top: 4px;
}
/*!
*
* IPython text editor webapp
*
*/
.selected-keymap i.fa {
  padding: 0px 5px;
}
.selected-keymap i.fa:before {
  content: "\f00c";
}
#mode-menu {
  overflow: auto;
  max-height: 20em;
}
.edit_app #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.edit_app #menubar .navbar {
  /* Use a negative 1 bottom margin, so the border overlaps the border of the
    header */
  margin-bottom: -1px;
}
.dirty-indicator {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator.pull-left {
  margin-right: .3em;
}
.dirty-indicator.pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-dirty.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty.pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-clean.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f00c";
}
.dirty-indicator-clean:before.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.pull-right {
  margin-left: .3em;
}
#filename {
  font-size: 16pt;
  display: table;
  padding: 0px 5px;
}
#current-mode {
  padding-left: 5px;
  padding-right: 5px;
}
#texteditor-backdrop {
  padding-top: 20px;
  padding-bottom: 20px;
}
@media not print {
  #texteditor-backdrop {
    background-color: #EEE;
  }
}
@media print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container {
    padding: 0px;
    background-color: #fff;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
.CodeMirror-dialog {
  background-color: #fff;
}
/*!
*
* IPython notebook
*
*/
/* CSS font colors for translated ANSI escape sequences */
/* The color values are a mix of
   http://www.xcolors.net/dl/baskerville-ivorylight and
   http://www.xcolors.net/dl/euphrasia */
.ansi-black-fg {
  color: #3E424D;
}
.ansi-black-bg {
  background-color: #3E424D;
}
.ansi-black-intense-fg {
  color: #282C36;
}
.ansi-black-intense-bg {
  background-color: #282C36;
}
.ansi-red-fg {
  color: #E75C58;
}
.ansi-red-bg {
  background-color: #E75C58;
}
.ansi-red-intense-fg {
  color: #B22B31;
}
.ansi-red-intense-bg {
  background-color: #B22B31;
}
.ansi-green-fg {
  color: #00A250;
}
.ansi-green-bg {
  background-color: #00A250;
}
.ansi-green-intense-fg {
  color: #007427;
}
.ansi-green-intense-bg {
  background-color: #007427;
}
.ansi-yellow-fg {
  color: #DDB62B;
}
.ansi-yellow-bg {
  background-color: #DDB62B;
}
.ansi-yellow-intense-fg {
  color: #B27D12;
}
.ansi-yellow-intense-bg {
  background-color: #B27D12;
}
.ansi-blue-fg {
  color: #208FFB;
}
.ansi-blue-bg {
  background-color: #208FFB;
}
.ansi-blue-intense-fg {
  color: #0065CA;
}
.ansi-blue-intense-bg {
  background-color: #0065CA;
}
.ansi-magenta-fg {
  color: #D160C4;
}
.ansi-magenta-bg {
  background-color: #D160C4;
}
.ansi-magenta-intense-fg {
  color: #A03196;
}
.ansi-magenta-intense-bg {
  background-color: #A03196;
}
.ansi-cyan-fg {
  color: #60C6C8;
}
.ansi-cyan-bg {
  background-color: #60C6C8;
}
.ansi-cyan-intense-fg {
  color: #258F8F;
}
.ansi-cyan-intense-bg {
  background-color: #258F8F;
}
.ansi-white-fg {
  color: #C5C1B4;
}
.ansi-white-bg {
  background-color: #C5C1B4;
}
.ansi-white-intense-fg {
  color: #A1A6B2;
}
.ansi-white-intense-bg {
  background-color: #A1A6B2;
}
.ansi-default-inverse-fg {
  color: #FFFFFF;
}
.ansi-default-inverse-bg {
  background-color: #000000;
}
.ansi-bold {
  font-weight: bold;
}
.ansi-underline {
  text-decoration: underline;
}
/* The following styles are deprecated an will be removed in a future version */
.ansibold {
  font-weight: bold;
}
.ansi-inverse {
  outline: 0.5px dotted;
}
/* use dark versions for foreground, to improve visibility */
.ansiblack {
  color: black;
}
.ansired {
  color: darkred;
}
.ansigreen {
  color: darkgreen;
}
.ansiyellow {
  color: #c4a000;
}
.ansiblue {
  color: darkblue;
}
.ansipurple {
  color: darkviolet;
}
.ansicyan {
  color: steelblue;
}
.ansigray {
  color: gray;
}
/* and light for background, for the same reason */
.ansibgblack {
  background-color: black;
}
.ansibgred {
  background-color: red;
}
.ansibggreen {
  background-color: green;
}
.ansibgyellow {
  background-color: yellow;
}
.ansibgblue {
  background-color: blue;
}
.ansibgpurple {
  background-color: magenta;
}
.ansibgcyan {
  background-color: cyan;
}
.ansibggray {
  background-color: gray;
}
div.cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  border-radius: 2px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  border-width: 1px;
  border-style: solid;
  border-color: transparent;
  width: 100%;
  padding: 5px;
  /* This acts as a spacer between cells, that is outside the border */
  margin: 0px;
  outline: none;
  position: relative;
  overflow: visible;
}
div.cell:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: transparent;
}
div.cell.jupyter-soft-selected {
  border-left-color: #E3F2FD;
  border-left-width: 1px;
  padding-left: 5px;
  border-right-color: #E3F2FD;
  border-right-width: 1px;
  background: #E3F2FD;
}
@media print {
  div.cell.jupyter-soft-selected {
    border-color: transparent;
  }
}
div.cell.selected,
div.cell.selected.jupyter-soft-selected {
  border-color: #ababab;
}
div.cell.selected:before,
div.cell.selected.jupyter-soft-selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #42A5F5;
}
@media print {
  div.cell.selected,
  div.cell.selected.jupyter-soft-selected {
    border-color: transparent;
  }
}
.edit_mode div.cell.selected {
  border-color: #66BB6A;
}
.edit_mode div.cell.selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #66BB6A;
}
@media print {
  .edit_mode div.cell.selected {
    border-color: transparent;
  }
}
.prompt {
  /* This needs to be wide enough for 3 digit prompt numbers: In[100]: */
  min-width: 14ex;
  /* This padding is tuned to match the padding on the CodeMirror editor. */
  padding: 0.4em;
  margin: 0px;
  font-family: monospace;
  text-align: right;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
  /* Don't highlight prompt number selection */
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  /* Use default cursor */
  cursor: default;
}
@media (max-width: 540px) {
  .prompt {
    text-align: left;
  }
}
div.inner_cell {
  min-width: 0;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_area {
  border: 1px solid #cfcfcf;
  border-radius: 2px;
  background: #f7f7f7;
  line-height: 1.21429em;
}
/* This is needed so that empty prompt areas can collapse to zero height when there
   is no content in the output_subarea and the prompt. The main purpose of this is
   to make sure that empty JavaScript output_subareas have no height. */
div.prompt:empty {
  padding-top: 0;
  padding-bottom: 0;
}
div.unrecognized_cell {
  padding: 5px 5px 5px 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.unrecognized_cell .inner_cell {
  border-radius: 2px;
  padding: 5px;
  font-weight: bold;
  color: red;
  border: 1px solid #cfcfcf;
  background: #eaeaea;
}
div.unrecognized_cell .inner_cell a {
  color: inherit;
  text-decoration: none;
}
div.unrecognized_cell .inner_cell a:hover {
  color: inherit;
  text-decoration: none;
}
@media (max-width: 540px) {
  div.unrecognized_cell > div.prompt {
    display: none;
  }
}
div.code_cell {
  /* avoid page breaking on code cells when printing */
}
@media print {
  div.code_cell {
    page-break-inside: avoid;
  }
}
/* any special styling for code cells that are currently running goes here */
div.input {
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.input {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_prompt {
  color: #303F9F;
  border-top: 1px solid transparent;
}
div.input_area > div.highlight {
  margin: 0.4em;
  border: none;
  padding: 0px;
  background-color: transparent;
}
div.input_area > div.highlight > pre {
  margin: 0px;
  border: none;
  padding: 0px;
  background-color: transparent;
}
/* The following gets added to the <head> if it is detected that the user has a
 * monospace font with inconsistent normal/bold/italic height.  See
 * notebookmain.js.  Such fonts will have keywords vertically offset with
 * respect to the rest of the text.  The user should select a better font.
 * See: https://github.com/ipython/ipython/issues/1503
 *
 * .CodeMirror span {
 *      vertical-align: bottom;
 * }
 */
.CodeMirror {
  line-height: 1.21429em;
  /* Changed from 1em to our global default */
  font-size: 14px;
  height: auto;
  /* Changed to auto to autogrow */
  background: none;
  /* Changed from white to allow our bg to show through */
}
.CodeMirror-scroll {
  /*  The CodeMirror docs are a bit fuzzy on if overflow-y should be hidden or visible.*/
  /*  We have found that if it is visible, vertical scrollbars appear with font size changes.*/
  overflow-y: hidden;
  overflow-x: auto;
}
.CodeMirror-lines {
  /* In CM2, this used to be 0.4em, but in CM3 it went to 4px. We need the em value because */
  /* we have set a different line-height and want this to scale with that. */
  /* Note that this should set vertical padding only, since CodeMirror assumes
       that horizontal padding will be set on CodeMirror pre */
  padding: 0.4em 0;
}
.CodeMirror-linenumber {
  padding: 0 8px 0 4px;
}
.CodeMirror-gutters {
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.CodeMirror pre {
  /* In CM3 this went to 4px from 0 in CM2. This sets horizontal padding only,
    use .CodeMirror-lines for vertical */
  padding: 0 0.4em;
  border: 0;
  border-radius: 0;
}
.CodeMirror-cursor {
  border-left: 1.4px solid black;
}
@media screen and (min-width: 2138px) and (max-width: 4319px) {
  .CodeMirror-cursor {
    border-left: 2px solid black;
  }
}
@media screen and (min-width: 4320px) {
  .CodeMirror-cursor {
    border-left: 4px solid black;
  }
}
/*

Original style from softwaremaniacs.org (c) Ivan Sagalaev <Maniac@SoftwareManiacs.Org>
Adapted from GitHub theme

*/
.highlight-base {
  color: #000;
}
.highlight-variable {
  color: #000;
}
.highlight-variable-2 {
  color: #1a1a1a;
}
.highlight-variable-3 {
  color: #333333;
}
.highlight-string {
  color: #BA2121;
}
.highlight-comment {
  color: #408080;
  font-style: italic;
}
.highlight-number {
  color: #080;
}
.highlight-atom {
  color: #88F;
}
.highlight-keyword {
  color: #008000;
  font-weight: bold;
}
.highlight-builtin {
  color: #008000;
}
.highlight-error {
  color: #f00;
}
.highlight-operator {
  color: #AA22FF;
  font-weight: bold;
}
.highlight-meta {
  color: #AA22FF;
}
/* previously not defined, copying from default codemirror */
.highlight-def {
  color: #00f;
}
.highlight-string-2 {
  color: #f50;
}
.highlight-qualifier {
  color: #555;
}
.highlight-bracket {
  color: #997;
}
.highlight-tag {
  color: #170;
}
.highlight-attribute {
  color: #00c;
}
.highlight-header {
  color: blue;
}
.highlight-quote {
  color: #090;
}
.highlight-link {
  color: #00c;
}
/* apply the same style to codemirror */
.cm-s-ipython span.cm-keyword {
  color: #008000;
  font-weight: bold;
}
.cm-s-ipython span.cm-atom {
  color: #88F;
}
.cm-s-ipython span.cm-number {
  color: #080;
}
.cm-s-ipython span.cm-def {
  color: #00f;
}
.cm-s-ipython span.cm-variable {
  color: #000;
}
.cm-s-ipython span.cm-operator {
  color: #AA22FF;
  font-weight: bold;
}
.cm-s-ipython span.cm-variable-2 {
  color: #1a1a1a;
}
.cm-s-ipython span.cm-variable-3 {
  color: #333333;
}
.cm-s-ipython span.cm-comment {
  color: #408080;
  font-style: italic;
}
.cm-s-ipython span.cm-string {
  color: #BA2121;
}
.cm-s-ipython span.cm-string-2 {
  color: #f50;
}
.cm-s-ipython span.cm-meta {
  color: #AA22FF;
}
.cm-s-ipython span.cm-qualifier {
  color: #555;
}
.cm-s-ipython span.cm-builtin {
  color: #008000;
}
.cm-s-ipython span.cm-bracket {
  color: #997;
}
.cm-s-ipython span.cm-tag {
  color: #170;
}
.cm-s-ipython span.cm-attribute {
  color: #00c;
}
.cm-s-ipython span.cm-header {
  color: blue;
}
.cm-s-ipython span.cm-quote {
  color: #090;
}
.cm-s-ipython span.cm-link {
  color: #00c;
}
.cm-s-ipython span.cm-error {
  color: #f00;
}
.cm-s-ipython span.cm-tab {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=);
  background-position: right;
  background-repeat: no-repeat;
}
div.output_wrapper {
  /* this position must be relative to enable descendents to be absolute within it */
  position: relative;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  z-index: 1;
}
/* class for the output area when it should be height-limited */
div.output_scroll {
  /* ideally, this would be max-height, but FF barfs all over that */
  height: 24em;
  /* FF needs this *and the wrapper* to specify full width, or it will shrinkwrap */
  width: 100%;
  overflow: auto;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  display: block;
}
/* output div while it is collapsed */
div.output_collapsed {
  margin: 0px;
  padding: 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
div.out_prompt_overlay {
  height: 100%;
  padding: 0px 0.4em;
  position: absolute;
  border-radius: 2px;
}
div.out_prompt_overlay:hover {
  /* use inner shadow to get border that is computed the same on WebKit/FF */
  -webkit-box-shadow: inset 0 0 1px #000;
  box-shadow: inset 0 0 1px #000;
  background: rgba(240, 240, 240, 0.5);
}
div.output_prompt {
  color: #D84315;
}
/* This class is the outer container of all output sections. */
div.output_area {
  padding: 0px;
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.output_area .MathJax_Display {
  text-align: left !important;
}
div.output_area .rendered_html table {
  margin-left: 0;
  margin-right: 0;
}
div.output_area .rendered_html img {
  margin-left: 0;
  margin-right: 0;
}
div.output_area img,
div.output_area svg {
  max-width: 100%;
  height: auto;
}
div.output_area img.unconfined,
div.output_area svg.unconfined {
  max-width: none;
}
div.output_area .mglyph > img {
  max-width: none;
}
/* This is needed to protect the pre formating from global settings such
   as that of bootstrap */
.output {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.output_area {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
div.output_area pre {
  margin: 0;
  padding: 1px 0 1px 0;
  border: 0;
  vertical-align: baseline;
  color: black;
  background-color: transparent;
  border-radius: 0;
}
/* This class is for the output subarea inside the output_area and after
   the prompt div. */
div.output_subarea {
  overflow-x: auto;
  padding: 0.4em;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
  max-width: calc(100% - 14ex);
}
div.output_scroll div.output_subarea {
  overflow-x: visible;
}
/* The rest of the output_* classes are for special styling of the different
   output types */
/* all text output has this class: */
div.output_text {
  text-align: left;
  color: #000;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
}
/* stdout/stderr are 'text' as well as 'stream', but execute_result/error are *not* streams */
div.output_stderr {
  background: #fdd;
  /* very light red background for stderr */
}
div.output_latex {
  text-align: left;
}
/* Empty output_javascript divs should have no height */
div.output_javascript:empty {
  padding: 0;
}
.js-error {
  color: darkred;
}
/* raw_input styles */
div.raw_input_container {
  line-height: 1.21429em;
  padding-top: 5px;
}
pre.raw_input_prompt {
  /* nothing needed here. */
}
input.raw_input {
  font-family: monospace;
  font-size: inherit;
  color: inherit;
  width: auto;
  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;
  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0em 0.25em;
  margin: 0em 0.25em;
}
input.raw_input:focus {
  box-shadow: none;
}
p.p-space {
  margin-bottom: 10px;
}
div.output_unrecognized {
  padding: 5px;
  font-weight: bold;
  color: red;
}
div.output_unrecognized a {
  color: inherit;
  text-decoration: none;
}
div.output_unrecognized a:hover {
  color: inherit;
  text-decoration: none;
}
.rendered_html {
  color: #000;
  /* any extras will just be numbers: */
}
.rendered_html em {
  font-style: italic;
}
.rendered_html strong {
  font-weight: bold;
}
.rendered_html u {
  text-decoration: underline;
}
.rendered_html :link {
  text-decoration: underline;
}
.rendered_html :visited {
  text-decoration: underline;
}
.rendered_html h1 {
  font-size: 185.7%;
  margin: 1.08em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h2 {
  font-size: 157.1%;
  margin: 1.27em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h3 {
  font-size: 128.6%;
  margin: 1.55em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h4 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h5 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h6 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h1:first-child {
  margin-top: 0.538em;
}
.rendered_html h2:first-child {
  margin-top: 0.636em;
}
.rendered_html h3:first-child {
  margin-top: 0.777em;
}
.rendered_html h4:first-child {
  margin-top: 1em;
}
.rendered_html h5:first-child {
  margin-top: 1em;
}
.rendered_html h6:first-child {
  margin-top: 1em;
}
.rendered_html ul:not(.list-inline),
.rendered_html ol:not(.list-inline) {
  padding-left: 2em;
}
.rendered_html ul {
  list-style: disc;
}
.rendered_html ul ul {
  list-style: square;
  margin-top: 0;
}
.rendered_html ul ul ul {
  list-style: circle;
}
.rendered_html ol {
  list-style: decimal;
}
.rendered_html ol ol {
  list-style: upper-alpha;
  margin-top: 0;
}
.rendered_html ol ol ol {
  list-style: lower-alpha;
}
.rendered_html ol ol ol ol {
  list-style: lower-roman;
}
.rendered_html ol ol ol ol ol {
  list-style: decimal;
}
.rendered_html * + ul {
  margin-top: 1em;
}
.rendered_html * + ol {
  margin-top: 1em;
}
.rendered_html hr {
  color: black;
  background-color: black;
}
.rendered_html pre {
  margin: 1em 2em;
  padding: 0px;
  background-color: #fff;
}
.rendered_html code {
  background-color: #eff0f1;
}
.rendered_html p code {
  padding: 1px 5px;
}
.rendered_html pre code {
  background-color: #fff;
}
.rendered_html pre,
.rendered_html code {
  border: 0;
  color: #000;
  font-size: 100%;
}
.rendered_html blockquote {
  margin: 1em 2em;
}
.rendered_html table {
  margin-left: auto;
  margin-right: auto;
  border: none;
  border-collapse: collapse;
  border-spacing: 0;
  color: black;
  font-size: 12px;
  table-layout: fixed;
}
.rendered_html thead {
  border-bottom: 1px solid black;
  vertical-align: bottom;
}
.rendered_html tr,
.rendered_html th,
.rendered_html td {
  text-align: right;
  vertical-align: middle;
  padding: 0.5em 0.5em;
  line-height: normal;
  white-space: normal;
  max-width: none;
  border: none;
}
.rendered_html th {
  font-weight: bold;
}
.rendered_html tbody tr:nth-child(odd) {
  background: #f5f5f5;
}
.rendered_html tbody tr:hover {
  background: rgba(66, 165, 245, 0.2);
}
.rendered_html * + table {
  margin-top: 1em;
}
.rendered_html p {
  text-align: left;
}
.rendered_html * + p {
  margin-top: 1em;
}
.rendered_html img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.rendered_html * + img {
  margin-top: 1em;
}
.rendered_html img,
.rendered_html svg {
  max-width: 100%;
  height: auto;
}
.rendered_html img.unconfined,
.rendered_html svg.unconfined {
  max-width: none;
}
.rendered_html .alert {
  margin-bottom: initial;
}
.rendered_html * + .alert {
  margin-top: 1em;
}
[dir="rtl"] .rendered_html p {
  text-align: right;
}
div.text_cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.text_cell > div.prompt {
    display: none;
  }
}
div.text_cell_render {
  /*font-family: "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;*/
  outline: none;
  resize: none;
  width: inherit;
  border-style: none;
  padding: 0.5em 0.5em 0.5em 0.4em;
  color: #000;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
a.anchor-link:link {
  text-decoration: none;
  padding: 0px 20px;
  visibility: hidden;
}
h1:hover .anchor-link,
h2:hover .anchor-link,
h3:hover .anchor-link,
h4:hover .anchor-link,
h5:hover .anchor-link,
h6:hover .anchor-link {
  visibility: visible;
}
.text_cell.rendered .input_area {
  display: none;
}
.text_cell.rendered .rendered_html {
  overflow-x: auto;
  overflow-y: hidden;
}
.text_cell.rendered .rendered_html tr,
.text_cell.rendered .rendered_html th,
.text_cell.rendered .rendered_html td {
  max-width: none;
}
.text_cell.unrendered .text_cell_render {
  display: none;
}
.text_cell .dropzone .input_area {
  border: 2px dashed #bababa;
  margin: -1px;
}
.cm-header-1,
.cm-header-2,
.cm-header-3,
.cm-header-4,
.cm-header-5,
.cm-header-6 {
  font-weight: bold;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
.cm-header-1 {
  font-size: 185.7%;
}
.cm-header-2 {
  font-size: 157.1%;
}
.cm-header-3 {
  font-size: 128.6%;
}
.cm-header-4 {
  font-size: 110%;
}
.cm-header-5 {
  font-size: 100%;
  font-style: italic;
}
.cm-header-6 {
  font-size: 100%;
  font-style: italic;
}
/*!
*
* IPython notebook webapp
*
*/
@media (max-width: 767px) {
  .notebook_app {
    padding-left: 0px;
    padding-right: 0px;
  }
}
#ipython-main-app {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook_panel {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook {
  font-size: 14px;
  line-height: 20px;
  overflow-y: hidden;
  overflow-x: auto;
  width: 100%;
  /* This spaces the page away from the edge of the notebook area */
  padding-top: 20px;
  margin: 0px;
  outline: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  min-height: 100%;
}
@media not print {
  #notebook-container {
    padding: 15px;
    background-color: #fff;
    min-height: 0;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
@media print {
  #notebook-container {
    width: 100%;
  }
}
div.ui-widget-content {
  border: 1px solid #ababab;
  outline: none;
}
pre.dialog {
  background-color: #f7f7f7;
  border: 1px solid #ddd;
  border-radius: 2px;
  padding: 0.4em;
  padding-left: 2em;
}
p.dialog {
  padding: 0.2em;
}
/* Word-wrap output correctly.  This is the CSS3 spelling, though Firefox seems
   to not honor it correctly.  Webkit browsers (Chrome, rekonq, Safari) do.
 */
pre,
code,
kbd,
samp {
  white-space: pre-wrap;
}
#fonttest {
  font-family: monospace;
}
p {
  margin-bottom: 0;
}
.end_space {
  min-height: 100px;
  transition: height .2s ease;
}
.notebook_app > #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
@media not print {
  .notebook_app {
    background-color: #EEE;
  }
}
kbd {
  border-style: solid;
  border-width: 1px;
  box-shadow: none;
  margin: 2px;
  padding-left: 2px;
  padding-right: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
.jupyter-keybindings {
  padding: 1px;
  line-height: 24px;
  border-bottom: 1px solid gray;
}
.jupyter-keybindings input {
  margin: 0;
  padding: 0;
  border: none;
}
.jupyter-keybindings i {
  padding: 6px;
}
.well code {
  background-color: #ffffff;
  border-color: #ababab;
  border-width: 1px;
  border-style: solid;
  padding: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
/* CSS for the cell toolbar */
.celltoolbar {
  border: thin solid #CFCFCF;
  border-bottom: none;
  background: #EEE;
  border-radius: 2px 2px 0px 0px;
  width: 100%;
  height: 29px;
  padding-right: 4px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
  display: -webkit-flex;
}
@media print {
  .celltoolbar {
    display: none;
  }
}
.ctb_hideshow {
  display: none;
  vertical-align: bottom;
}
/* ctb_show is added to the ctb_hideshow div to show the cell toolbar.
   Cell toolbars are only shown when the ctb_global_show class is also set.
*/
.ctb_global_show .ctb_show.ctb_hideshow {
  display: block;
}
.ctb_global_show .ctb_show + .input_area,
.ctb_global_show .ctb_show + div.text_cell_input,
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border-top-right-radius: 0px;
  border-top-left-radius: 0px;
}
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border: 1px solid #cfcfcf;
}
.celltoolbar {
  font-size: 87%;
  padding-top: 3px;
}
.celltoolbar select {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  width: inherit;
  font-size: inherit;
  height: 22px;
  padding: 0px;
  display: inline-block;
}
.celltoolbar select:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.celltoolbar select::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.celltoolbar select:-ms-input-placeholder {
  color: #999;
}
.celltoolbar select::-webkit-input-placeholder {
  color: #999;
}
.celltoolbar select::-ms-expand {
  border: 0;
  background-color: transparent;
}
.celltoolbar select[disabled],
.celltoolbar select[readonly],
fieldset[disabled] .celltoolbar select {
  background-color: #eeeeee;
  opacity: 1;
}
.celltoolbar select[disabled],
fieldset[disabled] .celltoolbar select {
  cursor: not-allowed;
}
textarea.celltoolbar select {
  height: auto;
}
select.celltoolbar select {
  height: 30px;
  line-height: 30px;
}
textarea.celltoolbar select,
select[multiple].celltoolbar select {
  height: auto;
}
.celltoolbar label {
  margin-left: 5px;
  margin-right: 5px;
}
.tags_button_container {
  width: 100%;
  display: flex;
}
.tag-container {
  display: flex;
  flex-direction: row;
  flex-grow: 1;
  overflow: hidden;
  position: relative;
}
.tag-container > * {
  margin: 0 4px;
}
.remove-tag-btn {
  margin-left: 4px;
}
.tags-input {
  display: flex;
}
.cell-tag:last-child:after {
  content: "";
  position: absolute;
  right: 0;
  width: 40px;
  height: 100%;
  /* Fade to background color of cell toolbar */
  background: linear-gradient(to right, rgba(0, 0, 0, 0), #EEE);
}
.tags-input > * {
  margin-left: 4px;
}
.cell-tag,
.tags-input input,
.tags-input button {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  box-shadow: none;
  width: inherit;
  font-size: inherit;
  height: 22px;
  line-height: 22px;
  padding: 0px 4px;
  display: inline-block;
}
.cell-tag:focus,
.tags-input input:focus,
.tags-input button:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.cell-tag::-moz-placeholder,
.tags-input input::-moz-placeholder,
.tags-input button::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.cell-tag:-ms-input-placeholder,
.tags-input input:-ms-input-placeholder,
.tags-input button:-ms-input-placeholder {
  color: #999;
}
.cell-tag::-webkit-input-placeholder,
.tags-input input::-webkit-input-placeholder,
.tags-input button::-webkit-input-placeholder {
  color: #999;
}
.cell-tag::-ms-expand,
.tags-input input::-ms-expand,
.tags-input button::-ms-expand {
  border: 0;
  background-color: transparent;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
.cell-tag[readonly],
.tags-input input[readonly],
.tags-input button[readonly],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  background-color: #eeeeee;
  opacity: 1;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  cursor: not-allowed;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button {
  height: auto;
}
select.cell-tag,
select.tags-input input,
select.tags-input button {
  height: 30px;
  line-height: 30px;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button,
select[multiple].cell-tag,
select[multiple].tags-input input,
select[multiple].tags-input button {
  height: auto;
}
.cell-tag,
.tags-input button {
  padding: 0px 4px;
}
.cell-tag {
  background-color: #fff;
  white-space: nowrap;
}
.tags-input input[type=text]:focus {
  outline: none;
  box-shadow: none;
  border-color: #ccc;
}
.completions {
  position: absolute;
  z-index: 110;
  overflow: hidden;
  border: 1px solid #ababab;
  border-radius: 2px;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  line-height: 1;
}
.completions select {
  background: white;
  outline: none;
  border: none;
  padding: 0px;
  margin: 0px;
  overflow: auto;
  font-family: monospace;
  font-size: 110%;
  color: #000;
  width: auto;
}
.completions select option.context {
  color: #286090;
}
#kernel_logo_widget .current_kernel_logo {
  display: none;
  margin-top: -1px;
  margin-bottom: -1px;
  width: 32px;
  height: 32px;
}
[dir="rtl"] #kernel_logo_widget {
  float: left !important;
  float: left;
}
.modal .modal-body .move-path {
  display: flex;
  flex-direction: row;
  justify-content: space;
  align-items: center;
}
.modal .modal-body .move-path .server-root {
  padding-right: 20px;
}
.modal .modal-body .move-path .path-input {
  flex: 1;
}
#menubar {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  margin-top: 1px;
}
#menubar .navbar {
  border-top: 1px;
  border-radius: 0px 0px 2px 2px;
  margin-bottom: 0px;
}
#menubar .navbar-toggle {
  float: left;
  padding-top: 7px;
  padding-bottom: 7px;
  border: none;
}
#menubar .navbar-collapse {
  clear: left;
}
[dir="rtl"] #menubar .navbar-toggle {
  float: right;
}
[dir="rtl"] #menubar .navbar-collapse {
  clear: right;
}
[dir="rtl"] #menubar .navbar-nav {
  float: right;
}
[dir="rtl"] #menubar .nav {
  padding-right: 0px;
}
[dir="rtl"] #menubar .navbar-nav > li {
  float: right;
}
[dir="rtl"] #menubar .navbar-right {
  float: left !important;
}
[dir="rtl"] ul.dropdown-menu {
  text-align: right;
  left: auto;
}
[dir="rtl"] ul#new-menu.dropdown-menu {
  right: auto;
  left: 0;
}
.nav-wrapper {
  border-bottom: 1px solid #e7e7e7;
}
i.menu-icon {
  padding-top: 4px;
}
[dir="rtl"] i.menu-icon.pull-right {
  float: left !important;
  float: left;
}
ul#help_menu li a {
  overflow: hidden;
  padding-right: 2.2em;
}
ul#help_menu li a i {
  margin-right: -1.2em;
}
[dir="rtl"] ul#help_menu li a {
  padding-left: 2.2em;
}
[dir="rtl"] ul#help_menu li a i {
  margin-right: 0;
  margin-left: -1.2em;
}
[dir="rtl"] ul#help_menu li a i.pull-right {
  float: left !important;
  float: left;
}
.dropdown-submenu {
  position: relative;
}
.dropdown-submenu > .dropdown-menu {
  top: 0;
  left: 100%;
  margin-top: -6px;
  margin-left: -1px;
}
[dir="rtl"] .dropdown-submenu > .dropdown-menu {
  right: 100%;
  margin-right: -1px;
}
.dropdown-submenu:hover > .dropdown-menu {
  display: block;
}
.dropdown-submenu > a:after {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: block;
  content: "\f0da";
  float: right;
  color: #333333;
  margin-top: 2px;
  margin-right: -10px;
}
.dropdown-submenu > a:after.fa-pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.fa-pull-right {
  margin-left: .3em;
}
.dropdown-submenu > a:after.pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.pull-right {
  margin-left: .3em;
}
[dir="rtl"] .dropdown-submenu > a:after {
  float: left;
  content: "\f0d9";
  margin-right: 0;
  margin-left: -10px;
}
.dropdown-submenu:hover > a:after {
  color: #262626;
}
.dropdown-submenu.pull-left {
  float: none;
}
.dropdown-submenu.pull-left > .dropdown-menu {
  left: -100%;
  margin-left: 10px;
}
#notification_area {
  float: right !important;
  float: right;
  z-index: 10;
}
[dir="rtl"] #notification_area {
  float: left !important;
  float: left;
}
.indicator_area {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] .indicator_area {
  float: left !important;
  float: left;
}
#kernel_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  border-left: 1px solid;
}
#kernel_indicator .kernel_indicator_name {
  padding-left: 5px;
  padding-right: 5px;
}
[dir="rtl"] #kernel_indicator {
  float: left !important;
  float: left;
  border-left: 0;
  border-right: 1px solid;
}
#modal_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] #modal_indicator {
  float: left !important;
  float: left;
}
#readonly-indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  margin-top: 2px;
  margin-bottom: 0px;
  margin-left: 0px;
  margin-right: 0px;
  display: none;
}
.modal_indicator:before {
  width: 1.28571429em;
  text-align: center;
}
.edit_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f040";
}
.edit_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.edit_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: ' ';
}
.command_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f10c";
}
.kernel_idle_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f111";
}
.kernel_busy_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f1e2";
}
.kernel_dead_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f127";
}
.kernel_disconnected_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.pull-right {
  margin-left: .3em;
}
.notification_widget {
  color: #777;
  z-index: 10;
  background: rgba(240, 240, 240, 0.5);
  margin-right: 4px;
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget:focus,
.notification_widget.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.notification_widget:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active:hover,
.notification_widget.active:hover,
.open > .dropdown-toggle.notification_widget:hover,
.notification_widget:active:focus,
.notification_widget.active:focus,
.open > .dropdown-toggle.notification_widget:focus,
.notification_widget:active.focus,
.notification_widget.active.focus,
.open > .dropdown-toggle.notification_widget.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  background-image: none;
}
.notification_widget.disabled:hover,
.notification_widget[disabled]:hover,
fieldset[disabled] .notification_widget:hover,
.notification_widget.disabled:focus,
.notification_widget[disabled]:focus,
fieldset[disabled] .notification_widget:focus,
.notification_widget.disabled.focus,
.notification_widget[disabled].focus,
fieldset[disabled] .notification_widget.focus {
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget .badge {
  color: #fff;
  background-color: #333;
}
.notification_widget.warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning:focus,
.notification_widget.warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.notification_widget.warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active:hover,
.notification_widget.warning.active:hover,
.open > .dropdown-toggle.notification_widget.warning:hover,
.notification_widget.warning:active:focus,
.notification_widget.warning.active:focus,
.open > .dropdown-toggle.notification_widget.warning:focus,
.notification_widget.warning:active.focus,
.notification_widget.warning.active.focus,
.open > .dropdown-toggle.notification_widget.warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  background-image: none;
}
.notification_widget.warning.disabled:hover,
.notification_widget.warning[disabled]:hover,
fieldset[disabled] .notification_widget.warning:hover,
.notification_widget.warning.disabled:focus,
.notification_widget.warning[disabled]:focus,
fieldset[disabled] .notification_widget.warning:focus,
.notification_widget.warning.disabled.focus,
.notification_widget.warning[disabled].focus,
fieldset[disabled] .notification_widget.warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.notification_widget.success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success:focus,
.notification_widget.success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.notification_widget.success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active:hover,
.notification_widget.success.active:hover,
.open > .dropdown-toggle.notification_widget.success:hover,
.notification_widget.success:active:focus,
.notification_widget.success.active:focus,
.open > .dropdown-toggle.notification_widget.success:focus,
.notification_widget.success:active.focus,
.notification_widget.success.active.focus,
.open > .dropdown-toggle.notification_widget.success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  background-image: none;
}
.notification_widget.success.disabled:hover,
.notification_widget.success[disabled]:hover,
fieldset[disabled] .notification_widget.success:hover,
.notification_widget.success.disabled:focus,
.notification_widget.success[disabled]:focus,
fieldset[disabled] .notification_widget.success:focus,
.notification_widget.success.disabled.focus,
.notification_widget.success[disabled].focus,
fieldset[disabled] .notification_widget.success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.notification_widget.info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info:focus,
.notification_widget.info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.notification_widget.info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active:hover,
.notification_widget.info.active:hover,
.open > .dropdown-toggle.notification_widget.info:hover,
.notification_widget.info:active:focus,
.notification_widget.info.active:focus,
.open > .dropdown-toggle.notification_widget.info:focus,
.notification_widget.info:active.focus,
.notification_widget.info.active.focus,
.open > .dropdown-toggle.notification_widget.info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  background-image: none;
}
.notification_widget.info.disabled:hover,
.notification_widget.info[disabled]:hover,
fieldset[disabled] .notification_widget.info:hover,
.notification_widget.info.disabled:focus,
.notification_widget.info[disabled]:focus,
fieldset[disabled] .notification_widget.info:focus,
.notification_widget.info.disabled.focus,
.notification_widget.info[disabled].focus,
fieldset[disabled] .notification_widget.info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.notification_widget.danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger:focus,
.notification_widget.danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.notification_widget.danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active:hover,
.notification_widget.danger.active:hover,
.open > .dropdown-toggle.notification_widget.danger:hover,
.notification_widget.danger:active:focus,
.notification_widget.danger.active:focus,
.open > .dropdown-toggle.notification_widget.danger:focus,
.notification_widget.danger:active.focus,
.notification_widget.danger.active.focus,
.open > .dropdown-toggle.notification_widget.danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  background-image: none;
}
.notification_widget.danger.disabled:hover,
.notification_widget.danger[disabled]:hover,
fieldset[disabled] .notification_widget.danger:hover,
.notification_widget.danger.disabled:focus,
.notification_widget.danger[disabled]:focus,
fieldset[disabled] .notification_widget.danger:focus,
.notification_widget.danger.disabled.focus,
.notification_widget.danger[disabled].focus,
fieldset[disabled] .notification_widget.danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger .badge {
  color: #d9534f;
  background-color: #fff;
}
div#pager {
  background-color: #fff;
  font-size: 14px;
  line-height: 20px;
  overflow: hidden;
  display: none;
  position: fixed;
  bottom: 0px;
  width: 100%;
  max-height: 50%;
  padding-top: 8px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  /* Display over codemirror */
  z-index: 100;
  /* Hack which prevents jquery ui resizable from changing top. */
  top: auto !important;
}
div#pager pre {
  line-height: 1.21429em;
  color: #000;
  background-color: #f7f7f7;
  padding: 0.4em;
}
div#pager #pager-button-area {
  position: absolute;
  top: 8px;
  right: 20px;
}
div#pager #pager-contents {
  position: relative;
  overflow: auto;
  width: 100%;
  height: 100%;
}
div#pager #pager-contents #pager-container {
  position: relative;
  padding: 15px 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
div#pager .ui-resizable-handle {
  top: 0px;
  height: 8px;
  background: #f7f7f7;
  border-top: 1px solid #cfcfcf;
  border-bottom: 1px solid #cfcfcf;
  /* This injects handle bars (a short, wide = symbol) for 
        the resize handle. */
}
div#pager .ui-resizable-handle::after {
  content: '';
  top: 2px;
  left: 50%;
  height: 3px;
  width: 30px;
  margin-left: -15px;
  position: absolute;
  border-top: 1px solid #cfcfcf;
}
.quickhelp {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  line-height: 1.8em;
}
.shortcut_key {
  display: inline-block;
  width: 21ex;
  text-align: right;
  font-family: monospace;
}
.shortcut_descr {
  display: inline-block;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
span.save_widget {
  height: 30px;
  margin-top: 4px;
  display: flex;
  justify-content: flex-start;
  align-items: baseline;
  width: 50%;
  flex: 1;
}
span.save_widget span.filename {
  height: 100%;
  line-height: 1em;
  margin-left: 16px;
  border: none;
  font-size: 146.5%;
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
  border-radius: 2px;
}
span.save_widget span.filename:hover {
  background-color: #e6e6e6;
}
[dir="rtl"] span.save_widget.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] span.save_widget span.filename {
  margin-left: 0;
  margin-right: 16px;
}
span.checkpoint_status,
span.autosave_status {
  font-size: small;
  white-space: nowrap;
  padding: 0 5px;
}
@media (max-width: 767px) {
  span.save_widget {
    font-size: small;
    padding: 0 0 0 5px;
  }
  span.checkpoint_status,
  span.autosave_status {
    display: none;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  span.checkpoint_status {
    display: none;
  }
  span.autosave_status {
    font-size: x-small;
  }
}
.toolbar {
  padding: 0px;
  margin-left: -5px;
  margin-top: 2px;
  margin-bottom: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.toolbar select,
.toolbar label {
  width: auto;
  vertical-align: middle;
  margin-right: 2px;
  margin-bottom: 0px;
  display: inline;
  font-size: 92%;
  margin-left: 0.3em;
  margin-right: 0.3em;
  padding: 0px;
  padding-top: 3px;
}
.toolbar .btn {
  padding: 2px 8px;
}
.toolbar .btn-group {
  margin-top: 0px;
  margin-left: 5px;
}
.toolbar-btn-label {
  margin-left: 6px;
}
#maintoolbar {
  margin-bottom: -3px;
  margin-top: -8px;
  border: 0px;
  min-height: 27px;
  margin-left: 0px;
  padding-top: 11px;
  padding-bottom: 3px;
}
#maintoolbar .navbar-text {
  float: none;
  vertical-align: middle;
  text-align: right;
  margin-left: 5px;
  margin-right: 0px;
  margin-top: 0px;
}
.select-xs {
  height: 24px;
}
[dir="rtl"] .btn-group > .btn,
.btn-group-vertical > .btn {
  float: right;
}
.pulse,
.dropdown-menu > li > a.pulse,
li.pulse > a.dropdown-toggle,
li.pulse.open > a.dropdown-toggle {
  background-color: #F37626;
  color: white;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
/** WARNING IF YOU ARE EDITTING THIS FILE, if this is a .css file, It has a lot
 * of chance of beeing generated from the ../less/[samename].less file, you can
 * try to get back the less file by reverting somme commit in history
 **/
/*
 * We'll try to get something pretty, so we
 * have some strange css to have the scroll bar on
 * the left with fix button on the top right of the tooltip
 */
@-moz-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-webkit-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-moz-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@-webkit-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
/*properties of tooltip after "expand"*/
.bigtooltip {
  overflow: auto;
  height: 200px;
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
}
/*properties of tooltip before "expand"*/
.smalltooltip {
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
  text-overflow: ellipsis;
  overflow: hidden;
  height: 80px;
}
.tooltipbuttons {
  position: absolute;
  padding-right: 15px;
  top: 0px;
  right: 0px;
}
.tooltiptext {
  /*avoid the button to overlap on some docstring*/
  padding-right: 30px;
}
.ipython_tooltip {
  max-width: 700px;
  /*fade-in animation when inserted*/
  -webkit-animation: fadeOut 400ms;
  -moz-animation: fadeOut 400ms;
  animation: fadeOut 400ms;
  -webkit-animation: fadeIn 400ms;
  -moz-animation: fadeIn 400ms;
  animation: fadeIn 400ms;
  vertical-align: middle;
  background-color: #f7f7f7;
  overflow: visible;
  border: #ababab 1px solid;
  outline: none;
  padding: 3px;
  margin: 0px;
  padding-left: 7px;
  font-family: monospace;
  min-height: 50px;
  -moz-box-shadow: 0px 6px 10px -1px #adadad;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  border-radius: 2px;
  position: absolute;
  z-index: 1000;
}
.ipython_tooltip a {
  float: right;
}
.ipython_tooltip .tooltiptext pre {
  border: 0;
  border-radius: 0;
  font-size: 100%;
  background-color: #f7f7f7;
}
.pretooltiparrow {
  left: 0px;
  margin: 0px;
  top: -16px;
  width: 40px;
  height: 16px;
  overflow: hidden;
  position: absolute;
}
.pretooltiparrow:before {
  background-color: #f7f7f7;
  border: 1px #ababab solid;
  z-index: 11;
  content: "";
  position: absolute;
  left: 15px;
  top: 10px;
  width: 25px;
  height: 25px;
  -webkit-transform: rotate(45deg);
  -moz-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  -o-transform: rotate(45deg);
}
ul.typeahead-list i {
  margin-left: -10px;
  width: 18px;
}
[dir="rtl"] ul.typeahead-list i {
  margin-left: 0;
  margin-right: -10px;
}
ul.typeahead-list {
  max-height: 80vh;
  overflow: auto;
}
ul.typeahead-list > li > a {
  /** Firefox bug **/
  /* see https://github.com/jupyter/notebook/issues/559 */
  white-space: normal;
}
ul.typeahead-list  > li > a.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .typeahead-list {
  text-align: right;
}
.cmd-palette .modal-body {
  padding: 7px;
}
.cmd-palette form {
  background: white;
}
.cmd-palette input {
  outline: none;
}
.no-shortcut {
  min-width: 20px;
  color: transparent;
}
[dir="rtl"] .no-shortcut.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .command-shortcut.pull-right {
  float: left !important;
  float: left;
}
.command-shortcut:before {
  content: "(command mode)";
  padding-right: 3px;
  color: #777777;
}
.edit-shortcut:before {
  content: "(edit)";
  padding-right: 3px;
  color: #777777;
}
[dir="rtl"] .edit-shortcut.pull-right {
  float: left !important;
  float: left;
}
#find-and-replace #replace-preview .match,
#find-and-replace #replace-preview .insert {
  background-color: #BBDEFB;
  border-color: #90CAF9;
  border-style: solid;
  border-width: 1px;
  border-radius: 0px;
}
[dir="ltr"] #find-and-replace .input-group-btn + .form-control {
  border-left: none;
}
[dir="rtl"] #find-and-replace .input-group-btn + .form-control {
  border-right: none;
}
#find-and-replace #replace-preview .replace .match {
  background-color: #FFCDD2;
  border-color: #EF9A9A;
  border-radius: 0px;
}
#find-and-replace #replace-preview .replace .insert {
  background-color: #C8E6C9;
  border-color: #A5D6A7;
  border-radius: 0px;
}
#find-and-replace #replace-preview {
  max-height: 60vh;
  overflow: auto;
}
#find-and-replace #replace-preview pre {
  padding: 5px 10px;
}
.terminal-app {
  background: #EEE;
}
.terminal-app #header {
  background: #fff;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.terminal-app .terminal {
  width: 100%;
  float: left;
  font-family: monospace;
  color: white;
  background: black;
  padding: 0.4em;
  border-radius: 2px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
}
.terminal-app .terminal,
.terminal-app .terminal dummy-screen {
  line-height: 1em;
  font-size: 14px;
}
.terminal-app .terminal .xterm-rows {
  padding: 10px;
}
.terminal-app .terminal-cursor {
  color: black;
  background: white;
}
.terminal-app #terminado-container {
  margin-top: 20px;
}
/*# sourceMappingURL=style.min.css.map */
    </style>
<style type="text/css">
    .highlight .hll { background-color: #ffffcc }
.highlight  { background: #f8f8f8; }
.highlight .c { color: #408080; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #FF0000 } /* Error */
.highlight .k { color: #008000; font-weight: bold } /* Keyword */
.highlight .o { color: #666666 } /* Operator */
.highlight .ch { color: #408080; font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #BC7A00 } /* Comment.Preproc */
.highlight .cpf { color: #408080; font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: #408080; font-style: italic } /* Comment.Single */
.highlight .cs { color: #408080; font-style: italic } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .gr { color: #FF0000 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #00A000 } /* Generic.Inserted */
.highlight .go { color: #888888 } /* Generic.Output */
.highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight .gt { color: #0044DD } /* Generic.Traceback */
.highlight .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #008000 } /* Keyword.Pseudo */
.highlight .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #B00040 } /* Keyword.Type */
.highlight .m { color: #666666 } /* Literal.Number */
.highlight .s { color: #BA2121 } /* Literal.String */
.highlight .na { color: #7D9029 } /* Name.Attribute */
.highlight .nb { color: #008000 } /* Name.Builtin */
.highlight .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.highlight .no { color: #880000 } /* Name.Constant */
.highlight .nd { color: #AA22FF } /* Name.Decorator */
.highlight .ni { color: #999999; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.highlight .nf { color: #0000FF } /* Name.Function */
.highlight .nl { color: #A0A000 } /* Name.Label */
.highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #19177C } /* Name.Variable */
.highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight .w { color: #bbbbbb } /* Text.Whitespace */
.highlight .mb { color: #666666 } /* Literal.Number.Bin */
.highlight .mf { color: #666666 } /* Literal.Number.Float */
.highlight .mh { color: #666666 } /* Literal.Number.Hex */
.highlight .mi { color: #666666 } /* Literal.Number.Integer */
.highlight .mo { color: #666666 } /* Literal.Number.Oct */
.highlight .sa { color: #BA2121 } /* Literal.String.Affix */
.highlight .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight .sc { color: #BA2121 } /* Literal.String.Char */
.highlight .dl { color: #BA2121 } /* Literal.String.Delimiter */
.highlight .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #BA2121 } /* Literal.String.Double */
.highlight .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #BA2121 } /* Literal.String.Heredoc */
.highlight .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.highlight .sx { color: #008000 } /* Literal.String.Other */
.highlight .sr { color: #BB6688 } /* Literal.String.Regex */
.highlight .s1 { color: #BA2121 } /* Literal.String.Single */
.highlight .ss { color: #19177C } /* Literal.String.Symbol */
.highlight .bp { color: #008000 } /* Name.Builtin.Pseudo */
.highlight .fm { color: #0000FF } /* Name.Function.Magic */
.highlight .vc { color: #19177C } /* Name.Variable.Class */
.highlight .vg { color: #19177C } /* Name.Variable.Global */
.highlight .vi { color: #19177C } /* Name.Variable.Instance */
.highlight .vm { color: #19177C } /* Name.Variable.Magic */
.highlight .il { color: #666666 } /* Literal.Number.Integer.Long */
    </style>
<style type="text/css">
    
/* Temporary definitions which will become obsolete with Notebook release 5.0 */
.ansi-black-fg { color: #3E424D; }
.ansi-black-bg { background-color: #3E424D; }
.ansi-black-intense-fg { color: #282C36; }
.ansi-black-intense-bg { background-color: #282C36; }
.ansi-red-fg { color: #E75C58; }
.ansi-red-bg { background-color: #E75C58; }
.ansi-red-intense-fg { color: #B22B31; }
.ansi-red-intense-bg { background-color: #B22B31; }
.ansi-green-fg { color: #00A250; }
.ansi-green-bg { background-color: #00A250; }
.ansi-green-intense-fg { color: #007427; }
.ansi-green-intense-bg { background-color: #007427; }
.ansi-yellow-fg { color: #DDB62B; }
.ansi-yellow-bg { background-color: #DDB62B; }
.ansi-yellow-intense-fg { color: #B27D12; }
.ansi-yellow-intense-bg { background-color: #B27D12; }
.ansi-blue-fg { color: #208FFB; }
.ansi-blue-bg { background-color: #208FFB; }
.ansi-blue-intense-fg { color: #0065CA; }
.ansi-blue-intense-bg { background-color: #0065CA; }
.ansi-magenta-fg { color: #D160C4; }
.ansi-magenta-bg { background-color: #D160C4; }
.ansi-magenta-intense-fg { color: #A03196; }
.ansi-magenta-intense-bg { background-color: #A03196; }
.ansi-cyan-fg { color: #60C6C8; }
.ansi-cyan-bg { background-color: #60C6C8; }
.ansi-cyan-intense-fg { color: #258F8F; }
.ansi-cyan-intense-bg { background-color: #258F8F; }
.ansi-white-fg { color: #C5C1B4; }
.ansi-white-bg { background-color: #C5C1B4; }
.ansi-white-intense-fg { color: #A1A6B2; }
.ansi-white-intense-bg { background-color: #A1A6B2; }

.ansi-bold { font-weight: bold; }

    </style>
<style type="text/css">
    #ipython_notebook img{                                                                                        
    display:block;
    background: url(coursera-logo.png) no-repeat;
    background-size: contain;
    width: 233px;
    height: 33px;
    padding-left: 233px;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
}

#ipython_notebook {
    height: 40px !important;
}

/* Format for custom error modal message */
.running-notebooks {
    padding-top: 2em;
}

    </style>


<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
body {
  overflow: visible;
  padding: 8px;
}

div#notebook {
  overflow: visible;
  border-top: none;
}@media print {
  div.cell {
    display: block;
    page-break-inside: avoid;
  } 
  div.output_wrapper { 
    display: block;
    page-break-inside: avoid; 
  }
  div.output { 
    display: block;
    page-break-inside: avoid; 
  }
}
</style>

<!-- Custom stylesheet, it must be in the same directory as the html file -->
<link rel="stylesheet" href="custom.css">

<!-- Loading mathjax macro -->
<!-- Load mathjax -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-AMS_HTML"></script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {
            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
            processEscapes: true,
            processEnvironments: true
        },
        // Center justify equations in code and markdown cells. Elsewhere
        // we use CSS to left justify single line equations in code cells.
        displayAlign: 'center',
        "HTML-CSS": {
            styles: {'.MathJax_Display': {"margin": 0}},
            linebreaks: { automatic: true }
        }
    });
    </script>
    <!-- End of mathjax configuration --></head>
<body>
  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">

<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="The-Project">The Project<a class="anchor-link" href="#The-Project">&#182;</a></h1><ol>
<li>This is a project with minimal scaffolding. Expect to use the the discussion forums to gain insights! It’s not cheating to ask others for opinions or perspectives!</li>
<li>Be inquisitive, try out new things.</li>
<li>Use the previous modules for insights into how to complete the functions! You'll have to combine Pillow, OpenCV, and Pytesseract</li>
<li>There are hints provided in Coursera, feel free to explore the hints if needed. Each hint provide progressively more details on how to solve the issue. This project is intended to be comprehensive and difficult if you do it without the hints.</li>
</ol>
<h3 id="The-Assignment">The Assignment<a class="anchor-link" href="#The-Assignment">&#182;</a></h3><p>Take a <a href="https://en.wikipedia.org/wiki/Zip_(file_format">ZIP file</a>) of images and process them, using a <a href="https://docs.python.org/3/library/zipfile.html">library built into python</a> that you need to learn how to use. A ZIP file takes several different files and compresses them, thus saving space, into one single file. The files in the ZIP file we provide are newspaper images (like you saw in week 3). Your task is to write python code which allows one to search through the images looking for the occurrences of keywords and faces. E.g. if you search for "pizza" it will return a contact sheet of all of the faces which were located on the newspaper page which mentions "pizza". This will test your ability to learn a new (<a href="https://docs.python.org/3/library/zipfile.html">library</a>), your ability to use OpenCV to detect faces, your ability to use tesseract to do optical character recognition, and your ability to use PIL to composite images together into contact sheets.</p>
<p>Each page of the newspapers is saved as a single PNG image in a file called <a href="./readonly/images.zip">images.zip</a>. These newspapers are in english, and contain a variety of stories, advertisements and images. Note: This file is fairly large (~200 MB) and may take some time to work with, I would encourage you to use <a href="./readonly/small_img.zip">small_img.zip</a> for testing.</p>
<p>Here's an example of the output expected. Using the <a href="./readonly/small_img.zip">small_img.zip</a> file, if I search for the string "Christopher" I should see the following image:
<img src="./readonly/small_project.png" alt="Christopher Search">
If I were to use the <a href="./readonly/images.zip">images.zip</a> file and search for "Mark" I should see the following image (note that there are times when there are no faces on a page, but a word is found!):
<img src="./readonly/large_project.png" alt="Mark Search"></p>
<p>Note: That big file can take some time to process - for me it took nearly ten minutes! Use the small one for testing.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">zipfile</span>
<span class="kn">from</span> <span class="nn">PIL</span> <span class="k">import</span> <span class="n">Image</span>
<span class="kn">import</span> <span class="nn">pytesseract</span>
<span class="kn">import</span> <span class="nn">cv2</span> <span class="k">as</span> <span class="nn">cv</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">io</span>
<span class="kn">import</span> <span class="nn">math</span>
<span class="kn">import</span> <span class="nn">time</span>


<span class="sd">&quot;&quot;&quot;</span>
<span class="sd">-------------------------------------------------------------------</span>
<span class="sd">    Loading the face detection classifier</span>
<span class="sd">-------------------------------------------------------------------</span>
<span class="sd">&quot;&quot;&quot;</span>
<span class="n">face_cascade</span> <span class="o">=</span> <span class="n">cv</span><span class="o">.</span><span class="n">CascadeClassifier</span><span class="p">(</span><span class="s1">&#39;readonly/haarcascade_frontalface_default.xml&#39;</span><span class="p">)</span>

<span class="sd">&quot;&quot;&quot;</span>
<span class="sd">-------------------------------------------------------------------</span>
<span class="sd">    Data loaded from the zip file</span>
<span class="sd">-------------------------------------------------------------------</span>
<span class="sd">&quot;&quot;&quot;</span>
<span class="n">zip_data</span> <span class="o">=</span> <span class="p">[]</span>


<span class="sd">&quot;&quot;&quot;</span>
<span class="sd">-------------------------------------------------------------------</span>
<span class="sd">    Hard-coded dimension for normalization</span>
<span class="sd">-------------------------------------------------------------------</span>
<span class="sd">&quot;&quot;&quot;</span>
<span class="n">thumb_dim</span> <span class="o">=</span> <span class="mi">64</span>


<span class="sd">&quot;&quot;&quot;</span>
<span class="sd">-------------------------------------------------------------------</span>
<span class="sd">    Hard-coded images per row</span>
<span class="sd">-------------------------------------------------------------------</span>
<span class="sd">&quot;&quot;&quot;</span>
<span class="n">img_per_row</span> <span class="o">=</span> <span class="mi">5</span>


<span class="sd">&quot;&quot;&quot;</span>
<span class="sd">-------------------------------------------------------------------</span>
<span class="sd">    Function to load the data from the zip file</span>
<span class="sd">-------------------------------------------------------------------</span>
<span class="sd">&quot;&quot;&quot;</span>
<span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span><span class="n">zip_file</span><span class="p">):</span>
    <span class="c1"># DEBUG</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;[DEBUG] Loading data...&quot;</span><span class="p">)</span>
    <span class="n">start_time</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span>
    <span class="c1"># Load the zipfiles</span>
    <span class="k">with</span> <span class="n">zipfile</span><span class="o">.</span><span class="n">ZipFile</span><span class="p">(</span><span class="n">zip_file</span><span class="p">,</span> <span class="s1">&#39;r&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">zipImages</span><span class="p">:</span>
        <span class="c1"># Open each image</span>
        <span class="k">for</span> <span class="n">image</span> <span class="ow">in</span> <span class="n">zipImages</span><span class="o">.</span><span class="n">infolist</span><span class="p">():</span>
            <span class="c1"># Image info</span>
            <span class="n">image_name</span> <span class="o">=</span> <span class="n">image</span><span class="o">.</span><span class="n">filename</span>
            <span class="n">image_bytes</span> <span class="o">=</span> <span class="n">zipImages</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="n">image_name</span><span class="p">)</span>
            <span class="c1"># Process image</span>
            <span class="n">process_data</span><span class="p">(</span><span class="n">image_name</span><span class="p">,</span> <span class="n">image_bytes</span><span class="p">)</span>            
    <span class="c1"># DEBUG</span>
    <span class="n">end_time</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span>
    <span class="n">elapsed_time</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="s2">&quot;%H:%M:%S&quot;</span><span class="p">,</span> <span class="n">time</span><span class="o">.</span><span class="n">gmtime</span><span class="p">(</span><span class="n">end_time</span> <span class="o">-</span> <span class="n">start_time</span><span class="p">))</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;[DEBUG] Data loaded in </span><span class="si">{}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">elapsed_time</span><span class="p">))</span>


<span class="sd">&quot;&quot;&quot;</span>
<span class="sd">-------------------------------------------------------------------</span>
<span class="sd">    Function for the parallel image processing</span>
<span class="sd">-------------------------------------------------------------------</span>
<span class="sd">&quot;&quot;&quot;</span>
<span class="k">def</span> <span class="nf">process_data</span><span class="p">(</span><span class="n">image_name</span><span class="p">,</span> <span class="n">image_bytes</span><span class="p">):</span>
    <span class="c1"># Load PIL image from bytes</span>
    <span class="n">image</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">io</span><span class="o">.</span><span class="n">BytesIO</span><span class="p">(</span><span class="n">image_bytes</span><span class="p">))</span>
    <span class="c1"># Convert PIL image to grayscale</span>
    <span class="n">gray_image</span> <span class="o">=</span> <span class="n">image</span><span class="o">.</span><span class="n">convert</span><span class="p">(</span><span class="s2">&quot;L&quot;</span><span class="p">)</span>
    <span class="c1"># Convert PIL image to numpy array</span>
    <span class="n">np_image</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">gray_image</span><span class="p">)</span>
    <span class="c1"># Detect text with (py)Tesseract</span>
    <span class="n">text</span> <span class="o">=</span> <span class="n">pytesseract</span><span class="o">.</span><span class="n">image_to_string</span><span class="p">(</span><span class="n">np_image</span><span class="p">)</span>
    <span class="n">text</span> <span class="o">=</span> <span class="n">text</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">&quot;-</span><span class="se">\n</span><span class="s2">&quot;</span><span class="p">,</span> <span class="s2">&quot;&quot;</span><span class="p">)</span>
    <span class="n">text</span> <span class="o">=</span> <span class="n">text</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="p">,</span> <span class="s2">&quot; &quot;</span><span class="p">)</span>
    <span class="c1"># Detect face boxes with OpenCV</span>
    <span class="n">faces</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">face_boxes</span> <span class="o">=</span> <span class="n">face_cascade</span><span class="o">.</span><span class="n">detectMultiScale</span><span class="p">(</span><span class="n">np_image</span><span class="p">,</span> <span class="mf">1.29</span><span class="p">,</span> <span class="mi">8</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">w</span><span class="p">,</span> <span class="n">h</span> <span class="ow">in</span> <span class="n">face_boxes</span><span class="p">:</span>
        <span class="c1"># Crop original image</span>
        <span class="n">cropped</span> <span class="o">=</span> <span class="n">image</span><span class="o">.</span><span class="n">crop</span><span class="p">((</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">x</span> <span class="o">+</span> <span class="n">w</span><span class="p">,</span> <span class="n">y</span> <span class="o">+</span> <span class="n">h</span><span class="p">))</span>
        <span class="c1"># Resize</span>
        <span class="n">resized</span> <span class="o">=</span> <span class="n">cropped</span><span class="o">.</span><span class="n">resize</span><span class="p">((</span><span class="n">thumb_dim</span><span class="p">,</span> <span class="n">thumb_dim</span><span class="p">))</span>
        <span class="c1"># Append to the list</span>
        <span class="n">faces</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">resized</span><span class="p">)</span>
    <span class="c1"># Build sheet</span>
    <span class="n">sheet</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">faces</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
        <span class="n">rows</span> <span class="o">=</span> <span class="n">math</span><span class="o">.</span><span class="n">ceil</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">faces</span><span class="p">)</span> <span class="o">/</span> <span class="n">img_per_row</span><span class="p">)</span>
        <span class="c1"># Build the empty sheet</span>
        <span class="n">sheet</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">new</span><span class="p">(</span><span class="s1">&#39;RGB&#39;</span><span class="p">,</span> <span class="p">(</span><span class="n">thumb_dim</span> <span class="o">*</span> <span class="n">img_per_row</span><span class="p">,</span> <span class="n">thumb_dim</span> <span class="o">*</span> <span class="n">rows</span><span class="p">))</span>
        <span class="c1"># Iterate faces</span>
        <span class="n">x_pos</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="n">y_pos</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="k">for</span> <span class="n">face</span> <span class="ow">in</span> <span class="n">faces</span><span class="p">:</span>
            <span class="n">sheet</span><span class="o">.</span><span class="n">paste</span><span class="p">(</span><span class="n">face</span><span class="p">,</span> <span class="p">(</span><span class="n">x_pos</span><span class="p">,</span> <span class="n">y_pos</span><span class="p">))</span>
            <span class="n">x_pos</span> <span class="o">+=</span> <span class="n">face</span><span class="o">.</span><span class="n">width</span>
            <span class="k">if</span> <span class="n">x_pos</span> <span class="o">&gt;=</span> <span class="n">sheet</span><span class="o">.</span><span class="n">width</span><span class="p">:</span>
                <span class="n">x_pos</span> <span class="o">=</span> <span class="mi">0</span>
                <span class="n">y_pos</span> <span class="o">+=</span> <span class="n">face</span><span class="o">.</span><span class="n">height</span>
    <span class="c1"># Build dictionary</span>
    <span class="n">image_info</span> <span class="o">=</span> <span class="p">{</span> 
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="n">image_name</span><span class="p">,</span>
        <span class="s2">&quot;image&quot;</span><span class="p">:</span> <span class="n">image</span><span class="p">,</span>
        <span class="s2">&quot;text&quot;</span><span class="p">:</span> <span class="n">text</span><span class="p">,</span>
        <span class="s2">&quot;faces&quot;</span><span class="p">:</span> <span class="n">sheet</span>
    <span class="p">}</span>
    <span class="n">zip_data</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">image_info</span><span class="p">)</span>


<span class="sd">&quot;&quot;&quot;</span>
<span class="sd">-------------------------------------------------------------------</span>
<span class="sd">    Function to search the string</span>
<span class="sd">-------------------------------------------------------------------</span>
<span class="sd">&quot;&quot;&quot;</span>
<span class="k">def</span> <span class="nf">search_string</span><span class="p">(</span><span class="n">word</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;----------------------------------------------------------&quot;</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Searching for: </span><span class="si">{}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">word</span><span class="p">))</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;----------------------------------------------------------&quot;</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">data</span> <span class="ow">in</span> <span class="n">zip_data</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">word</span> <span class="ow">in</span> <span class="n">data</span><span class="p">[</span><span class="s1">&#39;text&#39;</span><span class="p">]:</span>
            <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Results found in file </span><span class="si">{}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="s1">&#39;name&#39;</span><span class="p">]))</span>
            <span class="k">if</span> <span class="n">data</span><span class="p">[</span><span class="s1">&#39;faces&#39;</span><span class="p">]</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;But there were no faces in that file!&quot;</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">display</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="s1">&#39;faces&#39;</span><span class="p">])</span>


<span class="sd">&quot;&quot;&quot;</span>
<span class="sd">-------------------------------------------------------------------</span>
<span class="sd">    Main loop</span>
<span class="sd">-------------------------------------------------------------------</span>
<span class="sd">&quot;&quot;&quot;</span>
<span class="n">load_data</span><span class="p">(</span><span class="s1">&#39;readonly/images.zip&#39;</span><span class="p">)</span>
<span class="n">search_string</span><span class="p">(</span><span class="s1">&#39;Christopher&#39;</span><span class="p">)</span>
<span class="n">search_string</span><span class="p">(</span><span class="s1">&#39;Mark&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[DEBUG] Loading data...
[DEBUG] Data loaded in 00:22:14
----------------------------------------------------------
Searching for: Christopher
----------------------------------------------------------
Results found in file a-0.png
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAUAAAACACAIAAAD1bSf9AADCg0lEQVR4nEz9adC163IWhnX3PT3Tmt75m79vT+fs4Uw6OhqQhITRhBBoMNiOIRhHFAkm4ErixOUklTKxq0LFZVcI5cQpMEMIhlQCMWGoQGxAQiCBJKSjI2lvnT2dvfc3vd87rOkZ7/vu7vx491G86vm/aq3n7ru7r76uq/H3//4/oAqIoAqACgqICAAirKpIiEAKzCIIkDkbYwGgqet5MycVAn7ppQfvvvsBADLwdt3+4A98kVQX1Tz3kyYuIBaFQ+tZ0PiQo06xHSe+3g/z5Xy/7V5cXe6GwYcCEEPhvXFJdUzpxcXae9MOqR9HETGGvAv90BOhcx6++ZmF6uLqxV/6r/6sZE08DGP+zV/7teOT05RGNOHg8BABEVFViSiloarmAJLTxFmJHPPIknNOpXcxjtbYFGOaEqEnNPt2u++urXXKZuz6bj+CTEhxtThStDmNnJKiDUXV9XtvGxE8PHGrs7OTk7OnT3728OwLijCO1jljSJ3Dojj6tXe+9pf/3P/96qrPnBHwrVvLW4vijZfOCPJ8VcVu97O/vv3N8w2g6cfJBk+AqppZi+BQRVWbELxVZ3CYYsribeCcjpeLe2eH++3uer07O168cu9WSnEaYs7ZllVRlZfPXhwerS6v1qd3j5yzz5+fjz0/udhfDdPEPIkAoIgW3ntDwziqwpSzcY5FgjU5p+NFjYAA2vVjYgbjH50s/sk7HwXnxzgZMggAAPrpmxFD1lrbj+OsqprCvX7H/+gf+P7D+shVZTG7BXQAKoAZlFQF4AVCNe4+ss3cYrW/Pq+aIwS6uPiXdflSlsEHByooK6UBjQRXKbqUxiFeWCzL4ujp89+Yr+bL6mGWjXELJASqh/7qD/+hP/nqo89crTswhpn2bRdKP/TDzZFgZgUBAFElJFW1SMZZgyg5ffEzj/LYs+rFZjeO6Q/9wX9t4aaqsmVdOxcACckhegACYCQl+jR2EBUQiIyygjKCIKKCUZWUgUCIVFVUc5rW1hQ5ZhAUYUmTKkhmAVQBUTbGsaiCCmuMuXBF268tEYpkUCuqCAiAiAoAZIhZFRQQQEFEiICZEQkQATCl5J2z1nrnt9cv3njjpaHd3To7+vjxs6PD5o/+oe/FSfI45JE0mNimolguZy5PY0zjfHUgiLvrPMZ8tmrWbdcsTGVKjqts8Lrrd/2QTZ4m3g3dwXJWlI52+2EaEUFERKUoipRi3/dEZK211kyR/8x//qe7ft3t9tYVhGbs45hkPj/s2m4YOkIqqxoBRMQYm7kfutTUhQmUJZU+KPh236H1AQxndb5QHBB13A9THIJrgFMau9WiGbZ751xRNNYE53yXJl/4KYLmXPpFTPsiFJur3bye+duND7fXl9ent++1u83meicpz+fLqub7t85+9TfevX16hwgRqfLh7q3D86urz7z2GQS4um4/ueycxZiAjAVRIHDWklFL4Mk1dUkaD5oZWRinvF7vb5+cpDTcOjysLC5PDo/qan5QHx0ebLbXMk2hLqqqurzc1mU1jumzb36WDEx5Ort1O3bbJ1ebYI2oApEq+jJk5n7oT46WXdfBqP00kTOs6Cyu29YgVkWRhQvvq2A37SbllFIsixIAVG6CVwAIkUTBEPwH/7N/51/84s9ePm1/4Pd+23x+YMjwOLb918Nh48JnQBzgpJoIjob129OwHs4/Wj64W1cPry5/2vsHcdjl+IvB3SX2feybBQPWnDBOlz40KohqBdJm+/atW59/+vQfF3hknJeU0CDitvTuz/+5/+gv/Pk/1+24z0gEZRFiTojovU8p/VYmMEQIN7elIqIjs1hW4zhU3rT9mAUObzfLpvIUnGVCIiIFUhWFRGSRhCgoACgb51SE0LFsES2gEXVEBKKgQJjJIAgTWVVj7FIB0QyqrCJorAowCjCqojASGZaszM7aXbuzjbHoRKKmTKXF3/f7/k0FQTDf/CGqICqKhDfXqaqyZCRiZmPMOA03b+vs6LBweHiwsArb7f5f/dHvRjsGN+uuP1kUy7FlUvTWATEpEagJNksPYo0t2/0+zGbTOHVt66BgLFwwjy/Ox5ienj8/7zMgppRzHmfLmfH+kyeX48Rdt7fWiqj3PqXonGfOVun/9Bf/0zSuP/rw/ZPTh+++82vN8gTUVE1ljR2nrqlqH3xK0Xnf7dcAUhZLYxEImZmAu831YrGKw/b6uvOh9GXFmUE5jsM0jWM3AUuOcbfZnhwfr6+3gDSr6r7bLpfFMGRQMya1nkCTDSYzn55VVEq5eJUkHJ3eQnTPLz66ujhfLOrF8gDI/JOf/v/+jb/xCyKMSP/97z6ZzxuQxThuiA6+9tH5B+cvyiLsR1aAwjsFccZ65+rCGhFDSjDev33qTfjgo8vFvFmtmna3d4KnR8vCOwTBgFadqgjH7ea6bpbDkKpyniWvTg+s9yycUr68+OS99591EroU22GKrMpcFaVC8sbllLZjRGOzCBGmGA3hoimFObiQ4sQJfJCvfvJiVs+EWVWtsSJCRDcxgMrGh/Xm6qW7B/+b/8X/0NLGNUsDxpgyNCe7Jx+M8TdXt7/DukPW6931x0U4jN2YldP+q5v241c/9yf78XzffhxwDigA+emTv3p49BNkKOYdAlTVA++OlPYp9QAeta/q17bbXy7KVV2/TDCAWmMMoM0JrtYf/Zd/6S++/56o4EW7a8JMZFJAETFE8P8//YJoAKXxwaDev3N4dnzw/vufjIl/1+/5gSMPZ2cNp0jGOR/IldaVAIAGEAGgAAQABjWEpMJIoJoVMoBBzJwA0aapt8YCGkMkzALAuQXAPPWcoworo7KIgjAZIEQQ5WloATTFZF3Y7nYEzhcOMJKCIBAi/NYDAEgICggECAoqqgCAgIbIoAGFqqhDCOM49V388KMnP/Z7vn91q1wsD2zGWg5hjzwmI0woIJlMMJXXAMaUhjxI18wazNJU/ux0tTyqqjIa398/m90/mb318PTuqn50Z7la+a4fnz9fD+20mJdVSavVSlVTjinFnLOIEJmPnn8C0g39bnV0/OzZs9XRaTNvfHCc43Z7bckB0H67JdRuvw7eW2MBNEe0xlhSg+RCGMceXTg+vV3U88vHH0OS1EeLXieWvN9cvUCVppp1253h6FWAU+193LXYdTYNJo3dfr1dt13XGQsQmkevfu+zD94G6J89f//9r/8yZDlcHedM3bBPef2v/MDvyombphbmrq0uLvH55fpqgy/adoTojI5ZUmJvjSEU5nnpT+eNU15VeLIoD2ZLnoxB+/KDuycnq8OD5uW7t1579f7qaF7UVmVqypmz5LwbxtQsj8qqCi744ObzehoGRC1CsJYOFkev3b/vKWuOhTWVwcN5DZpQtAx+OZvNCo+gAMrMxloydt/HfuKYsnXeOrPrc13W1jpEQkAAuInemwAemQ0aQvp3/ye/17pobdlefphin+Owe/qRwEh4Nl1exf1l3Hcmr4bdheTRmODqz83r3/78G//MQrGavxnCbRYBCKe3/0icXoCYNBjO9fr6+XX7gYC3dpXSuUj35Mlfs8VhP24gtwoCwJz6nDdAw7w6+MN/8AffumUuuqEpKoEIZEBvole/+QAAeO+ssT74nPXO7bO6KgQw5mlZptnMcExkC0CDxhFZACDyqB6hQERVFmYAFREAowIABGpAjGSL6I0tra/BFkRWVEUZMQKA5CQqiAhAcBNsoIiaOYlqTswC3b5XxXGcgi/HOAmgKNjfunoAUBUQkdAwZ1VFVCQksqRijRUUACyKQkTms3k/tF/54rfu18+/5zsePnrtztX5ex5IR+acOXNTVsYAAJHxzhsAC5zRiAAolc4YX1jOicCRTXZeZQZhgSR+tfqW2QJT/JiH+59/+OHzdj+k1WJmAde7fjlfXFxdiar3gZmttf/Zf/ofbq6ebPZaFAVzZM4senW1mc9mdVMjAYCEUKQUURQFwBhFDnWBPAz7p6vDV6wpJSdQjjBZkdLPU0o+FJrjcrky1+yXTbCeCit5z9EYdORnFnNswZf+6uop99OURJ0Ly4Ox4/MPL3eX/9j5chhHNRadmWJ3ffFieXy4uWxvnT3q2w40dd1grf3FDz65d3Kr9nD7dLEdhUd2tgCBMhjvbE4TMh/M58MwnCxnlctdG0+PD0NZ5kx9358cnizn7qMPP8Gimp8ecgTnLEJ2JqNxZ2dNe3nF/tBZzJzqZu5Bi9KN/YQKUxvLsnzl/sO+H3/9o6dA2vdDEbyCjtM0K6t5XY2bTglZRAC6YazKwhpqp+QSI0JkTTkhIiIg0U36FRFENESzqnn24un/+I9/6Xh5kturfmqr+rZEl6DP4w6tdXaWpB03X7d0G9wCaZlSazKzZnTsadVeXtsZFGFRz+70/ScoYdZ8drN5l8yccy7Kut2c67QOxaHxB5KA02J79d589rBL54XedpYAvEorGn1YNdUrf+iPH9T/17/x3/zyumlm4xitL/ppoJusdXP7AAbn0AQEvHW8dITXl+tZ5d58/VGBxrlSQCw5ImtMAUCAAMQgpIoqDKjGOmUFRABWjcIZSRCDiiJKih3ihGoBK04RkCUnIlBjSEhVAEkxI6mwqma6KWqMIXRkvPVBEnPiqq4lqwARKKiKiIgwACCSKiAhEd2gWQhASDcvKaW4mC8ePbwLEB/cfdD215/73Gfu3Tl7+rXfSM+6tE6aUvDWFYG8QWuLpraFFVWwN422JWuFgbMOYw8gqhGJiHxV1qAyX8wL6xdlY5179PBRif6Lrz44WS3SOJYeSYEA5vN5EQoRZpGU0vHxMrFdLU/W6zamqZ4tUo5NVThnrTH73VXXXhujwgkRVVGHCEOSbbt+uj299RaKoEpKPSLtPnnXCh/dubtczV1pIXJ/ubVRGqNeOsvb44Nls1g1q8ViXhSFXZ0sy0W4/eDOw5cfffbllw7qahaqw0XpDPJAEu3zx5dkK7BlP0mEar2WYZApbyWP//5/8G9dXV+r6kFz9P7z52++fO/gcPHOhx9HTjHHxIkMpZQNYVMWaYoOqfQ+Tenlu6vjg/J4sXTCB02F07TfdsF74woE44uinC2M9UVTl1UDNggFS4JKdV2zCIAqi/euKqvFyeHY6bDuu9gezwoCbcoyZ+Ys3loBcc4hqKqCAqgCEosmFlUQgMjZB++MvTk+CqCqclP6CXdDPwv4f/kzf+J3fOcfzMM3UmwVdtP03GAGJeCZhVPCQ4RTZ74EepSHTtkYUwMFWyxcc6SYs1zHbuj3F1cvflUzKHI3bAmJ885Q3l89c1D0u9ytN3maoiTFOo3r/e58t37W989T3iYZFIioVB3rejmbn/7of+8Lf+zfuI8wvf7KkQgTGRZlESKTmQmp6/v9bmetsY5YZRzZgDk8PSACa8k6QgRjUIRVMyiAIqACEKIhsio3YHBWBVBLpiDyCISIoGrIEJaqVnJHmC0hkRPJwhOSMidDgirMQgSIZCwSiqScY+KcpymhqjOKkDh3KIkAAfC3sjCr8jfzMRAZa6yCqGrOmZnnTXP+4vyXv/q1xap+7Y2Hn/vcS6cH/smvvweRhWHadnGcOGXnrSs8IzIA+cCUgYC8Q2NUjbUFoPWuQDRKJKw5pTiNRVEA5OA9ciakPHV3by+FM0heVc3Y51ldq6oyq+pisVzM5wBgyXhP3bAvq/nBye2irHPS6+t9HKY0xSI4yTmNvYyjyRHaK7jedM8ew9jefnQ/d0kTc5yCcTJNhyevjJMAZLEE+30gXC3n89VisVwuFotmsSrKRVXOm3pVFb4qQgils7Ysq5TZGnOwPMg5AUsZ3HxRXDx/5oPb7zYscn3Vpwkyc0yuH3Q+P/7Sl799u98Uhe9T/+Pf/cVM034zPr8e2ikr2MQQYzZkHNl5XVuE1aJS1CJUrjwMYTFMQ2Gp8OQClKHUaVoenxgXVDGUVV03KWdwVsEaV3lXzWY1IoYiWO+UhcgogiV777N3X37r7szR3eODRVUp89nh4TBFMoYzx5iq4B2SIco5W2OnmLphGlOKIlk1Zr4pmA2Z38pjOfOirl57cPzv/NSPLpplHD4WZuFdjJVzj5SbnBhsnQUyR0uNKqmq9QeAEwCQKmRx5sQvXw6z24iUkwR3qAppHI0hcsE4O/aXIbj15TOdjE6yu3gOyPVslbS5fP5L48RdfzFOrDqpUJ6uOUWVPSAcHf/A69/+3X/8j3zpyflmNStuchQZm3ImIhEeUyQilXTr7FhZjGFfyN3D+0VVcJ4ISTUCZiRGDIgkkhUSQsSbIlyzCqtklaQgnKcchfMImghBJIEICCMAoVEh4QxsrbU5jqAqzDdtCBAi6jj2KcUYh5wHInQ+2MKrAVW8+cstoQUAQBURBBQRRCIyRAQIzAIAqqoqJycnP/TD35Wm3ee/5YvBmZw2lnX7/uNZ1eScDchsueh3gxKS8ZlzEQoGNADWeRWeYkbhEGrOyiKEYnwhwmSRGAxmYUWOQEpOKx8EQQRL4FtV9WzXkUI39lVhMzNw5hyttbOm8XWxXe9zDpnVGdf1Q103pfchmGncD93u4PB4fXE+b+aapF1fVc3x8emZDS63fYqT85WFhEogSX21qhf7dkdDdLaKsQPSEAJInIbsizmLFGWtqsgjoHJmNBYkzefzHPV6c5mtMABQZOGjw2VZ11G13e2Hob18fnl4ejBblBcv1geLo5wvft+PfPs//+qTkzszYzjH8e33L3wIMTOgddbkxJlzGnlRhEHkoC4CWBdCWVYKUJhiD11VFsF7EHa+xADAslgUaYyisSgbsq6qjPdNd3VNouQdAdy8dgKHhOgRKTVBv/ils3ffPr93fPDV9z7suv3hop7GabmYjVM0Br1z0zhYa2POqlpWlWRWUQDMmRWUWTKzd9ZZm1I+WK7qgK+9MlscPTf+WAcdd0/ToG52yGkf2SMWSBbAiDogi1pZP0tpRxSASHVSjZodEBEVvrYxXoBaAEJq49QjGWXxftEN3ergTrvtRKe+j2ANK4eihuL1/WUc50OoljqgtQmxAJmIvCgb5IP6jengk+//na8Pbfjbf//nDJnMGQBiit5aQljMahatard98aLvY1MIj8/c7ERVAK1CnsZcVEvRlmSOaJBRdBRBa5yiAFhQBVQFISJQVrUImKbOuUoBQDNzRCJVQHRKOaW9QZM1iUpOQ84ZtDY2WInKQoZdcJ8OktrJWwuQEWEax5va+AZ+MABIZG++1TmXcxLOoEDGHB0cPnn8yauvP3zrC2+WnlQGGcbrjy4IPFLyhkF56Puhb533ZKwxxoYAmoiAUEUYVJwtUmpFo/WQUlYAlqiaJA/T2EnOwinn0VpjLRS1c0VZzenorDEGihDmTcUpB28RsO/Hm7qOs4oa4dFaRRBvTFWSD9pt145MU5T99bVeXsHF81r3Dz7z5vHde856EuquLmrvAmZKbBRCtdIkPKUanEdynkLwZVGBorGzxcFta1wIoWrqUAVwNRhnLDoSZ5xIZp00Q3s9Dm2M/cQxj8PYt1PuRk5JlY1zwz4PewEozi83wxDfeOuNW0fHrz240++7J4+Hd1/sslLMFDOLauH9Deq7mM0W82q5rAymB/dODLG1Bg0y4HK+ApEQzOps0cxDFaY8TcYXoZ7bEMiAtyZYLJrKlt4qIIi3HgRUFQGUs7VkLJbVyb2XXr9z5/h733z9wfG8BJjXRY4jIazmNWEOFp0h79xNKs6cM7MqEBIgWntT5+mUExlslu7xsxc/9rt/IOuSRkj7TmI9jEvva4DCmkBoEOimTQNARAIkohqgJirIzKxZASjHiYHRlmBXQIg6qqixBZIRYEH21nbdpfXCWRCAY89JOUGoZozYb7VvW8TZMFwZ6/r+w5TWLFvWtUJ7fPrlB4frn/6ZXwBEZmZmQnLOE5n5bEaICIioZem9xdOTE2NrMhYARSXH0ToSGRCZZRLOqjc4800iZIAMZlQYQFn10xJXVI0NwqqiAITkREABEAkArCuElVmtKQlqH+bGOVBRNSwCAM47zgzgEOw0ibCPE1jXEHPKOYqwSL7p4wEgcxrHEQGGaQDUnOJP/Yk/8Nu/40vvvf0bKuthfDHlka96HNJ6s/G2JIvOWhSerxZF6Yb+GjSl1JLJIgPnSXOyZBXUkrWO0KBxCDIZBY1ZYgTGrEKhCb6IaWRmZ8lbLokWdfWFz9yaGXGqL909eXj/LHgrIi8uL/ddJzFO4yQqqhlJjYOUxpSSdW7seshSF9Xq1uL41Qfh4AzAKotBD0zN7IDFZFZjCsSgKTZ1VXpLsXPOGSEisaEomtoGg0TOO9AknD5FFVE4T8K83ewMQoojOZmvqpwYhVKMwdj2+iLGMY99sFiU5XqzFgRVaPe9CJ+cHW327dc/PH/ncfsbT8/LYAmTIAOiCIgIM6swAhysFsbhoi5RRXNWzm27v/vwpcxsrWs3cnz7FcAatKyXt6xvnCtdKK1BtopNUVZkdOBpzENURSJCUWWpq5pjBME4parx9x48evTWwy+88fCVO83F1dVu1wVH05Rmda2KiMbSp0MXMoYMxZQUb8ozKVywxhqko9UCpuFf/8nvfv7s104Pvm2///lhejaNZE1CLUCtCKqSghrrnPeKUXQUnVgHABZGZaMSQD2JgyR5Gg2qsQ1jKcIGjcWKtCSpirC0ZKe0s67a77vnH13DaHiQbr33NhiDKpIlDdMWoWG1aXIEJctofLAID159/Xu/YAHQWut9UNCbJmDoe2vsbNZ0XQuaDxfFg3uPqvokRzbGAYAvGhU0WIgAgVVg5lFEVJVzRgBl5QgqXsWooMrNaAcUCa1DIkRCdEQelAAUiUCMscEaH+NIFoWZRQXRkvOucMaO48ACcZqc94hK1pAhJCZVJTI3bbCqfNoAKwBAZm6a2e1bt7//d/7A/+rf+4+OXr5dVEa5cuT56hsac+yHEiiUgagIRWODQ8Q4jb5wZIElhapQSGQkFAUAxhRvWhyQXASXYorjpKKMIAY5paltk6i1kPPoTA3MztqqKA5Xh/NZeXrgttfrqpS795ZHB3Nrbc551+9ZQVSnvpeU4jiBmsJWnqwFbxSayq8ObvMUUZOmCTWpDsYY72vU5GxwziujM0Vur+P+grwxhLYM5fzI+UAGnbOomQBUMU8jTylPvXIiAWXwtuq7aeo2zJvd5hJVUozCGnOULGlMPHK769r9/vD4JEUGkMKEx++9/8qrX7reXo8Mm91+P3GXUNQpKypU3hJy5czds8Ou76xqjrFo5jmN7fZ6uDovHRvpQbVeHp++dA9AU7/19SFab0sjJtna2XpWzJfGF7Q4bG6/fPDw5Wq1Ao05Tq5wxltWKqqFGiUK1toUewCm0Lz82ivf9+br909ODHPj6LAK88KhcspcFkXXtQjAzGQo5aSAAMiSc8513ZxfXX35c2+9+tLL91/5zv3m58cdR62HVJjiFLESUUAyzlnrACCnyGlANCJobAXkv5myDGRH6BwVKKo5pdhyHp2bTUPMSQ0FIicJXO2b+fzq4ioUB0VZPH/+eLsZY5pSf41ZXpy/zZoBimE436w/GdNviLBmydOlcYv57JXf+2/+CVZJnG8QXBBAROdcTDnnMfjQVM00ZTbZEgEYRAdqVBXJigrhTMkZW5Nt0HgyAcgCEJnCujlRILREhEgAKMoqWXLLHG+AegBEMsxZs0qaEFWUfREQ0CBZtJp0mqZpmmJKzvosVJZLAUPWpziRsQrWEhkF+RS1wpsZAMU01VVTFKEoAgB+9Vd/5ez47DP37263TwKNRKF/UWlsfWGLouSM1uqUYlOXfbcvljPRTA4ha9/3rJnj6CwY8kVZIWRVznkCKK31xvlxmCw5RTQlSrJAGKeMphRINqAIskx9j1/5yre8++EH9bwfxT84O14udvQ2XbftNDGAUZTZYkFEkiVPEqdRJi6DeheMoTj0Tb1QUSAgBSULaIwjY0oFVBXvjHK2dkmUWYSsF84gCREMWBDVLEQWmYFFVUADAiJEFTSWvIboSx2xLIgldcPQT2PR1FGNNTYDOWMlDcK83m22m6t+M/zYj3/vbnc9TeOTTTvFZL0TAWb2ziGoI5zNlvvd3oBBoGZexG7fDy98sWjKFTha3TopmzkiCiinXnLXLBbkC0TjqCQTOKE6Fhm9A1VwxqZ97+pC8hiU4xjJGk45ZyjrM5aYk5CxeRqresETPXy9mX988WsffxhFcopN4QEptT0geOdUlFkQkYgQgAgJTVF5Vil9cXTg771sc3eNssHp6uLJ/r1f73/HD/92VRHhm+QLAMCAZFUJVJEABAiNYiBEFQFEYKsABAJgDFrFSfLkg+/b3llb1kssq/764+32GoHy1FnvUxqur56FYqYoPuB+2N16AOSqXfux9ctuMznbl+XhNLyrQoBe4QmoEtz0kUiIIuJCyQDDmDbtOFmJxkz9DuA0ZQmFE4loHRpnbFAAMgIACE50AiBFBQVVVs2KqKB0A2wpEwa0LDwgApHjnAWEEyMiIJAN09Qb51UFEa2305BVgKzlJKqgCNWsitMuFCEB6aCcM1mkT7PuTVOCBACIWFeNiGTmi6uLZ8+fGqTf/ePfa4K99+ClFCdra+63wGycoeCtc4ZCWZaopBBBB4QoYtCKC6U1paGyqGty3jrMZMAA2QrQioiwiAgZdE7isGcYCEtny1CGdr8BJGYmS0Wh+93V4eHi9OzOg0dH+/12vpx97vMvPbxzcvHxY1ZwvsiZ4xj7tktRnCt88DaQQ83DzhgnqopGEckXoAY153HHORKQMhgyKtEaBcmQB8ijck8oBi2Bd2iQ1XgnKSMigliDeYpIjjlOYzuOI3MwGERyGnsyGIpqvWuZeRjHsY8pc1G4wvvgnWZ5+Nlb7z59MuX0X/yf/2MFNM4lliwMCJzzTXGU4lg65yzcPl1N22G1LOZ1uby3PHr15PYbb85O7lNZqzMmqAshzJbgSFFcKJVIQcCws86Y0toK0QkQBqsAaoytF+XqOCwOqQzGuRinG4aQCjf1SlNkIZRcHM1Ojw+ODhY++OWsbkKogs85e+eJ0DtvjLPWIYAh55xLKZHC0Xx5fO8uj30cf7O9vq7mR//0Z6+Xd47RL5TB+5IsIQ2IHskAGGODKogooIBmVAI2mpnQEDlAA6yGC5Od10CKPGUUY6jqtuPm8VPr5wXZ5cEiFMXth595/fPfE/Rot97G0YztRHicZXJqxzEZM2+37fqjn4txC7mOU+vDsileUwDRm5PINzRmImy7vigqR6XVZrm6RaoKLoSSOSMaUFAWFr2JGEVBa8maTznJQECABqxzxhoiY6xBIkQFQDIVgMkJ0TSIxpVkrFOFmLMPM+ObnFNOqW87AhBmZnbWiSizdG1PRvfbDadIhGRQVa3ecKERRAQQrLXCHNNkjZ2maTFf7Pf7zXazvmqnk2HRLLsxTd9435WBmV0VQGHcblbHB5lBrBbzA1OAgNGshmZpimidC4YFc85kSmuRKIBkTgKgiqZsGkQah7UNRFSoTgkHSgEJ+mGsmopZGCaQqBSEZd7My+b68cePLWGosB27u2WDCFOMN8Pv4MzYtcCxDIU11oCDGwjNh5Qyp0E4e+9FEcGJjNZ75WyNFWZQIuuVxRh7c6wQDWt2s1mOsTlcTP0gGVOMQMoiSLYqPZmcZAjBjhHJujilzbhJWaak5XKZk6r6omjGcQQg8jYnc3JwgET/x//9n/VmlnO+wRGdIQSb4lSv5rX1lQ9esUT/8OGdw3snxlhjCMEbJyypCMucWoUpYUc2GFNaKkRQpVdUEBG8AaoyAnJKoMKg1oZpGAGJ0Ngi8NRbG4a+JfLGmTG2CKCQ4tSJ4tnJcrPPLkzvvPfRJMqZb0QvosoiKWVDZK1F0BtS8b5vf/SHvuP0uIKI4z5yXP7zn/768vZseXhCyGAKRMNZgIy1KScmJNWAdEPjNQCUeVQVwhxjNrZAVCAHAqhBBYEZNauOoMkYBbTt1dU4ZAABkK/93M/HBEq59i7J1PV9vWwMQobJWgPqpr53c+3Hd0CPZ34Wx70PFQEqIqgYJAAoQsEM86bKnMqAs8Z6b1xRxGnvAclbJGN9UARTFML2U84UMNraOUvEaRoBFcCoCiKhuym5AQRBDCIDGWONcAYCzgCgaCGEZhpaay3aEjBqjFMeiYwnk2MESEWoFXTq+7quc2bv7JTTmKYbvA2+yd5CzgyghN8EG1M6OTr91m/7wiuv3losZ3HcAU7TLotIXQVIU+7X1ps4RmctmeB9APQI5EOjQMYHQ84XczJFqGesgOAAkRWMKWy1hKJiA2ALNDUgqTBzDrachtGHajabD2NWa2xRHJ/dsa4AZ84vLs7uHC0X9enpbUPF6a2zFDMniLEf+90U49XFdY69N5DH6ziNzIkIETQOIwExZ2N8SgBaIwqo40lZRJA+rYeUyJAwA4SbARqFoIDCPLR7YeWUQdkaKwxIZspChpq6cAFVwJhimNJm0w834N2QYh6mqbu8eJHzaI1bLJaE+sE7Hw5j/O1f+dYxJSLMmRFRFEQVAeiGEmeNAn/+y68dPzopfGmxAPAKyjEh8DisRVnAuOLAhZkakzUBJP00OpF5Uk7OBUIwBtEYZ33O6kPpixIIrDOsWQ2bwoEVMQIIKSclYgYCSlMqSyoKv5zNYkyOjLWWmadpSjEBASunnI21ADCbNRzj5948DRj77fvtRp89H3/mw9Fqc3boY8rCMA4TWUX0nBHRkS2JrALexDAiIXkyLuURIIKyMCOWig7REAVvT707cFQBI088tiMABjcDTTn28/nq8kU/DEQHx8P2aV0QqRlaVWONWQ2pXxzdXz+f+svzyh+PY9vu30kpKSgCOOetdcZQ5gwg3/4dX3Sebp8eG2w9jd5WiBGQkRQtKgKrKAQ0hgCIyFhLRICaM5N1SA7AKBpFw6xIRgQVHZAFJBFUEIUkQEBGVFUxji0g5zQpMhqDvgDUmKccY4y9sxTjlKfRWEjTCJJZIqiCogUE5mzIqup/RxCGgGDIpJxTng6W8926e3D/AY8Sx37cr1ermm5EbmoBFA1mzcEasiis1jlCQutjHMEwWVQ2LBNZR8aBGjJOQG44I2QIIaFFMjUIYoaUxVAJCnGavHfMOSyPIktRFmwr0fLg9Pjo7NHbv/7uqpkZU6bUU1FaS6iGJPvaTe3EpEKOKKt4pU/JQuaGJCPqbBAdOUXrGkTDkgBRhIksqBjrRSYFEGZyNqeIytYHVJ/HhEgcM3M2ZHKOxtiYU1FVjOrW3XrfOx/afltXdoyxv7oOs4IjzhdHOWfAlLt06/Zp2+1T1v/8r/+tNx690o+RiAgxM3vnjo9WmRP5IgR5+c7t2WIhaVBfCicDlGJry8IYEmMQA5GgdQCWJClPQGgROAtgVpkQizT1SGTIcBxjVoCsEpkH73R7fn71YveNx+fr3WaI49jmxWw1Rb13/9bt40NrR1+Ytp0K4nnlVcE7vN5NKbOCojGAIKLWGBUhY7t2XzdZ8aq7HnTED3/z4/UQ7pwt9kOPWHrnFZSMQTWgQKYAUBUFQ4QIhADKnI1zCAZxCYqIVliQDBkTJwYFJLG2LgonksTuS8IYr/tpY9H6sry83JvSXG2Gi3/5LgFmNqFM+8uLenYXXE67IXV+u1V7aQ9uX4pISn3WjTGGWUTkZhKmoOM0/sxP/4vFwj59/sxq7s3zs4NbqB2aMksObq6YEKsbCmTKalxQZkQVjcY6zkCGRABQUVkx56zGGc1JwSRGRxhj66hB1GGamHvvTKgOct5KirF7QWhVY2YyFpmTuVEe5hTzWJVzb40CxXFQBOusFZEbAg0iMt/wWklBQeH05Gwcu1snS8pm37ZD2/KUOPLBQROHnBMXdYkGbVAgsMGDsUiiHMFYBc4TIXoih1YQVJi9r1SByJDBNDIRpDiSGjIDYjLGCFASVQjGobcwTgNqLut6HCM4z6rBgl8Fj7Lv9nGMI0/kgChwzqBCBsdBNKUQSh9E2fQtz2o0ZEAB8EY2hzf4JxlQtXmKRAEBkciQN9bkOHKOoGJtIaQAQmgAMgCokDBYV+Qpcs5T3/uqNGVFylMaqno+W3SMuHm+ttbFxJJy09SE5IyP01TPZ+2+reb1btsersIsmP/4f/nH/spf/fsIqAo5s6qySNvtHhyv5sFDTscHs25zXTQ+9i2SGGMVBxBPkg2pgsmCFh2IgCgSKbB+Km5lBbhh6qcYpxydDygjCOtEY7v+2q9/tG7b9W5I4Kbkt11vbJBJU+Krd77x8eMXX3jtrChsCLjexPmsuHc6f3bVe0uhmPVDG3MmQwAgIgxMxnzXVz7zo7/3Owo/XH/8UXe1e3Ed3nm8aWb+/r0zH47QOMmMHgBJgVXBkFOST/mxn0pniAwyK9qgIoh000KyMIAFiCmxsV7BWFewACu6sDKJu/V2mCaDXNeFmr7di/fFdr27VR6M4zXCPVWw3g0C1fK4KstpjzYcGAO767cz86fCWSVEVJayKhCJ0F1d7w8ayx21/bBYLYAUiYaxBzBl5RV6ViRXCGTQDIKGbgAnVkFEFFVCuOFMpT4RqQhYY4dpq6JKbYpsbK2aWKe4v8ppL8zGkuQY42BskSKB4jiMwBwjh1DklNpdq0hlKDkzZ7FEKPqpltAYo/ppNY1krtdXs7p2rrjcPLv/8BQ05pSNnZGmEkcepph4fnAwTXvnPZrC2EBmQPVINQKTURFEZJYypcmHJRIYNDHFHEckC9ZZAWtTGgUNAigaAulERxcqTimOQzNfTRnUwND389VpO/TX6/OFtQb08KDiFH2YgwpzzkkM0Wxe7683MWf1SKA3w3EWQARrnUJSNSLZGK+KxtkcJ1AhsioCQjkLkCWClPeQJyKUHDmrcygySSYgEE0p9pxFFcgEFmbJlkyKQ9EUcdv64Jaz2cX1lkHc6KYs5cw5P+ZUppQsWGGJ4i+v18sDSZwJjQojmTJ4kezIoIA37mBRGZymsSurObPJUbt9e71+dnnRla7shzhrbpEtjk7rgzvHZAtDhTIgKEAidEBWhZUjolqiqdtx3D/5+Nn5s+tdu53Avdh2hszJaXXr1v0H9+/YunDOG2O2Ly73u+3zd96eqtoXpXFGI1g0zNFaP+QJAKwxAoqEnGQcx9Wskl13/uGH82KjGL72tR02x2fHx/04ADtlSDGFurYE4xhDWScZyC1zmoJHZkSyqJYs5TRaW8YUjXGQFQ0CEhrktCOL1lVgrMUxpexKhKFMcWzCbZqVIpfbdJEzkwZrsR+zCLZtd5qPcwZEBwzCjOT22xfWmOOHx5iNskGAGwmeqlrnvHMKaojipD6UV+tdXc7U6JDyvGqYuSpmMbVT3EjqFY0vTjUbYwyhJedUAQhFPlXvKUlOkzHeoM+xy2nshh5katudMWHoh+uLi+PTM9bki4qMOF9NQ+t9ZR0MbedCPXaZyI5j9GUVswCn+WI1DgNnASQCtHCj/FVAJCJiEVAQZeFsjAGA3W43Dvh9v+M74jRK2ksrNnhSMqGsqlrIAoZo/KwMPE2ATiEL5ymKidk4h86KZEVGzGlKUSEU8xw1T9cKJAQpOlXjPYKgMKD3DihzKkPgWG1fXJCD2f2XkXW3Pt930Zf+8vLcl0VRu4v19Y0Sw5DZt9vFwbzb79GaMpScp6Frm6ImpDylUDoiB0gAYIhUooJTyQDCSdQqAQlkIgOKnIggAAqnKcculAegOeckSQGh768VMcZY1FXiFEqHLMOwjTFeX7eQpamKDAgIbTd5G9I4+KIuadZ17Ww+J0JQk6dYLBcn9z4f4992Hr1zzlLOqQ7eIHZdfOUOPnp0H7Qvy+aXf/FX+r2ZptEYv+u3PZRh5ubN6r0PH986WIEz28uvHz04nC3veT/L056sqCZDjpXJWp4mUDTkJo510zx4ad7H0ZeFUjA+Lw5W3pUqJJq88THGpq7nVXO0PHrxyYfDMBogW/uqDcu6XF+1AKQAIYRhGplZQX/Pj/zQxSfvXLZb5aw6f/b2x+vBct91WYckVdEoJM7Q79ex28Z2FzP0U56vTp0L9UFRBALMZXOSU0mqOU6AGcCpZskZBFUEgfMk4/Q0j127mdbXm6aZFXVjLDnPL17sDg5uzZZ+/fiTKWpm4ky7tmvbOPG/uPfZl1m3WRRtuzir2mfby/OPVndvoy3TOBChIZtSQoQYo0HrPUoeRe2Ti6vDmaHgyRab3U60rSp/8fTZ1ENZFePYpsjj8A2CumkOqmZlfKoWjbMzRGIWxOiCJ3EMU56uQfLQiSf7ztu/tt9uQxGcL6yvnj/fdW0E07Zxe7qyBsmZYIw0y1VKwjkDkC3qdt+SsU0zb/vWaOiHtqwqVrE3zhsAcOPjYa0XFlQxZFm4H4YH907W1+v1futwGNbtEh142+63p6e3+hRLX4/aY8ppvAKoCczYts5OvjzsdzuT1dpKABDcFLfMav1RN/WcYwajI/vS79t9oMCp9QHRNIY8sgFKfddnjvW8UeBh88zPF5WlXraIJ3EEEbAVF85UdSEsu+0mFPaGAaoilqpp7HyYTcPeOx+MchbVSMa6UANYkcGQITQCFoRzioRAN55B3ilkAMlj4jSqQLKDMkviFHeaNSeME7hqNsI45f3j914ktO+++3g+X7378cd375zM69nl+mqYxrIoFDWEsFtfhpJC2SiCDb4oGwWZpoQ6oCFVZWZCqYKfYqzKwgDN5p45C9Pu+QtTHL7+1mt+US0OllNOhauenz83ikokU3TCKA0ZpyKZBzJGcrLOAhIwsyqgAMI0tQA2504EVkeLUFY+eCSwoUxTBGEDicdsEQVyisw5Lw8Oh8dPyLjLi03XjfaGIS/Awpk552ytRTRvf+1Xuqxfee3W4fG9/tnHQ8JFVe2mhAnjlIuyFkkAcP34Q1uv7r/xZSRPvo59l9tdd/7xJk1M5P1mvjyuZ6dowHgPADkPIonIqOjUdTnz5ZOn+3bTzObHdw7C/Ja1NhSliL66PFGOu/1FWZZJcz9GUZnPzcXV8O670w/hmKZssATcUljs+l8zgqqSZQRIIqqS8VMBgAFOP/lj3/03/58/7d3BrpsWs+V7Hz8+PJq//vIhd9OTp1fBz997/8PNth3zeLw8DEUzpfOmmYA+ef21uwBDM6c49aK5LGfCzlgztM+RbOLdsMsfX66vt9Lu/MfvXeyHkUWPG398ML/72r1VccZp3F20oAPymLIxRoTZktvvurJZgCKLAHq0MHNlipFE7I3nxjeVgzfoKyKSqhiiGCfjAhIFE6ah/+CDF198cDvGXajDZtxerfe7D9+/2vC8ru6fLg4WASBPe6oXlvwYVrcAoupeIm+vrn092+82xm2fPrkWMYL2cnfhnb21qoYRura7d/voeIXV8iTJBKDoDYkhQsTA/Xi9flIdH66WhxfrfVnNnz55Vs7DYl4778ZhIANoDRlL1hnRdrfFZIxy5V1OUxGanMVodt6ncVC0ZACMsLJdgayTUZ/HkfMoOWm26D2iQQAkh0bH7Q4NILBmnjhmcJf7tbQ4DO2u2zx7fn16dsbk9ynffXDr2dOrr3fPjPWC1A9DOwx3T4+aqhqnFGoqnG93e0bT1NUwctevAdGQMZYQtC6LNEURuX/7bHX4EgJuLj6Rsnjrc2+5AqP0hQFSa8A8uH0vj1uwRmJWRRDgMQJEgoJQFTHnjGAQjQhLnsi4m16pmc/UW1+VxntrrWaWmAyiIsQpqwCSBXCgZNAMsT06OrredrOmQRPGFxeFd5v1Dgk/pS4BiOTLfQ/omsptnn+AUytgrDHWOJaRFS63zyzdX2/efeVL38NUTmlyMMa2A6GJczi5o/v1MIkAcTasYkkNucxZleKYq9ok4KnvLh+ft/1u33e+mB2VlaPEUdBaQwCiZIpHL32xLp69/d57yeZBpimDI5MEDB1wZnIcY6yIF8tq2OWx/7AqH6k5AQCBTymhxphHd0+1H4ehB1daNC+uBgCTso49oxaZHY/59qOX7gBKon6/ef+99y43/cGiX6zC135Z3nrrlMwWyZZVrYREIDFJNsKSxurF+UUckLKpQvnSchnnMF8dvPalh8vDw3p+MPRbyS19Fqfd2O7Wu+uL7fqqKhejsqB9/vyKDB2fnakoGkgxO2ONTRYRAG+0E6AooDfuHAhAqmKt//Abj6tAH733fvCucraLqbs+byfdd/n8or/ctnVZZ0nvV+XnPnO/8GW778Lj+C1f+WLXbsq6ICzWl7v1VndPPtl0+8jjJ8/Wuy5GRVVdNMXjZ/b1l29RMIJmO6XNsxcnpycoLQC4oszDxHkkA3VRTi2AU00gPIXCf/zBJ0dHR2QJAUJRDKljYRWIkavSX62flavVjURSGJw3Keb+8ury6dPZ6mh1dmvXbp2l9pNPMJMNc1JfhkI0giYHYmxFRMaRiAz7jatn2rYfPv3Gh4/PxWLW4nrfBmcTy/0HD0R5MSvKsjk+Pv74owsG2w9ZFbw1VRG6cRQAzTz1ky9CM6+JclWX47gd0wQ305Ipl95t9l1R2pPV4vg4SBqGOPj57OjeCVCv3DhbTV1EsgyXxs+URsjO2jB00ZhMYdRkOHdgnaaIvrCWVIFZkGBon+do1pdX1XzuCR1Q3Az7bl1WVBQH1mGWJJyENSpaYeFkrTWGVKEqYBp5u19nVk7ZGZPlhvmrOd8olhtj4LVX7uD4yb69rOr7ojtu5cm6JUMH8/ucpVm8GjMTbHWIbIapayUVztg0DKYKpTEiShZFJwKb0mi9ZbLeh+vL87KYkzFj3ztXBh83F+t+N8zmZVHbelHXsyUnyOCncWrq4qW7h08qPH9xpZ09WNjnlxmdjbFXUessqGCwvtDdegolJ97fQD8EKMIG+dVX78zni8N5s43JBNMNwziO20333MFiCccPTucHt2tf5cwxR+fN537bm/ur8+1V3u9Sae351bTk6fDMKk6GCkTIyiogeRy7bbt9bLyq4mxWzR7eXx0si7klnCHC2F55R1kkTomMucmnd+99dui2OiVVNYac80M3IJpgPQHHNMWYLIBR5Zvr58aeEn6rqkYQlZw5ESrA2HbHR6u6Obzc7p+/2PRT3I/JB9fFCADP9u3zf/F25dzBsnz13tEwtAaRbEXk1rsPnz67vtjuLnftmFKfIWXx3kpKi7I4Ol5tRj5aLEzwY46E9OE3vlFZv1p5sN4WAbPp1tfGF3UJWXjqd1pUzhkRygwpjs76aZjIeM6IjpBlu76umlI5qQXOMXPSPu53m5GNXx70YwfnT2Omb3zwbnfVHxwup/zk7Pj08GgeU6rr0vqaNRtbg/K4ux6nYZj2Y5d/8+l1yg6YrnfrrOJcoTL1l1Ndwb27D4h4t9289vKjd957PMU2JhZOIrqYzb0t1HEdColTsSiypPffee/4dI5IBOidyzHeFKWr+XKxtCG4MXYx5rPbhwiSJwQnVskWDkTVzjiD1cR5VOgwtypFSuoJhDvNFaFRgMTJoCUEFUtQ5NgLM4sozbbnV1/76tf+2s/+CiuyqorcW83vnNTf8z3fOq8OS0RjMMaJU74xqigrf3pUr9u1Ia3KMKY8TvEmA9dVEyP/xI98AWUTY35+RaHcGVuoDsbZrt9PaR/zsbGW+91+Oq/E7PbxH/6Df/LO+f7B2cnxcT2rq6Ojg7uvfs56JUygCcERgsgoY8u7/ZSB4y4p931u22m93V5e7+/dOqtKDymFuljU9eJoWfiSvKuL4qCsx7LzMsWsde2Gcbz+5LJZNSJWOS1O33z27O/wMlr7KprmhvPvjLHWfPuXP7e5vjpYzI4Wdb/mxOzAsIpztqqL5ck9HyrNOOkkwrULMWfnZs60RdiLM8xaVA4AOI1ufoRgrZ2J3TtXpfZFbK+PD48v1/vDZZE5F9YQyrgf6kVhTBmCU80GgokRLIbS+xBEEpAvyjDt+uXRUd/1N7OUaZxKq8aaeemtghKZG07jjaIQEOGbqgZWUdWyCN1+4DgezmeCObMYA3fvHlXrISt029112wHDvK5YpmnE+XJFmBgMSgRTvPTa6fKw+G/+0VU3RGuMVWWywxAdwXazq4PPWZySM46AC4+cuOOpe7I7ODwoSzNrZpZsihOn5Ivywa3DF5tNnMbjo+UwJW9Klmysy0mNscJqvCsXje5670rvaOJdSvnyybNiNRPWzcUuc7Jd2q9bpWrU7QfPPqmbov0IXjx/cXY6z5wFjXOlL5xMCck0y8WLF0832/2YUj9EUK2L4vTu6Rffev3s7q04jVfPz8f4pCz8rDnY/uoHq1mdWaIMnlwZKhE2jtoudXVfFLNuv7m+3OyvW+XT3/mDP4iAKSXrLAKWjnRiZXKhIITZPBACJyZyBHaMg4mUy7F/+vHT9578mf/6F8iYw9XRV9767Jv37p68ehTXe2OcK5wiFCYAYtacpzGnQdgNu0ESrp++4MdPHq+HD9f5e7/jt33vj/7w//v/9Td/8Ed/+M/8J3+WO/oLf/OftX33g19483d8++em1Ko6NITGOi/zWV2XI3VjZXI38I2lo6gczf2dW2fjfjuVdLkNxi+sJ2QcY//iah1F2mkDJgOZaeoh52fvf/j46f6Hf/9P/kg0fdsy5uvNLtSzPO7QVMb6zJkMttuOx5H7kWMeL38NafH4Yk1k17v+27/rezBeaT+dnd6+Or/EQOvnF1dPhtnBwXy1kKyrxenF5aWZNfu2dyb9y3/6G/NC+k1PliV2tqyjOUb1Xf9svrpHhBaNgJTBllV1vd8WZXhw9+Qbu+cokDgj4H5/xWZeV1VMMWVnvbPOdnmfJs393go0btbxxWa99h0uD3MzP4x5VxVnIozkOPaGvGiRNNczMmKsdapwdXGxvHUrTiA6xGnK3eWw3fKQu/1wcHQ6W55O3VCWnqw1RP3UL+bldt2C4nJ2bK0iaJom+6lpDqCiqgKiWkMpgYIQGQSx1nHW9XU3a2wI/pMnH9XlfPXqwX431iEWRXnw4O4wnHfbwVtX19W07yAnoLYIR2jEYJ9kmJX4HV9++evvX9pSNJmiqaxxFMx77z99vt7XM7s6Ogpl8fH77927fezLmfBYlouyKJqqYMAI4n3I3TTuB/LNkc3R8Zh5vWuJzBB7AgXlsR+NAYtclqXyDY9cDGHcrouj4+ffeLy6e+fOvaPtdp9iau41CLGpYb++2u2nxLvNJNO4+9JXvhRCMV+sMikWJu8n4RS7aYxMSKtZvTpYDXH6F7/41b/6t/7B+WZdNw2oHh+dBNCHh8svvvmK2Y7ekiO8UahZS1fXmztn9/Z9d//Vl9/9jV9ZhFXGKaz7Z++/K8KIKIwKitYvZ+HkyM5qP03JWGudF0RC7NudBfjL//U/+Nm3356vVjHJH/ijP/Wrv/DL89nq3effKEiS7qoqOF9WCmXV5Dg6X0pKIDKNkTi54Nq+L+ezYbttvP/CKyepwL/+l//i+fMX/+H/+hc+/8qjo8WSVWJMP/PVr37bW68s6qaNvXUuRuu9E6FXHtDji8uI1lLOqjcmbJfb4cnzt//EH/lOmCYde81ofNNdj+v9FIIf++H500v7bYVzBY97GePlVX/v4aP3f+VXl0d3x360HvJuu9teajw6vHsSijozWyAElMRT5MtnTyGUu4vH3vknT6/efOu2xE3pVlTtrjaXl8POQ5XITZzH64t6NQM04yCzsvzo6ZV1WJrm4/fe/czrpzzmqqDtNVZz9+Azb+xffF1xEMbM3NQ15/Ty/fubqxeFq24tbt39/Opv/+L/rXHuBq6rVsujWbG9eDZfrYjj7vycfFEf3HIV+sJen1+hRWz83BwWFh1IsIXRG0e7xHHQGId+8qFSpao82O4ulXFRLmaLypMAtZxovd019ZzK5bq/ME19frnZbboHn33EnFIaD06OFjL12y4VmlIax8k6g6Bp0htTO1RUBEJUBUyJbwCtG3Arc84Q2nY6PZ0JaxGaFOXJe08Ojw9+7qtvtykbgNPV8l//vs8P4jjFuigRPOeiqIkQchY0ldq0Wrizo2mz6X1RBmN/9Te/8eqXvvgbTy6aVf0rv/rBRxd9t9/+5O/8ro8+fvzZ1x5mYiTfd3uDEaypyyYOo4DYUELuk9EqNDloRP3gw49Wi9ogWnfDFklKYv1MEQIpqQrSwIy77d1X7ibAZuVWB2e/+iu//Ff+2n/70fWuy/Ggrr/tM6/2/ebHfuT3Gp1GCDalvutCMwdQXxQZxIMvSjiYKzM/P7+oimKxmP3AF16rDo7+yn/516uyeOnslg32G588br/6m2+89ODIkIgMCXbdvhZnjZ0yz6vm/MUlR9OO+3zdX9Gm/8b7/E0ijbVEAKuZO5jNjINVvWBWyaIWcs6g+nP/+Gd/6fHTeb341m9/49d/6Z2f+ft/9+sfPfnWL791++z0/msP8sXTk5deG4Y9AjNPCoYAOOc0Tsip33c5s7O+nq1Whyfl5ZMo2iXzE9//fTlxs1yM+040ao6bzfq7vuXVjz7+8Nado8WsiTF6Z0IIxpL1eDIrL9oUvE1TEhFrbR2as+Oj5epw88njYZoWi6Or8+txHBez4vFVC0Sf/7Y3wLiU+2Bnb//61+r69Lzjrz+/vvrND85frA/mxWcent09vd3Myt3zi1AtDAUWRYXMY3/5zFL15NnlpFpU5a2Xbz28/xqY1Ef3q5vp//Ff/c2z1cFiVq3m8ziNZ4dHWZ+eHc+9g9XB8fZ6v1jMOV0mkqltQ1GqD91+P42XzeLu9vnbDu56f0ZIzhEo3L59+PyTZ9F0abNpFivu9rBaCaiA3j16cHhUtzEpD08/eXJ2/7PTsP0bf/4v/coHz7eJi+AOFouuGx6ensxc/qk/+of2+2tDFSpwTjL2BCBRrC22/ebodDWv73Tb/ZNf/efGh24y+ziJC5+cX3VDSpIWTdjt+6PDI06Jg68re+/RIdlghNxx3Y+PQcEZzSl6QgtinXU5Z1BQEET6rZHSjbRQAaZx6vv+7hsvP3pU755Nu6vdxR4+fvb82TiW84N/73/6R/53f+pPf9+P/9A//Pmv3ardUV25oLNmxZnGVkKAFNk6Y1HF69FBsyjt5bN93unv+td+R1HX//CfGZOL45NTAJwtqu12/86H5+98eP4T3/cGWBKCxLYuClWeprGuynbXEVEau7oqVLUrKkkRpYrCxhhjLSHWdZi6vvSOx55soaJ5HIt6PsVcOnrvn//cX/67v4Cu/D3/gz/Mff/5b/38n/5T/8mtR49KnrrdzkzJNEXisiYEVckGBDSp93Z7uZniJA7vnB790td+49/6H/3Rj158/Gzz4ju+7Yto6Ozg+ORg9cZrp3/n7/3M4aq+e2v1sJp99evPzg4PY+QQwn57XdS3LKEHnAf3fJgY+Pw3rwS0rqoU440YtaoBrSEiJCs5BudT7DOnzdU1lvBTP/GDi6OjzeX2rR97GW1MMS3nc28rFKlf/lxMnXNWOJNBSyZPrbASStx1zMIci1CqTG3Xrk5PhOUILKKJkedN3RG4sELVk+Mj58Nm0QDj9fqiKisFI6Un9MbSd37b5/7G/+en205FjaqmlL7zt71aObe9HKZxrEI59HsR2XXpeojB24v1QDAqT8EhpOFF2/zzf/4v7907+Yk/8JP/7J/+k6/82Ml/9r/9C2988eGvvPfOdtd/63d9uzIyJ2MUlSwEJL9r10XRkMhiUdyryvffff/yxeXv+eP/7i0e8hj/7t/7b4vF4XoCTmZ8fvVL737yx37y++raxmje+OwrTz56nFJmRk7mut337VhX1YunT6vZ0fHtN4rZanP53qyqPcBXvvzG2O7r2n/59VcDltvr3Uur1RWgqhqkdX/NeFiWNrcTQvin/+gfn7+4NvXsO79yeufh3caJA7tcLnIyZZAkA2FGCJpFgfPUtu0Qqvl+vV3OKm+9Cebk9MHZm5+bpilxoqTbzfqV3fX1en1xvXnng8d1Ufb77UuPHqYJkukw10kUCaz6g4PltV6r5OCNMpAzNsbROc+sACAqhFb0hsshAKCiWTMSXl8/m1V3Y7nvxvGjJ8/vHh48fHD37zz9F3/h//Dn3nzpgW4ufueX3xzHtt3v58vFalWWpfFF2e9aAEUwIslana8Kc/fe3UdF+2Jvt2Z6fvEHf+j7xZelc2io8QiyfvPVO6lP5+dPT48tGOuLklyheWwWy/1mUzZVu94vZotu7IFTQfBP//E/+tEf/TGwyKzOFzlNXT/IOBXWluUqjW2cJlYA0O3jy5/5jXf+5cfP//Af+sMX43T++PzZJ8/ff/ejN9787Pf9rn8lvbhon16dffYuWpI0goCFLuvMujJyl/bTxAny9PLDR3nff/ubb/DVi1cOmtvzeZ3M2emj8eLa5oGh+qM//sObbk3BuXD4hrjNtlVL7b53wa5fnC/dcVnPdR8f3Tvz2xjaCQD2bRuct86cHh2enZ0F3xgTkKz3wBrRWB16hPzWl173VYWYF/Wyrg84MudoMKfYg7HGZEMzjqM1yGN2wWkGh24a+tRO6KwxPiY2aokoTZFBnUFC573JOVpnQUSArXMco/PO2aqZz1MaDVHMHApXUdVN8N1fePXv/dL7fVIQCCFcfPj2D/34bzNp+ujjFwYOBMg5Yc79mDjnoWvvLE4MDpJzf705rNO3f/7k0SufO//61x6dlKZt/+d/7Cd0zA+/5e7x8a26nrfbddXMiGjsIirmaeKoAn21nHGK7S5a7V753MNv/PI/KmaLV45WP/aD35OBFr4Y9u1HH30UJ7M+f3ylXTU7ItWqBmc9KMQhW185F7IM10/jq58tcnXXhZdDDd45kfjwwf0P3n3fB39QNWbkspn91E98/5/663/Xe68iLz+8bx2mMel2bJ+vgy/e/OLnbz24W9ehrmoE5C46RVNW2eY4dpxFOBlX8tCjQllW1y8uqno29S1LmvZj7lWrJJrLqmSLq9tni9PTZbt5GfX1N/cWcGx7Y6yhLoTbU98bS2Vj99srUDtv6rGLOcWcIhFZIpP50wUTNwZ3iIhoAFRUiIwzhoz5wd/zvaV3AKOk9Maju2+98pmU4h/7sR8FTxUVxEqAneFyVQy5G1Nf4VxZDCEigSiKElmiLLHX0kEYgAmAj+aLJFKXqIhoDOfVyWouR+3xrTJNU+4m4woBNXamOSIqgDgPU9erTFVwvcLP/+LbP/ETP97vWx+aLNw0zTD2rqrgcgcBxnFIY6zqZla7Fuy8Wv3Jf/t7VovZZ1f3f+PJuwTb49nJ517/jN1c5HF/enclqZutZtMOxti7sDSWRL2zput2zvpQlycnx3IWinomoohQGvjiS28UweV5PfW7brfd7bbLulkcHn700dPSWX+47PrkzChACMpj5EkWVVh2GipYEd+Y1Bgia2mKKYTKGsqSScG6IDyhGcGa+tat1cGBdSHFwZAd4xoDKiZEH/wSlIAhc6+S88jGWU6JGIeuDb6wCimrCvgQQMQZ8iEoAPpCxcRu8EXBIlVVj+MgymSwbGbOVILJU8ldBCux68hJTP39e2+GX/1gyHpDpP/eH/xOyoPk6wcPH37w0TCNe+dCP4516ZfLxYfPz48Wx8pbdPPqED53MDOuBDMHVxTBTUOPopLFu4KcG4fe+4KAQAABmPtpTGh0Xi3KohzGnkmWp4er1byoGhNCdevs9LCWKZ9/42kPSsenL99Nn/nKZwEQuOguN1vZzJr85KpvB6khCokJmod88fTp4d17wntJl/uhf/2lO1/9l2/3Q3fvzpn3tp1aAbn76O7QtQKVZDGWOY0Ehov2c7/9rSQJYJby6G2Yug6Z26vr+cER7KJvKsLKhmwA8zSmaUSAOEyLg8M4xqqZjX2f+1jeWuzbtqyWUzeRTuNuUIe+XkaejleHw+66Oq3MEKv50X7bl/WSWVDMbLYU1qkfidh4QvTWeXsj6P/mGElF2XyqzwQEYmYA5TRpNi8+flZi8fDBXevKJKlACiPPysYUxMAx58Ibjrmum6NlbXwpSS2GlHprrXFzkcFb54Ibpl19UEPO43XnUuua2hhiyQiieRRMghiaA6VNPZuFuhQBHbNKNuamqc4gakwAJOLt7VuP5s/WM5cHN8vBt7vOBRt8SbBh5uALM6dQzkB7HMYf+Td+V84xJ7l+/ngx5B/58rcmppoMY3AL7wuvxgonQx5M0sSKCSIjqzFmHmqxEsfJeMI8ebIUM4EIS24Ha83YtSZFK/HkaGEtnh3UQ6yvd12c1FvbpzwOE+12xwfHjQ26iYeLgwNnbxyXWSQmfu3uYhEWZCaLNaLNPCIlssW8qYlqMghqEFAErKl80WCpHKdxGsqy4Jzjvi3Luh+2yAqIkslSaK92SaltRzBQFzbHbOvSOKLQIBaIEMpKOAcLApN1mUCzsDGBEFhIBNTauLsufdVvN5qki+dv3Ln1y0/WOeWUc+LEo6jG86fp2Xl/ctq0+1xWhZK72q4fnBwPkZtCc9y4ehanPjNWpbabc/UNIBpjfbMAFFLSnNH5zBkUrDEx99vdTkFTVMFuNp8ZC+WqBAo5wTDtXXCFUi7o7qM71lZaLgrbsSiB5sSIcYz9SX3y9MUHL84vjo9muzbeOb1TBv7lX/xn33f7xzfrX8PdhYgcL44vr69jzl/87Gs85IJ8Xc6mSX//l9/8O+8+Jx2rEOqyzGmsTz8X89YCpvyuxvn2elPaxs6L1a1TU4Q8ZiAlyNY61aySDEm3HZ33OWtR1eOwnh94mVmwvDhehGLGDOBNecIW9ep6XdjS+HC0uGcdAfQ5TwezAhBzzMoTiN/vO0I0SJKzMQb+O5sZbupnQ2BuRtvTNJIhIrxhRy+qZey7drtrqoN6vtTUVdZQhm6/XsyOvTMyTvvLjTNmtTx1wVpTxGm6oVyLgnI2ZDRH1djUcxFgF04eLTlFJKeABoxAJA8EN9ZnEsLMkAVJkDMzI1rnfOynupn3u37o+xElFNW//2//ZPH82c/8rX/4LX/8p1RiFqNCYxcLZSOgANZQsAZw8dp3nzpTeFtqRfODU4CkmnLKMGUQgCnFacJ5ZYBi3wcKiMJ5NAiE7mRh1i+2TT2b9p2xg3Y7VZnNFmE+k2AsWWStqjlEVx8s3AxTN946OHv2YmPyDnIehqGfcijCi/Prw7DcTe3dolYTGOVGLGaNYZb53KFkJI+QlY0a4713oSJbAhIZd7MpS0UdBSSbxoGsDbYkgDgMKqrMmLMKKAZEk6fBGudtmDcOPaEjBMMxGfQAXgFBwRhENUgEqoY8ADgDpEZESREQgXOwjvMkWS2FyPHo8Kh/96l3DgAK6xPvpt3a1PTK68dDNw2brqn8btBNl157+X4TAoAvai8gTXOqgoawngVmNmTVoMYISkLobMmZCW7Sb8aMVb263O+qWRmHfWEtlsG7pqgr5uTRMjNYb5nAkyFnIOdonLWcE6dp7AwZn3U4ntfPd/LkfH121PRTl2Jazu6ef/TOw898frv9pCiLbmwF+a1X7pcQQYxyjpFDU/3u3/uv/sKf+S/K1eGsrsb9zjiPBZXFAg0FORakQyqZk04T5szMobCWDPCoGYy3Bl2KHZHJWdBYsL6oVoqQuSuKufWLnFpjnaRIZc1Mq9MTFXRoGBg4k5k58L5qpn5PPuboCbUMKaYYvAOg3XbvjLfwTQmwyqfuQKr6TTIWAIDkfHR0+2RVXXWNM74svYWBSpMIgisbf6gInJMxwZCvimCNNxTilMe+BwIilwCqeoGcbWhS3INFBHYu5JhYjbUGFBAZebCWVFF49K7KQsAoSYnQ+6BsN5eXKhFa3K/3GFzfdy6UJsbn7/1mDibImDN4XwiL0xHUoIIN9dDvxm70oayaqttvq2ZGn/K+o3DiQXiIGEUI6ltHSBrb1puAMUsvFAox4m3oLluvBUSofYUo1lvNyomH661Rygpj1znbMFuGMbZ52ayGfV+IsQyYNViXhNp9X5QNJlnag/1+AyOsVvdFuAyBEL33lW/Wm6dHx4/6fgiFeLfw5Yp5dMakKQFnNAYVASXL6KAyzqjJhimO54SuKMphuy1KzxOjcpboZ8X+erPfbl1VeF8Mm6FalNY4HtgCo1FXhDwlBCBGV5Rd2xahzjwpAlmrDMrsrCE1fTcY8AwxDxNrjDlWdc0i/dUnobSKKzfTPDIZ3G7G6yFedxgVv+3Lb4pMzi/RGmdIMnOesqozzlhri1IYUQ0hcBqJnGQ2N6aNCilmRbze7dHg6UntijI0jYCSIePKEIppipqyik5DL8LQ9qKSjNMcecwWAcVIygfzqk+sCsME+/1QltU4wMfvtIe39+XqJQMfFN7uezo9OSG1SKpZXTCg0A6Xf/SHvudv/+LP8/CU/KEL5IxmBgKDYC1SGnuDYq0HXzntPjXJZiQjoMSxZxYFw8wIjCygxpDxpaJCCMbj4sak1qRRKSMXZEhYDBo0qFkRwtBvralBACDFmDPjuG8VDaFdzOd9N9JvrXNFQgVW0BtjgZv9ZgCAZJ6fP96ef6OqTVXZvm29d8aYppo5Z3naw3ht8mba71RcUS0QeBqTZCbrDGiaRkTox17JKGE5O0BCawvU1khvuA9EBkeDaBGAmTQZxGnYYO6KgAgOpACG2Lfz+SyEOjP4ukbQEJo4miJPV0+/cVLN4Zqrng3h5uoJ7z4x1hqPADBfHNXLA1uUOYn3FSfmmDgmjqrsJCchkHlR3TkFBMhqmCxYnhSSIqA1XlM6qO9KH/urvn+2y9cdiVUiUTG+pLpmV5jqoDo8PHp4cnx2fLw41UlxhxolpTxfzKZxQjRCNMSp21+ZtDs8mKcxPru6WtYLUrKGrrdbZ/3h8ghEnfU3UmpDxvkDyQaUFEhFCNhbV7gABgjQRqSUDTvKmGP0tuw2I6hBa0pXgGgZgvcOVRmkXtYxJwDklCUlApTMCHrDOJ/63lmLwDfiijiNqizCCEZFyZokQztsfCBL5Iydxo4I0aJzC1+VhoIqGcqnx/OPX8R9z/2Ym/KMxWZOAKhZOCZQ9KawtgjFgsCQiHMGydiyAABnA9kA5JGKPApkLUMTe758MWXQ3a431jsfjDECWpYzX9ZkTVk1hI4lSowwDigTik59nMaBgJHhsAj91LdjbLtp6Nsxtrtu7bx1/uD26Vmv6fbp4mjeFM4aa9AI2mQsexeOP/vw2xaHztwKpjSmQQjGVKqknDVHR4AiQEgImjKpAUVjraUZKKY+S9IsDIjWORU2zqE1tpgZa4d2n8YRVJwvEB0kiywyMoGz6FCNtR7JGCpAKSf1foHkCbWcHZJo3w0sSs7Zm2EvkbkxnFYQa5wKg95YvQOjbvcbR8+b5beAOhPONxdP6+rIuYyIlmzKybvKuvbwIJAhHyok4pxzjGMf0VhOGXIU55zzaBUBc+4szRSjprG9fOY8GO8RAhGosnMN2oll4Hijnh9211fBmXbbpcSAPuehLKrIab/Z++Ho+PiVxf23kOzq7u3d/llZ1V5NHjuE0vsagQwatM4Zd2MikXkQjaIkzAlyqOeubByRiIAAgtGcrXOK4oKPOXISmNWzuLq82qY0NbOZB/S2FsyEHOoqVOhDGYcBUjbGpmGHjMhoFU8Xq3efns+q+um2FREfjIwZGlAYbCX7cT0vdC/qrDlarvpuaHEsCl+5ArB0tuCUrUMgR85z6hEmtMppVDAIDhVVRKYoGQGR0IhoVa7IogqwlRthurMYWXgY49AVTYloDNkbE3JgtdaDCBD9FiOekBTAeq+gmoTQMYOzroUOxAxDCoa8cyKacmSpFIehH42wI//Jx+c/+/WYwQgIGNOEwhixznPMIOJcQUg3W/Q+zRpVhUSkMHZtTuxNmB0fgXXt5SZYT5CIOHjvwe2et0cPz8g447wIABqBiCRkDaAaR7nPKtL2Ecl2wzROSVnSFG0ovTMG6LqdEkM/xVvHdde23iDZ0A/rb/2u74Jnu6NqkadBlKvFLE8J0DnvwDt/trJlIFAW42yBrEDWWaecAYHBAJOigm0QkKfkiwUA8zA4Y7abaxOsgEzTWPggAmQ8GQx1qYAqSEYIiNGEookpe2PjNCoioev31818NTEDq3UuT4OxOo3JBy9orcHddutd/U1b2U9NOQAAhflmWWTmpArWOkPEupr6K8DZ4rBcnX52//QamKfM8/kSCTlNki2FpqgsWgL0qoBobAhd39dhlrOCjswd6QFnBXWqaGwwtQdVEGYVBVQWY8tpGKz3iLMYRxkGyMkZB6A5Jl9Uhly324wk+/2wWsy//vF0hKvy9Fba9rt3z2HcVAtQV4OugYsbiy9FvbFNBBXnXOGXIiAYqfAiEwgaAiB0ZDmLKKKiElDwcYxMakINvD2ZL/MwAMo0dHZPttiGEJxW8fKFtSYZ8r7MggiGYup3W8mUuiHHrkQzADjrBHw/dbc++2hzcdW41fz08PmHT7949+Vf+eQbLgRL9Hy9OVveZY67VueLAiFp1ijqA5ExhEGUEEF5RFFCFRZObFypQDlNlqjrdiym8Ac2WCAjnCBHscFZzZoMGeMs55QZjfMg2ZCXzABABGCAiERASZ0PKcUUo7CRFIHdftca8gm6elG2V2sQMdbkqGizb+pGZH/9bHd99SvvSWY1BuKYAMBRLxLSMHlXGGutcUCKVFhPYowxJGlI415ihFEAaOhaYRVNzngehsJgCRIiT9Lr1M4WRRVKZjDWGxuAreDOOyeZOcdiHqZ29FwMrQrnmKL1Jbfj0A2+CKu6HAVi5kUzH6Z8dnz69N1fv/Pm933n93zn08fnr86O1tcvqiJYZ+IUnSsRCIwjyLE7B0AWLSoLGlWFwMGNFSQA4c0OThLRnEdjnXWoSCCYsqdZqTF554dxGNq2bBCtBetF2BbEmRQEyAKzilpjgdB6utkS5+smC6sqEOQ4sLYqYL0XUAFQBGutfro0DQi/ueKBEBBRJN8sWXfWc87GGoSgIxiR/lKG8w2BYQZnQj9GFlRTK/nzi7WCZhGGzMpMpM6EZaVMBk2ONkWJ0xiKOoRG5FPzCCSfJpZovKsNlZyVqBAmRe9dGWxAJREBsGUz45SEB98E7z0X5pMnnzydfqm8U8H2omiMmHj60kkVAjIjFApKgEYRBQghFC4UgQA1T4iTdYCSLBgDhAw4ZY0qMd0YmogkFFFQ7z0gorUgMiq+WK8FpOu35XwOLgiYsql8WRKRcjaqU7sDEhKSnNXw/4+9P439NU3z+rBruZfneX7bfzlbVZ2qrurqrurpvaeH2WAYzAAeLAeCLcVEOFHMC8eLgokSkZhYiMgiXiYxRo5CcIKjCEeyDNhgCJiYATPjYZgZZumeXqa7q7rWs/633/Js93JdV178qnuAIL+kR+nzeXH01//VOffR/dzPc1/fBUMIje8Pe1VRnT1TnlN3fupWIQ1jrnLWLj905940zqYwjnmugojLpgUFKRnBvAPTYlr0GNlkwBTZNYYspTIzO8+hkSmXcYqhicsVMmc1sQoBlWYXQ1UjQgbePryQ/eQQjczERAQBQhOJHbkGObJvmAMgOfIISGAmFlz0vhNEM7h8ukVVNCtSFp4365VOpb/ONxf4xa9O6LgJ7I7lWojE7L0HZDVg1ygKMkFw0rjQNbXk+XA17/o0iIPG5soK6eZQZtldXB62w6OrvRFXAqQsVL/8hS9vHz+c+hsEEyH0YhTMAoCL7RooIDtVE0tkzBTMrKgCIAKdLZfLGHOuD55eEvmxn588vGniiYrZbM1m07XNMefLu0jEUhUExmFen9wuNYdueWxNZWZAQTMkQnCeOvpWOREYo2sBvRmpElKI7YrZp2mymiXPeRrHq0udJtEkouyi80uD4H0HeEwNNQQ6Fv0658exVxPVQt5Ucpon550Z+BhKregAVAkACUkBjqWiRysS4TGwm4+hc0whzSWlOY0jIZaMbMwUAcg5x+yklIdPnh6G3eXFdjxMacxjfxCZgVzTrhTFDCRlrK3Ms6lUycTe8BjJmV3sgGMtuZaUjwlvhJLHWkues1UicJqridaiKQ1S8pSmpm2atvtPfvLvrO+/plZ50zSk3/yLf+XLf/UX5/5ghmZOajGpMXgtCWqRnEQqqpCqq4yToKp3UaoYIJELIUoVULZiNVUEqmORScEqGLB5QfrGew/a5YlgB36l5FWdCCAGLa72o/ZJZ9FShsMjU5vGHEJ7etqJ1iyl1to23rmwve6ncbpztkEsr53fahgPw/Dew8cuNggwjxMxA2AtE5O3iiAOkczsGCOsaibGPiDhB/3rSs1iXUzzXCl49A5ZOaDrOEuJXaOR1MHydDOmcdgdyu5gWh1HQkrzpKCGopbFCpBomXLal7S3spvHm1J7wDqn6nxYr1aeUUWXHD796ovBkSh4Kk8e1ymDVG0cE9qxSGnKe63CziE7ACDnzRN5YuPU93m31b7UOaNKv7t59yd/+t/7iZ944+d/pt7s+ycPtvP4hTff+fM/94v/2S9+4UmfDjMABBNXLob58oA5qygjEBMSKAhwRIyuidxoysnUVGy5XhWReS5aZdN20XkkHg9lt0uP370xm26uD8vzpo6jYCIPyIhox0OrlGxFMSyWYWE6H+93TVSlGJiBEJnCKLZVnedxJO+RGXyjxshkIJJrrblUCb6FD6LRhmG/1ZrqXKQmgMChEQBVYc9ghNwgO2QSNc/BcahSpADiSfAb1zRiUEomJlAVqO44BCakbxv7j7fQBopGgLboFs6RFBDm6WYffO6aVg3YKjJKHmPjjY1Q333w6NbZWd8f2q7GEL78xa9f7sZPfur587M7jCEP6XB5HZdt05VjCiEzFzXH3qyaZfTRlNiFMk/s0fIgYqoeERA55ZnYk6ulBLOhWy4vL7an69PV5sQvl9eX7+M8yTzF9vxDr55rsSoFq8GyMzBRlZwLUghNFTU1UJNawVBEoS3Ot7VMVCQNF7k/xPZMZnRNA2ZEaGhprGw19VNFyQXfefDkJXTn9++VuXLTmEJNM5gnpx5zSgKKUvxUFS3MaTKFrvFjnptutR/HYhmHOSr4eydda4smfP71+//tF78Zlq2pgUNE0pxs4Rj8PIwOAzhlAsSAEAlZrYJTOvZVplQOu3a9mMo+tKGOMh223MRiForlpFhh0rK+dVvySApSK0rF2cSLhlzNnA8iYtWOcgAAk1JAhBRNte1ilQyEHgDR7fY3xM0nXrqL5F+6c8cFNz65eeeNb475zBRefG612+c+SV+SY2TXKimRIlUOC0ERE9YqJWlKw8N3yvxu+9zH3TLM03z26qt/7Hf9drdsD9v98P7u4uri3vl6tVlPaX745GnXxJPA+92FbzZ0mFwXnWMDNFQwU6kmQOxMJ2dcKJlSBU05t8tF8L6/HuaUahVP9HQ3nm6aTloo/fXV0+fbW+3Kg81gUGvx3gOI1ASAAHjrzt1Sxxg6MxUxRgYk8h5AERwjlLkpoKFtmBskZ1oJUIAVgBjFjJ0DhMXmBBRDbHI/XozD2f0XfVxIVUdI6AydGQEdMxKO0/6JCEupKJRyllxqraChVjP0EECzPb64cqLVsf+gW/2Dh/kHGCgYbfs+zwMiQq7BO4cuzfns9I5IrZIF9ObJoznVvp9/7a2rw/ir9+/eXizc+28+pFvd3/rS137yK1/73jtnv+NHPu+9lpyn90duLDSd8/4Y8W2miBBCEDMkzHnyjkqqVi3EOKd6zLglDiLSLdr9IFyaeSqnq5NtP5eULUMbT7zzaRw5gls2EGIMkZmlSmwXCIjISMEUQcAIJVVQc9H5k0XVSpAgT9eP33LFmrPbWo41teLbZZaKm0XMtztMp/vBChZp9rvxenmIC45xXYsQMblGUgWMJaF3bdEhOOfR9cPu5rBLpCmXRdOllLfjfHtz3texibEhrzRI9S8sA2ndHXrFkNK8WizEqOZSZYpx4bpWVaUW5xqtagqIbKg1FWKWeRbBx1/81V/+1a997oc/1UIwgjD5lOtOaprnw01qutUvf/Hvf+P9d3/o0x995aXnxmEX4jLnnmsI3Wkuow8OFasWFBSpphXUwBTNRESkHoN0wCz4KEAvrFahCSC5v3wgY8j5fuB+0XalZMd456Tbp2pm+yE9f2spUrzzWZILgU3KPGgd6643rYdDvf25+1Dp7KVFuXeW5prKrFZf+Ohr3Z3T4Wr75OHT0G1OXzzr1tHQgm+cj+Nh5xe7NPm4bI5HDwJIqSpVTAWM1MREpQKamky5nJyf7PoLBHM+TrVc7vK6Wz144wv7fnjRPSf5YB3mUrxzaZoA2bOWmpAa8hFJaxUf2aqIAnmHSEBgQtM4W+0VYxO7qsmRgYvkMGtCopzHZr0yOTaeOZln57iO4mM0c7VO7EtNAV0gDgACgCoJAES1pNQ0QQ2yZjRy1CXpD9ur1XpRirD5auX05MwxkZkYqIgAALM3MyICVbVqoK13OaHoOBRr3WKuQ3RtSRMSOQ5axOFKc9/q/rWzFXl8590Hi6b5yMu3heAP/rYfOPRT57o8ZAAM0bdnbu4nAkdA5AJULCbRxVKzqrBj7wjBwKyWSoTMoKLTODjgnKZxP4BqqSaiWYpIXi2Xv/SFb3zuez+2u3pg2eJi0dy6M/V9mqcYGgMsRdGTC9FURYEMKS4BxbXerBiA93G+eqyltm6RjKqyYye+Zq/Le+dWsszz6d3V5XtvEUrTxg3HnEVSbXyQvBdG4MgQlASFebGENCtYuzx5+N47frlY00qGMbLsUmVmJCLAqd+u7EzVMwR2HGjxg6+9PFXd7fo758uqZemjFHGMItP26ub2/Y9M8wQ6hbioACZGhAqQhpEo1LwFH99+mv7WX/ibry7O/oe/53en3a4C1ATMy9ryn/xr/+9uc4tB9ttD/Mgrh3Lz6OmD515+ycgZGCLXVNUygeUPrjykSi61zOPc+pDnooTsqNYkEWTWCrr0PnqfZ7e9PCjXw1BFa9t2xNqiouqqi1rmKtmxV5XgKE8TBUaxNEnd9/tHF/d/9MdMWbSCCvmGsaokaA1iWPjVyb3V3VdeVI6aMhD0u4tSiw/dan03jb3zHrrGqqmpHnMvqrBzuewYrGhuO+/JTVO+udk35GITmhByrbmKlPTVb/Y//s//CMP7T99/9/ZHPnlqGnzQCsyBfSgl94dDu9CU0gqjAZZUCZAYCRtVUMlQZkyzKovJzeGdeHLuu1VJkxZBMLMSG3999R5jQFySZTbKagQ8XB9Wz5vMRuTJu2MoqoggmKEde0JjE/I8zlPvOALRNB+8920Xh92w6MJh2tWSiJwTEfxWrCYSihYAUGEiJGA1UbUmhFRYpoReG3bBOUNi1lxLHobpcABHi7OT+24ZV5t52ueh7yIvT29vTu4Zeco5D5eA4E42FKzOUIcpRFfrdDQrH/8qyGqSahqathvTYClnk7BsCSBNk1uu09iTR/Jcam66BnORAvM0T1p862FOwcfaLcyXbtWOBylSHXkEAGREME0CHp03ZwxgqIBo/aGosG9kuin73eK5DxflkicOPp4s908fyziSaALuQhduneXHF3Mdu1VsPV89vjw92+icKHr1wBgQFRxLJjA3jFO73Dza31R2x/wo71hMtMh+GM/Pn9tsTgqBY4yLmMb9Sy+c3/TJZDrsy62T81JKCEFFQmh954bDLi46IlYTMwEzUAA17/20v/CxufPiR3/vD68nN7/z9je//stf+NCtO/2cZhFA+tlf+8aq7V5chY1b3F6cbC/3XdMSKgQEIq0ZVRAMwYidiTDhNM4GhkiLxaLM2eT4YmY5Z2RCxs1yXeayWHZjf1lrDU7bSB5aNWybpVoKZKB5nnZqt9QMVBQEEGTI3Pnx4ZM6T+vv+ajnWEticsfJR/ARgvc+emdqJ2Y1jbMa5f5Q0nRyesehn8cBMDTLtdQkJR9nKAZGROx47Hs1AKbGt/00F5VStFssnHdgEjznKoTom0ggF4/y2+8+OD/75K995Wsv/9Bn5pyckeNQimQpruHLq4uubatWUA0hmhmAiczELHmuKQOqqDWr1fbikQpZZe99TgdGHHbbR2+8+/aDy7/297/Y1/pbXnvld/zw5yQXXyWsliqCyAgkYiqzqSCoGpgVA1UtAC7nkQlKOohU5/zUTygQgg2HG3YcDKqp++AC7diPBGD6Qcysqn3Q1ASGxEBOTaZ5dr6VxmqZSrEYm0m1iKzOX5DDRbsMSWu7WMXlwhxlwyzmCSqZO71rDlELQnHBzQnzNPg2ainON2ICamo2H3Y+uH6/Dc7bgoGgTIeUMiKN4ww+NA2Wqs5FYl/LFEIgon1/NU87q7m9dVsOZEXBBZNJrWsWCCZlGitQbBtm8DGkYQox1JpRhCiajDUfAHNGpXKT9klrsBBqKrFbQp/Ju6mM6a2nX3v7HQ3wq998l8y+/6WX7t09O11uihSPQx5U6xAXUceCymChlP3TpzdbyuZgTEXFjr3YlZ1rHZI7lHnuy4fvbFzTqM66n6zWyNx6R2iOXSmZyRAMQQEVDKQqEpgYM5WU0ExqoaajauP17v4r51rkpdunjDTBZI+ul8TOud/3A58MZBaDmJoUKXPYnHPXhdUSLOWUg3dSE6iWeSaCee7B1Ew8xZxEc5VakXgY9sxOCYjRs8+S5rEIbbeHWqFx3l9dH26db+bp4Jt4umz7YZrH2RQUFVGO0w7xlHcH5yn49eLOC7UqEdWSSY85bMghMLo8TE6S1ByrpjQGJVQPmkqeGUmsoHlFlJLU5Fs9iTXn2QBEBZgUUasBYuNC1soAjpgJRERFY2Az+uVf+JXYLpIOG3drqJPLQp6LOa15Px3GqVapi9Wm5jn4dux3bdsZGYBKyVIymIopddFUl5vb/dXl/vEFeYvrVR7Sozcf/8yv/qpv2k++eP903dWavvjFr95eb1565cWzF15StjSNGDDEJs1D03WqAqglTbWMwW/URiIwFUBVzSUXoqBYj5Gjxi7Nw5TwAzcSHe37gEiIQAZ6/BMATIGJZ7HWN6ha5PjAgxhiSbOUDGKljujaGNjmgt4xYKrppD1RhLnOAFimftEucpkXsROQsFrUwy7vhrZpjNnMTACJtKoROB+k6jz0vm3QjDlWHKd+ajvKU3ZN2y4jGm/1hqtT1SGPDNicn2ZJ1EVDP82TGTRde/xePCY/Si4YOO9nXq4tENTBodNUZU5qc52KPzkZa3rjb/zMdbVPff/37qS0rZunsjnb7C4eX1zf3JT88198gzq/ic0X337r7PZ6hEowbK9C1xyaxbqkSQpolrmfxzyHrmmB3r68jMEDY03VhzDneTfqi2f3ck7NopsruHEed4fbd58bHz5GU88eAKoURkSFkmq7aHMeHHkkb0jMTqQiUZ4nNPW+ESvdrXW52VODx2HbUuPydK1V65DMTkFynqYihZuWl1wJlqs1+66kg6VJLRgIIYfo0zwSExCjYkq5SimSnXOlSNN2UrJlHlMWhZPNKTIStPM0+M6L1WW72m7n1157gdG98/5l2zQP3r/56GvOQAx4ngbHoeY5HbbAunr1dRO1XCy46avvUgpzmR0o5oSLhVutnv7aFxjQLbpZ63gx1jSF1TouY7nngnaQd8vNUnTpGcXACJEcM9Ki6Yex7RaGOowpApZSGudL1dPlKjjPwNfjpKrR0699/ZtJ4/5mUKfjdHYSccq5CWE6ZLTwxa9/ZX22vpH0A8+fVcmMWKUSQ00ZkYgZCNk74lBSIXab288Z6M3QP3r3vccPH7Uufu71j3U+EnjgenbrNHaxaZoY2lomBN92SyYntTRdd2xyr1WYu5JHkZ2olDyj+ZyLVZymWop4V4epj20zzzpniNE5kcpEqkc9Fn2749vwA3UHERnA1957+up6gcrni8UwjSdxVWpSsyrana8pxDwc0OOybTi2N/0Nk5uncdU4F2IVbeKySp7n2UV3LHif0mSiq5OzlJOjVlWoFh+6YRq8ZwBqViupFalNU5rmEmNLqIvz9TxnJBqmeXN263DoEfGbD9/FXJwPOs2QVW8vGkc2r9LUe99lTY58ydrELu0OHHwYSGZDYtFZihK6dGngu/ZD91eEq//RnfEwG8LVm9/I0j662T554xvIQIBDqt/74RcduxW5kyZAKXNJS79WOvRXRUswIFCtxVSdgcuQ+5LMDB3NUwKAOc3WNXMth3nqnD+Mw9tvlB/+5Lm6tt9PjXLjIyKaqWqNTdQqAFprcT4CmKoAGCIiECC7QGaVHZmYVQmbda1V2Bk6UK1zjjECIYjWWbw1JP5YjhGaJo2pa71KQQRVcSGoSE6JiIl8zgeR2Yc4z6lbrnPJeTBwzLQQV1uENJda06LrCnp0vioCcgi2WCxiZCvQRb8f6tOLnjwzIgGpivOgInnozz7+UVLtp4NjD19+CtM4vPv27rBfv/Lh4vT03q1qBT/yonDZvn8tCoeYItHjx+91pxs+dN15Xt89mw4K7kmzOGEOxARMrjTjvl+erNI4mcqqba5udmiwaANqtRhUtYvxyW7fxICAiza+f3E4HBaru93+8N5wgS/cfyWwvHnx8Ke/+OXVatF18fHNDj736Zpn7xoQLaWglSLAnp2LqmKaSy4AIGZi0DWL9rXXX3nt4zLPNw+e3FxfnJ3dKZad82TM5EtJUnVx0lSwOs5Tf9F2y2oZkGK7VBjZRZERDBlZNM3jXDKKETNXjOiXQ5YQA7OWNDkkNPjAunC08gMoIhmoqTE70WKAP/+FN7/nd//QcN1j4KaNzE7MmKk9O83Z+v1kRKv1womik+dur8dDX8pUZeFAm4UHhHkoy/PTPIyMwsG3q01/mPfb0UcgVjWuCgToHZsRAKScEAAtG+B0KHETfGzMXC1J8oGJ55yWyzbl9HPvfHOaq1uFWsZp6PlSadFWFcFgtXrEsGis1pIHjh4Nay7kAECQwKDk/Y33eCi1Ac19ggyE1bXhe374B0zg4qd/xlAFGBBfv/9C6mcUmfqDNY7Z12GkexuZ3TA/xQY8dzIDCF+km6GUd7YXY8mr1SrXGr0Tlei6/tC/9NydOs+jVBH4O++9/cK9k836BLhWNW5cmuaq9ezOHamCaEdJepomXrbH8Z6qSqkuBB9dLtUUSsloCMR+sZKiRChSmSIFB5qqqmtbYFWtoLWkCqV3HSN0VnKIjZSqtRTJiC42yzn1x6S0POemXQ2HwfkIBDArUmDWsaQutoJlv732p7TuljPY/rB3jue55HRa8hgJmN2Dx5fjeNXEpSNjYtHqzHGLMs37+alzzdWb78gbQ7qPH/39v/NWVRNb3r0jaHk4nK9fqzpdvv/Ne899Znf9/tWT9157/pU/9yd+wnW3+8f5Q49Wjfef+cynilzj+T3nCIGBASyH4EqupNLXuW2cVhGrPjjluuLm648enqy6ItWRq1WXi9XF1fUrL7x0nfzLp6unl+/92jfeT7N8+hPfM5c87tOLL95HUTOpllkZZrPjZbQ7tZKlqPMhxMWsPZpDMO/BM4/9Hj0u7p1v7t/rlsv9xZWharFULS4aR2rKtZ8NpGlv7bc36KDUMQyZggOUtusAapXRlHIRwgClFi1FkNmP+32aStstsqhz7FRVTcWEjIj4WyHvbGTHDj4F3B7Gvr8Mvs21cK9N06iBiYzzmBMIkBKoaLtcmYiLjIbeeylCCpJmZsqlzBMxRrBMInMW9h5ldLRQUSND9NM4EWGqs3fBu2YahqZty35CJFMNwc1T8hTDypdx8t6P0xRD7OcxmWkaabXY3LnVXz2utSBJYGYiFZOanIM6TSYUu1VJMxsSsVaFY6F6xM0rz+Wra5tqu17bxIZofcLIn/3+3/Sh/iOL1Une9Y/feOtad4vGOY13zs/qXM1jOuzAcbh7Z0rzlK+b1eawu3ELG4fR2DkA9gw1EwOaA9PofS12yGMkR841Xbzep+eeW7KFuYl5SM2SmzZO02G5PBeZgFAsm6GKkGcwsJpBJffpg4bucUK1oiXSgpyb5zGEoEX9ItSSp35m782HShNU0VrAsaGBuXF37ZpQaj42USI4JpfziERmmIrF0AC51XI1l1pSVqR57j37rlvO0wBG3jfeg+HIRHfOIyBeXM61Hhx39++dXX3zykdcr0/AiMkBAjKKk9CSyTzv997pwy99qa/8wz/ye10TIRfixjwQOymVI1mK7eoWtV70yYuvvHh9uP70b/t4096VqhcXD7/4S++e0OKjP/Byt14Rkg+d5sTB++B941NfialxfNgNXRcO20No4rFW3sfgiOdUbp+efPPmQXDx8ubm/PZH/8YvfOn9B9vf8vnXng+LpzdPl6sTt2qg0jRXqTW0XK0QaZqH1eYcreZZDVSLSN3HsKhaCcGshtBIDCLaLAOY5XFcblbzbqBjfycFQs15IHZorpa5aSIvlsRsDGQwDVdDvwshVDVTqx+UJxI7qPNWhE8265zmeRxj41ytAmgfjFrJqQkCA8AxI5rZA5gjZMKGw3Kx3l5tz5+/D2ZNbGupjcR+GJCCgCKHqZ+X3hPRSXuWcolBai3sGE0b18wy5TxzwJxKt1hKLuO+t+HQru4QwHDonQsqpWkWUnQeynJxXsokIl3bNotgZszQNGG4uQ6hGceBMIrIulmGEydjZYwG3J7dnUtv84hox2NWNJuqb4Kp5akYkZljqeQY5qohxPNT0epcxDamlDG6UnOzXplA4/UMN9ixFf7w9338xf2LVtL+Yiu5hvWCvV1f92C8vntGzkNJcxq5QSqmjHdO14c0b/d9u2hKSoa1ZndyEg/ztGD3cDo8GYZtP2eTNvrtdqc4I0OIJ+PYd8sFgiBY1eyMY7NRq2jM7AwQBBQqgjetUotqH/yGmjiXTJGMVG1SIEXzbYvIU06hbZVJZyupIJjOIlDMrEohx+iIXbDj5SWiIDnfIgcRU1MWIMI6pxi8gEnWXGSzXk79ROwrzI7dYchN6M5PFznPnvw49Q0iN82Th++fnt4NLQYfAIzbZWvVkFan53/2T/4/v7rr/8M/+38MVAQLNEJEVTIDc8Q0HKoYGzx6+yvpwX5cDKf3b5fd0FkOg32su/0Dv/PjqS2LO8V86tq7ORdk8jEoGjkfW0R0+5stgeWcjG256h49ffLbPvdaoHi13z+5PpysTlJ5q1u2/X73U3/3Zw7DAGDP37rtjOl6O5d52vfXe0gkn/34yylNTRPZUbNaFJlRnao1sdNajFCtIBOTYxcV0Nj5NmqpaIgOcj8aMxgoW8m9mrTREUNOyaxWqW7isGio1Iqu6TbzQCIFGDzDarO4uUopFyLwcQU2U64+tsw05YMzAFU9NrSqKpEDOObLAhEBEpiqas6TR97v+hjbwzieNctcJlNwcekaG8fkmoDz4LQOT+ayn9B1KDqMN83J8vyVl4yRePDVKWE/HhxhyuNidYKEBbxXjb5hx0TsHE9pZhdK2k2k81iatnWQOHLTNakfiiR1aGRtXBwOWyIC5/7SX/nb/8yP/WaHCmYlpSY2tevMqhlbqcgITIbHatNGpKKJBct5rqLgfBei5uJ8rCU7H5KUxclGS9GcyAXX+nmYGt/M44wUDTEdxsWds2G3rzm76HPajX0Ez/uLm82tdWibqHbn1mqfe+c6BBXE0ksu2rR8sR2Xrd/ZnNHe2E8hdlUr0XKzpGF/geABBdk3oct5Ys8AYsYK1QAlDc1qjYRIDrEi6HF+KyWwd3OafRO1goi40EAgRpjGvFhsKPhcBkGlJlJFAgue56rTOIbF0q9bJjMQEwAmREfMHEOZsuRaSlE179xySWBcVYehjy6A8en69Gp4IzpuW2dqy2W8vE4gLoYC0ASfb58sATRLiGSqiTh4F1NYeSbk8If+yL/2qz/1lXH32Fy72JzsHz1Q38s4mkrdvp+fCGa1ZG1dINf+6cWVfeMOn7iSc5/g1jp3yTVR58COJQKipbzlJqRpZmQjLSnHpiP2paSua0X1/PRE6iQ2kZb7m65IAQAGGnNJpZytNvM8odVSE5GmoWaBB0+fVpDPf/qjoLXW0fmGmU1R1YiolCK1sHPsaJrmpluJgYoxRSIGBk8uzyk0DbuShwmQmSzGthbJUxG1wFhzzlNBqtyEJrp+v0PH5AYP6zK9i9giIJGVXIkBgYsUlczgajFHRAysdqzSATM9lmAjoIgiqpoi0Hq5viq4RqhYmm4J7BBIUYdpf3F1KbM0MQxjuXr65HGeowvX0+7DH/9Ib/3ll9/wX/jCc4v1ay9s+GTtlquxjDG4s1u3AVQds8iYDnnql0uf0lAVwNi0sA8MbtFSmSowWLZJJx+cyeQ4THPJUs5vr+c0d23353/p7/1z/9yPQ60mhuZlNoKQpe5urm7fvaumtVYE42iZMiqaqKREdRoe9ZvXX5umyXtfcjImkaxkUhJ4Qqb+6RUhOgpzf9OcnE9Tny258xO/XHvTw+Vl22gSHLYXniIg+RCayJ7WhHb9YD+WcZxnBSDnUp0s2dNdzwOLWa3VEXrUxzd7ZzBLdaFTpJpz23a5lOVqaSbEzpBFamwXRIRmZh8M7VWP/m0GR0eZvZmJZsdsjCAKaIvVMqVDVWN0iGAqVcUx9UPvY0BAqRVUXAx5nhH90VPIPkhJYOCcqylrLmCGiHNKORcjcOSk1qEUt4in3UrLcPtsVerUeE6FvAs+5Hsnp5vVErI6rqqO2QO6rBqatsyjw2Rd+MjnXx++/Gi3m4Zl66sdbzcXzcLSra5rw60zqD2Z0G7g0D3+5lscaExDPI/QAa0iIqbdvj39CBCr5DbQsJs84zBNKqQV0XwVSYXMdHO27LfXqOTbRstFydJ1y0XX9X1/vlmv4nLKBQF+/pe+fH5+zmhjyg+vb87Obn3qIy+KDjnnbtGJVTZWc875eUyMgECEVEperJeq0MQgImDeDJCYHHtnpQxEEBufNBnIdJhj9LUmMihFas1H6V8+TPOw6xYbYpcKMWvJod9NIiFNE7nQD+PJ+gwCln6gaATOgZmawPEOy+g4r6fjZzCimRG6Y4Vnnql00DkHpOjIilbJbcNdh1dTvXp3+87F063Jb/nNH/3Qx17uunW3umsE24dP/pv/+r/7y7/6pU9ML7G999LJ+Sc+9mrS4fr66WpzYoQKxIrsScTQGFCkjgKeQA1w3idgIzJD8w5UFMyneWR0XdMdpmG1XFWRk8X65nJeLD2l0TXRzDyHfug357dSyUzsfHShEcmm2rTLkkpDunv4VvPy80aqVYIPpWTgCNExmYDO28EVs1wrojMlyanfAVkqmZdcoM8yacBRcDtXZ2nGenb3fHm+9F2rE+kITez7XA0shrg/pCbEiuJjnNPknDczRjZT14R5TBRcrphL70OMIKFpcxpj1xqgD53zjYiiwyqCx8iKcrR+ak2FY2eAhAhMEVtTNVEgVJPQtLkmVlWFkgqZmVpF8V1jJo6C916npJHRecdeFdSMDIxRTEFZVXNOIJV9Y1aRMIamFJF5XnXLsQlXj550y0CSNs/dV9hutzIMpW0XN/1+v7sBuyfzNS1uk/Mi0jTOJLM7Bi2BWwd+umjiaR53yerilRfunJ8BM+fD6ux8fHR5/cb1oo2Hed+2yxe+73sR6j4dspW4WkoubdNkEbDKzs9DmQ6zGac8oHliLAUKVDRqmqBSwDUIuggLLXYr+tG3CuM0T0yupNLE0DgS8ZXd05vrs/X6YredSv7sJz/qGyAgx94A2QMQknKaJ+IGQNFIStI6zlZP776gtQiQd43WWiETWoXCHk24Sin9aJEd23zYGdSa5zInbLr95eVbv/pzL37yY7defAWwquWmdVaB0G+3V013Qgxt7AL4EGieyDmWmrrYHGMo6Vv30B+Eyx4/gwHA+6iqZkjkLnM+XYR+mM9PGtGc6lHoV6bpEIP/+v7yuuRU61/4S3/3ye6vqkHwXkTPT287hsDxjadPRO2rTy4vnj79HT/2PQbNbts3wXn24BlIES3EME2jbxwY44oQAbnNqagUq7l6D+S1cuQWA00lNTHOKRFACOEP/nt//C//sX+/H7chw64ObbNu2jZVcN7IB62muYQYSxFAirEVhPb+93DkEGKe8mG7NfMuFHIocwJRSlj7mRWas9Naiwvx6vKRgnokCf7pw4u333tfzfzaH26G1enyhc0ZoHWntxGwSip5nESvDxMgNk2ju6loSWrjNDrnSs3ERwMJ3Fl2ECPV0sQGQjS1qkIpd4uFiDKhSPWRCNiFqKYqpZTRoGgFU3axMcOsE1pLqQ7XO5uK7aciylx2Tx8Uak7u3W/WCyvm2ljDWKbaLG/NaTdPfVMXsyZqG+dAQQ3NOco1qG2lgKmZuuVyIzXnKp5pmtJ+33vXLlcNUhtbXm+6oa+Pr6fv/dCqWQMP15YJkBX4/GRZpkFXbSmDiwtAqnkKPqKDWooBCvrm1dtm0uEJ+2hFq2asQALj00tysHzteQ5865VbeUqitYzVMzkLeZqglhCD39zKCq7KcPPA0Bmrg67YMO5yiF3JAyKknNI0r+LjjkOaBwQCxieX+//6jXeCD4dp/EO/938g2+t3Bv2rv/DfffzlFxZtOwyDVHnu9knbMBumGggrACoAqoEWH5dkNA8qpAQY2pOQp92XvyxTXwo6vwRgF9yTp1/cb8fTze2hR2h8JTr025TssN3PZRSYN+vz28+fvPDKS5/6/h+WdqqluLCoRcjHWvamrl20UofONQASg88ppTwv2kWuKc/4gRJLVezYxgBKSIgkKgjfalsxy9V+8Ve+9Knf/f1DElXPLKvNZtjtUjos2vbJ421SGGo5jIML8f7dF1Ip3ntRcYiGQICqGpzzxF+fy6/8F3/vd33vZ15/5U4l9VitzKFpkbkW8D7u99sQwbdORdggopumhIKquF52291BUHQuRlarOGZTVdPb53f+7T/7Z//N//HvGevQKM3jnrtg9WZS9c5/0FquEiID1HL0WpGRb/I8qxGHqLOSYTqMDlBKdZXcom1W7XAzOcBxOHgX98MeCG6eXsy1Nk1ouuamP/jgN8u171rMg3NEFPLlTYhxtzssFm1wvD0MahWPTyRmVVU1REUEA3nw5LF85CU0mMcU0VWHhMEHr2beB0BAMKmZfFAt7J1UAVUf25ILCGkl9H46HLqAu8fXtoc8TT54qyBGw6GVqNdfeyM23jVhc/ec49J3up1uFn4RvJaSl5sOADi2IAoIJmbQOz41PyI4RMgplVqRbZ4m9uQhxOCs4vXh/Vt3Fyn4ado2m9Wbbz387GdeP1weHl9fx7Cccik1l2kHdnIs/QAEQhSpRAxYEIioigKyV6jBeW4DEoGhM5GSzaov6oUyFvakaj6AVEIxyQrMAuikEui0v5z3I/GJQHbYie4Qa0qJyV1uLzbr5U9/+c1//kc+C9Yf9uPp6Qs54//n4Ve981OaEOCENvH2RhZP/6lPf7Zt6vnZauzc+Ul3++4LeT93qxa0ZZ9Lzc5QtDDFcX9BlvaXB+a1A9xNc//Wwy998+FPP36yiA0RraJfRNrvZzbs8L0Prc4/8ZnXnvvocy/wyxXBqATXQjXJ+f0H73ZnL0rHrJ7D5mb75OTsdN8/wjo9fvB2zkh+VaC0gcGopBy9K1pzqjGs3NF+REQiAngs4uFj571oEfkg887MdruDinWLbp4nASKbxDRnef+9q0VcXe52VQyIkIAI73ZNdM2yWcxVxjx5xz/6sU+sl91/84Vf3o59163+9i9/5d1HT/7Z3/pZ13nP3gwNAiIaEyge74oArJQhcuu8U2fjXAQH57xUNZNxOrRxycSGWEXQ7J3x6l//03/mj/6+f8afd0/eufxjf/G//L/88T8Sccw1edcAmPN+msbQdt3yBABqn9hPkkATJ1Fy3jE5jItuIXOyVFlh/PI78eS2ltSAu97unNqcp91hu50mdvH6cvvO00e3bt/q33/8sQ/F2u+0YnWzkWyHw3K1GFMiptXp4r2rnY9xmhIippxiiMfjt4r82pOL4Dc1b29tTqdpNEcAXLKw82pwDNNVyeSZmAHEeZ+mnlFryYShQpX+MD947/JQJQWraFpBa8Ntv7861IQa9+Pokp8vt5dvfPMw95969ZVPf+7jc+q7RVuSpVJaF/VoI1WtZVLB6EPBEREAzcdQaimlVkEObfBSclEpP/vmwz/wWz45D1lwrwkrypPHj3np7MLef3q5HXPX0p0K+ycPNZxyyESUqrrQRlo4z1ozABIbIhA1iKiiIAoA7BjRqSgQVVJSdkY2KrkgOCuqb7DpNiKCXIFgePquVquyJ3ZzuZGc85TEtJay7JqS09VU/vRP/uwf+PzHaLX60ttv/pWvv7UKi6ZtDmmOoXl/e/H6nfXLd+5Grb/y/juvn5zUbjld7+4vlzd58FUQmUIEhTznEBa1Crtm0Z6s13fmg1y88QgSsD/5zMee+8Qnwhe+/sYvvvtrmyY4pd/323/8E5/9NDGp1DTtHcNh2DuPZUz9uI3RXz5+/PJnvi8uGMRyTlWmtvWHw2VL62Hemzu/vr46PWOPMM9psXDovSjE4EVINDsAw2Ma0tFe/4GjEEWFyVcpiOScY6tJqqo13szIeW9oceGQT199SYer3apbDf3BETHAb//wh/+p3/pDuSAmSmqS04K8a0O7aD5890Nfe+PLP/vmG0Xq421/8fiJwourlRK0BCaaTVzozhAJKiAAu5pSQXbzNLoYHHGqRU1FQGdHkUzNOT+n5JwDgOLdH/srP6kAnu3W+fnbT7750Vsd+w6gIvqUJkQEMNGMiN5TniaFMs7zxTuP0/VQbg6x2OmtNYGr/USiFtxy7vNNmdIQFk4J2tbdW550oT3UhFjvnd3tp3R+ury+ufn8939EIWOSy4unT64OfR4Xi4VvwoP3r7pucTMMaiaq3gczO9qvGawq/9Qv/+LnX3y+OtgN48I3porOAzABIAQAAwR2bCJgBGAhNnkcJPfIC1fg137y53nBy1t32/VJ0CWy5cMeoYI/PXXcbjY51yml7TyegD3/4eem8fLi4uHh6tGHXv+YjyTzXOro4toRV6kMoHVMaUegtSTn/HDoVVQAkB0RzHNmYgr4/sUT40+D47v3bj29qj66/e7x+Z17d6f7T2++rkTL5+6/8dYbi2b8zR+tJoJELqDUa/Wg6lWBkQUmxhaATZEI2ZFq1lKgiiNQAVPQqiiERvM4sA+Iwk5zSuhAqNs+3XGyWgqQSE5ENPaHaapduyxjdd7NU+1NoOD/4+e+3hDe5HISFuAIzRCwqrzx6N2z8c7px18O1cDo6dXhpAVkKzkvmvb8znN9yUyegE25ptwsT8xVBSPyfi0nr5xt2rNUiYCI3Cd/5Hv/p56RfRr2pGgOlGFOPWKd9gOQzFP2gEo6p+n+57/XPCBoypdWixTNqTrHFWG/pWnWzdlZbGLbxFKK83Eu46Jb9GOPAPM0OWYqpRxDsI5HrZoS0vH9GQEJsdbqnXPsTtbdPKX15rSW1C5XzpkPpOBefPm1tx78FFZ4MO5++COvft+rH9VBY0txEbsCquKZ2ZGphk2Lovs0nTYhOvD+ds5lniE2TL7VrMSQp9S1C4AgksAcOByHMcaWyCNizpPUIllOz07neT5mhhzf849PbgcYXOynQ9s0f+r//l/9qT/+P6MyBjoFNABidmps5sg555c5ab/fP/jK2yfPvXqy3PuXXl43dzGwW4SjdC7fHBw7/IjN88SLOG9vto8fmebHlxc343T3zklL+r2f/eR64Y6PQK0HKWXaz4/2+83J+c3NTWjGm2EohoCUawJQAEBkRBQRZg4cvng9fPn9vx+9//EfvD8Nhx3J3Rfum5mhMxVgRCCp6mJQVXZomCgEqjz11wj8+u/+QU4VXShjict10drMQbMuQJwLFSrU2sD6RGEcRjlMZ+uNSVrHmLY3fPusXXSLrhOtRSsYpjQRYhUhRJHCwD62u/2YITO5aZ7YeWI/DymFCLBC8IRhnrfr9d1+0lOpzs2ORRX+1s9+0RxO49Vf/OU/9+/+7/6It4TWGIQ8Zx88OUZVqIyEhqCaSF3JSVWQFMHXLFYrAEhOkioyet/UkqXkWufQLsZcbBzyPEz7bWy7sZ+C96WkVCl0qzEXYChJdodR1RofSq3P3Tt123lOOSKtl/7iAC01WYaqMD3cA/hG6Be/+OVPvv7iS+uzUCwsT2ua4yLmnJcNJ+WSJkngXE5zpnYTmrU77/bX29a1YCAiOWUdsnc07SdD7w2TpDROc5n9um19fPzWNxddu7p3enr/bpXqnC/zttYbMzJwwzh2i9X++t2LqwmImkhmmubJe9xeX8bFcn+zm/PEjP04uFLKt6RXhIjVCgKagZkcPR5qgkBSay55mvZgQXJPq4CkJgaSV8wyTT/44Q9Dee8rT9/7vh/+7OHd/ta9UG0SVqPcnJ2KFYzu8q9/ffN9r8wf2nzu5FPddv7cRz80AWVU1KrK85w4hNRfO48GQghqxQU3H2YmRwhEFcTQgNW3nVfTlItzTqp45g+yCAwNYE5T9BGBjJD1OZFtSjvnvfedmDEqmNU8GoL3Xdfe+tgP3UFiueDpathunzACPJYIKnMapr7MZXPr/GY4hFV7dXGFLtyUOhPdv39vvz+ctN3t1cqwljxbrjXHeRrfv7qaVM4jrlbN45urUmutIAZgCEAAKiqIcLQNAFk03IGM1aZeEKXpzqZhPLt1x3FUzWAGZshUa2HnEYHdhlnKeMNQu8VSRNm5aTgoIpTi2AEDeMkiHEinWtLBdw2Riwyw6NRyTdl3HoYtOYqxqbUAQk4SQuN9rCU1bTMceq1VRcY5cSCdIJe5aUIBUaRvPnyqRjG0KDIcrk9PN08eXy3WG6TStVSylWqg+SQ2aaJKrqJYQslDjAsXo5qZAJgSs6oBGQIamCo6XgAjOk+q7KjkbLudsNU8a80oBVUZWWqBWq8f7EzVeV9FVJIqIvPUFx9wnBMRnmw2a7PoAyEy4TwN41jaNjTOSS6qmmB6eDV096qj2qxPnsv7rg1f/dpb9f7uw+cvnsbo2UkqbdOmOgFRqdTQLmeNzcLAzIzYrU7Pbh4/unV+J+eUc05DXzMCwDRcRO8OeQJmsdq/+bBdtev79+5+6CUAI+dIBxUhdm24u7+ZhuHAoRv6dLNLoLJaL8dpXC6Cqs7ztFyt5pSd41VY7ve7RdcQH6XmR/XGsQ8JGRGOcuijxsNA9ZgvwkHUiopWLXmq82w1D7sBKi/Xa/H5T//7//vTl5ev/QufzasJz5leGLp7+txr39fdagpU//nNtJJPfOLDH7v9wg987JNxsVqtGvG1quWUiF1Nc9MumuDBSpa9lTyXVHJih8Oul1xzymASAs4pTVNf6ywipeZvx9DD0SYLpqoAcO/8zv/q3/kPQtsyLhAiAhmIWsm5NzA0s5qd9z7E4IJfn8bTE+jQHEsIdnZaTjfhxQ8vX39dNpv2zrl5BN/sqynT82dn66b52EsvfO71V3Ee880NlZrmNAwDO95ltWrTNI1jUXVFFUAdo2OCb4WNHWEOKrWyEYd+mK7UO3/r4nrXtUFlrjIQMTH5LkqZERABS0nstJYBlMNio9ygc+Kd32z8YnXIQ0q9Yqk6e09pHoEsLrqmXSYdpEVkz8CL5anXENrbZZpUqQgYeEKyWmrNaFJLcuyAuT9MNVvNQgSLrquinW8d1r//jbdLzoerr2F9M/hFE6Joz64CxsOhfOTl23LMNQyeyXWx+Yk/+X8GmE1nkTrNfS0VAJG8qn0QEWcmtTJH5wLHAFpqySUnNaUm+BCICA3mMm8P+zHn3fXNkwdPHz58mqtWowfvXai4m8trFBPAXEdmabum7RpwCACOKKXhf/6v/wvE4AlRjRHNrHVx228Xm6Ucdss2Tv0YvPvRz3wyGr/x/ptvvf2li4v35t3Fk7ffBc8htiGEw+4QYldqJXaqSt6Bd7eev/f46bv7/ZP97kK1AuZp2ocu9nMuzAlwff7c67/5hz76/b/5/OWPIHccWjXwcWnGQN3QA6BT5JrzPO4BXFWqOTH6nAuoIcKY8nAYS06p7xmxVnFmcLQNEjMhBB/h21nvdtzGAIaA2nWLqXqCkquxa1E8e6xzjsvF0G+nq/H77r764K/9faZkH7u+89rHp/21bPP2ycOrX/hP68UTubGTu99jtrNG7rDQurhFtHm+2222N9fBc02DmqUpmwqTY46ZUGsqqTof4rJTzcN+a34xFlEB5wJ4NAQRFRPvvKmqgoF1bXec1qSUjLHMT6FZBfEAyt6lOYUmBoB5HKSady2CIjD5sLp3uyubm/ee6na6vj50yy6esIth7GE6XCVTYatJ7j3/HJUM0vtoFGB3sV2entRUxv1hLmMtu2GeTk47QxmnQVSQ2Uy7QA+eXBgyEgJUxy4we3ZS626/RzTnm3ceD6cvdZt18/Ty+t7du2yGqIROkgGzSBEV50hKJmRmMjHGUE2Jg5kB29p1aRqlJoRaSg4xpGkOMaRpiD4gOFBF35ZxzHMOLeXDFNsxhBNQkTwpIYETVROdDkOaK5gpaLUKxIfDuF4tcy3jMBWD4H1NT1M+PT09vbiaHSzX6w1TvLm6aMLqbN3uJ2L2SBZj3B7qX/8bf/l3/OhvJyQXwtyXbrERq0RkJiJEcEzYdBhcnq9qSlJrXJ5rTiKjSilaUk3b/fbmZlsV9ofJBc+OtsN+Ce2ibfr9vh/mIT+2Y+iai5v1CTr6xa9+ZdNGInPu9N/5E/8JhwUhLtswjaNjZypff/wktMu0eyKWr7eH05PVNOQX736ITG6ur67ef3hFlLOevnJvLhOg9/5EtVNNJatzpmyEYOTuvPSyzPPTB+9rLkzUnSzG/e7k3nlzcgeYfWhUtUrt2g4RVYuU2h8GQpOaVKoagPLV9c04lhBXbdeIZvJgqs5BvyuRIyD0afTMJZdpnp2qICEimakiA6GUjB/E2hiAEjlAI0JVJedZGB3kUpeLTrM0bdfngdgvll0di9fYbu607d3yzszJe+89fRgi4POvwfMgMAtN6Gpcrc2YvDhcpnwAhanvFyenc38NKG1zUspUy7zvp1VY+MaVPAOAY/LNcqp42O82d86H/VDmGdSYGdTADIlMj+Vs6NhVqSKyaNtf+MbVp59Tt154v5SStUoaZDpctt3C+RbQpEqRyhwLCAVevXSOH+ZaTGp1gnWYSz/EGM+ffwE9iE1YjaQ8eTj5GDmE0/NbRRVIQ2x857/wSw8cQykptoumDVfXe0RDsru32k993/f++D/7Bx49efiv/iv/5v3n7gNCLjLPc4xBlR3bNis6G6fkTeu5EYHzsZQJmQnV9PioRbAkc3HkUk6KiV2jBs5FsZrqxDGKVlKtkvvDIWBEAwYb+zF4bxCjIwIEBfK+6zZ5zrHtVRBQpZqxkyJk5JD241StouuqSUNBgikRZ/rlb15VhDZ4oqVVLdX6Xu6/dDdNY2paz2HIuYvBhXa73zJAyWnh+We/sjs/+canX3u1aR24XMtj8t77M+SAVR2FEDxozmMveS5DMRdKSghSxjmPwzzVaehvtrs5VTQk9rvDwN6vsNsdBha1mkNworZctGHVhNh2y3WZD+9djc+dn15N5Qc+94lvvPnNQ18aBqy6btt3doMZrjenl8G6RYsx3jk7d42vJNthXER/srnV3n+h26yQ3M2jq+WdUx/jcDhs5wehaUWZ3UmaJ/YOkAA8LdvzD7UmGZBMpDm7DYjI5gOrTN6zD7GUHom11nkagud5np48fsTMSHA41KdPx9hEsWm16pCOJymPkzXNKk0zEtZJk6knF5olMTMCocExhgPMmI/HMiAd30vVzACQCA2qmAzjfNj2UgVNpn7KpcQQbQm4BjohdanMV/NwIZiLzkIjN8rrgutCG4q3l25zNmVxbRRDLXOIbbN0i9azzSerTdss5zRLNRFom1a1KrAhx27RTwphxRgVdd7vmCGDIZEZeA5EDGbHITYismMVNTAm95/+V39zLu9IGbRWUDET55gsHvY9AkqZkdl3TaojoqWpOBfBgFAcqprYlNarLvgG+77st3WYx76fU2Z2YGSEcX2aU58nub4eri9GbuKdu7deeOGF882GoE6p1lJzzjnHv/E3vvaH/rU/+mf+T//RX/wL//HZGkutqtWxc+QRNGV5/Pixi0vG3Lbt44dPmqadxz0AqM7z0KuUmodxvJ6GMaW5SkWkWnIpucxJtJQ0Hl9CPvifmwtNVUxqqVM/Rt8AUJ76NPXjeADinEq/m+ahSKFaKpELodGSiDjNOaW83KyLGXledItcS9u0wXuK7Re+8c1SChggrW7df9mAu44YpYlxf/Gu71ZqsZ8mBjtZLjwTIx/vl3faBw/9YTf0/eGwS8Ph5vLhuHtUal/qKDoPY59TyamIiY/RiPI8V52K6XjYlpwePrxQ5TFjTcrkGFxKuT8cUp5TFe9cbJqsGEO3aNpDf/n3fv5XN8uVAmrOP/8LX9pvZzJtvA/BRecIyTCE2Pzf/spfr7pUgAxTqSXV7BZdVjAmBKjDNE27Uw5wmDWPXaBa02G/zUWSIDKhCQOBiOQaQ4PEjA6BY2y7drlYrsBA1aTaPA4xeMkHqzUGl+beoKxPTtC5q+vd9famW0RASOMAVp0PpgYqVaWUGmKYpzl4MuSi+P6DS1JTRFRQRCbi45cwERMxIRMxAAGASBGRv/qTP1dKFjHnnNWUUjYV713SSU0nmUpraWUZa1nRdX06cg8nLre1+Fp8tqjEQlSbRVNrNjBqIjHH4MmBjllSMqGSUlWTWiTPwzxM8+x82N7snQ9IPKX59p1bbdvMaU45lVpiCIhwDMT1PgBASnMt9TjNLrXcO7/37/6/vqDrE3NcrZKjolJEvOtqTSWlowI8+Ijs2+Wq5AwGTOyct1LJ0TTsLWed59gsY2jaGMxMEQQNVOdhb+q1Yan6+OJyf+jPT86b4JFssVwbwDAVVbh9Nj14/IAQLw98efH0f/1v/eHt9sY517Stc8GghrhAChc37zZhlUo21GG/MyHGTUkVDUs6sAOpueRZ6gygAIzOiRTng9TiQnRUDeZa+1IqN546732oVeJi1bTL2C4dUdWqqIK5H/dS5xB46vsQIiGqmeQipSASxWbMOYbonDODqmoI4zyN01VlFhVRCaHLc5VqXdPeXD8FqC7cfenll/p+e77azGMa+7nxsY3BOyair3zxzXZ1R2SuY2VYS2oDrnZXh/7mSZW531+l+VDmIeVa1Q7bJ3XaS+73T54+fPPN999///2HD5arzZPL6znN/Tx79t5RrZWcN2Q5pmkixBCJXa152W0eXR5O100/zsH709ieuEgCTC4wt8EDANRp2fivfvOdFz77aWTc7Yd+nH1ob/bbuaapTNVMTHxBKEUPVzrneRqWy01OFsIypzGn6bDf15rNhB3N09B1K2Z3nBeyd4joHK83JzFGYhqHQQQUZRx2AFBKBdZac/AcXPDOp2nmaE1LhNk5LTURSgy02/aIcZyZjbqmuf/8cw6BSi3eOQBgQlMgcgp2fFs7fgrjBxIaerzdIROAjmXawNI3sLu6IliE6C1QF9cCGFfr/fUOUuW2a87Ohuuni2UnQOx9KQVzNlN0XIs63ynUeX/tgqumFcWxS+MIkD3xcUQ0HPr1+vzQT6vujALuDwcAPez7ZRMJMLIvNccQcklHJ/Oc5hgCkSslV6mE1LXdkGfftCVTsMG3nfMh1epJ8jh5WbFrTDTXeXV6XlIxAXIOwRCg5tSsVs15s7z/QhnngLFYytOOsYjS6a1bYdmkuV5ePYhxM02HfR1v9v1y0TFn0JkQ33/4FNCWbYto89WjP/S/+D1//i/8SsP1P/o//Mf/mz/xL/+HP/G//Hd/4i/EEKd5FINaByT82oOrj945VQmEMiVbBJ/yoQoRpqZt0CoxaVVwbhonB468D/4E2cwYqoawRgNcACgIqBkiugBgolbnOhYfPRnWcU4iMpaTl55jD77hXGpOKRAHspytpDzNKaXqYrzZ7Tg4zw5EI4Wf++KvdG2Tk9Sq4zjWMjjiufSbk3Bzc333/F6et3kqSEFmAcRpmjh4RPTeX14Ngnm1vDvO25xnIFg2q9BuVOnBm2+sTk9Kmpm4VslTHvuJDPt+t9sdxBEiqwiCLbpWFaJnRsw5ERIACIIxqllofLFap6RQ5nmophF848M4V0FFYCXqYhyHfbNaAAC7MIxpvVn/4i/97OsvfuhkvUDyQ+pbH9DZfuq9J4heQFMmAB6fXsOKx6lvF22pBw6NIXbLJSAwsmmJMQ79gZAcu9g0HwihwEpJOWXvSY2C74bhiY+8343O+5RmZgCtw7SLIaQ83L73Qi7lcLNFdmbUEF9f96vVZr8/INX9nN9+dNE2DbFzzA7ROedFAckpGBg4HwDxWxdaVFUBMRWZc7q4vJmzzTntDhOHDllLyUjkm459o6Usz8/WZ6dd19U0t8s1OvKBETCQ8+0SPQbviIEIpIBrzowa4hjakNJEaE1ojknOAP7szm0DWJ+cJClXTy4gp2XXMELWWlSQjZjmNBMdOy+OplNCNGZmYmZOKUOtIPan/sx/rtYYOFUNjph4seqQyECQg4+LaZhVDEGJjJ1D4BDWZFxn0bGwcalJU2m7jWQKzcI3DCaEulyex8a5gEMu23G4c2/FoMHHp0+vd2nOuZRamO39p/z7fu+/Mo6HLDKZzJMlA+cZ0IgxhmCmTLQ/+HeuemSd5/LoweNhuAExz9mzz9N1OjzJ40PThCbdslNVAzBTPC4Bo5YKBsE3QMjIbGhmUjI7Uiiui+QdMKWSfOTFZuFi9s7yOEqaQGS/H+aKRQyDY+dD2wq69clZt1iHEPpDn+b0uDcTPFmfN+3S5gHFp/lysfAEQXMQ8zcXDxaLk7bhIc9FFRlFpEqttc5qxBDaulgvm64LsTPLCJVcObt7utk4pBlp3O8f9Pvrq9328fZmP1VetI7Dfj8zRxeCADBz03jHsOna2Lg5zf3Yo8Mpp/GwZysq/dDfPH7rmy50JCYqk6QR5b1+1+cSnN46az/9+u2j8qEJzqH7qV97dxQzxeoUsh2GPhXBEC4Pw/U2zwnnydKs6ZD31wldNNWpv6ppQOYqlvOUa3KOxaqLMTStC8HUVPTYMmMAzlMtFRRLmQhxODwFHESm2ECMKJIi4zxlZF/zPPbXQDJPo9RcS1aVB08eV9NcyjCOBjaMM0mtTI6Y1YyIEJHJ0THkhj2SR2I1cy4gYAhhX6bQnD5+ejOPxYWW/dL51vvYdg0DLNrlcrVxTGmemiZE8mnug3NIwGjsfJFK5Oc8AmpVJUKVrGBVpGQJfplnKVlqqbXqnEsR84EP/UFzQcdjklpyGzqomLLMWcxA7VgjjkjsnFOtah/AjkWF2AXvHlzvLicpc645a5ljiOw8IJJzYoqE7KjUCUCZHRMROjIGYaiIiqDg0Nec6pSJPYqKVBATEwCbc3p8eXjy9HC6bgl0zvnB46u3Ho/bSWuFquIwPriaANKDh+87H1Oehz5fPu0JwZFj5P1+H2NUNTH9b3/+G8RWslTVPJdat1apmrJfKSxqaqxCSWnue/Zea0UiKQWMoXrOoOOkU4ouMDIhugzL0No4lWF2ZjCXq4ePIvtaZbFqvTtJc3EAOUsp1CzPFEMBoxiHedoe+mSSVIZxMsLYxnmcH/fDsmlFUUSt3J7TuOjuTvMwHeb1gsHmX/jC9cXNVbH8wgtnfZmdY+fdsTmg1DLlySj4uHLBucBG6hrnfIPIwzg13aJdbW4/9+Lt++cf+/iL5yft2WbReTpdx/OzRRMcATAhMR7DY/qpN5WujbFxTeM2J8tu0aKV3X5bpbbLtUhNUoJ3IcYPvfriZz75amig8Xbv9OThk2sAEJNpmhzTz3/1Sy6RpRqJQ3Tr1XJKaZoyN23cLLOykRtLcaH13qcp+YBEMk/9od8O8+RjS871/QEAvCMFUzMOEQj0WN+rWko1ABFJKZv5ENdqvO+f7vc377/34Go7jtWQfQjtPM+lZDDvfUDDXIDIZYWL7eFmyI4bqXrr9gr/pf/JH/x2LvTxLRqOg1QzM6umx9MfAdsm3Or8h++ej7lcTeMyxt//Y7/VK1KILi4RlEiQvAIgM5TC7AABQU0I0BARFI/hOIgEJioZiUvOVgQAUNmKKRaAQRNpCKCWdpfcLiE42w7mWdEb9OC4f3xzXe2tJ+/+S//2T8AznvHdCgHAUfMAaAAmpvpBsTcaHn9rZmBg4zTNuaZcUpoXi/j7f+cPsZCjhSOHDoAY0AF4AkIxpKiIqgB2TPslAGc6mgqiAiWFCqxAyBzJRfZLLRVbAw9aHCBYdTWjb9aOnGU1NJWKJIjOcmXQKPX59fI7uXjPeMZ3GgcASAQAdPStHa1/AGBGgNWO5bGoqoS8auPlbnv7tHv946/jXnnhMSgQgRoCgQAwIhIQg1YgBfCAhiYgCdlh6MAyWDAzIi/VmQEQABX0YN4bKvmFRbKa0TJFhdFkKswmLiABguOI86xutWldQcf//f+8Zzzj/79xAB8E2H1LEf0P8UGlohkAqtlYLToWwJfCwvuFI2YXyXkxQVJEj6hgLKlyMDgaJI4CYOq+9VhoiACqM1QCVEJ0jExm4tcLq7mOibtm2mUSAxNqnNQCBs63VRRMdNbgFkCTWFb0/+SX7BnP+I0D/eN/+639rGBHbwMSBu+HKUu1JNhSp1ggNgAqZT7WtEIwRAVXqKlKFZBARVWBFBANPACriEoFACDCaNSwIalUA1EtpkaLUAViWKJnUwJkaggcVJnsg5DNrKUKMPkI4dkGfsZ3Ne4f+1tTAzRmJqvExEoKlktZN75p2t/7+R8FapgBbdRC5BwYgFQQMGgRTbEQdUgeQBCRGJTAVKxCDMtqScGIAKABZMDK3KCqAakzKQf6IGl+BqqaAZ0zBDKWWupu51YLWDLPJmaRm3+yy/WMZ/zG4gMfkn2rFxgBFYwAU01jmkGqilQpTIQICBD8wo+OfSKYQJQIyXkgBAgEUaU3JlBGUFBFxxDUWBirA0Ci7MzQsQJAI2jAqqCmqljVxLXOxzUv17bwwj7EM+7IfARCtASULJAYWBL0gX3j7R//BvGMZ3yXQAJ2fFs+NtcbGAEaQXSNZ0ccATCEiIimyoh3zhtd9mSGvgUX1RgBiRhZzTtqW9CC3gM5sIqAJoTQKKA6D4qYFcgUDqoFkYHQoUdmDA4IpGZQqXUbOfBqrdGMGGRGpTIzW8NMDGBVah3IV+ThO72Az3jGdxLSY4/oP4x9EO4OolVUc80pJ2ZOSb7v9d/kigOFio4YnBegaEZmDMDA4Tixtixgpirggkk1YSgCkJAqmGd3imSEDIJShZhBI8amymjLhdvckgigjoOn9dpU0YTZWa3sGmwddEhuYZUEn91CP+O7mm9b+f8hjnFNBAiAnj/4Tm7apo3k5isXPIAjzCogagAjWEUFtAxSTBUUgARUwczqHi0TOEQGAyI2PAAGs6x1tDoy1zL3KoOpcLPWecAq6onaIOgkKYBTBKNRUNRQa8FqeR4UAODZBn7GdzWOiI7GGkI62pLoH5glIUKMjZUkVnOq2mBwvlAlb2AtqIFDkQPUlp0DUOQlgJgWQo+GIoKalBmOWRIMpoXIi0ygbEiIJlXZtypqqQIQqDM0TQWJXIg57QERSLGJUMCqoAFHKtvBgvfPTuBnfHdDaPDBYfsPXmV9a4YUvZ/msZZqBk30P/DZ10ULO4ck7DIxoiTC4IJHboDXahWJzFTtOBoGch7JIyYztUomGUVBBUEBE7AiFTAgVggEXIkrAsa2A0UpmYmAQJQAVHNGreSl7ntlE5KU03d09Z7xjO8wDo4aLACADzSTejwtEY8SbDU7lkqXYp/42Od9P2E1IG/iABM7bybgnCmCFkQDIYetOgRjJiEXAaJphZqAHSApeIOtVWeOQZk8Ss3HlFXnuBSxUqCK5CK1ODTqGh3Y7OAQyjgCeykA2YCJmvAdXb1nPOM7zD86Bz5Kr47q6GP52rePZXbOBSOo5IUjcyDUqBSBGnOG5EyJWKUW8i16xRpqTcKEjIYOzaNmSQlxUnXAQFYkG6A3naBxUHNOlTgws0hBV5Fd6XvNPaLWg5BTDIRCJfWIyISF/tGv92c847sKBwDHwe+3gx3x27JKgiL6bTXlMPVs5nwAKsDeIJB36sAHpm5hJgTeoGhBdGwG5sWHVkAde0SsJYkBIJk5QDWpUr05I65WteZJcuuDqykZgaAiOBt3jKjVDIx8MBBgo+igdKyW56L+Hy9EecYzvktwYnrMv+JfT2b94F5a1VR//Yib0xSA0ScI3kjME1kEZnNRpZpaqVsrgowMUGN0BcEBiqV8QzGCo1KVO59yznJoF6fkx2EcKasYTv2TaA0MoXEePBOFPBVnOpcSFqd52kFg7Qs5roFJJ6a2pGTw7Bv4Gd/VuGOT6PEOC/GDHDsFlGNcL6KZichqdfIv/ov/tFg1jxyigdcaZOEQHRCYqIoSejWjKrBeQe6LZtIOoWJYlHk/XFyUebu8e/9QDqy8H79qdemYh93Nk6e7Oy+e72rarBZpzlQookMdpHocq9Ye5gqxMZksYhrRcSjjxM2qpMN3dvme8YzvLAQAjpj+YRvSP+JLCn7BaN/36U8N6d3d8CjTaCdCJ1QtV+u1IkIxHGvN6hU5KgxaM/PCZgEopRyAYMozdCc3D76h+6u8/ca8rYfxq1fX7/qVP7lTLh992QUtZcBVVzlP87VKkXIwMGUjh4Y7gJ4IfTqAkkaH0IdN+092uZ7xjN9YOAAQ+2D2a2b6rY1LgMWUPTmIP/4jL718t7zxi3+pbZeCuN2K78/PnvPTcDhZr3N6GLszA8UqniMFSvuD820pl1aZGXU6pJLVas0lLm9fXl2lHRR72uoohJtu48LpvXubXEudp/7h2+H8OQXfjXvMHTmUKTvPVgj5OGqu2LYhkSgHfjYHfsZ3Ne5Yx64E397D8K27aAAgg4WDT37sztU2D/O4O0yr7ny8fvD8h9r3v/Llk9v3xsPsg2qeyEgoVUWaDa2qDsAO9Gq8nhmcJCPl/vIqLiEf9n6Mq3u3m+ZWFmL2Ptd29aEQ5tLvyXlwNlxe7/t+3TZsAKQ6CjaNMph5iIkzVaomHcgzM8MzvqtxAEc1BxyTdH79KDYDgCp6I7VXyuN+3icfcXvz1rjr9K3Hy7CayhvNvY8Mu7luGAwY5xA2rnOgbRovsEKesh0Ow81UUp1zIioO790+P+OX1piFPHjfxta39JyaOnfmFo3aMKf96uRsTFNGs5TcwkuxcAZSQYSAujTchNWSl7GAfEdX7xnP+A7zQSLH8chlpONI6YNsfwMAbiMN11cAq5c+/GJEuXj0yLVsFaVBlHZ/eUV0U/qbsG58sw5hZSpgc2iX082l9n3abqerlMs0F0Q4+G7pcRUCqJEF7zhUJpxGRqtgziLw7Fw0i/7eS7u3d6vQBrfSZq9qZhXZlzyAM60IOHGz/g6v3zOe8R3FHZvh6ChW/v9BJScBdSeSlQo1i9VLL97TD8m0vdKcZMzp8ful1KZNdeiWzy+tHYm6nJFQXFzWknDV4baWmxtevXL+8VfTyN/4mS+uCM5f+6hXrLWXR0PZvXf3c5+Ws9sQGdVcpnncW0mnJysHDjxD9SrCjiko5MjrUxsHmrNa/09+yZ7xjN84OEQUVSAiJPi2LcngmGeVRbDUr71dPvuR245gvry20FK6qpcXxK7dvJpOqQm4u9yxW6W5nnRrRAwYtZJrOMwRwqJv93TnI81pl0p666e/+tEf/02/8nf/9ptfevvFV+InPvIyff5jzD+cxrr75S9hWJzdPRURJGWFECIxkqvMTZ4mbhrTAnOhZVTfg3UC5Tu6es94xncYIsQPDEmm8ut1KgAAZhZjLCJf/drXpjLLVK5+5cu/9jd/ihfr5fd85uw3/WD38u32/OTy0bubl55T1fkwaWKthl4QFFUtiVFYvvjKnVfvYZrw4uLjP/a5hz/5S7/yxP/K/vK3/st/+P/6t3/tP/8vfurBz/7diHT28dfwdvPOz/4i+oHJN90p+sSRdJjzbs8iOMwunuK6UShWkXiOz4RYz/juxsG3cqH5H1BTHmdJiGhqTPzo0dPN6mx4/Gia7YUf+Ozf+dt/9+t7GHL5+P3u9/zYj93/2GfmPivS6b077AgQVFBN5TDBzRBfOtPd3qrS4jye3YXdBeeLT3z0U29e7f7wv/FvLZtud7boXn39jb/7pec+cnutw+mPfM/1e4/vnL2WV2huyU3QixraSE7QtxhcOL9TLp84vzCtYvk7tnLPeMZvAJyo4j8solT89Z+PPzRd/HP/5V//A7/rB584P3/zTZ3ivuZdPzzRD/9nP/el79mOH/v+Ty82vm06U4M6q4JMe5l3snAokYqYy6cvLceLK4Llh3/3P/18e/6jG9C5abxVKWT98rd8ghWv33wfdteb+6/Wk65bdqUqE1W8zf1gtqVAKLOSdw5IqWaB+GwO/Izvaty3N6990GMGZobfknOoKQCA2IOHN67o/Rdvv/+Nt2+f37uP84f4uc9++rWPrsbOnQ5PHsMu8okjECPEpgGtWDMbCrl4+4Uyj9ZPi1sfrtut77DpPEDgdTTDhlDqCaKVNN969XNlKrA7cJpcgFoNm2U8WZS6g2mjM1qdiQWZCCuC8PwdWLJnPOM3Du7bFmAFONbDAsBxgvTtcsIqFQjjeXPXn374E6+H5ekPRmBS2E8+nJT9sNisOG58G3Q+mI+URyKn5sjAjQOebpxf5R506AkY6axtXOVGx8E1DSRByiBTxAjtIkZXumXVvWiglGMjuezJcLZMBYgLhlMsaEMlceKf2Qmf8V3Nf5+S6dt30iLqiIPrYnMauo6asWNHtbIPKRUjUB/9yknOGBtMoylKPiAZuGpdcIGZuN2cIiJ2a4axllrzBOHEmC00yi3GW6ChDKPMgwOJ8cyp803USW2bwcXQbrhrNLZApRQRMggEWv9JLNIznvEbFXdsHgQAtWMZ9K8LKr91GoNjAnRlzjzP0AbGztqsciBYMnnrYgQl6AgKKAE6LTtIFYv49UYkWT7aJWx9djul0ZiKIBqg7vK0d0nD6oU6zZZ2VitQS4QKjSFr7UEj8kplJ+OIE/GisWlr4wTYagF85gd+xnc3//gNcNzG9O09TP5/+0f+4HK/4wYtWdFcRXx7V8oAKjL0zXLNIKqqtco8kTMlpm6JREgLUwAyEFV2Ma6NQCSBESpGf89wB/MhYKu29B1KJqszTAUbNl2AmkgxAcwmNeNQbKgmVecB2q7oMynlM76rcWYAaAgIBkjHakIlJFE1sONAyXtqtzdU0MdWa2EGk0l2o2oBVWKHFdQJqNOyI4BSqw9LI1NSSEXqNbZ3DSfAqODIEDN4xMoVFYA6EoGS0BSFSclcC2glT1YdAlodNc9lnr13RqAumFaMJDkjPAt2f8Z3Nb9+AhOhGSgaE/8DSdGGiKu2Obv/kr732Er2IdYpsSNDX6VaKS4COUNkKQOFVnKCBFl61218d0qdWl0DOORoADb2yB4imbIqeecBPcioWsAHJRGsyF60oFKpByyGoibomk7mycSpilSF4ogh7Z5JKZ/xXY37YGwEhkjHmiRRBTBEMIOjUvrp1a689wjVE6gZE5pYRWxCcEKnTbckMtMZuSo2AGBYtJKkOW+37CNxIaeGLQHi8kznAknViWM1Y4IkRui8Lj3MM3qSWkyraUYmSww4E5DWoikDqSXD4nUaBEu7XnynF/AZz/hO4r5VC/zriXb2DyqiCcHsj/4b/2ruL6Pz1Cwt78G5sNiI2rgdui4SBWKqxUAN8yhzslHBR/SNjqXmwTj51ca1hdqlTQbkKaDRMXGrogA4A2ZMouAMwbch6YxKNmeDrAIIyj6Yw5J6UDbFMqlvdJq+U+v2jGf8hsDBt3bvP5Lq/sFvFNHjrXQVfGBf0QX25+IUPEnaO7fwp2fQBi0zt+uaquVCmDT1rjiaCZQ0V0Zf83Zu4/IE2DUYvCIxeygKBgYGiY0VGEANTfM86YzQH5AN/r/t3cnvZcdVB/AzVNUd3vAb2u12k7atiMQJMchJlBAkBgnEoAgJIjYsEFs2iAUo/wWwyoYNYktgjwTJKogwKAgQEZCEhO443W633b/pvTtU1RlY/LrbTWyxdFv63c/q6e5eSVe37q3vOQeKW2taas5WGC1awDpNvA7GtVn6Qi+uNkJAB3dwe1zE/wQiMtF+2JOsjNbUbQBn6EJqeq86P9hh59g0WkEEJZd8dl9FVWpzdD3c6HHDvFm14dCnPQwYa533Z6YZSg2hVUJIwalF6h01NB0ENkeKyY2ggjcOoi5sJbsoxz4mQxPzGvvAq57bQ0pLT6zFlXZZ0A+AQI8fvE/lscBNvvCLv4Kogc1VMW0ZtY4n5WJQmYEP8+6BD6M763RuJandRUSlkRRRMm9S2e8hG7iKYPNCKvvTFLPUfUgHvuqxCzArhehsBBBWQbOhKIB6ZUUgBrcKhXUWFISIut/HmMK2kZkTv0cN82JxdQR4as+MiE/u3kdTvwP91EsvOwQ3BAT3WE8egAz59nfLbkPppq7vwxxVHGDQ8SH54b3v3vmXkzdnTD+e/KUbx6kicgirjRrhalPziJUZALmzQYgb4ss65MZJkaPlGroEwLY7p4ogmZCNnLwgM6bUJKa5EhO3k8T4LBdvsXjW3jvIQYiXlcHu0MSWYCQXkMbkwkVsd1pPHsyyO/0OXH/xxvj2g+IYA3zpq1+Pbew8RHNE/ArAa2f1pR6fa6/D+f3jn/t0bA6Z57I77QCFJ2yiAoEHN9X9QwqdRyDmOu/qnAkZUtDJL+9v71duxXXGFLhduThQsty8n4u1WHzQBAB4kqYEAHcIzKJ6eT1g8LMTOEoQN2BmZW/7qdy/M5z0R7/wmc1ufOvh2Rv37h9s281q8/tf+OlE/XgSt7eeq6U2XaQIaMYNUcMmDDXoXMPRzeHBG00F1oY4AwQKicBc9ujJxABjbEBNdZ4oBhcAUeQCmADQFUT2lLamxcPyBF5caT9czIAA/nicCgKaqVm1kjUPVicvqlKr9enDH2bQYnTt+uaVT/yYUHv3W2/d+afXkTfbj1/zJoWjbf/CEabYHG6ROtUWKRUdsdkyYbrxwiyzjQpKiMkUXRghuDoiuYB7APAYg7laJDOAyg7qwAgmtAEmx4itvesfLRZXyDsfsQLzZfGguhEiEopoNUN1iAwmVos76TCpyPpjL9Q6YptKvmjXhy9+9MXmM695RgzetEmDG8Bcarc9ANM6G7A6YEx94AjBXRW7wzpPnieEgrTRPAVsHVGlhNDU6RRDa3mgEA2UV9GqIJACAMYYUFwpOOiSxFpcae+8A4sqEz2pTAIlRGhS9LQu8wRYCVnmN2V4czc52EUtRtjhet1sDurFyNhYFE7ATeOWgSGtgpiWMvoG0CMFNrRCyg5aKjexTIPOI9Im8uSqWoqbomnNWc05GnTRhaDOTkCb1qGz3Q6pgKJFRmrqbilmWFxp5OCPwlj4dJwDL0+F1dyigAjECOQ6lTJclKYBpcRsPnFKYhoiSx5kmMs8m4uhh1WngM6MKRJFjBGYMCYkH2XaDafVJKwPNYWipehgbOhmymZMgRiTlwQcAQ2qmYvNe/AT7s2KeDCzWucSl6/Qi6vt0XRCQgJEVX0SpWQiNUO37ngrb5yDo8goYz2vcPjpV+aH+7hJ7ea4aWNgbg83joBkQOjVu8Pj/XQe20iobXdQJRObGOS6i826SW1YVW9XPhtQ8pohcuBGigAH8GCyRy5m0Sq4ksZjKxcIlbEhMOCt2kwBEZpxWrbQiyuNLmchmTuY4+NmlABw2WIWEdAnw8YnRA9KMR2+kDhJg6G9BlK9CiBpGVmEBWJpQ01edZ0OGAjNXWaX7MARvOEO6iwmlUmKFlSMEZtWQ4RAnBqKaFCBgzp6QlcjcrY9YeHQ1KrQHcynb6u4iakVpqWlzuJKI3ic2TAwgHcFmxLOb93lvjHLFBip6W7d2o0VwvZ8f+5mVgUuxjAYZgAlgsyoujv18YJH9d0+n7xNsBtuf1supuHknlxcnLxxJ1AjdcjzjEQKCoGKFEBzqBjVXIAjBCZPgOReKAVPnNxwuIhAkosHVDOry1foxZUWLvfMTzJYl4ORLi+au85w597Jj756Db1zxPZYp5SQCMaHHCIMxufDfFHk5Jwq9x96cXdyOgslZepKd31jm4aucd6dMzXT6X0HPdk/6LrD87vfx9WKYzNJWcVGHTAiYAAkdtVStGSrgQQ9OZpanqFJHlD2c+2CTmd1btpVY6F91gu4WDxL4dEY0ccJSnV78k0LwV3nb47lJYucCjQtJWx41ub5Ml7UrPlMT++MJ9PbQ9UBwvp/vkM2nAWjTta8Lbdvr+3W0fTW8fGNdN1gVVY3Dnh7oKrilGJoNj2YGe+objhGLYDIbtXBxYlIqWtNtXoEZiD1UrBNySrwNaBQdXA7f8brt1g8U4GJ4Kn+dUz05DcCAjR//2/f/uWPfcTXa4oNNIR81OJgXdBz/f6379y9ePuOTQdH3W//we+c7u611DlMGLqGOo6hlHkc7//rX/3d2W2zOuIFf6i3j37ytXDzuX7bYXAw0NwyYwyt1EG0aBargKAmIDQwEbFDQJ0cK1lQsFRJrZacp3a1RCkXV1ow98vuz4QEAAjIiOr26MlMOJeJYsQYiVtKnYKyYgwgLby+f/tNr2+V+vlf+tTFxWkfNkQO1MfIImMwcMQ+rtL65uc+f3Tyg7t/87Xbt2f/67/9x9eur3/mcx9LxzdCHx08dR0YuGQ0A0QHRXJsAKADd4Rqtbg3SBVkNA4+ClBtVn0u47NdvsXi2Qrw+NZ9T2aKxFXGKqsIxrQin5HQRfUsVwjf2j1Ap1V36+QHb3z/e7dfeP7al7/81Rs3r7/+4OR7P7h77bnnA+PNbvMPXzcK6bxURbr74P7v/drvxkbYFbKE9QYhuAgYaR7M2GQiqgAJcSQ6knnvBQFMRLhvbYAy71OfTJ24fx/XarH4wAnweP98eSB8OeCbEA3c3IG8jX06uF7zaL5GNOIQfdVECTfTr/7G4c/ffvW/vvv6l/7kLzBwVvvNz/7sr7/ymenBcOASXm6Hi7MvfvYnu1u38nkJ1LBwWK3WL6+agyZjpgiqXFQQwL2iojm7KiAbQcCeY1f3D9RBa0au4rNNDtCmQACACDUvs1UWV9r/1xjd3SMGd7l37xvPH7wieSpkTb9lsnh42KiYyurw4sXQ/tatT9i6+8p//PuL3SpuDtJPhE8eforQ9T/PetmOJx5yAof+R1p+aes+V4+xBS1MxIwEbDKpyIDI7tlBEVg9g6JbVCjKQXN1bKjr7PSkGFFahSDzfmkru7jSwuUZEgA4AME7cwovAx5ZhYn/8M+/8cdf/LhattJLHIUN3UQqIxUL25s3j0dOh8evfvhVaxL1SSSH3IJI95FroKXzhnpQmJAIsFIM6OLamGdwQARyMmCE6DaDjUAN05Yoq1TVEkGnaXYM6FrnPBXlVVPnoQCaLVHKxZUW3t3L7mkpJpG6XW8bOyr1Yds0xKvQNDJP6Gzq0DXt89sWo7URtyGGNZq3qZeIoWQCq3MTW4ipnatRyVlL5JCITQAJkNnM3YzQsRaV6iXhOhKDZJHspirTUKsCUWqcgq6eO7JcRsGax0S793e5FosPlvAkfGVmdtlVh8js0VuxquDlEXF5k+CgSkFfkzo6RsZSRveRuq0ftjEEx4yMRKEUaUKrgYACtBXMahCr6CkldXI0C0CC2JgLIRhgnXeItc6DqrbQgUtA92g665whtOl8nsY897BFyFlgqhrEytJWdnG1EQI+BkxEgPYoBf1Oaztm/MuvfTN2fRlGAnJXq+bi4MGAAZJXztNkGMETIkkep3HSOc+7XX7wRsmidUadYlBggAgUzJ3BnTAqMLgJpZzVOKTDA2IHmTQX2ytwULWc59Bgf3RAYRCZ5zKpm0azbhnwvbjS6D13zj9Eqvzzf9+e6uCRcylS1L2YzojCRFUvTCVuehNTr1VLu93EPsYUVaR9/tjZAckQTREhmIGaqs/qxQ3Qp5zHsnsoMgCqhwZC0stGdinIUNALGqW2UwXBLmtwJzeXEJCX6YSLK+3pE+BHj1z6v33eAYA5MseTMcR+M897ddNiTuy1BowUiBPWYbZaaxkJuRazUom46XsvmgKQ1hAYIRBFJDYPTuoYHAoKM4YAkIdaMRBGE3Ak8lBzzmU2wBhqCGne2TB4NchlFpE+pq7fvt8Ltlh8kPxwhMPADd5do+dq+kd/9qco0cVF1C27GWEMDiH2RhOAIca26SBAbKKZACOYIQUAcmDGCCQQQMBFRIFNRYuBsw6zuyuFtt+CF3D1UirAxcMTqxWg5aPj4WxH7Oam5Kk/arseDEyWjhyLK+3pG9gBnJ7aUT+9t2big+2B132bWrAMAMwdIgEqBDY1MIcIkjPszfcDV5/PzzkiEwckcFGR0LS1FiLXGECDAZpLHU/ydKqaOaUQOzDSWihxnue0iRQxXOuVhQOAYykZxBykShWo3bKDXlxt/wursxcfI/zmFAAAAABJRU5ErkJggg==
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Results found in file a-3.png
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>
----------------------------------------------------------
Searching for: Mark
----------------------------------------------------------
Results found in file a-0.png
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Results found in file a-1.png
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Results found in file a-10.png
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Results found in file a-13.png
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Results found in file a-2.png
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Results found in file a-3.png
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Results found in file a-8.png
But there were no faces in that file!
</pre>
</div>
</div>

</div>
</div>

</div>
    </div>
  </div>

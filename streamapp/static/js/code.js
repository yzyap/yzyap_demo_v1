/*var c = document.getElementById('canvas');
var ctx = c.getContext('2d');
var imageObj = null;
var rect = {};
var drag = false;   */

var demoWorkspace; 
/*
function init(){
  console.log('init fired..') ;

  c.addEventListener("mousedown", function(e) 
    { 
      mouseDown(c, e); 
    }); 

  c.addEventListener('mouseup', mouseUp, false);
  c.addEventListener('mousemove', function(e) 
    { 
      mouseMove(c, e); 
    });           
}

function mouseDown(canvas, event) {
  let canvasrect = canvas.getBoundingClientRect();
  rect.startX = event.clientX - canvasrect.left;
  rect.startY = event.clientY - canvasrect.top;
  drag = true;
}  

function mouseUp() { 
  drag = false; 
}

function mouseMove(canvas, event) {
    if (drag) {
        let canvasrect = canvas.getBoundingClientRect();  
        ctx.clearRect(0, 0, 640, 480);
        rect.w = (event.clientX  - canvasrect.left) - rect.startX;
        rect.h = (event.clientY - canvasrect.top) - rect.startY;
        ctx.strokeStyle = 'red';
        ctx.strokeRect(rect.startX, rect.startY, rect.w, rect.h);
    }
}

init();

*/

function fBodyResize(evt)
{
  console.log("body resize!");

  hpage = $(window).height();
  wpage = $(window).width();  

  hnavbar = document.getElementById("pageheader").offsetHeight;
  wnavbar = document.getElementById("pageheader").offsetWidth;
  wcontainer = wpage -10;
  hcontainer = hpage-hnavbar;

  containerWindow = document.getElementById("containerWindow");
  containerWindow.style.gridTemplateRows = "520px " + (hcontainer-520-40) + "px"; 
  //containerWindow.style.height = hcontainer + "px";  

  //containerWindow.style.gridTemplateRows = sideWindowHeight + "px " + sideWindowHeight + "px;"
}

function fPageLoad(evt)
{

  fBodyResize();

  openTab(evt,"bloktab")            
}

function openTab(evt, tabName) {
  // Declare all variables
  var i, tabcontent, tablinks;

  // Get all elements with class="codeWindowTabContent" and hide them
  tabcontent = document.getElementsByClassName("codewindow_tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";

  if(tabName == "bloktab"){
    if(demoWorkspace == null)
      demoWorkspace = Blockly.inject('blocklyDiv',
          {
            media: '{% static "/media/" %}',          
            toolbox: document.getElementById('toolbox')
            });   
  }
}
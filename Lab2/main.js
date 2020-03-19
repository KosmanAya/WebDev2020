window.onload = function(){

var toDoList = [];

document.getElementById('btn').addEventListener('click', function(){
  var input = document.getElementById("sometext").value;
  var obj = {};
  obj.task = input;
  obj.check = false;
  var i = toDoList.length;
  toDoList[i] = obj;
  console.log(obj);
  out();
});

function out(){
  var out = "";
  for(var key in toDoList){
    if(toDoList[key].chech == true){
      out += '<input type="checkbox" checked>';
    }else {
      out += '<input type="checkbox">';
    }
    out += toDoList[key].task + '<br>';
  }
  document.getElementById('out').innerHTML = out;
}

}
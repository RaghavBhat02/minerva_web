let counter = 0;

function count() {
  counter += 1;
  document.querySelector('h2').innerHTML = counter;
  if (counter % 10 === 0) {
    alert(`Count is now ${counter}`)
  }
};

document.addEventListener('DOMContentLoaded', function() { //DOMContentLoaded is needed, because the document needs to load completely, because this technically loads BEFORE button, so we have to wait till the whole document loads and then use this
  document.querySelector('button').onclick = count;
  // i could also say document.querySelector('button').addEventListener('click',count())

  document.querySelector('form').onsubmit = function() {
    const name = document.querySelector('#name').value;
    alert(`Hello, ${name}!`)
  };
  //Change font color to red
/*  document.querySelector('#red').onclick = function () {
    document.querySelector('#hello').style.color = 'red';
  }
  //Change font color to green
  document.querySelector('#green').onclick = function () {
    document.querySelector('#hello').style.color = 'green';
  }
  //Change font color to blue
  document.querySelector('#blue').onclick = function () {
    document.querySelector('#hello').style.color = 'blue';
  }
  */
   document.querySelectorAll('.color_button').forEach(function(button){ //can use any name you want for the argument. it will take each (hence ForEach) .color_button, name it as whatever and pass it in as "button" or whatever other name you choose
// => is shorthand for writing a function. "(input) =>"
    button.onclick = () => {
      document.querySelector('#hello').style.color = button.dataset.color;
    }
  });
  //the following code below may not work, so you may have to use a variable instead of "this"
  document.querySelector('select').onchange = () => {
    document.querySelector('#hello').style.color = this.value; //this means whatever the event happened to, select was changed. So this is the select.
  }
});

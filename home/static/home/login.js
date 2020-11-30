// Check if there is already a username, first name, last name, email value in local storage
if (!localStorage.getItem('username')) {
    // If not, set the username to "" in local storage
    localStorage.setItem('username', "");
}

if (!localStorage.getItem('first_name')) {
    // If not, set the first name to "" in local storage
    localStorage.setItem('first_name', "");
}

if (!localStorage.getItem('last_name')) {
    // If not, set the first name to "" in local storage
    localStorage.setItem('last_name', "");
}

if(!localStorage.getItem('email')) {

    localStorage.setItem('email', "")
}


document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('input[name=username]').value = localStorage.getItem('username');
    if (document.querySelector('input[name=firstname]')) {
        document.querySelector('input[name=firstname]').value = localStorage.getItem('first_name');
        document.querySelector('input[name=lastname]').value = localStorage.getItem('last_name');
        document.querySelector('input[name=email]').value = localStorage.getItem('email');
    } else {
        localStorage.removeItem('first_name');
        localStorage.removeItem('last_name');
        localStorage.removeItem('email');
    }

    document.querySelector('form').onsubmit = () => {
        //add everything to local localStorage
        localStorage.setItem('username',document.querySelector('input[name=username]').value);
        if (document.querySelector('input[name=firstname]')) {
            localStorage.setItem('first_name', document.querySelector('input[name=firstname]').value);
            localStorage.setItem('last_name', document.querySelector('input[name=lastname]').value);
            localStorage.setItem('email', document.querySelector('input[name=email]').value);
        }

       // Stop form from submitting
       return true;
   }
});

function createClassList() {
    if (!localStorage.getItem('class_list')) { //if class_list doesn't exist in the local storage
        const emptyArray = [];
        localStorage.setItem('class_list', JSON.stringify(emptyArray)); //add class list to local storage (the values here will class_url from the Class model)
        localStorage.setItem('iHTML_list', JSON.stringify(emptyArray)); //add a parallel array of innerHTML equivalents
    }
    let class_list = JSON.parse(localStorage.getItem('class_list')); //get class_list from local Storage
    let iHTML_list = JSON.parse(localStorage.getItem('iHTML_list')); //get iHTML_list from local storage
    return {
        class_list,
        iHTML_list
    };
}


document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('#add-button').onclick = ()=> {
        let {class_list, iHTML_list} = createClassList();
        console.log(Array.isArray(class_list));
        const add_class = document.querySelector('#add-class').value; //find newly added class_url by doing this: from the form's select element with id #add-class's value
        const query = "option[value=" + add_class + "]";
        //when doing querySelector, since it's in a string you can't simply do "option[value=add_class]"
        //because it would think that whole thing is a string. Therefore you have to do "option[value]"  + add_class + "]"
        //so that the value of add_class merges into the string. Here we just put that into a variable to make things easy.
        const add_class_iHTML = document.querySelector(query).innerHTML; //find the innerHTML (readable version) of the class_url (which is the value submitted (add_class))
        class_list.push(add_class); //push class to class_list
        iHTML_list.push(add_class_iHTML); //push the innerHTML to the parallel array
        localStorage.setItem('class_list', JSON.stringify(class_list)); //set those items to local storage
        localStorage.setItem('iHTML_list', JSON.stringify(iHTML_list));

        const li = document.createElement('li'); //create list item
        console.log("value:" + add_class);
        li.dataset.value = add_class;
        console.log(li.dataset.value);
        li.innerHTML = add_class_iHTML; //set its innerHTML = to the innerHTML of the added class
        document.querySelector('#class-list').append(li); //append it to the class list

        const delete_option = document.querySelector(query); //delete from the top select (the top select is first, so it will find the top one one first but either way it shouldn't exist in the bottom select at this time)
        delete_option.remove();

        const option = document.createElement('option'); //create same option now for the bottom select.
        option.value = add_class; //set its value equal to the value(class_url) of the newly added class
        option.innerHTML = add_class_iHTML; //set its innerHTML = to the innerHTML of the added class
        document.querySelector('#remove-class').append(option); //append it to the remove class 'select' element



    }

    document.querySelector('#remove-button').onclick = ()=> {
        let {class_list, iHTML_list} = createClassList();
        console.log("hello: " + class_list);
        const remove_class = document.querySelector('#remove-class').value;
        console.log(remove_class); //find the value(class_url) of the newly removed class
        const query = "option[value=" + remove_class + "]";
        //same reasoning as the const query in the document.querySelector('#class-add-form').onsubmit
        const remove_class_iHTML = document.querySelector(query).innerHTML;
        for (let i = 0; i < class_list.length; i++){ //for loop
            if (class_list[i] == remove_class) { //if the value of the class = remove_class then delete it from both arrays
                class_list.splice(i,1);
                iHTML_list.splice(i,1);
            }
        }

        localStorage.setItem('class_list', JSON.stringify(class_list)); //set those items to local storage
        localStorage.setItem('iHTML_list', JSON.stringify(iHTML_list));

        let delete_option = document.querySelector(query);
        delete_option.remove(); //delete the option from the bottom <select> (it's the only <select> with that value so it will delete from the bottom one, the top one does not have that value)

        let option = document.createElement('option'); //create the same option again but this time in the top select.
        option.value = remove_class;
        option.innerHTML = remove_class_iHTML;
        document.querySelector('#add-class').append(option);

        const queryList = "li[data-value=" + remove_class + "]";
        let li = document.querySelector(queryList); //delete from the
        li.remove(); //delete from the list

    }

    document.querySelector('form').onsubmit = () => {
        let {class_list, iHTML_list} = createClassList();
        if (class_list == [] || iHTML_list == []) {
            alert("Please select at least one class before continuing!");
            return false;
        }
        console.log(class_list);
        document.querySelector('#class-array').value = JSON.stringify(class_list);
        console.log(document.querySelector('#class-array').value);
        localStorage.removeItem('class_list');
        localStorage.removeItem('iHTML_list');
        return true;

    }
})

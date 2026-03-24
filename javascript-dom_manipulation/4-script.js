const addItem = document.querySelector('#add_item');
const myList = document.querySelector('ul.my_list');

addItem.addEventListener('click', function () {
    const li = document.createElement('li'); // crée un <li>
    li.textContent = 'Item';                // ajoute le texte
    myList.appendChild(li);                 // ajoute le <li> à la <ul>
});

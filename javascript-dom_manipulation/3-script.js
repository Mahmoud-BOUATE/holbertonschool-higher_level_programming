const toggleHeader = document.querySelector('#toggle_header');
const header = document.querySelector('header');

if (header.classList.contains('red')) {
    header.className = 'red';
} else {
    header.className = 'green';
}

toggleHeader.addEventListener('click', function () {
    if (header.classList.contains('red')) {
        header.className = 'green';
    } else {
        header.className = 'red';
    }
});

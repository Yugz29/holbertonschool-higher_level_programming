const addItem = document.querySelector('#add_item');
const myList = document.querySelector('.my_list');

addItem.addEventListener('click', () => {
  const newList = document.createElement('li');
  newList.textContent = 'Item';
  myList.append(newList);
});

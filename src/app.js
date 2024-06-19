// Elements
const form = document.querySelector("form");
const input = document.querySelector("input");
const ul = document.querySelector("ul");
const listItems = document.querySelector("#list").children;
const list = document.querySelector("#list");

console.log(list);

const addItemToList = (task) => {
  const listItem = `<li class="list-item">
<span class="list-item-text montserrat-regular"
  >${task}</span
>
<div class="list-buttons">
  <button class="list-item-edit barlow-condensed-medium">
    Edit
  </button>
  <button class="list-item-delete barlow-condensed-medium">
    Delete
  </button>
</div>
</li>`;
  list.insertAdjacentHTML("beforeend", listItem);
};
form.addEventListener("submit", (e) => {
  e.preventDefault();
  formDataFc();
});
// console.log(form.querySelector('input[name="task"]'));
// FormData Element

const formDataFc = () => {
  const formData = new FormData(form);
  const task = formData.get("task");
  addItemToList(task);
  form.reset();
};
const renderListItemsDynamically = (todosArray) => {
  const listItemsArray = Array.from(todosArray);
  console.log(listItemsArray);
  window.addEventListener("DOMContentLoaded", () => {
    listItemsArray.forEach((item) => {
      list.insertAdjacentHTML("beforeend", item.textContent);
    });
  });
};

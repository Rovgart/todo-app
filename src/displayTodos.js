export const displayTodos = (todos) => {
  const todoList = document.getElementById("#list");
  todoList.forEach((item) => {
    todoList.insertAdjacentHTML(
      "beforeend",
      `<li class="list-item">
        <span class="list-item-text montserrat-regular"
          >${item.task}</span
        >
        <div class="list-buttons">
          <button class="list-item-edit barlow-condensed-medium">
            Edit
          </button>
          <button class="list-item-delete barlow-condensed-medium">
            Delete
          </button>
        </div>
        </li>`
    );
  });
};

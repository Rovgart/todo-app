import { fetchUserTodos } from "../api/fetchUserTodos.js";
import { fetchLogin } from "./fetchLogin.js";

const form = document.querySelector("form");
const signIn = async () => {
  const formData = new FormData(form);
  const username = formData.get("username");
  const password = formData.get("password");
  console.log(username, password);
  const fetchLoginValid = await fetchLogin(username, password);
  if (fetchLoginValid) {
    window.location.href = "http://localhost:3000/src/index.html";
    console.log(fetchLoginValid);
    fetchUserTodos(fetchLoginValid.user_id);
  }
};
form.addEventListener("submit", (e) => {
  e.preventDefault();
  signIn();
});

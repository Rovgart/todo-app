import { fetchRegister } from "./fetchRegister.js";

const form = document.querySelector("form");
console.log(form);
const signUp = async () => {
  const formData = new FormData(form);
  const username = formData.get("username");
  const password = formData.get("password");
  console.log(username, password);
  const fetchRegisterResult = await fetchRegister(username, password);
  if (fetchRegisterResult) {
    window.location.href = "http://localhost:3000/src/index.html";
  }
};
form.addEventListener("submit", (e) => {
  e.preventDefault();
  signUp();
});

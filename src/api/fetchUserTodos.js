import { displayTodos } from "../displayTodos.js";

export const fetchUserTodos = async (user_id) => {
  try {
    const response = await fetch(`http://localhost:3000/api/tasks/${user_id}`, {
      body: JSON.stringify({
        user_id: user_id,
      }),
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });
    if (!response.ok) {
      throw new Error(
        `Failed to fetch user todos ${response.status}: ${response.statusText}`
      );
    }
    const data = await response.json();
    if (data) {
      console.log(data);
      displayTodos(data);

      return data;
    }
  } catch (error) {
    console.error(error?.message);
  }
};

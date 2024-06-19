let logged = false;
export const fetchLogin = async (username, password) => {
  const options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      username: username,
      password: password,
    }),
  };
  try {
    const response = await fetch("http://localhost:8000/api/login", options);
    const data = await response.json();
    console.log(data);
    if (!response.ok) {
      throw new Error(
        `Failed to register ${response.status}: ${response.statusText}`
      );
    }
    if (data) {
      console.log(data);
      return true;
    }
  } catch (error) {
    console.error(error);
  }
};
export { logged };

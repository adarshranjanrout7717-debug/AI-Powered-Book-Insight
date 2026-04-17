const BASE_URL = "http://127.0.0.1:8000/api";

export const getBooks = async () => {
  const res = await fetch(`${BASE_URL}/books/`);
  return res.json();
};

export const askQuestion = async (question) => {
  const res = await fetch(`${BASE_URL}/ask/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ question }),
  });
  return res.json();
};
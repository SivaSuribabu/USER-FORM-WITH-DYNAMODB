
const form = document.getElementById("userForm");
const status = document.getElementById("status");
const API_URL = "YOUR_API_GATEWAY_INVOKE_URL/submit"; // replace with your API Gateway URL

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  
  const data = {
    name: document.getElementById("name").value,
    age: document.getElementById("age").value,
    mobile: document.getElementById("mobile").value,
    state: document.getElementById("state").value,
    country: document.getElementById("country").value,
    marital: document.getElementById("marital").value
  };

  try {
    const res = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });
    const result = await res.json();
    status.textContent = result.message;
    form.reset();
  } catch (err) {
    status.textContent = "Error submitting form!";
  }
});
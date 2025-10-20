document.getElementById('userForm').addEventListener('submit', async (e) => {
  e.preventDefault();

  const data = {
    firstName: document.getElementById('firstName').value,
    lastName: document.getElementById('lastName').value,
    mobile: document.getElementById('mobile').value
  };

  try {
    const response = await fetch('https://YOUR_API_GATEWAY_ENDPOINT', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });

    const result = await response.json();
    document.getElementById('status').textContent = 'Data submitted successfully!';
  } catch (error) {
    console.error('Error:', error);
    document.getElementById('status').textContent = 'Submission failed.';
  }
});

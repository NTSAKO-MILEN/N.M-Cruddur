// frontend/src/main.js
const express = require('express');
const path = require('path');

const app = express();
const PORT = 3000;

// Serve static files (like index.html, bundle.js, etc.)
app.use(express.static(path.join(__dirname, '..', 'public')));

app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '..', 'public', 'index.html'));
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(`Frontend server is running on http://localhost:${PORT}`);
});

const express = require("express");
const app = express();
const PORT = process.env.PORT || 3000;

// Test route
app.get("/", (req, res) => {
  res.send("✅ Your AI Receptionist backend is live!");
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

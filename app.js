const express = require("express");
const mongoose = require("mongoose");
require('dotenv').config();
const projectRoutes = require("./src/routes/Project");
const app = express();

app.use(express.json());
app.use("/projects", projectRoutes);
const connectDB = async () => {
    try {
        await mongoose.connect(process.env.DATABASE);
        app.listen(process.env.PORT);
    } catch(e) {
        console.error(e)
    }
};

connectDB();
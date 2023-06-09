const express = require("express");
const mongoose = require("mongoose");
require('dotenv').config();
const projectRoutes = require("./src/routes/ProjectRoutes");
const app = express();
const cors = require("cors");

app.use(cors());
app.use(express.json());
app.use("/projects", projectRoutes);
const connectDB = async () => {
    try {
        await mongoose.connect(process.env.DATABASE);
    } catch(e) {
        console.error(e)
    }
};

const server = app.listen(process.env.PORT, () => {
    console.log(`Server is running in port: ${process.env.PORT}`)
    connectDB();
});

module.exports = { app, server }
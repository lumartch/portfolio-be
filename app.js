const express = require("express");
const mongoose = require("mongoose");
const projectRoutes = require("./src/routes/Project");
const app = express();

app.use(express.json());
app.use("/projects", projectRoutes);

const connectDB = async () => {
    try {
        await mongoose.connect("mongodb+srv://lumartch:@cluster0.my6yvi8.mongodb.net/?retryWrites=true&w=majority");
        app.listen(4280);
    } catch(e) {
        console.error(e)
    }
};

connectDB();
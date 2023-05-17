const mongoose = require("mongoose");

const schema = mongoose.Schema;

const projectSchema = new schema({
    name: {
        type: String,
        require: true,
    },
    projectLink: {
        type: String,
    },
    overview: {
        type: String,
        require: true,
    },
    imageUrl: {
        type: String,
        require: true,
    },
    description: {
        type: String,
        require: true,
    },
    tools: {
        type: [ { type: String } ],
        require: true,
    },
});

module.exports = mongoose.model("Project", projectSchema);
const Project = require("../models/Project");

exports.getProjects = async () => {
    let projects = await Project.find().exec();
    return projects;
}
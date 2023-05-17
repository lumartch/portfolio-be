const Project = require("../models/Project");

const getProjects = async () => {
    let projects = await Project.find().exec();
    return projects;
}

const postProjects = async () => {
    let projects = await Project.find().exec();
    return projects;
}

module.exports = { getProjects, postProjects }
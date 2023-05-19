const Project = require("../models/Project");

const getProjects = async () => {
    return await Project.find().lean().exec();
}

const createProject = async (requestBody) => {
    const project = new Project({
        name: requestBody.name,
        projectLink: requestBody.projectLink,
        description: requestBody.description,
        overview: requestBody.overview,
        imageUrl: requestBody.imageUrl,
        tools: requestBody.tools
    });
    return await project.save();
}

const findProjectById = async (id) => {
    return await Project.findById(id).lean().exec();
}

const updateProject = async (id, projectData) => {
    return await Project.findByIdAndUpdate(id, projectData, { new: true } ).lean().exec();
}

const deleteProject = async (id) => {
    return await Project.findByIdAndDelete(id).lean().exec();
}

module.exports = { getProjects, createProject, findProjectById, updateProject, deleteProject }
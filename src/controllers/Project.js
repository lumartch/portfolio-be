const ProjectService = require("../services/Project");

const getProjects = async (req, res) => {
    try {
        let projects = await ProjectService.getProjects();
        res.json({
            projects: projects,
        });
    } catch (e) {
        console.error("Error: ", e);
        res.status(500).json({
            message: "Project no retrieved.",
        });
    }
}

const getProjectById = async (req, res) => {
    try {
        let project = await ProjectService.findProjectById(req.params.id);
        res.json(project);
    } catch (e) {
        console.error("Error: ", e);
        res.status(404).json({
            message: "Project not found.",
        });
    }
}

const createProject = async (req, res) => {
    try {
        let projectSaved = await ProjectService.createProject(req.body);
        res.status(201).json({
            message: "Project created",
            projectSaved: projectSaved,
        });
    } catch (e) {
        console.error("Error: ", e);
        res.status(400).json({
            message: "Project already exists",
        });
    }
}

module.exports = { getProjects, createProject, getProjectById };
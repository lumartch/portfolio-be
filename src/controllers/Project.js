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
            message: e,
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
            message: e,
        });
    }
}

module.exports = { getProjects, createProject }
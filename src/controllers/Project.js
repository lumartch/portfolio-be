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
        let projects = await ProjectService.createProject(req.body);
        res.status(201);
    } catch (e) {
        console.error("Error: ", e);
        res.status(500).json({
            message: e,
        });
    }
}

module.exports = { getProjects, createProject }
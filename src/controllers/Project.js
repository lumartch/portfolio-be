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
        if(!project){
            res.status(404).json({
                message: "Project not found.",
            });
        } else{ 
            res.json(project);
        }
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
            message: "Missing values on the body",
        });
    }
}

const updateProject = async (req, res) => {
    const { id } = req.params;
    const projectData = req.body;
    try {
        const updatedProjecData = await ProjectService.updateProject(id, projectData);
        res.status(200).json(updatedProjecData);
    } catch (e) {
        console.error("Error: ", e);
        res.status(500).json({
            message: "Internal error",
        });
    }
}

const deleteProject = async (req, res) => {
    try {
        const { id } = req.params;
        await ProjectService.deleteProject(id);
        res.status(204).json();
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: "Internal error" });
    }
}

module.exports = { getProjects, createProject, getProjectById, updateProject, deleteProject };
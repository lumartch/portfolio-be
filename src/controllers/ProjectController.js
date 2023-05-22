const ProjectService = require("../services/ProjectService");

const getProjects = async (req, res) => {
    try {
        let projects = await ProjectService.getProjects();
        res.json({
            projects: projects,
        });
    } catch (e) {
        const errorMessage = `${e._message}`;
        res.status(500).json({
            message: errorMessage,
        });
    }
}

const getProjectById = async (req, res) => {
    const { id } = req.params;
    if (id.match(/^[0-9a-fA-F]{24}$/)) {
        try {
            let project = await ProjectService.findProjectById(id);
            if(!project){
                res.status(404).json({
                    message: "Project not found.",
                });
            } else{ 
                res.json(project);
            }
        } catch (e) {
            console.error("Error: ", e);
            res.status(500).json({
                message: "Internal error.",
            });
        }
    } else {
        res.status(400).json({
            message: "Argument passed in must be a string of 12 bytes or a string of 24 hex characters or an integer.",
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
        const errorMessage = `${e._message}`;
        console.error("Error: ", errorMessage);
        res.status(400).json({
            message: errorMessage,
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
    const { id } = req.params;
    if (id.match(/^[0-9a-fA-F]{24}$/)) {
        try {
            await ProjectService.deleteProject(id);
            res.status(204).json();
        } catch (error) {
            console.error(error);
            res.status(500).json({ message: "Internal error" });
        }
    } else {
        res.status(400).json({
            message: "Argument passed in must be a string of 12 bytes or a string of 24 hex characters or an integer.",
        });
    }
}

module.exports = { getProjects, createProject, getProjectById, updateProject, deleteProject };
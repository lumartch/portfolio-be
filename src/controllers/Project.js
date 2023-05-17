const ProjectService = require("../services/Project");

exports.getProjects = async (req, res) => {
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
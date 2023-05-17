const express = require("express");
const projectController = require("../controllers/Project");
const router = express.Router();

router.get("/", projectController.getProjects);
router.get("/:id", projectController.getProjectById);
router.post("/", projectController.createProject);

module.exports = router;
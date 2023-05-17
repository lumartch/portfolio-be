const express = require("express");
const projectController = require("../controllers/Project");
const router = express.Router();

router.get("/", projectController.getProjects);

module.exports = router;
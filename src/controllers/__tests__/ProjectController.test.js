const Chance = require("chance");

//What we want to test
const projectController = require("../ProjectController");

//Dependencies

const projectService = require("../../services/ProjectService");

const chance = new Chance();

// Mocked dependencies
jest.mock("../../services/ProjectService");

describe("When calling the update project controller", () => {
    let id, projectData, updateProject;
    beforeEach(() => {
        id = chance.guid();
        global.console = { log: jest.fn(), error: jest.fn() }
        projectData = {
            name: chance.name(),
            description: chance.string(),
        }
        updateProject = projectData;
        req = {
            params: { id },
            body: projectData,
        };
        res = {
            status: jest.fn().mockReturnThis(),
            json: jest.fn().mockReturnThis(),
        }
        projectService.updateProject = jest.fn().mockResolvedValue(updateProject);
    });

    it("Should call projectService.updateProject with the id and the projectData", async () => {
        // ACT
        await projectController.updateProject(req, res);
        
        // Assert
        expect(projectService.updateProject).toHaveBeenCalledWith(id, projectData);
    });

    it("Should call req.status with 200 status code", async () => {
        // ACT
        await projectController.updateProject(req, res);
        
        // Assert
        expect(res.status).toHaveBeenCalledWith(200);
    });

    it("Should call res.json with the updated project data", async () => {
        // ACT
        await projectController.updateProject(req, res);
        
        // Assert
        expect(res.json).toHaveBeenCalledWith(updateProject);
    });

    it("Should call res.status with 500 status code when ProjectService.updateProject service fails", async () => {
        // Arrange
        const error = new Error("");
        projectService.updateProject = jest.fn().mockRejectedValue(error);

        // Act
        await projectController.updateProject(req, res);

        // Assert
        expect(res.status).toHaveBeenCalledWith(500);
    });
})
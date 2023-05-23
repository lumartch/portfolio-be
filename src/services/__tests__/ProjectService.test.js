const Chance = require("chance");

//What we want to test
const projectService = require("../ProjectService");

//Dependencies
const projectModel = require("../../models/ProjectModel");

const chance = new Chance();

// Mocked dependencies
jest.mock("../../models/ProjectModel");

describe("When calling the update project service", () => {
    let id, projectData, updateProject;
    beforeEach(() => {
        id = chance.guid();
        global.console = { log: jest.fn(), error: jest.fn() }
        projectData = {
            name: chance.name(),
            description: chance.string(),
        }
        updateProject = projectData;
        projectModel.findByIdAndUpdate = jest.fn().mockReturnThis();
        projectModel.lean = jest.fn().mockReturnThis();
        projectModel.exec = jest.fn().mockResolvedValue(updateProject);
    });

    it("Should call Project.findById with the id, project data and return document after property", async () => {
        await projectService.updateProject(id, projectData);
        
        expect(projectModel.findByIdAndUpdate).toBeCalledWith(id, projectData, { new: true });
    });

    it("Should call Project.lean", async () => {
        await projectService.updateProject(id, projectData);
        
        expect(projectModel.lean).toBeCalled();
    });

    it("Should call Project.exec", async () => {
        await projectService.updateProject(id, projectData);
        
        expect(projectModel.exec).toBeCalled();
    });

    it("Should return the updated project data", async () => {
        const data = await projectService.updateProject(id, projectData);
        
        expect(data).toEqual(updateProject)
    });
});

describe("When calling the delete project service", () => {
    let id;
    beforeEach(() => {
        id = chance.guid();
        global.console = { log: jest.fn(), error: jest.fn() }
        projectModel.findByIdAndDelete = jest.fn().mockReturnThis();
        projectModel.lean = jest.fn().mockReturnThis();
        projectModel.exec = jest.fn().mockResolvedValue();
    });
    it("Should call findById with an ID property", async () => {
        await projectService.deleteProject(id);
        expect(projectModel.findByIdAndDelete).toBeCalledWith(id);
    });
});
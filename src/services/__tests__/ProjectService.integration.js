const request = require("supertest");
const app = require("../../../app").app;
const Project = require("../../models/ProjectModel");

const mongoose = require("mongoose");
global.console = { log: jest.fn(), error: jest.fn() }

beforeAll(async() => {
    await mongoose.connect(process.env.DATABASE);
});

afterAll(async () => {
    await mongoose.disconnect();
})

const projectOne = {
    name: "Hello",
    projectLink: "World",
    description: "Hello friend",
    overview: "asdw",
    imageUrl: "123456789",
    tools: ["HTML", "java"]
};

const projectTwo = {
    name: "Project 2",
    projectLink: "Project 2",
    description: "Hello friend",
    overview: "Project 2",
    imageUrl: "Project 2",
    tools: ["HTML", "javascript"]
};

describe("GET /projects", () => {

    it("should return all projects", async () => {
        await Project.deleteMany();
        await Project.create(projectOne);
        const response = await request(app).get("/projects");
        expect(response.status).toBe(200);
        const projects = response.body.projects;
        expect(Array.isArray(projects)).toBe(true);
        expect(projects).toEqual(expect.arrayContaining([expect.objectContaining(projectOne)]));
    })

});

describe("POST /projects", () => {
    
    it("Should create a new project and return a created status code", async () => {
        const response = await request(app).post("/projects").send(projectOne);
        expect(response.status).toBe(201);
        expect(response.body.projectSaved).toEqual(expect.objectContaining({
            _id: expect.any(String),
            name: projectOne.name,
            projectLink: projectOne.projectLink,
            overview: projectOne.overview,
            imageUrl: projectOne.imageUrl,
            description: projectOne.description,
            tools: projectOne.tools,
        }));
        await Project.findByIdAndDelete(response.body.projectSaved._id);
    });

    it("Should return 400 code and an error when required field are missing", async () => {
        const { overview,  ...incompleteProject } = projectOne;
        const response = await request(app).post("/projects").send(incompleteProject);
        expect(response.status).toBe(400);
        expect(response.error.text).toContain("{\"message\":\"Project validation failed\"}");
    })

});
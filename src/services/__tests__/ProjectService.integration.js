const request = require("supertest");
const app = require("../../../app").app;
const Project = require("../../models/Project");

const mongoose = require("mongoose");

beforeAll(async() => {
    await mongoose.connect(process.env.DATABASE);
});

afterAll(async () => {
    await mongoose.disconnect();
})

describe("/GET projects", () => {
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
    it("should return all projects", async () => {
        await Project.deleteMany();
        await Project.create(projectOne);

        const response = await request(app).get("/projects");
        expect(response.status).toBe(200);
        const projects = response.body.projects;
        expect(Array.isArray(projects)).toBe(true);
        expect(projects.length).toBe(1);
        expect(projects).toEqual(expect.arrayContaining([expect.objectContaining(projectOne)]));

    })
});
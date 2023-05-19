import http from 'k6/http';

const getProjects = () => {
    let response = http.get("http://localhost:4280/projects/");
}

export default function (){
    getProjects();
}

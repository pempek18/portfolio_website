# Portfolio Website

## Overview
A personal portfolio website built with Flask, showcasing professional experience, services, and completed projects in industrial automation and programming.

## Features
- Responsive design with modern CSS
- Multiple sections:
  - Home page with professional summary
  - Technologies and skills showcase
  - Services offered
  - Project portfolio/implementations
  - Professional experience/CV

## Technical Stack
- Backend: Python Flask
- Frontend: HTML5, CSS3, Jinja2 Templates
- Design: Responsive grid layout, custom CSS variables
- Assets: Custom images and PDF downloads

## Project Structure
```
.
├── app.py
├── Dockerfile
├── requirements.txt
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── technologies.html
│   ├── production.html
│   ├── experience.html
│   └── services.html
└── static/
    ├── styles.css
    └── img/
        ├── pyTorch.png
        ├── gx_works.png
        ├── beckhoff.png
        ├── weintek.png
        ├── ultralytics.png
        ├── indusoft.png
        ├── python.png
        ├── llama.jpeg
        ├── csharp.png
        ├── kuka.png
        └── cplusplus.png
  ```

## Steps to run
1. Clone the repository
2. Build new image
    ```
    docker build -t portfolio-app .
    ```
3. Run new container
    ```
    docker run -d -p 5000:5000 --name portfolio portfolio-app
    ```
4. Verify state
    ```
    docker logs portfolio
    ```
5. Open `http://localhost:5000` in your browser

## Steps to rebuild
1. Remove old container and image
    ```
    docker stop portfolio
    docker rm portfolio
    docker rmi portfolio-app
    ```
2. Steps to run, step 2-5

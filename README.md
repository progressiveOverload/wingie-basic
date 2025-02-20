
# Wingie Basic

## Introduction

Wingie Basic is a project primarily written in Python with Docker support (but used podman to deploy). This document provides information on the DevOps setup and practices used in this repository.

## Table of Contents

- [Introduction](#introduction)
- [Deployment Instructions](#deployment-instructions)
- [Infrastructure Setup](#infrastructure-setup)
- [Monitoring and Logging](#monitoring-and-logging)
- [Contributing](#contributing)



## Deployment Instructions

To deploy this project, follow these steps:

1. Ensure you have Docker installed.
2. Build the Docker image using the following command:
   ```bash
   docker build -t wingie-basic .
   ```
2.1 Or pull the container from Docker Hub:
   ```bash
docker pull sannjo/my-fastapi-app:latest
   ```
3. Run the Docker container:
   ```bash
   docker run -d -p 80:80 wingie-basic
   ```
3.1 In case you've pulled from the hub run via Podman:
   ```bash
podman run -d --name my-fastapi-app -p 8000:8000 sannjo/my-fastapi-app:latest

   ```
or pulled from the hub and run via Docker
   ```bash
docker run -d --name my-fastapi-app -p 8000:8000 sannjo/my-fastapi-app:latest
   ```


## Infrastructure Setup

The project is containerized using Docker. The following files are relevant to the infrastructure setup:

- **Dockerfile:** Defines the Docker image configuration.

## Monitoring and Logging

To monitor and log the application, consider integrating with services like Prometheus and Grafana. Set up logging to capture application logs for troubleshooting and analysis.

## Contributing

We welcome contributions! Please follow the guidelines below:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.


---


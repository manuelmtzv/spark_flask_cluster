# Spark-Flask Docker Cluster

This repository contains a Docker configuration for setting up a cluster environment with Apache Spark and Flask using Docker Compose. It enables you to easily develop and test Spark applications with a Flask front-end.

## Prerequisites

- Docker installed on your system ([Install Docker](https://docs.docker.com/get-docker/))
- Docker Compose installed on your system ([Install Docker Compose](https://docs.docker.com/compose/install/))

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd spark-flask-docker-cluster
   ```

3. Run Docker Compose to build and start the containers:

   ```bash
   docker-compose up
   ```

4. Once the containers are up and running, you can access the Flask application at [http://localhost:5000](http://localhost:5000).

## Services

### Spark Master

- Image: `bitnami/spark:latest` ([More information](https://hub.docker.com/r/bitnami/spark/))
- Exposed Ports: 
  - Spark UI: 8080 (Mapped to host port 9090)
  - Spark Master: 7077 (Mapped to host port 7077)

### Spark Worker

- Image: `bitnami/spark:latest` ([More information](https://hub.docker.com/r/bitnami/spark/))
- Dependencies: Depends on Spark Master
- Environment Variables:
  - `SPARK_MODE`: worker
  - `SPARK_WORKER_CORES`: 1
  - `SPARK_WORKER_MEMORY`: 1g
  - `SPARK_MASTER_URL`: spark://spark-master:7077

### Backend

- Build: Dockerfile.backend
- Dependencies: Depends on Spark Worker
- Exposed Port: 5000 (Mapped to host port 5000)
- Volumes:
  - Mounts current directory and data directory for data sharing
- Commands:
  - `python` (Default command)

## Scaling and Resource Configuration

You can easily scale the Spark cluster by adding more Spark worker containers. Additionally, you can adjust the resources allocated to each worker by modifying the environment variables `SPARK_WORKER_CORES` and `SPARK_WORKER_MEMORY` in the Docker Compose configuration.

For example, to add more workers, simply duplicate the `spark-worker` service block in the `docker-compose.yml` file and update the necessary parameters.

## Development Environment

This project includes a Devcontainer configuration for Visual Studio Code, allowing for seamless development within a containerized environment. Ensure you have the [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension installed in VS Code. Open the project folder in VS Code and select "Reopen in Container" from the command palette.

## Usage

1. After starting the Docker containers using `docker-compose up`, initialize the backend API:
   - If using Docker Compose directly:
     ```bash
     docker-compose exec backend python app.py
     ```
   - If using the Devcontainer in Visual Studio Code:
     ```bash
     python app.py
     ```

2. Visit [http://localhost:5000](http://localhost:5000) in your web browser to access the Flask application.
3. Use the provided routes for running Spark analysis (`/run-analysis`) and reading files (`/read-file`).

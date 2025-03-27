## Running the demos locally

To run the demos locally, you need to have docker installed.
For older docker versions that do not have docker compose, docker-compose is needed.

[Install Docker](https://docs.docker.com/get-docker/)

To run the demos you need to run the following command:

```bash
docker compose -f Docker/docker-compose.yml up --build -d
```

or for older docker versions:

```bash
docker-compose -f Docker/docker-compose.yml up --build -d
```

You can find more information about docker inside the ./Docker/README.md file.

## Challenge Ports :

The challenges start from the port 4000.

You can access the challenges with localhost.

## Solutions

The solutions are in the ./Solutions/ folder.

More information about the solutions can be found in the ./Solutions/README.md file.

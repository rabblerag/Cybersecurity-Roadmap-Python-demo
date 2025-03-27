## How to add challenges

Create a folder

File structure

```
.
└── challenge
    ├── challenge.py
    └── flag.txt
```

Write the python code as if one is running it in the terminal

The Dockerfile is responsible for copying the challenge.py and the flag.txt

## How to run the docker

### For the first time

```bash
docker compose up --build -d
```

### Any other time

```bash
docker compose up -d
```

## How to stop the docker

```bash
docker compose down
```

## How to access the docker terminal

```bash
docker compose exec challenge /bin/bash
```

### How to access the docker logs

Because `-d` : is detached, this means none of the logs will be displayed

```bash
docker compose logs -f
```

## How this docker compose works

It uses the host as the network medium, so the challenges can be accessed via localhost.

Each challenge is a service with the same Dockerfile image but with different ports and source code.

> Each of the docker services is limited to 0.5 CPU and 1GB of memory. This is just as a precaution to prevent any malicious code from consuming all the resources, however each challenge code is incredibly simple and won't consume much resources.


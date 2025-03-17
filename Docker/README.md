## How to edit the challenge

In the `challenge/challenge.py` file

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

```bash
docker compose logs -f
```

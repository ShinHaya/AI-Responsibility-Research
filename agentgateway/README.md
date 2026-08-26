# agentgateway Docker environment

This directory runs agentgateway with Docker Compose, following the official
[Docker installation guide](https://agentgateway.dev/docs/standalone/main/setup/install/docker/).

## First-time setup

Create the local environment file and replace the UID and GID values with the
output of `id -u` and `id -g`:

```sh
cd agentgateway
cp .env.example .env
id -u
id -g
```

The `.env` file and generated runtime state are ignored by Git. Do not place API
keys in tracked files.

## Start and verify

```sh
docker compose up -d
docker compose ps
docker compose logs --tail=50 agentgateway
```

On the first start, agentgateway creates `agentgateway-config/config.yaml` and
its SQLite database. Open the admin UI at <http://localhost:4000/ui>.

The host port binds to `127.0.0.1` so the unauthenticated local UI is not exposed
to other machines. Change `AGENTGATEWAY_PORT` in `.env` if port 4000 is already
in use.

## Stop

```sh
docker compose down
```

The generated configuration and database remain under `agentgateway-config/`.

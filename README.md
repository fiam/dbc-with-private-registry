# Build Cloud with a private registry

A minimal Python web app (using Flask) with Docker and GitHub Actions for automatic publishing to GitHub Container Registry (GHCR). It includes multi-platform builds and auto-tagging.

---

## What It Does

- Serves a simple web app on port `5001`
- `/` returns the current server time
- `/healthz` returns HTTP 200 OK
- Automatically builds and publishes to GHCR on every push via GitHub Actions
- Tags images as `v1`, `v2`, ... and `latest`
- Multi-platform builds (`linux/amd64`, `linux/arm64`)

---

## Live development with Docker Compose

Run `docker compose up --watch --build`.


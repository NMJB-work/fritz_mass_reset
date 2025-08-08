# Fritz Mass Reset - Dockerized Package

This archive contains a Dockerized backend, frontend, Selenium container, and Redis queue for managing mass FRITZ!Box resets.

## Quick start
1. Install git, curl and npm:  
   Ubuntu/Debian
   ```bash
   sudo apt update && sudo apt upgrade -y && sudo apt install git curl npm
   ```
   RPM-based distributions, such as RHEL or CentOS:
   ```bash
   sudo dnf update -y && sudo dnf upgrade -y && sudo dnf install git curl npm
   ```
2. Install docker and docker compose:  
   Docker: https://docs.docker.com/engine/install/  
   Docker compose: https://docs.docker.com/desktop/setup/install/linux/  

4. Clone this Repo:
   ```bash
   git clone https://github.com/NMJB-work/fritz_mass_reset.git && cd fritz_mass_reset
   ```
5. Edit `docker-compose.yml` and set a strong `API_TOKEN` in the backend and frontend sections.
6. Build & run:
   ```bash
   docker compose up --build
   ```
7. Start a worker to process queued jobs (in another terminal):
   ```bash
   docker compose exec backend python worker.py
   ```
   or run the worker inside the backend container with RQ: `rq worker resets`

## Notes
- The backend enqueues reset jobs to Redis. Worker(s) consume them and execute resets.
- If you prefer immediate mode, call `/api/reset` with `use_queue=false` in the JSON payload.
- Protect the API token and run in a management network only.

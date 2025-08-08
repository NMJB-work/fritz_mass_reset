# Fritz Mass Reset - Dockerized Package

This archive contains a Dockerized backend, frontend, Selenium container, and Redis queue for managing mass FRITZ!Box resets.

## Quick start
1. Install git:
   Ubuntu/Debian
   ```bash
   sudo apt update && sudo apt upgrade -y && sudo apt install git
   ```
2. Clone this Repo:
   ```bash
   git clone https://github.com/NMJB-work/fritz_mass_reset.git && cd fritz_mass_reset
   ```
3. Edit `docker-compose.yml` and set a strong `API_TOKEN` in the backend and frontend sections.
4. Build & run:
   ```bash
   docker compose up --build
   ```
5. Start a worker to process queued jobs (in another terminal):
   ```bash
   docker compose exec backend python worker.py
   ```
   or run the worker inside the backend container with RQ: `rq worker resets`

## Notes
- The backend enqueues reset jobs to Redis. Worker(s) consume them and execute resets.
- If you prefer immediate mode, call `/api/reset` with `use_queue=false` in the JSON payload.
- Protect the API token and run in a management network only.

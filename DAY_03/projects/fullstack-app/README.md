# Full-Stack Docker Compose Application

## Architecture
┌─────────────┐ ┌─────────────┐ ┌─────────────┐ │ Nginx │─────→│ Flask │─────→│ PostgreSQL │ │ Frontend │ HTTP │ Backend │ SQL │ Database │ │ Port 8080 │ │ Port 5000 │ │ Port 5432 │ └─────────────┘ └─────────────┘ └─────────────┘


## Services

- **Frontend**: Nginx serving static HTML/CSS/JS
- **Backend**: Flask REST API
- **Database**: PostgreSQL with persistent storage

## How to Run

```bash
# Start all services
docker compose up -d

# View logs
docker compose logs -f

# Check status
docker compose ps

# Stop all services
docker compose down

# Stop and remove volumes
docker compose down -v
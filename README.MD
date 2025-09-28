# Project Golang Backend

This project is a **URL Shortener** with analytics and modern tooling.

## Tech Stack

* **Backend**: Golang

  * [Gin](https://github.com/gin-gonic/gin) – HTTP framework
  * [GORM](https://gorm.io) – ORM for Postgres
  * [go-redis](https://github.com/redis/go-redis) – Redis client

* **Database**:

  * PostgreSQL – persistent storage
  * Redis – caching and fast lookups

* **Frontend**:

  * [Next.js](https://nextjs.org/) – React-based web framework

## Features

* Shorten long URLs into unique short codes
* Redirect short codes to original URLs
* Store link data in PostgreSQL
* Cache lookups in Redis for performance
* Basic analytics (click counts, timestamps, referrers, etc.)
* Web UI built with Next.js

## Development

### Prerequisites

* Go 1.22+
* Node.js 18+
* PostgreSQL 14+
* Redis 7+

### Run Backend

```bash
go run ./cmd/server
```

### Run Frontend

```bash
cd frontend
npm install
npm run dev
```

## Project Structure

```
/cmd/server        # Main server entrypoint
/internal          # Application code
    /api           # Handlers
    /db            # Database models, migrations
    /cache         # Redis logic
/frontend          # Next.js frontend
```

## Roadmap

* [ ] User accounts and authentication
* [ ] Custom short codes
* [ ] Detailed analytics dashboard
* [ ] Deployment with Docker
* [ ] CI/CD setup

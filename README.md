Python App with Nginx Reverse Proxy on AWS EC2

## Project Overview

This project demonstrates deployment of a containerized Python web application using Docker and Docker Compose on an AWS EC2 instance.

Nginx is used as a reverse proxy to forward incoming HTTP traffic to the backend Python application container.

---

## Architecture

Browser
↓
EC2 Public IP :80
↓
Nginx Container
↓
Docker Internal Network
↓
Python App Container :8080

---

## Technologies Used

- Python
- Flask
- Docker
- Docker Compose
- Nginx
- Linux
- AWS EC2

---

## Features

- Containerized Python application
- Multi-container deployment using Docker Compose
- Nginx reverse proxy configuration
- Internal container communication using Docker networking
- Port mapping between host and containers
- AWS EC2 deployment
- Linux troubleshooting and log analysis

---

## Project Structure

```bash
.
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── nginx
    └── default.conf
```

---

## Docker Compose Setup

```yaml
services:
  app:
    build: .
    container_name: myapp
    ports:
      - "8080:8080"

  nginx:
    image: nginx:latest
    container_name: mynginx
    ports:
      - "80:80"
    volumes:
      - ./nginx/default.conf:/etc/nginx/conf.d/default.conf
    depends_on:
      - app
```

---

## Nginx Reverse Proxy Configuration

```nginx
server {
    listen 80;

    location / {
        proxy_pass http://app:8080;
    }
}
```

---

## Deployment Steps

### Build and Start Containers

```bash
docker compose up -d
```

### Verify Running Containers

```bash
docker ps
```

### Test Backend Container

```bash
curl localhost:8080
```

### Test Nginx Reverse Proxy

```bash
curl localhost
```

---

## Key Concepts Learned

### Reverse Proxy

Nginx receives external HTTP traffic on port 80 and forwards requests internally to the backend application container.

### Docker Networking

Docker Compose automatically creates an internal bridge network allowing containers to communicate using service names.

### Service Discovery

The Nginx container communicates with the application container using:

```nginx
proxy_pass http://app:8080;
```

Here `app` refers to the Docker Compose service name.

### Container Isolation

Each container has its own network namespace.

`localhost` inside one container refers only to that container itself.

---

## Troubleshooting Scenarios

### 502 Bad Gateway

Cause:
- Nginx container running
- Backend application container unavailable

### Connection Refused

Cause:
- No service listening on target port

### Timeout

Cause:
- Security Group or network-level issue

---

## Commands Used for Troubleshooting

```bash
docker ps
docker logs myapp
docker logs mynginx
curl localhost
curl localhost:8080
```

---

## Screenshots

### Running Containers

(Add docker ps screenshot here)

### Browser Access via Public IP

(Add browser screenshot here)

### Nginx Reverse Proxy Configuration

(Add nginx config screenshot here)

---

## Outcome

Successfully deployed a multi-container Python application architecture using Docker Compose and Nginx reverse proxy on AWS EC2 while understanding container networking, reverse proxying, and layered troubleshooting.# EC2 Nginx Python App Deployment

## Overview
This project demonstrates deploying a Python application on an AWS EC2 instance using:
- systemd (process management)
- nginx (reverse proxy)

## Architecture
Browser → Nginx (port 80) → Python App (port 8080)

## Setup

### 1. Clone repo
git clone https://github.com/Yogitha01/ec2-nginx-python-app.git

### 2. Run app manually
python3 app.py

### 3. Setup systemd
sudo cp myapp.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start myapp

### 4. Configure nginx
sudo cp nginx.conf /etc/nginx/sites-available/default
sudo nginx -t
sudo systemctl restart nginx

## Verify
curl localhost

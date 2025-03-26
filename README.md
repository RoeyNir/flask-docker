# Flask Hello in Docker

This is a simple Flask application that returns a message when you access the root URL (`/`).  
The main goal of the project is to show basic understanding of Docker, Dockerfile, and docker-compose.

Everything runs inside a Docker container, and the setup includes port mapping and a shared volume.

---

## Files included

- `app.py` – the Flask app
- `Dockerfile` – defines how the image is built
- `requirements.txt` – lists the needed Python packages
- `docker-compose.yml` – manages the service and its configuration
- The `logs` folder is automatically created during `docker-compose up` as part of the volume mapping (`./logs:/app/logs`).  
  You don’t need to create it manually — Docker handles that

---

## How to run

Make sure Docker is installed and running.  
Then, in the root directory of the project, run:

```bash
docker-compose up --build
# To demonstrate that the service works as expected without using a browser,  
# you can run the following command from the terminal:
curl http://localhost:5000

# Hello DevOps Practice

This repository contains a minimal web application written in Python using
[Flask](https://flask.palletsprojects.com/). It is designed as a
practice exercise to demonstrate the essential components of a modern
DevOps workflow, including unit testing, containerization, continuous
integration, and deployment.

## Project structure

```
hello-devops/
├─ app.py                # Flask application with a single route
├─ test_app.py           # pytest unit test for the app
├─ requirements.txt      # Python dependencies
├─ Dockerfile            # Instructions to build the Docker image
├─ .github/workflows/ci.yml  # GitHub Actions workflow definition
└─ README.md             # This file
```

## Running locally

1. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

2. **Start the application:**

   ```sh
   python app.py
   ```

   The app will be available at `http://localhost:5000/` and should return
   `Hola Mundo` when you visit the root URL.

3. **Run tests:**

   ```sh
   pytest
   ```

## Building and running the Docker image

1. **Build the image:**

   ```sh
   docker build -t yourdockerhubusername/hello-devops:latest .
   ```

2. **Run the container:**

   ```sh
   docker run -p 5000:5000 yourdockerhubusername/hello-devops:latest
   ```

   Visit `http://localhost:5000` to verify it returns the greeting.

## Continuous integration and deployment

This repository includes a GitHub Actions workflow located in
`.github/workflows/ci.yml`. The workflow performs the following steps
whenever code is pushed to the `main` branch:

1. Checkout the repository.
2. Set up Python and install dependencies.
3. Run unit tests with `pytest`.
4. Log in to Docker Hub using secrets.
5. Build the Docker image and tag it with both the commit SHA and `latest`.
6. Push the Docker image to Docker Hub.
7. Optionally trigger a deploy on Render if the necessary secrets are defined.

### Required secrets

To enable the CI/CD pipeline, add the following secrets to your GitHub
repository (`Settings` → `Secrets and variables` → `Actions` → `New
repository secret`):

| Secret name            | Description                                                                     |
|-----------------------|---------------------------------------------------------------------------------|
| `DOCKERHUB_USERNAME`  | Your Docker Hub username.                                                         |
| `DOCKERHUB_TOKEN`     | A Docker Hub access token or password with permission to push images.            |
| `RENDER_SERVICE_ID`   | *(optional)* The ID of a service on Render to trigger deployments.               |
| `RENDER_API_KEY`      | *(optional)* API key for Render. Only required if you wish to auto‑deploy.       |

### Deploying to Render

Render offers a free tier for hosting web services that can be deployed
from a Docker image or directly from a Git repository. To deploy this
application:

1. Create a [Render account](https://render.com/) and link it to your
   GitHub account.
2. Create a new **Web Service**. Choose **Docker** as the environment.
3. Under **Docker** settings, point Render to your Docker Hub image
   (e.g. `yourdockerhubusername/hello-devops:latest`).
4. Set the **Port** to `5000`. Render will expose your app on a
   public URL.
5. Copy the generated service ID (available in the service settings) and
   generate an API key under **Account Settings → API Keys**. Add both
   values as `RENDER_SERVICE_ID` and `RENDER_API_KEY` secrets in the
   GitHub repository.
6. On the next push to `main`, GitHub Actions will trigger a new deploy
   on Render and the service will update.


## License

This project is provided for educational purposes and does not include
any license. Feel free to adapt and extend it as needed.

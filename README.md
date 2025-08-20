# Práctica de DevOps

Este repositorio contiene una aplicación web mínima escrita en Python usando [Flask](https://flask.palletsprojects.com/). Está diseñada como un ejercicio práctico para demostrar los componentes esenciales de un flujo de trabajo DevOps moderno, incluyendo pruebas unitarias, containerización, integración continua y despliegue.

## Estructura del proyecto

```
hello-devops/
├‑ app.py               # Aplicación Flask con una sola ruta
├‑ test_app.py          # Prueba unitaria pytest para la app
├‑ requirements.txt     # Dependencias de Python
├‑ Dockerfile           # Instrucciones para construir la imagen Docker
├‑ .github/workflows/ci.yml  # Definición del flujo de trabajo de GitHub Actions
└‑ README.md            # Este archivo
```

## Ejecución local

1. **Instalar dependencias:**

```sh
pip install -r requirements.txt
```

2. **Iniciar la aplicación:**

```sh
python app.py
```

La aplicación estará disponible en `http://localhost:5000/` y debería devolver `Hola Mundo` cuando visites la URL raíz.

3. **Ejecutar pruebas:**

```sh
pytest
```

## Construir y ejecutar la imagen Docker

1. **Construir la imagen:**

```sh
docker build -t yourdockerhubusername/hello-devops:latest .
```

2. **Ejecutar el contenedor:**

```sh
docker run -p 5000:5000 yourdockerhubusername/hello-devops:latest
```

Visita `http://localhost:5000` para verificar que devuelve el saludo.

## Integración y despliegue continuos

Este repositorio incluye un flujo de trabajo de GitHub Actions ubicado en `.github/workflows/ci.yml`. El flujo de trabajo realiza los siguientes pasos cada vez que el código se empuja al branch `main`:

1. Clona el repositorio.
2. Configura Python e instala las dependencias.
3. Ejecuta pruebas unitarias con `pytest`.
4. Inicia sesión en Docker Hub usando los secrets.
5. Construye la imagen Docker y la etiqueta con el SHA de commit y `latest`.
6. Empuja la imagen a Docker Hub.
7. Opcionalmente dispara un despliegue en Render si se definen los secrets necesarios.

### Secrets requeridos

Para habilitar la canalización CI/CD, agrega los siguientes secrets a tu repositorio de GitHub (en **Settings → Secrets and variables → Actions → New repository secret**):

| Nombre del secret      | Descripción                                                                                       |
|-----------------------|----------------------------------------------------------------------------------------------------|
| `DOCKERHUB_USERNAME`  | Tu nombre de usuario en Docker Hub.                                                                |
| `DOCKERHUB_TOKEN`     | Un token de acceso o contraseña de Docker Hub con permiso para subir imágenes.                     |
| `RENDER_SERVICE_ID`   | *Opcional* Identificador del servicio en Render para despliegues posteriores.                       |
| `RENDER_API_KEY`      | *Opcional* Clave API para Render. Solo necesaria si deseas auto‑desplegar.                         |

### Desplegar en Render

Render ofrece un nivel gratuito para servicios web que se pueden desplegar a partir de una imagen Docker o directamente desde un repositorio de Git. Para desplegar esta aplicación:

1. Crea una [cuenta en Render](https://render.com/) y enlázala con tu cuenta de GitHub.
2. Crea un **Web Service** nuevo. Elige **Docker** como entorno.
3. En los ajustes de **Docker**, apunta Render a tu imagen de Docker Hub (por ejemplo, `yourdockerhubusername/hello-devops:latest`).
4. Establece el **Puerto** a `5000`. Render expondrá tu aplicación en una URL pública.
5. Copia el identificador del servicio generado (disponible en la página de servicios) y genera una clave API en **Account Settings → API Keys**. Agrega ambos valores como `RENDER_SERVICE_ID` y `RENDER_API_KEY` en tu repositorio de GitHub.
6. En el siguiente push a `main`, GitHub Actions creará un nuevo despliegue en Render y el servicio se actualizará.

## Licencia

Este proyecto se proporciona con fines educativos y no incluye ninguna licencia. Siéntete libre de adaptarlo y extenderlo según sea necesario.
https://github.com/FelipeJsSM/hello-devops/edit/main/.github/workflows/ci.yml

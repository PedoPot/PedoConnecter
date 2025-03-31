FROM python:3.8-slim-buster
LABEL "Project"="PedoConnecter"

USER root

# Copy the src
WORKDIR /app
COPY src/ /app/src/
COPY ./requirements.txt /app

# Install python dependencies
RUN python3 --version
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r /app/requirements.txt
RUN pip3 list --format=columns


EXPOSE 9341
CMD ["fastapi", "run", "/app/src/main.py", "--port", "9341"]

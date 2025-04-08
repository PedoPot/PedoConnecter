FROM python:3.13.2-slim-bookworm
LABEL "Project"="PedoConnector"

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

USER 1001

EXPOSE 9341
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9341"]

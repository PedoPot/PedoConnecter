FROM python:3.13.2-slim-bookworm
LABEL "Project"="PedoConnector"

USER root
ENV PYTHONPATH=/code
WORKDIR /code

# Install python dependencies
COPY ./requirements.txt /code
RUN python3 --version
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r /code/requirements.txt
RUN pip3 list --format=columns

COPY ./app/ /code/app
USER 1001

EXPOSE 9341
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "9341"]

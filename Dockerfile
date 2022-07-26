FROM python:3.8-slim
WORKDIR ~
COPY . ./
RUN pip install .
CMD ["uvicorn", "medium.main:app", "--host", "0.0.0.0", "--port", "8080"]

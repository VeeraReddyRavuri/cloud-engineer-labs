#Layer1: Base Image
FROM python:3.11-slim

#Layer2: set working directory - all commands run from /app inside the container
WORKDIR /app

#Layer 3: Copy app into image
COPY app.py .

#This container listens on port 8000
EXPOSE 8000

#always run python
ENTRYPOINT ["python"]

#default argument
CMD ["app.py"]
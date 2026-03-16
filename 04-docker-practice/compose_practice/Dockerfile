FROM python:3.11-slim
WORKDIR /app
COPY app.py .
EXPOSE 8000
HEALTHCHECK --interval=10s --timeout=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"
CMD ["python", "app.py"]
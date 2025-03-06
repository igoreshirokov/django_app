FROM python:3.13-slim

WORKDIR /app

USER appuser

ENTRYPOINT ["/app/entrypoint.sh"]
FROM python:3.13-slim

WORKDIR /app

# RUN groupadd -g 1000 appuser && \
#     useradd -u 1000 -g appuser && \
#     chown -R appuser:appuser /app

USER appuser

ENTRYPOINT ["/app/entrypoint.sh"]
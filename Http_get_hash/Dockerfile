FROM python:3.12-alpine3.20

ARG COMMIT_HASH


RUN apk add --no-cache \
    rust \
    cargo \
    gcc \
    g++ \
    musl-dev \
    libffi-dev \
    libgcc \
    make \
    build-base \
    openssl-dev

RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chown -R appuser:appgroup /app

USER appuser

LABEL commit_hash="${COMMIT_HASH}"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

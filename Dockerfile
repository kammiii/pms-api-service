FROM python:3.10-slim AS builder
WORKDIR /app

RUN pip install "poetry>=1.2"

COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create false \
  && poetry install --no-root --without dev

FROM python:3.10-slim
WORKDIR /app

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

COPY . .

EXPOSE 8000
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

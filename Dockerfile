FROM python:3.9.9-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt


COPY . .

VOLUME [ "/data", "/app/config" ]

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]

CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:create_app()"]

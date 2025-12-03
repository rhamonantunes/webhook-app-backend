FROM image-registry.openshift-image-registry.svc:5000/webhook-app/python:3.11-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

## Test ACS
RUN apk add --no-cache curl

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "wsgi:app"]

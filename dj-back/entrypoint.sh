#!/bin/bash

CERT_DIR="/app/certs"
mkdir -p "$CERT_DIR"
cd "$CERT_DIR"

# Generate certs if they don't exist
if [ ! -f "localhost.pem" ]; then
    echo "Creating local CA and certificate with mkcert..."
    mkcert -install
    mkcert -cert-file localhost.pem -key-file localhost-key.pem localhost 127.0.0.1 ::1
fi

echo "$(ls)"

echo "$(find -type f -name "manage.py")"

# Run Django dev server over HTTPS
# exec python manage.py runserver_plus --cert-file certs/localhost.pem --key-file certs/localhost-key.pem 0.0.0.0:8000

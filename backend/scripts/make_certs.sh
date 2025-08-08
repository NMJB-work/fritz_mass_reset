#!/usr/bin/env bash
set -e
mkdir -p backend/certs
openssl req -x509 -newkey rsa:4096 -nodes -keyout backend/certs/key.pem -out backend/certs/cert.pem -days 365 -subj '/CN=localhost'
echo "Generated backend/certs/cert.pem and key.pem (self-signed)"

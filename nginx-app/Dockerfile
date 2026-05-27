FROM nginx:latest@sha256:5aca99593157f4ae539a5dec1092a0ad8762f8e2eb1789085a13a0f5622369f6
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*
COPY index.html /usr/share/nginx/html/index.html

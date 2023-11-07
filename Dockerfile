FROM python:3.11.6-slim AS builder
ENV DASH_DEBUG_MODE False
WORKDIR /flask

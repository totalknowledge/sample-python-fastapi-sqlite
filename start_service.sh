#!/bin/env sh
echo "Starting FastAPI application..."
cd app
uvicorn main:app --reload
cd ..

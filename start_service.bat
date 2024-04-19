@echo off
echo Starting FastAPI application...
cd app
uvicorn main:app --reload
cd ..
pause

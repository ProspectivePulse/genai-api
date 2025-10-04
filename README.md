# ML Service with FastAPI

[![CI/CD](https://github.com/ProspectivePulse/genai-api/actions/workflows/ci.yml/badge.svg)](https://github.com/ProspectivePulse/genai-api/actions/workflows/ci.yml)

A minimal production-style ML service built with FastAPI, Docker, and CI/CD.

# GenAI API Starter with FastAPI

This project sets up a basic **FastAPI** backend as a foundation for building **GenAI-powered APIs**.
The goal is to integrate **vector search (FAISS)**, **Vertex AI**, and **CI/CD pipelines** in upcoming stages.

---
## $\checkmark$ Features (Day 1)
- FastAPI app with:
	- '/' -> Health check endpoint
	- '/ask' -> Accepts a query parameter and returns a placeholder response
- Auto-generated interactive API docs via Swagger UI ('/docs')

---
## Requirements
- Python 3.9 +
- Conda or virtualenv
- Packages:
	- FastAPI
	- Uvicorn

Install dependencies:
'''bash
pip install -r requirements.txt
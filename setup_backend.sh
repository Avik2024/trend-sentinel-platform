#!/bin/bash

# Ensure backend folder exists
mkdir -p backend/app/{routers,core}

# Create empty Python files if they don't exist
touch backend/app/__init__.py
touch backend/app/models.py
touch backend/app/schemas.py
touch backend/app/database.py
touch backend/app/crud.py
touch backend/app/routers/__init__.py
touch backend/app/routers/trends.py
touch backend/app/core/__init__.py
touch backend/app/core/config.py

echo "✅ Backend folder structure created!"

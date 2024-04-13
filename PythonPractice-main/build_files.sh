#!/bin/bash

echo "Running Flake8..."
flake8 .

echo "Running isort..."
isort .

echo "Running Pylint..."
pylint .

echo "Running Bandit..."
bandit -r .

echo "Running Mypy..."
mypy .

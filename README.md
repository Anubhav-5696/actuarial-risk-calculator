# Actuarial Risk & Premium Calculator

This project is a Flask web application that calculates expected loss and estimated insurance premium using basic actuarial pricing concepts.

## Features

- Calculates expected loss
- Calculates estimated insurance premium
- Uses claim probability, coverage amount, expense loading, and profit margin
- Containerized with Docker
- Deployed on Kubernetes with 3 replicas
- Uses GitHub Actions for CI/CD

## Formula

Expected Loss = Claim Probability × Coverage Amount

Premium = Expected Loss + Expense Loading + Profit Margin

## Tech Stack

- Python
- Flask
- Pytest
- Docker
- Kubernetes
- GitHub Actions

## CI/CD

The GitHub Actions workflow automatically installs dependencies, runs tests, and builds the Docker image whenever code is pushed to the main branch.

## Kubernetes

The app is deployed using a Kubernetes Deployment with 3 replicas. The Deployment controller keeps 3 pods running and automatically replaces a pod if one fails.

# AMOK - an API Mock 

## Overview
This project is a **FastAPI-based mock server** that provides a generic way to simulate API responses for various HTTP methods (GET, POST, PUT, PATCH, DELETE). It allows developers to test API calls without requiring a backend service, making it ideal for frontend development, automated testing, and integration testing.

## Key Features

- **Dynamic Routing:** Handles any API request dynamically based on the URL path and HTTP method.
- **Configurable Responses:** Uses fixture files to define expected responses, including status codes, headers, and content.
- **Call Tracking:** Maintains a record of received API calls and provides an endpoint to retrieve call counts.
- **Default Response Handling:** Returns a default response if no matching configuration is found.
- **Environment Variable Support:** Allows configuration of the fixture file directory via environment variables or command-line arguments.

## Components

### Mock API Router (`amok_router`)

- Routes all incoming API requests (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`)
- Reads response configurations from fixture files
- Maps responses dynamically based on request parameters
- Updates call counts for tracking purposes

### Call Tracking Router (`calls_router`)

- Tracks API call counts for different request methods and paths
- Provides an endpoint to query call counts for specific requests

### FastAPI Application (`app`)

- Registers the mock API and call tracking routers
- Exposes the mock API under `/api`
- Exposes call tracking under `/calls`

## How It Works

- Requests are intercepted by `amok_router`, which determines the expected response based on a predefined fixture file (`cfg.json`).
- The corresponding response is read from fixture files and returned to the client.
- If a request doesn’t match any predefined response, a default response is sent.
- `calls_router` allows tracking how many times an API endpoint has been hit.

## Use Cases

- **Frontend Development:** Simulate backend responses before an actual backend is implemented.
- **Automated Testing:** Test API integrations without requiring a live service.
- **Load Testing:** Simulate various API response scenarios for performance testing.
- **API Prototyping:** Quickly define and iterate over API response structures.

## Configuration

- The fixture file path can be set using an environment variable (`FIXTURES_PATH`) or passed as a command-line argument.
- The `cfg.json` file maps request keys (method, path) to specific response files.

This project provides a **lightweight and flexible solution** for API mocking, making it easier to develop and test API-dependent applications.


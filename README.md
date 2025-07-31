# Notification System

## Setup Instructions

1. Clone the repository.
2. Set up a virtual environment using `uv`.
3. Install dependencies.
4. Create a `.env` file from `.env.example`.
5. Run migrations using Alembic.

## Design Rationale

The system is designed to be modular, allowing for easy extension of notification channels. Each component has a single responsibility, making the codebase easier to maintain.

## Transport Mechanism Justification

FastAPI is chosen for its speed and ease of use for building APIs. It supports asynchronous processing, which is beneficial for handling notifications.

## Test Suite

Run tests using `pytest` to ensure coverage for main components.

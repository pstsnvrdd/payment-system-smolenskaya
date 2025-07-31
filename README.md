# notification-system-smolenskaya

## Overview

A modular, extensible backend for dispatching notifications across multiple channels (email, SMS, push). Clean architecture, config-driven, and testable.

## Design Rationale

- **Channel Abstraction:** All channels implement a simple interface for easy extension and testability.
- **Routing:** Strategy-based routing supports user preference, message priority, and fallback logic.
- **Observer Pattern:** Decouples notification events from listeners (logging, audit, etc.).
- **Configuration:** `.env` controls enabled channels, priorities, and fallback policies.
- **API:** FastAPI (REST) chosen for rapid dev, wide compatibility, and async support.

## Transport Choice Justification

REST (FastAPI) is chosen for its simplicity, testability, and broad client support. gRPC is an option for high throughput, but REST suffices for most notification systems.

## Setup

1. Clone repo and `cd notification-system-{your-name}`
2. Install `uv` and create env:
    ```
    pip install uv
    uv venv
    uv pip install -r requirements.txt
    ```
3. Copy `.env.example` to `.env` and adjust as needed.
4. Run Alembic migrations:
    ```
    alembic upgrade head
    ```
5. Start the server:
    ```
    uvicorn app.main:app --reload
    ```

## API Examples

**POST /notify**

```json
{
  "user_id": "user_123",
  "message": "Welcome to our platform!",
  "channels": ["sms", "email"],
  "priority": "high"
}

# Kafka-Project

A simple Flask web app with a Kafka analytics consumer script.

## Requirements

- Python 3.11+ (or installed `py` launcher)
- `pip`
- Optional: local Kafka broker on `localhost:9092` for analytics

## Install

From the project root:

```powershell
py -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Run the web app

```powershell
.\venv\Scripts\python.exe app.py
```

Then open:

- `http://127.0.0.1:5000/`

## Run the analyzer

The analyzer listens on Kafka topic `clicks` and prints counts to the terminal.

```powershell
.\venv\Scripts\python.exe analyzer.py
```

> Note: Kafka must be running on `localhost:9092` before starting `analyzer.py`.

## Notes

- `app.py` serves the frontend pages and click endpoint.
- `analyzer.py` consumes Kafka messages and prints per-user click counts.
- `venv/` is ignored in git.

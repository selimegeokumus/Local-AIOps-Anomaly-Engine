#  Local AIOps Anomaly Engine & Log Analyzer

An end-to-end, privacy-first AIOps log monitoring system that streams system logs via Redpanda/Kafka and performs real-time root cause analysis using a local Ollama (Qwen 2.5) LLM.

---

##  Tech Stack

- Streaming Event Bus: Redpanda (Kafka-compatible)
- AI / LLM Engine: Ollama (qwen2.5:1.5b)
- Backend Automation: Python (kafka-python, requests)
- Containerization: Docker & Docker Compose

---

##  Architecture & Workflow

[ send_logs.py ] ---> [ Redpanda / Kafka Topic ] ---> [ main.py Listener ]
                                                               |
                                                     (If level == ERROR)
                                                               |
                                                               v
                                                    [ Ollama Local LLM ]
                                                               |
                                                               v
                                                    [ AI Root Cause Analysis ]

1. Log Ingestion: Microservices or test scripts publish JSON-formatted logs to the system-logs topic in Redpanda.
2. Filtering Engine: Python consumer continuously listens to the stream and filters for ERROR or CRITICAL entries.
3. Local AI Analysis: Upon anomaly detection, log payload is forwarded to a local Ollama model instance for automated Root Cause Analysis and remediation steps.

---

##  Quickstart Guide

### 1. Start Infrastructure
Run Docker Compose to spin up Redpanda and Ollama services:
docker compose up -d

### 2. Pull Local AI Model
Ensure the Ollama instance has the preferred lightweight model:
docker exec -it aiops-ollama ollama run qwen2.5:1.5b

### 3. Install Python Dependencies
pip install kafka-python requests

### 4. Run AIOps Engine
Start the primary anomaly detection listener:
python main.py

### 5. Simulate Logs & Test
In a secondary terminal, trigger test logs:
python send_logs.py

---

##  Features

- Zero Cloud Dependency: Runs completely on localhost using local open-source models.
- Low Latency Event Streaming: Powered by Redpanda C++ Kafka API implementation.
- Actionable DevOps Insights: Generates clean, bulleted root cause analysis and immediate remediation strategies for system failures.

---


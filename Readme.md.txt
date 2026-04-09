# Email Support OpenEnv Environment

## 🧠 Overview

This project implements a simple and reliable OpenEnv environment that simulates a real-world email triage workflow. The environment is designed for training and evaluating AI agents on customer support tasks such as classifying and routing emails.

This environment follows the OpenEnv specification with `step()`, `reset()`, and `state()` APIs.

---

## 🌍 Motivation

Email triage is a common task in customer support systems. Agents must understand user queries and route them to the correct team. This environment provides a clean and reproducible setup for evaluating such decision-making.

---

## ⚙️ Environment Design

### Observation Space

Each observation contains:

* `email` (string): Content of the email
* `urgency` (string): Priority level (low, medium, high)

### Action Space

The agent can take one of the following actions:

* `billing` → route to billing team
* `tech` → route to technical team

---

## 🎯 Tasks

### 🟢 Easy

* Single email
* Clear classification

### 🟡 Medium

* Multiple emails
* Mixed categories

### 🔴 Hard

* Complex emails with overlapping intent

---

## 🏁 Reward Function

* +1.0 → Correct classification
* -0.5 → Incorrect classification

Rewards are deterministic and provide meaningful feedback during execution.

---

## 🧪 Grading

Each task is evaluated using a deterministic grader:

```
score = correct_predictions / total_emails
```

This ensures reproducibility and fairness with scores ranging between 0.0 and 1.0.

---

## 🤖 Baseline Agent

A simple rule-based baseline is provided in `inference.py`.

Example logic:

* Emails containing "payment" or "refund" → billing
* Emails containing "error", "login", "not working" → tech

---

## 🚀 Setup Instructions

### Install dependencies

```
pip install -r requirements.txt
```

### Run API

```
uvicorn app:app --reload
```

### Run baseline inference

```
python inference.py
```

---

## 🐳 Docker

To build and run:

```
docker build -t email-env .
docker run -p 7860:7860 email-env
```

---

## ☁️ Deployment

The environment is containerized and deployable on Hugging Face Spaces using Docker.

---

## 📊 Baseline Performance

The rule-based baseline achieves consistent and reproducible scores across all tasks, validating correct environment behavior.

---

## ✅ OpenEnv Compliance

* Implements `reset()`, `step()`, and `state()` APIs
* Uses structured observation and action spaces
* Includes 3 tasks (easy, medium, hard)
* Deterministic grading with scores between 0.0–1.0
* Containerized with Docker for reproducibility

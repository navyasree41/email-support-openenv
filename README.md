# Email Support OpenEnv

\---

title: Email Support OpenEnv

emoji: 🤖

colorFrom: blue

colorTo: purple

sdk: docker

app\_file: app.py

pinned: false

\---

This project implements an OpenEnv environment that simulates a real-world customer support email triage system.

Agents process incoming emails and classify them into:

* **billing** (payments, refunds, transactions)
* **tech** (errors, bugs, login or system issues)

The environment provides:

* Step / Reset / State APIs
* 3 difficulty levels (easy, medium, hard)
* Deterministic reward system
* Baseline inference agent
* Dockerized setup for reproducible evaluation

This project is designed for training and evaluating AI agents on structured decision-making tasks.


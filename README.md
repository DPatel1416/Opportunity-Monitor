# Opportunity-Monitor
## Overview

Opportunity Monitor is a Python-based web monitoring application designed to help users quickly identify new job opportunities posted on Hiring website and website where user has to constantly refresh page to pick shifts.

The application continuously monitors a specified URL, analyzes the page content, and sends real-time Discord notifications when potential job postings are detected.

This project was originally developed to help a friend monitor online employment opportunities and available work shifts in real time, providing instant notifications whenever new opportunities became available.

---

## Features

- Automated website monitoring using Playwright
- Continuous polling every 30 seconds
- Dynamic webpage content analysis
- Detection of job availability indicators
- Instant Discord webhook notifications
- Timestamped monitoring logs
- Error handling and recovery
- Easily configurable monitoring interval

---

## Technologies Used

- Python
- Playwright
- Discord Webhooks
- Requests Library

---

## How It Works

1. The application opens the target webpage.
2. Every 30 seconds, it retrieves and analyzes the page content.
3. If job-related keywords are detected, a Discord notification is sent.
4. Duplicate alerts are prevented using an internal alert state.
5. Monitoring continues until the application is stopped.

---

## Project Structure

```
OpportunityMonitor/
│
├── monitor.py
├── README.md
├── .gitignore
└── myenv/ (not included in repository)
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/opportunity-monitor.git
cd opportunity-monitor
```

### Create a virtual environment

```bash
python -m venv myenv
```

### Activate the virtual environment

Windows:

```bash
myenv\Scripts\activate
```

### Install dependencies

```bash
pip install playwright requests
playwright install chromium
```

---

## Configuration

Before running the application, update the following variables inside `monitor.py`:

```python
URL = "YOUR_TARGET_URL"
WEBHOOK_URL = "YOUR_DISCORD_WEBHOOK"
CHECK_EVERY_SECONDS = 30
```

---

## Running the Application

```bash
python monitor.py
```

## Educational Purpose

This project was created as a learning exercise to gain practical experience with:

- Web automation
- Browser scripting
- Real-time monitoring systems
- API integrations
- Python development
---

## Author

Dhruv Patel

Computer Science Student  
Ottawa, Ontario

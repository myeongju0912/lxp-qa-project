# LXP QA Automation Project

## 1. Project Overview
This project performs QA automation testing for the LXP (Learning Experience Platform).

Automation testing was implemented using Selenium and pytest, and performance testing was conducted using Apache JMeter.

The test target is the Sandbox learning test functionality within the Courses menu.

---

## 2. Project Structure

LXP-QA-PROJECT
│
├── config/
├── pages/
├── tests/
├── conftest.py
└── requirements.txt

---

## 3. Test Environment

- OS: macOS
- Language: Python 3.x
- Automation Tool: Selenium, pytest
- Performance Tool: Apache JMeter
- Browser: Chrome

---

## 4. How to Run Tests

pip install -r requirements.txt

pytest -v -s

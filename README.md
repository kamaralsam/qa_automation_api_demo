# QA Automation API + UI Demo 🚀

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.12-blue" />
  <img src="https://img.shields.io/badge/pytest-9.0-orange" />
  <img src="https://img.shields.io/badge/Selenium-WebDriver-green" />
  <img src="https://img.shields.io/badge/Project%20Type-API%20%2B%20UI%20Tests-brightgreen" />
</p>

**Author:** Kamar Alsamerraey  
**Tech:** Python · pytest · Selenium WebDriver · webdriver-manager · Requests  

---

## 📌 Overview

This project demonstrates **end-to-end QA automation** skills by combining:

- **API testing** with `requests`
- **UI testing** with Selenium WebDriver
- **pytest fixtures & test structure**
- **Manual QA documentation** (test plan, test cases, bug reports)

It is designed as a clean, industry-style example suitable for a **Junior QA / QA Automation / SDET-in-training** profile.

---

## 🧪 Test Types

### 1️⃣ API Test – ReqRes Users Endpoint

**File:** `tests/test_users_api.py`  

Covers:

- Sending a `GET` request to a public API
- Asserting `200 OK` status code
- Validating JSON structure and data types

```python
def test_get_users_list_returns_200_and_users():
    response = requests.get(f"{BASE_URL}/users?page=2")

    assert response.status_code == 200

    data = response.json()
    assert "data" in data
    assert isinstance(data["data"], list)
    assert len(data["data"]) > 0


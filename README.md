**QA Automation API + UI Demo**


Author: Kamar Alsamerraey
Tech: Python · pytest · Selenium · WebDriver Manager · Requests

🔍 Overview

This project demonstrates end-to-end QA automation skills, combining:

API Testing using requests

UI Testing using Selenium WebDriver

pytest test structure + fixtures

Manual test documentation (test plan, test cases, bug reports)

It is designed as a clean, industry-style example for a junior QA/Automation role.

🧪 Test Types Included
1. API Test

Located in:

tests/test_users_api.py


Covers:

GET request

Assert status code

Validate response structure

Validate data types and list length

Code sample:
def test_get_users_list_returns_200_and_users():
    response = requests.get(f"{BASE_URL}/users?page=2")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data and isinstance(data["data"], list)

2. UI Test (Selenium)

Located in:

tests/ui/test_login_ui.py


Covers:

Navigating to login page

Entering credentials

Waiting for inventory page

URL validation

⚙️ Project Structure
qa_automation_api_demo/
│
├── manual/
│   ├── bug_reports.md
│   ├── test_cases_ui.md
│   └── test_plan.md
│
├── tests/
│   ├── api/
│   │   └── test_users_api.py
│   ├── ui/
│   │   └── test_login_ui.py
│   ├── conftest.py
│
├── utils/
│   └── config.py
│
├── venv/
├── README.md
└── requirements.txt

▶️ How to Run Tests
1. Activate virtual environment

Windows:

venv\Scripts\activate

2. Install dependencies
pip install -r requirements.txt

3. Run API tests
pytest tests/test_users_api.py -v

4. Run UI tests
pytest tests/ui/test_login_ui.py -v

🚀 Tools & Libraries Used

Python 3.12

pytest

requests

selenium

webdriver-manager

✨ Purpose

This project showcases the essential core skills for:

QA Tester

QA Automation Engineer (Junior)

Software Test Engineer

SDET (in training)

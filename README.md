# 🤖 E-Commerce UI Automation Framework (Selenium & Python)

## 📝 Project Overview
This repository contains a robust End-to-End (E2E) UI automation framework designed to validate critical user journeys on an E-commerce platform. Built with Python and Selenium WebDriver, this project strictly adheres to the **Page Object Model (POM)** design pattern, ensuring high maintainability, code reusability, and scalability for the test suite.

## 🛠️ Tech Stack & Tooling
* **Language:** Python 3
* **Browser Automation:** Selenium WebDriver
* **Test Framework:** Pytest (Test runner and assertions)
* **Driver Management:** WebDriver Manager (Automated binary management)
* **Design Pattern:** Page Object Model (POM)

## 🎯 Automated Test Scenarios (E2E Flow)
The automated suite simulates a real user's purchasing journey, validating the following core functionalities:
1. **Authentication:** Secure login validation with valid credentials.
2. **Inventory Interaction:** Dynamic product selection and interaction.
3. **Cart Management:** Accurate state management of the shopping cart (adding/removing items).
4. **Checkout Integrity:** End-to-end validation of the checkout process and order calculation.

## 📁 Project Architecture (POM)
```text
ui-automation-selenium/
├── pages/                 # Page Objects: Element locators and page-specific methods
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
├── tests/                 # Test files containing the actual execution steps and assertions
│   └── test_ecommerce_flow.py
├── conftest.py            # Pytest fixtures for WebDriver setup and teardown
├── requirements.txt       # Project dependencies
└── README.md
```

🚀 Getting Started
Prerequisites
Python 3.8+ installed.

Google Chrome installed (WebDriver is managed automatically).

Installation & Execution

Clone the repository:

```Bash
git clone [https://github.com/IvanCGCA/ui-automation-selenium.git](https://github.com/IvanCGCA/ui-automation-selenium.git)
cd ui-automation-selenium
```

Set up the virtual environment:

```Bash
python -m venv venv
# On Windows: .\venv\Scripts\activate
# On Mac/Linux: source venv/bin/activate
```

Install dependencies:

```Bash
pip install -r requirements.txt
```

Execute the automated suite:


Run Pytest to trigger the browser automation:

```Bash
pytest -v --tb=short
```

(Add the --headed flag if configured, or just let Selenium launch the browser to watch the magic happen).

Linkedin: www.linkedin.com/in/ivan-vega-porras

UI Automation Engineered by Iván Vega Porras

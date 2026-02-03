# Playwright UI + API Automation Framework – Demo E-Commerce Project

A test automation framework built with **Python**, **Playwright**, and **Pytest**, targeting a demo e-commerce website.

This project demonstrates a clean, scalable automation architecture including:
- **UI automation** with Playwright (Page Object Model)
- **API automation** with Playwright `APIRequestContext`
- Clean **pytest fixtures** architecture (modular fixtures)
- Minimal & consistent **Allure** reporting (local + CI)
- **Docker** execution (headless)
- **CI/CD** with GitHub Actions and **GitHub Pages** publishing of the Allure HTML report
- A small **integration** layer (API + UI) for cross-layer validation

---

## 🔧 Tech Stack

- Language: Python 3.x  
- UI Automation: Playwright (sync)  
- API Automation: Playwright `request.new_context()`  
- Test Runner: Pytest  
- Parallelization: pytest-xdist  
- Reporting: Allure Framework  
- Containerization: Docker  
- CI/CD: GitHub Actions + GitHub Pages (Allure HTML)

---

## ✅ What’s Covered

### UI Tests (Examples)
- Register user
- Login (valid & invalid)
- Logout
- Test Cases page validation
- Products page & product details
- Product search
- Add products to cart (price & quantity verification)

### API Tests (Examples)
- Get all products / brands
- Search product (valid + missing parameter)
- Verify login (valid/invalid/missing parameter)
- Create/register user account
- Method not supported scenarios

### Integration Tests (API + UI)
- Example: **Verify login via API** → then **login via UI** using the same user

### Failure Debugging (Allure Attachments)
- Automatic screenshot capture on **test failure**
- Screenshot is attached directly to the relevant **Allure test case**
- Works in **local runs**, **Docker**, and **CI** (GitHub Actions)

### Parallel Execution (pytest-xdist)
- Parallel test execution enabled via **pytest-xdist**
- Helps reduce total suite runtime while keeping stability
- Example run:
  - `pytest -n 4 --alluredir=allure-results`

### Allure Reporting (Minimal & Practical)
Project conventions:
- allure.feature is used to group tests by system area
- allure.title is used to provide human-readable test names
- Automatic screenshot attachment on UI test failures
- No over-tagging (story / severity only when truly needed)

### Secure Secrets Handling
- Passwords are never stored in JSON or source code
- Sensitive data is injected via environment variables:
  - os.getenv("USER_PASSWORD") for local runs
  - GitHub Secrets (USER_PASSWORD) in CI pipelines
---

## 📁 Project Structure

> (Names can vary slightly by repo, but this is the intended structure)
.
├── api/
│ └── clients/
├── pages/
├── tests/
│ ├── api/
│ │ └── conftest.py
│ ├── ui/
│ │ └── conftest.py
│ ├── integration/
│ │ ├── conftest.py
│ │ └── test_login_api_then_ui.py
│ ├── fixtures/
│ │ ├── api_fixtures.py
│ │ └── ui_fixtures.py
│ └── conftest.py
├── utilities/
├── data/
├── pytest.ini
├── Dockerfile
└── README.md


### Fixtures Design (Important)
- `tests/conftest.py` contains **shared** fixtures (e.g. `base_url`, `existing_user`, `user_password`) + Allure hooks plugin.
- `tests/fixtures/ui_fixtures.py` contains UI fixtures (`browser`, `context`, `page`, `home`)
- `tests/fixtures/api_fixtures.py` contains API fixtures (`api_request_context`, `auth_client`, etc.)
- Each test area loads what it needs via its local `conftest.py`.

This prevents loading UI fixtures when running API-only tests, and keeps CI stable.

---

## 📦 Test Data Management (Read Files)
data/
├── invalid_logins.json
├── user_data.json

## 🏷️ Pytest Markers

Configured in `pytest.ini`:

- `smoke` – fast critical tests
- `regression` – broader suite
- `integration` – cross-layer tests (API + UI)

Examples:
- Run smoke only:
  ```bash
  pytest -m smoke

## Run integration tests only:
pytest -m integration

## Run smoke tests excluding integration:
pytest -m "smoke and not integration"

---

## 🔐 Environment Variables (Required)

This framework expects the existing user password to be provided via an environment variable.

- For local runs, the variable is read from the system environment.
- In CI, the same variable is injected using GitHub Secrets.

The same mechanism is used across UI, API, and integration tests.

## ▶️ Running Tests Locally (No Docker)

1. Create and activate a virtual environment:

cd playwright-ui-api-automation  
python3 -m venv .venv  
source .venv/bin/activate  

2. Install dependencies:

pip install --upgrade pip  
pip install -r requirements.txt  

3. Install Playwright browsers (one-time setup):

playwright install  

4. Run the test suite and generate Allure results:

pytest --alluredir=allure-results  

5. Run smoke tests only:

pytest -m smoke --alluredir=allure-results  

6. View the Allure report (Allure CLI must be installed locally):

allure serve allure-results  
### Example run with environment variables and parallel execution

USER_PASSWORD="your_password" pytest -n 4 --reruns 3 --reruns-delay 1 --alluredir=allure-results

## 🐳 Running Tests with Docker (Headless)

1. Build the Docker image:

cd playwright-ui-api-automation  
docker build -t playwright-tests .  

2. Run tests inside the Docker container and export Allure results:

docker run --rm \
  -e USER_PASSWORD="your_password" \
  -v "$(pwd)/allure-results:/app/allure-results" \
  playwright-tests  

3. View the Allure report locally:

allure serve allure-results  


## CI (GitHub Actions)

Tests are executed headlessly using the same Docker image and pytest configuration used locally.

In CI, the existing user password is provided via GitHub Secrets.

Create a repository secret with the following name:

USER_PASSWORD

This secret is injected into the GitHub Actions workflow and exposed to the test runtime as an environment variable.

Steps to configure:

Open the repository on GitHub

Go to Settings

Navigate to Secrets and variables → Actions

Click New repository secret

Set the name to USER_PASSWORD

Set the value to the existing user password

Save the secret

The workflow automatically passes this variable to the test execution environment.




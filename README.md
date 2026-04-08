# QA Portfolio — Playwright + Pytest

Automated test suite for [SauceDemo](https://www.saucedemo.com) e-commerce platform.

## Tech Stack
- Python 3.14
- Playwright
- Pytest
- GitHub Actions (CI/CD)

## Test Coverage
- `tests/test_login.py` — authentication tests (valid login, invalid credentials, locked user, logout)
- `tests/test_inventory.py` — product page tests
- `tests/test_cart.py` — shopping cart tests (add, remove, multiple items)
- `tests/test_checkout.py` — checkout flow tests (valid data, empty fields)
- `tests/test_api.py` — REST API tests using JSONPlaceholder

## Page Object Model
Tests follow the Page Object Model pattern, separating locators from test logic.

## How to Run
```bash
pip install pytest pytest-playwright requests
playwright install chromium
pytest
```

## CI/CD
Tests run automatically on every push via GitHub Actions.
# LingoBuddy Test Automation

Automated test suite for [LingoBuddy](https://github.com/jgone99/lingobuddy), a full-stack Spanish/English language learning web application built with Next.js, Postgres, and Clerk authentication.

## Overview
This project demonstrates end-to-end test automation using Python, Pytest, and Playwright following the Page Object Model pattern. It covers UI testing, API testing, access control verification, and game interaction testing against a dedicated test database with controlled test data.

## Tech Stack
- Python 3.12, Pytest, Playwright
- psycopg2 for direct database access
- Page Object Model (POM)
- Supabase (test database)
- python-dotenv for environment management

## Test Coverage

| File | Tests | Description |
|------|-------|-------------|
| `test_api.py` | 1 | API endpoint authentication |
| `test_homepage.py` | 2 | Translation feature (EN→ES, ES→EN) |
| `test_authenticated.py` | 8 | Access control for protected routes |
| `test_snowman.py` | 4 | Snowman game score and highscore behavior |

**Total: 15 tests (14 passing, 1 xfail)**

## Key Implementation Details
- **Page Object Model** — each page has a dedicated class encapsulating its locators and interactions
- **Authenticated testing** — Playwright `storageState` used to persist login sessions across tests
- **Database integration** — psycopg2 fixtures with rollback teardown for test isolation
- **Controlled test data** — dedicated Supabase test database with a single known word pair for deterministic test behavior
- **Parametrized access control tests** — single test function validates all protected routes
- **Known bug documented** — `test_high_score_increments` marked `xfail` with root cause identified

## Project Structure
```text
Test Automation/
  conftest.py
  pytest.ini
  requirements.txt
  .env                    # not committed
  auth.json               # not committed
  tests/
    conftest.py
    auth_setup.py
    config.py
    helpers.py
    pages/
      __init__.py
      home_page.py
      login_page.py
      snowman_page.py
    test_api.py
    test_homepage.py
    test_authenticated.py
    test_snowman.py
```

## Setup
Requires a local LingoBuddy instance, a Supabase test database, and a `.env` file with credentials. See `tests/config.py` for required environment variables.

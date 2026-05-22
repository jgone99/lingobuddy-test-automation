# LingoBuddy Test Automation

Automated test suite for [LingoBuddy](https://github.com/jgone99/LingoBuddy), a full-stack language learning web application.

## Tech Stack
- Python
- Pytest
- Playwright
- Page Object Model (POM)

## Test Coverage
- Homepage translation feature (English to Spanish, Spanish to English)
- Authentication and protected routes (in progress)

## Structure

tests/

## Running Tests
```bash
# Install dependencies
pip install pytest requests playwright
python -m playwright install

# Run all tests
pytest -v

# Run specific test file
pytest tests/test_homepage.py -v
```

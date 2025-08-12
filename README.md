# 🧪 Simple Test Project

Automated tests in Python with pytest and Playwright.

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
python -m pytest tests/ -v -p no:allure_pytest

# Check code quality
flake8 .
```

## 🤖 CI/CD

- ✅ **Automated checks** on branch push
- ✅ **Flake8 linter** for code quality
- ✅ **Pytest tests** for functionality verification

## 📁 Structure

```
├── pages/           # Page Object Model
├── tests/           # Tests
├── .github/         # GitHub Actions
└── requirements.txt # Dependencies
```
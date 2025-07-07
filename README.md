---
title: CppCheck‑Py
emoji: 🚀
colorFrom: red
colorTo: red
sdk: docker
app_port: 8501
tags:
  - streamlit
pinned: false
short_description: Streamlit-based C++ syntax checker (subset) with CLI and web UI
---

# CppCheck‑Py

> A Python‑based syntax checker for a defined subset of C++.

A web and CLI C++ syntax checker built with Python and Streamlit.

- **Live demo:** [CppCheck-Py on Hugging Face Spaces](https://itsjerry125-cppcheck-py.hf.space/)

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Folder Structure](#folder-structure)
- [Installation](#installation)
- [Usage](#usage)
  - [Command-Line](#command-line)
  - [Web UI (Streamlit)](#web-ui-streamlit)
- [Testing](#testing)
- [Development & CI/CD](#development--cicd)
- [License](#license)

---

## Project Overview

CppCheck‑Py is a streamlined syntax‑checking tool written in pure Python. It processes C++ source code within a selected language subset, identifies syntax errors, and reports them in a clear, user‑friendly manner. Designed for both command‑line and web‑based integration, CppCheck‑Py emphasizes modular, object‑oriented design.

---

## Features

- **OOP Lexer & Parser**  
  Implements a class‑based lexer and recursive‑descent parser to tokenize input and verify grammar rules.

- **Comprehensive Error Reporting**  
  Pinpoints syntax errors with line and column information, offering suggestions to correct common mistakes.

- **Pretty-Printed AST**  
  Displays a human-friendly abstract syntax tree for valid code.

- **Dual Web UI Input**  
  Upload a file or type/paste code directly in the browser.

- **Modular Design**  
  Separates concerns into dedicated components (lexer, parser, checker, error utilities) for easy extension.

- **CLI Interface**  
  Quick command‑line access for file checks.

- **Automated Testing & CI/CD**  
  All core logic is covered by unit tests and deployed automatically to Hugging Face Spaces.

---

## Folder Structure

```
CppCheck-Py/
├── backend/              # Core syntax‑checking service
│   ├── main.py           # CLI entry point
│   ├── example1.cpp      # Example C++ files
│   ├── src/              # Module source code
│   │   ├── ast.py
│   │   ├── checker.py
│   │   ├── errors.py
│   │   ├── lexer.py
│   │   ├── parser.py
│   │   ├── token.py
│   │   ├── utils.py
│   │   └── __init__.py
│   └── __init__.py
├── app.py                # Streamlit web app (root for Hugging Face Spaces)
├── requirements.txt      # Python dependencies
├── setup.py              # Packaging and CLI entry point
├── tests/                # Automated tests
│   └── unit/
├── .github/workflows/    # CI/CD pipeline
│   └── ci_and_deploy.yml
├── README.md             # Project overview and usage
└── LICENSE
```

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/D4PHOENIX/CppCheck-Py.git
   cd CppCheck-Py
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv CppCheck-Py
   # On Windows:
   CppCheck-Py\Scripts\activate
   # On Linux/macOS:
   source CppCheck-Py/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **(Optional) Install as a package for CLI**
   ```bash
   pip install -e .
   ```

---

## Usage

### Command-Line

Check a C/C++ file for syntax errors:
```bash
python backend/main.py backend/example1.cpp
```
or, if installed as a package:
```bash
cppcheck-py backend/example1.cpp
```

**Output:**
- If syntax is correct:  
  - Shows "✅ Syntax is correct!" and a pretty-printed AST.
- If syntax error:  
  - Shows "❌ Syntax Error detected!" with line/column, message, and hint.

### Web UI (Streamlit)

You can use the web interface locally or on Hugging Face Spaces.

#### **Run locally:**
```bash
streamlit run app.py
```
- Open the provided local URL in your browser.
- Choose "Upload file" or "Type code" to check syntax.

#### **Try the live demo:**
[CppCheck-Py on Hugging Face Spaces](https://itsjerry125-cppcheck-py.hf.space/)

---

## Testing

Run all unit tests:
```bash
pytest
```
or, for more details:
```bash
pytest --maxfail=1 --disable-warnings -q
```

---

## Development & CI/CD

- **CI/CD:**  
  Automated tests and deployment to Hugging Face Spaces are configured via GitHub Actions (`.github/workflows/ci_and_deploy.yml`).
- **Coverage:**  
  Tests are run with coverage reporting and JUnit XML output.
- **Deployment:**  
  On every push/PR to `main`, if enough tests pass, the app is deployed to [CppCheck-Py on Hugging Face Spaces](https://itsjerry125-cppcheck-py.hf.space/).

---

## License

MIT License  
Copyright (c) 2025 Daud Noman

---

## Acknowledgements

- Built by Daud Noman, Muhammad Arham Shafaat, Wassam Kham
- Powered by Python, Streamlit, and Hugging Face Spaces

---
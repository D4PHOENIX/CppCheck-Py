# CppCheck-Py

> A Python‑based syntax checker for a defined subset of C++.

## Table of Contents

- [CppCheck-Py](#cppcheck-py)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Features](#features)
  - [Folder Structure](#folder-structure)
  - [Installation](#installation)
  - [Usage](#usage)

---

## Project Overview

CppCheck‑Py is a streamlined syntax‑checking tool written in pure Python. It processes C++ source code within a selected language subset, identifies syntax errors, and reports them in a clear, user‑friendly manner. Designed for both command‑line and web‑based integration, CppCheck‑Py emphasizes modular, object‑oriented design.

---

## Features

- **OOP Lexer & Parser**  
  Implements a class‑based lexer and recursive‑descent parser to tokenize input and verify grammar rules.

- **Comprehensive Error Reporting**  
  Pinpoints syntax errors with line and column information, offering suggestions to correct common mistakes.

- **Modular Design**  
  Separates concerns into dedicated components (lexer, parser, checker, error utilities) for easy extension.

- **CLI Interface**  
  Quick command‑line access for file checks.

---

## Folder Structure

```
CppCheck-Py/
├── backend/              # Core syntax‑checking service
│   ├── main.py            
│   └── src/              # Module source code
│       ├── lexer.py
│       ├── parser.py
│       ├── checker.py
│       ├── errors.py
│       ├── schemas.py
│       └── routers/      # API route handlers 
├── frontend/             # Web UI
│   └── app.py
├── tests/                # Automated tests
│   ├── unit/
│   └── integration/
├── docs/                 # Documentation and diagrams
├── requirements.txt      # Python dependencies
├── Dockerfile            # Container definition 
└── README.md             # Project overview and usage
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
   python3 -m venv venv
   source venv/bin/activate  # (Windows: venv\Scripts\activate)
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

- **Command‑Line Check**  
  ```bash
  python backend/main.py --file path/to/code.cpp
  ```
  Runs syntax analysis on the specified file and outputs any errors.

---

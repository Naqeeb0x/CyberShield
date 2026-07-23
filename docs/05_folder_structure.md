# CyberShield V1 Folder Structure

## 1. Introduction

The folder structure of CyberShield is designed to promote modularity, maintainability, scalability, and separation of concerns.

Each directory has a well-defined responsibility, making the project easier to understand, develop, test, and extend.

The structure follows common software engineering practices used in professional Python applications.

## 2. Project Structure

```text
CyberShield/
│
├── backend/
├── frontend/
├── docs/
├── tests/
├── uploads/
├── vfs/
├── database/
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

## 3. Folder Descriptions

### backend/

Contains the Python backend application, business logic, database interaction, authentication, parser, detection engine, and API.

---

### frontend/

Contains the user interface, including HTML templates, CSS stylesheets, JavaScript files, and static assets.

---

### docs/

Contains all project documentation, including architecture, database design, API documentation, and user guides.

---

### tests/

Contains unit tests, integration tests, and future automated testing scripts.

---

### uploads/

Temporary storage for newly uploaded files before they are processed.

---

### vfs/

Stores the original evidence files used by the Virtual File System.

---

### database/

Contains the SQLite database and future database migration files.

## 4. Backend Structure

```text
backend/
│
├── app.py
├── config.py
├── database.py
│
├── auth/
│   ├── login.py
│   ├── register.py
│   └── password.py
│
├── parser/
│   ├── parser.py
│   ├── windows_parser.py
│   └── linux_parser.py
│
├── detection/
│   ├── detection_engine.py
│   ├── rules.py
│   └── severity.py
│
├── alerts/
│   ├── alert_manager.py
│   └── notification.py
│
├── incidents/
│   ├── incident_manager.py
│   └── evidence.py
│
├── reports/
│   ├── report_generator.py
│   └── export.py
│
├── vfs/
│   ├── vfs.py
│   └── file_manager.py
│
└── utils/
    ├── logger.py
    ├── validator.py
    └── helpers.py
```

## 5. Frontend Structure

```text
frontend/
│
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   ├── upload.html
│   ├── logs.html
│   ├── alerts.html
│   ├── incidents.html
│   ├── reports.html
│   ├── settings.html
│   └── profile.html
│
├── static/
│   ├── css/
│   │   ├── style.css
│   │   ├── dashboard.css
│   │   └── auth.css
│   │
│   ├── js/
│   │   ├── dashboard.js
│   │   ├── upload.js
│   │   └── alerts.js
│   │
│   └── images/
│       ├── logo.png
│       ├── icons/
│       └── backgrounds/
```

## 6. Frontend Organization

The frontend is divided into two primary components:

### Templates

Contains all HTML pages rendered by the backend.

### Static

Contains assets that do not change during execution.

These include:

- CSS stylesheets
- JavaScript files
- Images
- Icons
- Background assets

## 7. Coding Standards

To maintain consistency and readability, CyberShield follows the coding standards below.

### Python

- Follow PEP 8 style guidelines.
- Use descriptive variable and function names.
- Keep functions focused on a single responsibility.
- Avoid unnecessary global variables.
- Write meaningful comments where appropriate.

---

### HTML

- Use semantic HTML elements.
- Maintain consistent indentation.
- Keep page layouts modular and organized.

---

### CSS

- Group related styles together.
- Use meaningful class names.
- Avoid duplicate styles.

---

### JavaScript

- Keep each file focused on one feature.
- Use descriptive function names.
- Separate UI logic from business logic whenever possible.

---

### Git

- Commit changes frequently.
- Use meaningful commit messages.
- Push completed milestones to GitHub.

## 8. Naming Conventions

The following naming conventions will be used throughout the project.

### Files

- Python files: `snake_case.py`
- HTML files: `lowercase.html`
- CSS files: `lowercase.css`
- JavaScript files: `lowercase.js`

---

### Variables

Use descriptive `snake_case`.

Example:

```python
failed_login_count
parsed_events
current_user
```

---

### Functions

Use action-oriented names.

Examples:

```python
parse_logs()
detect_bruteforce()
generate_report()
authenticate_user()
```

---

### Classes (Future)

Use PascalCase.

Examples:

```python
LogParser
DetectionEngine
ReportGenerator
```

## 9. Module Responsibilities

Each backend module has a clearly defined responsibility to ensure modularity and maintainability.

---

### Authentication Module

**Purpose**

Manages user authentication and authorization.

**Responsibilities**

- User login
- Password verification
- Session management
- Role-Based Access Control (RBAC)

---

### Parser Module

**Purpose**

Processes uploaded log files and converts raw log entries into structured events.

**Responsibilities**

- Validate uploaded files
- Parse supported log formats
- Extract security-relevant information
- Store parsed events in the database

---

### Detection Module

**Purpose**

Analyzes parsed events to identify suspicious activities.

**Responsibilities**

- Execute detection rules
- Assign severity levels
- Generate alerts
- Record triggered rules

---

### Alerts Module

**Purpose**

Manages security alerts generated by the Detection Engine.

**Responsibilities**

- Create alerts
- Update alert status
- Assign alerts to analysts
- Maintain investigation notes

---

### Incidents Module

**Purpose**

Manages confirmed security incidents.

**Responsibilities**

- Create incidents
- Link related alerts
- Track investigation progress
- Record resolution details

---

### Reports Module

**Purpose**

Generates investigation and security reports.

**Responsibilities**

- Generate reports
- Export reports
- Summarize incidents
- Produce security statistics

---

### Virtual File System (VFS)

**Purpose**

Stores and manages uploaded evidence files.

**Responsibilities**

- Store original files
- Organize evidence
- Verify file integrity
- Retrieve evidence when required

---

### Utilities Module

**Purpose**

Provides shared helper functions used across the application.

**Responsibilities**

- Logging
- Input validation
- Common helper functions
- Error handling
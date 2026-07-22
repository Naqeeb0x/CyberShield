# CyberShield V1

# Software Requirements Specification (SRS)

Version: 1.0

---

## 1. Introduction

The Software Requirements Specification (SRS) defines the functional and non-functional requirements of CyberShield Version 1.

This document serves as the primary reference for the design, development, testing, and maintenance of the project. It describes the expected behavior of the system, the features it must provide, the users who will interact with it, and the constraints under which it will operate.

The objective of this document is to ensure that all future development follows a well-defined plan and that every component of CyberShield is built according to clearly specified requirements.

## 2. Purpose

The purpose of CyberShield Version 1 is to develop a modular Security Operations Center (SOC) platform that assists security analysts in monitoring and investigating security events.

The system will provide capabilities for user authentication, security log management, rule-based threat detection, alert generation, incident management, dashboard visualization, and security reporting.

CyberShield is designed as both a learning platform and a portfolio-quality software project that demonstrates cybersecurity concepts, software engineering principles, modular architecture, and secure development practices.

## 3. Project Scope

CyberShield Version 1 is designed to simulate the core functionality of a Security Operations Center (SOC). The system will provide a centralized platform for collecting, analyzing, and managing security-related information.

The scope of Version 1 includes:

- User authentication and authorization
- Security log upload and storage
- Log parsing and validation
- Rule-based threat detection
- Alert generation and management
- Incident management
- Dashboard for monitoring security events
- Security report generation
- SQLite database integration
- Modular backend architecture
- Interactive web-based frontend

The system is designed to be extensible so that additional features can be incorporated into future versions without major architectural changes.

## 4. System Actors

CyberShield Version 1 has three primary user roles.

### 1. Administrator

The Administrator is responsible for managing the entire system.

Responsibilities:

- Manage user accounts
- Assign user roles
- View all logs
- View all alerts
- Manage incidents
- Access system reports
- Configure system settings

---

### 2. SOC Analyst

The SOC Analyst is responsible for monitoring security events and investigating suspicious activities.

Responsibilities:

- Upload security logs
- View parsed logs
- Investigate alerts
- Create incidents
- Update incident status
- Generate investigation reports

---

### 3. Viewer

The Viewer has read-only access to the system.

Responsibilities:

- View dashboard
- View reports
- View incidents
- View alerts

The Viewer cannot modify any system data.

## 5. Functional Requirements

Functional requirements describe the features and services that CyberShield Version 1 must provide to its users.

Each requirement is assigned a unique identifier for easier tracking during development and testing.

---

### Authentication

**FR-001** The system shall allow registered users to log in using a username and password.

**FR-002** The system shall authenticate user credentials before granting access.

**FR-003** The system shall deny access if invalid credentials are provided.

**FR-004** The system shall allow authenticated users to log out securely.

**FR-005** The system shall enforce role-based access control (RBAC) based on user roles.

### Log Management

**FR-006** The system shall allow SOC Analysts to upload supported log files.

**FR-007** The system shall validate uploaded log files before processing.

**FR-008** The system shall reject unsupported or corrupted log files.

**FR-009** The system shall parse valid log files into structured data.

**FR-010** The system shall store parsed log data in the database.

**FR-011** The system shall allow users to search log entries.

**FR-012** The system shall allow users to filter logs based on attributes such as timestamp, severity, source, username, IP address, and event type.

**FR-013** The system shall maintain the integrity of uploaded log data without modifying the original evidence.

**FR-014** The system shall record metadata for every uploaded log file, including upload time, uploader, filename, and processing status.

### Detection Engine

**FR-015** The system shall analyze parsed log data using predefined detection rules.

**FR-016** The system shall detect brute-force login attempts based on configurable thresholds.

**FR-017** The system shall detect suspicious login activities, such as multiple failed logins followed by a successful login.

**FR-018** The system shall detect unauthorized USB device connection events from supported operating system logs.

**FR-019** The system shall assign a severity level (Low, Medium, High, Critical) to each detected security event.

**FR-020** The system shall generate an alert whenever a detection rule is triggered.

**FR-021** The system shall record the detection rule responsible for generating each alert.

**FR-022** The system shall prevent duplicate alerts for the same event within a configurable time window.

### Alert Management

**FR-023** The system shall automatically create an alert whenever a detection rule is triggered.

**FR-024** The system shall assign each alert a unique identifier.

**FR-025** The system shall display the alert timestamp, severity, detection rule, source IP address, username (if available), and alert status.

**FR-026** The system shall allow SOC Analysts to acknowledge an alert.

**FR-027** The system shall allow SOC Analysts to update the alert status (New, In Progress, Resolved, Closed).

**FR-028** The system shall allow SOC Analysts to add investigation notes to an alert.

**FR-029** The system shall allow users to search and filter alerts.

**FR-030** The system shall maintain a complete audit trail of alert updates.

### Incident Management

**FR-031** The system shall allow SOC Analysts to create an incident from one or more related alerts.

**FR-032** The system shall assign each incident a unique incident identifier.

**FR-033** The system shall allow analysts to set the incident priority (Low, Medium, High, Critical).

**FR-034** The system shall allow analysts to update the incident status (Open, Under Investigation, Contained, Resolved, Closed).

**FR-035** The system shall allow analysts to record investigation notes for each incident.

**FR-036** The system shall maintain a complete history of all incident updates.

**FR-037** The system shall allow analysts to associate multiple alerts with a single incident.

**FR-038** The system shall allow users to search and filter incidents.

**FR-039** The system shall allow users to view all evidence associated with an incident.

**FR-040** The system shall allow analysts to close an incident after the investigation is complete.

### Dashboard

**FR-041** The system shall display the total number of uploaded log files.

**FR-042** The system shall display the total number of generated alerts.

**FR-043** The system shall display the total number of active incidents.

**FR-044** The system shall display alert severity statistics.

**FR-045** The system shall display recent security activities.

**FR-046** The system shall refresh dashboard data without requiring users to manually update the page.

### Reporting

**FR-047** The system shall generate investigation reports.

**FR-048** The system shall allow users to export reports.

**FR-049** The system shall include alert and incident summaries in generated reports.

**FR-050** The system shall record the report creation date and report author.

### Administration

**FR-051** The system shall allow Administrators to create user accounts.

**FR-052** The system shall allow Administrators to modify user accounts.

**FR-053** The system shall allow Administrators to disable user accounts.

**FR-054** The system shall allow Administrators to assign user roles.

**FR-055** The system shall record administrative actions for auditing purposes.

## 6. Non-Functional Requirements

### Performance

**NFR-001** The system should process uploaded log files efficiently.

**NFR-002** Dashboard pages should load within a reasonable time under normal usage.

---

### Security

**NFR-003** User passwords shall never be stored in plain text.

**NFR-004** The system shall validate all user inputs before processing.

**NFR-005** The system shall enforce Role-Based Access Control (RBAC).

---

### Reliability

**NFR-006** The system shall recover gracefully from invalid user inputs.

**NFR-007** The system shall preserve database consistency during failures.

---

### Maintainability

**NFR-008** The source code shall follow a modular architecture.

**NFR-009** Every Python module shall have a single responsibility.

**NFR-010** Every function shall contain appropriate documentation.

---

### Usability

**NFR-011** The user interface shall be simple and intuitive.

**NFR-012** Error messages shall clearly describe the problem.

---

### Scalability

**NFR-013** The architecture shall allow additional detection rules to be added without major code modifications.

**NFR-014** The system shall support future database migration if required.

## 7. Security Requirements

### Authentication Security

**SR-001** The system shall store user passwords as secure password hashes.

**SR-002** The system shall never store plaintext passwords.

**SR-003** The system shall require authentication before accessing protected resources.

---

### Authorization

**SR-004** The system shall enforce Role-Based Access Control (RBAC).

**SR-005** Users shall only access resources permitted by their assigned role.

---

### Input Validation

**SR-006** The system shall validate all user inputs before processing.

**SR-007** The system shall reject invalid or malformed input data.

---

### Audit Logging

**SR-008** The system shall record important security events such as user logins, failed login attempts, log uploads, and administrative actions.

---

### Data Integrity

**SR-009** The original uploaded log file shall remain unchanged after processing.

**SR-010** Parsed data shall accurately represent the contents of the original log file.

## 8. User Stories

### Administrator

**US-001**
As an Administrator, I want to create user accounts so that new users can access the system.

**US-002**
As an Administrator, I want to assign user roles so that users receive appropriate permissions.

**US-003**
As an Administrator, I want to disable user accounts so that unauthorized users cannot access the system.

---

### SOC Analyst

**US-004**
As a SOC Analyst, I want to upload security log files so that I can analyze security events.

**US-005**
As a SOC Analyst, I want to view parsed log entries so that I can investigate suspicious activity.

**US-006**
As a SOC Analyst, I want the system to automatically detect suspicious behavior so that I do not have to manually inspect every log entry.

**US-007**
As a SOC Analyst, I want to investigate alerts so that I can determine whether they represent real security incidents.

**US-008**
As a SOC Analyst, I want to create incidents from alerts so that I can document investigations.

---

### Viewer

**US-009**
As a Viewer, I want to view dashboards so that I can monitor overall security status.

**US-010**
As a Viewer, I want to view reports so that I can understand previous security investigations.

## 9. Acceptance Criteria

CyberShield Version 1 shall be considered complete when the following conditions are satisfied:

### Authentication

- Users can securely log in and log out.
- Invalid credentials are rejected.
- Role-Based Access Control (RBAC) is enforced.

---

### Log Management

- Supported log files can be uploaded successfully.
- Uploaded logs are validated before processing.
- Log entries are parsed correctly.
- Parsed logs are stored in the database.

---

### Detection Engine

- Detection rules identify predefined suspicious activities.
- Alerts are generated automatically.
- Alert severity is assigned correctly.

---

### Alert Management

- Analysts can view, search, filter, and update alerts.
- Investigation notes can be added.

---

### Incident Management

- Analysts can create incidents from alerts.
- Incident status can be updated.
- Investigation history is maintained.

---

### Dashboard

- Dashboard displays security statistics.
- Dashboard displays recent alerts and incidents.

---

### Reporting

- Reports can be generated successfully.
- Reports include alert and incident summaries.

---

### Software Quality

- Source code follows a modular architecture.
- Documentation is complete.
- Git history is maintained.
- The application runs without critical errors.
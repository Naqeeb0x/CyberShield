# CyberShield V1 Database Design

## 1. Introduction

The database is responsible for storing all structured information used by CyberShield Version 1.

The objective of the database design is to provide an efficient, secure, and scalable storage solution while maintaining data integrity and supporting future system expansion.

SQLite is selected as the database management system for Version 1 due to its simplicity, portability, and suitability for desktop-scale applications.

## 2. Database Objectives

The CyberShield database is designed to:

- Store user information securely.
- Store uploaded log metadata.
- Store parsed log events.
- Store generated alerts.
- Store security incidents.
- Store generated reports.
- Maintain audit logs.
- Support Role-Based Access Control (RBAC).
- Preserve relationships between different system entities.

## 3. Planned Database Tables

Version 1 will include the following tables:

1. Users
2. Roles
3. Log Files
4. Parsed Events
5. Detection Rules
6. Alerts
7. Incidents
8. Incident Alerts
9. Reports
10. Audit Logs

## 4. Roles Table

### Purpose

The Roles table defines the different user roles available in CyberShield and supports Role-Based Access Control (RBAC).

---

### Columns

| Column Name | Data Type | Constraints | Description |
|--------------|-----------|----------------------|----------------------------------------------|
| role_id      | INTEGER   | Primary Key          | Unique identifier for each role              |
| role_name    | TEXT      | UNIQUE, NOT NULL     | Name of the role                             |
| description  | TEXT      | NULL                 | Description of the role and its permissions  |

---

### Primary Key

- role_id

---

### Relationships

- One Role → Many Users

---

### Used By

- Authentication Module
- User Management Module
- RBAC System

---

### Notes

- Initial roles:
  - Administrator
  - SOC Analyst
  - Viewer

  ## 5. Users Table

### Purpose

The Users table stores information about every registered CyberShield user.

---

### Columns

| Column Name  | Data Type | Constraints          | Description                              |
|---------------|-----------|----------------------|------------------------------------------|
| user_id       | INTEGER   | Primary Key          | Unique identifier for each user          |
| username      | TEXT      | UNIQUE, NOT NULL     | Username used for authentication         |
| password_hash | TEXT      | NOT NULL             | Secure password hash                     |
| full_name     | TEXT      | NOT NULL             | User's full name                         |
| email         | TEXT      | UNIQUE, NOT NULL     | User email address                       |
| role_id       | INTEGER   | Foreign Key          | References the Roles table               |
| created_at    | DATETIME  | NOT NULL             | Account creation timestamp               |
| last_login    | DATETIME  | NULL                 | Last successful login                    |
| account_status| TEXT      | NOT NULL             | Active, Disabled, or Locked              |

---

### Primary Key

- user_id

---

### Foreign Keys

- role_id → Roles(role_id)

---

### Relationships

- Many Users → One Role

---

### Used By

- Authentication Module
- Dashboard
- Audit Logs
- Incident Management
- Report Generation

---

### Notes

- Passwords will be stored using bcrypt hashes.
- Usernames must be unique.
- Email addresses must be be unique.
- Deleted accounts will be disabled rather than permanently removed.

## 6. Log Files Table

### Purpose

The Log Files table stores metadata about every uploaded log file. The actual log file is stored inside the Virtual File System (VFS), while this table stores information required to manage and process it.

---

### Columns

| Column Name      | Data Type | Constraints           | Description                                      |
|------------------|-----------|-----------------------|--------------------------------------------------|
| log_file_id      | INTEGER   | Primary Key           | Unique identifier for the uploaded log file      |
| original_name    | TEXT      | NOT NULL              | Original filename uploaded by the user           |
| stored_name      | TEXT      | UNIQUE, NOT NULL      | Filename used inside the VFS                     |
| uploaded_by      | INTEGER   | Foreign Key           | User who uploaded the file                       |
| upload_time      | DATETIME  | NOT NULL              | Date and time of upload                          |
| file_size        | INTEGER   | NOT NULL              | Size of the uploaded file in bytes               |
| file_hash        | TEXT      | UNIQUE, NOT NULL      | SHA-256 hash of the original file                |
| processing_status| TEXT      | NOT NULL              | Pending, Processing, Completed, Failed           |

---

### Primary Key

- log_file_id

---

### Foreign Keys

- uploaded_by → Users(user_id)

---

### Relationships

- One User → Many Log Files
- One Log File → Many Parsed Events

---

### Used By

- Upload Module
- Parser Module
- Dashboard
- Report Generator
- VFS

---

### Notes

- Original evidence files remain unchanged.
- SHA-256 hashes verify file integrity.
- Metadata is stored in SQLite while files remain inside the VFS.

## 7. Parsed Events Table

### Purpose

The Parsed Events table stores every structured event extracted from uploaded log files. It serves as the primary data source for the Detection Engine, Alert Manager, Dashboard, and Incident Management modules.

---

### Columns

| Column Name     | Data Type | Constraints         | Description                                      |
|-----------------|-----------|---------------------|--------------------------------------------------|
| event_id        | INTEGER   | Primary Key         | Unique identifier for each parsed event          |
| log_file_id     | INTEGER   | Foreign Key         | References the uploaded log file                 |
| event_time      | DATETIME  | NOT NULL            | Timestamp of the event                           |
| event_type      | TEXT      | NOT NULL            | Type of security event                           |
| source_ip       | TEXT      | NULL                | Source IP address                                |
| destination_ip  | TEXT      | NULL                | Destination IP address                           |
| username        | TEXT      | NULL                | Username associated with the event               |
| hostname        | TEXT      | NULL                | Host that generated the event                    |
| severity        | TEXT      | NOT NULL            | Informational, Low, Medium, High, Critical       |
| raw_event       | TEXT      | NOT NULL            | Original parsed event data                       |
| parsed_status   | TEXT      | NOT NULL            | Parsed, Failed, Ignored                          |

---

### Primary Key

- event_id

---

### Foreign Keys

- log_file_id → Log Files(log_file_id)

---

### Relationships

- One Log File → Many Parsed Events
- One Parsed Event → Zero or More Alerts

---

### Used By

- Parser Module
- Detection Engine
- Alert Manager
- Dashboard
- Incident Management
- Report Generator

---

### Notes

- Every uploaded log may produce thousands of parsed events.
- Parsed events are immutable after successful parsing.
- The Detection Engine analyzes parsed events rather than raw log files.

## 8. Detection Rules Table

### Purpose

The Detection Rules table stores all predefined detection rules used by the Detection Engine. Each rule represents a specific security condition that CyberShield can identify.

---

### Attributes

**rule_id**
- Data Type: INTEGER
- Constraints: Primary Key, Auto Increment
- Description: Unique identifier for each detection rule.

**rule_name**
- Data Type: TEXT
- Constraints: UNIQUE, NOT NULL
- Description: Human-readable name of the detection rule.

**description**
- Data Type: TEXT
- Constraints: NOT NULL
- Description: Explains what the rule detects.

**severity**
- Data Type: TEXT
- Constraints: NOT NULL
- Description: Severity assigned when the rule is triggered.
- Allowed Values:
  - Informational
  - Low
  - Medium
  - High
  - Critical

**status**
- Data Type: TEXT
- Constraints: NOT NULL
- Description: Indicates whether the rule is active.
- Allowed Values:
  - Enabled
  - Disabled

**created_at**
- Data Type: DATETIME
- Constraints: NOT NULL
- Description: Date and time the rule was created.

---

### Primary Key

- rule_id

---

### Foreign Keys

None

---

### Relationships

- One Detection Rule can generate many Alerts.

---

### Used By

- Detection Engine
- Alert Manager
- Administrator Module
- Reporting Module

---

### Initial Detection Rules

- Multiple Failed Login Attempts
- Successful Login After Multiple Failures
- Suspicious USB Activity
- Multiple Account Lockouts
- Administrator Login Outside Business Hours

---

### Design Notes

- Rules are stored separately from application logic.
- Rules can be enabled or disabled without changing source code.
- Future versions may support custom rule creation.

## 9. Alerts Table

### Purpose

The Alerts table stores all alerts generated by the Detection Engine. Each alert represents suspicious activity identified from one or more parsed events. Alerts are reviewed by SOC Analysts before they are escalated into security incidents.

---

### Attributes

**alert_id**
- Data Type: INTEGER
- Constraints: Primary Key, Auto Increment
- Description: Unique identifier for the alert.

**event_id**
- Data Type: INTEGER
- Constraints: Foreign Key, NOT NULL
- Description: References the parsed event that triggered the alert.

**rule_id**
- Data Type: INTEGER
- Constraints: Foreign Key, NOT NULL
- Description: References the detection rule responsible for generating the alert.

**severity**
- Data Type: TEXT
- Constraints: NOT NULL
- Description: Severity level assigned to the alert.
- Allowed Values:
  - Low
  - Medium
  - High
  - Critical

**status**
- Data Type: TEXT
- Constraints: NOT NULL
- Description: Current investigation status of the alert.
- Allowed Values:
  - New
  - In Progress
  - Resolved
  - Closed

**created_at**
- Data Type: DATETIME
- Constraints: NOT NULL
- Description: Date and time the alert was generated.

**assigned_to**
- Data Type: INTEGER
- Constraints: Foreign Key
- Description: SOC Analyst currently responsible for investigating the alert.

**notes**
- Data Type: TEXT
- Constraints: NULL
- Description: Investigation notes added by analysts.

---

### Primary Key

- alert_id

---

### Foreign Keys

- event_id → Parsed Events(event_id)
- rule_id → Detection Rules(rule_id)
- assigned_to → Users(user_id)

---

### Relationships

- One Parsed Event can generate multiple Alerts.
- One Detection Rule can generate multiple Alerts.
- One SOC Analyst can investigate multiple Alerts.

---

### Used By

- Detection Engine
- Alert Manager
- Incident Management
- Dashboard
- Reporting Module

---

### Design Notes

- Every alert must reference both the event that triggered it and the detection rule that identified it.
- Alerts are reviewed by analysts before becoming incidents.
- Closing an alert does not automatically close its associated incident.

## 10. Incidents Table

### Purpose

The Incidents table stores confirmed security incidents that are created from one or more related alerts. It tracks the lifecycle of an investigation from creation to closure.

---

### Attributes

**incident_id**
- Data Type: INTEGER
- Constraints: Primary Key, Auto Increment
- Description: Unique identifier for the incident.

**title**
- Data Type: TEXT
- Constraints: NOT NULL
- Description: Short descriptive title of the incident.

**description**
- Data Type: TEXT
- Constraints: NOT NULL
- Description: Detailed explanation of the incident.

**priority**
- Data Type: TEXT
- Constraints: NOT NULL
- Description: Priority assigned to the incident.
- Allowed Values:
  - Low
  - Medium
  - High
  - Critical

**status**
- Data Type: TEXT
- Constraints: NOT NULL
- Description: Current investigation status.
- Allowed Values:
  - Open
  - Under Investigation
  - Contained
  - Resolved
  - Closed

**assigned_to**
- Data Type: INTEGER
- Constraints: Foreign Key
- Description: SOC Analyst assigned to the incident.

**created_by**
- Data Type: INTEGER
- Constraints: Foreign Key, NOT NULL
- Description: User who created the incident.

**created_at**
- Data Type: DATETIME
- Constraints: NOT NULL
- Description: Date and time the incident was created.

**updated_at**
- Data Type: DATETIME
- Constraints: NOT NULL
- Description: Last modification timestamp.

**resolution_notes**
- Data Type: TEXT
- Constraints: NULL
- Description: Summary of how the incident was resolved.

---

### Primary Key

- incident_id

---

### Foreign Keys

- assigned_to → Users(user_id)
- created_by → Users(user_id)

---

### Relationships

- One Incident can contain multiple Alerts.
- One User can create multiple Incidents.
- One SOC Analyst can manage multiple Incidents.

---

### Used By

- Incident Management Module
- Dashboard
- Reporting Module
- Audit Logging Module

---

### Design Notes

- Incidents represent confirmed security events rather than individual alerts.
- Multiple related alerts may belong to the same incident.
- Every status change should be recorded in the audit log.

## 11. Incident Alerts Table

### Purpose

The Incident Alerts table establishes the relationship between security incidents and alerts. It allows a single incident to contain multiple alerts and enables an alert to be associated with an incident.

---

### Why This Table Exists

Instead of storing alert IDs directly inside the Incidents table, CyberShield uses a junction table to maintain a flexible relationship between incidents and alerts. This design improves scalability, avoids data redundancy, and follows database normalization principles.

---

### Attributes

**incident_alert_id**
- Data Type: INTEGER
- Constraints: Primary Key, Auto Increment
- Description: Unique identifier for each incident-alert relationship.

**incident_id**
- Data Type: INTEGER
- Constraints: Foreign Key, NOT NULL
- Description: References the associated incident.

**alert_id**
- Data Type: INTEGER
- Constraints: Foreign Key, NOT NULL
- Description: References the associated alert.

**linked_at**
- Data Type: DATETIME
- Constraints: NOT NULL
- Description: Date and time the alert was linked to the incident.

---

### Primary Key

- incident_alert_id

---

### Foreign Keys

- incident_id → Incidents(incident_id)
- alert_id → Alerts(alert_id)

---

### Relationships

- One Incident → Many Alert Links
- One Alert → One Incident (Version 1)

---

### Used By

- Incident Management Module
- Alert Manager
- Reporting Module

---

### Design Notes

- This table allows multiple alerts to be grouped into a single investigation.
- Additional relationship metadata can be added in future versions if required.
- Version 1 associates each alert with only one incident, but the design can be extended later.

## 12. Reports Table

### Purpose

The Reports table stores metadata about investigation reports generated by CyberShield. Reports summarize alerts, incidents, and investigation findings for documentation and future reference.

---

### Attributes

**report_id**
- Data Type: INTEGER
- Constraints: Primary Key, Auto Increment
- Description: Unique identifier for the report.

**incident_id**
- Data Type: INTEGER
- Constraints: Foreign Key, NOT NULL
- Description: References the incident associated with the report.

**generated_by**
- Data Type: INTEGER
- Constraints: Foreign Key, NOT NULL
- Description: User who generated the report.

**report_title**
- Data Type: TEXT
- Constraints: NOT NULL
- Description: Title of the report.

**report_summary**
- Data Type: TEXT
- Constraints: NOT NULL
- Description: Summary of the investigation.

**generated_at**
- Data Type: DATETIME
- Constraints: NOT NULL
- Description: Date and time the report was generated.

---

### Primary Key

- report_id

---

### Foreign Keys

- incident_id → Incidents(incident_id)
- generated_by → Users(user_id)

---

### Relationships

- One Incident → Many Reports
- One User → Many Reports

---

### Used By

- Reporting Module
- Dashboard
- Incident Management

---

### Design Notes

- Reports provide a permanent summary of completed investigations.
- Multiple reports may be generated for the same incident if required.

## 13. Audit Logs Table

### Purpose

The Audit Logs table records important system activities to provide accountability, traceability, and support security investigations.

---

### Attributes

**audit_id**
- Data Type: INTEGER
- Constraints: Primary Key, Auto Increment
- Description: Unique identifier for the audit record.

**user_id**
- Data Type: INTEGER
- Constraints: Foreign Key
- Description: User responsible for the action.

**action**
- Data Type: TEXT
- Constraints: NOT NULL
- Description: Action performed.

**target**
- Data Type: TEXT
- Constraints: NOT NULL
- Description: Resource affected by the action.

**timestamp**
- Data Type: DATETIME
- Constraints: NOT NULL
- Description: Date and time the action occurred.

**ip_address**
- Data Type: TEXT
- Constraints: NULL
- Description: IP address from which the action originated.

**details**
- Data Type: TEXT
- Constraints: NULL
- Description: Additional information about the recorded action.

---

### Primary Key

- audit_id

---

### Foreign Keys

- user_id → Users(user_id)

---

### Relationships

- One User → Many Audit Log Entries

---

### Used By

- Authentication Module
- Administration Module
- Incident Management
- Reporting Module

---

### Design Notes

- Audit records should never be modified after creation.
- Audit logs improve accountability and support forensic investigations.
- Significant security events should always be recorded.

## 14. Database Relationships

The following relationships define how different entities within CyberShield interact with one another.

---

### Roles → Users

Relationship:
- One Role can be assigned to many Users.
- Each User belongs to exactly one Role.

Purpose:
This relationship implements Role-Based Access Control (RBAC).

---

### Users → Log Files

Relationship:
- One User can upload many Log Files.
- Each Log File is uploaded by one User.

Purpose:
Tracks ownership and accountability for uploaded evidence.

---

### Log Files → Parsed Events

Relationship:
- One Log File can generate many Parsed Events.
- Every Parsed Event belongs to one Log File.

Purpose:
Maintains traceability from parsed data back to the original evidence.

---

### Parsed Events → Alerts

Relationship:
- One Parsed Event can generate multiple Alerts.
- Each Alert originates from one Parsed Event.

Purpose:
Allows different detection rules to trigger alerts from the same event.

---

### Detection Rules → Alerts

Relationship:
- One Detection Rule can generate many Alerts.
- Every Alert references the Detection Rule that generated it.

Purpose:
Provides transparency and traceability for alert generation.

---

### Users → Incidents

Relationship:
- One User can create many Incidents.
- One SOC Analyst can be assigned multiple Incidents.

Purpose:
Supports incident ownership and investigation tracking.

---

### Incidents → Incident Alerts

Relationship:
- One Incident can contain many Incident Alert records.

Purpose:
Allows a single investigation to group multiple related alerts.

---

### Alerts → Incident Alerts

Relationship:
- One Alert can be linked to an Incident.

Purpose:
Associates alerts with investigations while keeping the database normalized.

---

### Incidents → Reports

Relationship:
- One Incident can have multiple Reports.

Purpose:
Allows multiple investigation summaries to exist for the same incident.

---

### Users → Audit Logs

Relationship:
- One User can generate many Audit Log entries.

Purpose:
Maintains accountability for user actions throughout the system.

## 15. Entity Relationship Diagram (ERD)

The following diagram illustrates the relationships between the primary database entities used in CyberShield Version 1.

```text
                    +-------------+
                    |    Roles    |
                    +-------------+
                           |
                           | 1
                           |
                           | *
                    +-------------+
                    |    Users    |
                    +-------------+
                     |    |    |
          uploads    |    |    | creates
                     |    |    |
                     |    |    +----------------------+
                     |    |                           |
                     |    |                           |
                     v    |                           v
              +-------------+                 +---------------+
              |  Log Files  |                 |   Incidents   |
              +-------------+                 +---------------+
                     |                               |
                     | 1                             | 1
                     |                               |
                     | *                             | *
                     v                               v
             +---------------+              +------------------+
             | Parsed Events |              | Incident Alerts  |
             +---------------+              +------------------+
                     |                               ^
                     |                               |
                     | *                             | *
                     v                               |
                +-----------+                        |
                |  Alerts   |------------------------+
                +-----------+
                     |
                     |
                     | *
                     |
                     v
           +------------------+
           | Detection Rules  |
           +------------------+

Users -----------------------------> Audit Logs

Incidents -------------------------> Reports
```

### Relationship Summary

- One Role can have many Users.
- One User can upload many Log Files.
- One Log File can produce many Parsed Events.
- One Parsed Event can generate multiple Alerts.
- One Detection Rule can generate many Alerts.
- One Incident can contain multiple Alerts through the Incident Alerts table.
- One Incident can have multiple Reports.
- One User can generate multiple Audit Log entries.

## 16. Database Design Principles

The CyberShield database has been designed according to the following principles.

---

### 1. Normalization

The database follows normalization principles to minimize data redundancy and improve consistency.

Examples include:

- Separate Roles and Users tables.
- Separate Log Files and Parsed Events tables.
- Separate Detection Rules and Alerts tables.
- Incident Alerts junction table for linking incidents and alerts.

---

### 2. Data Integrity

Primary Keys and Foreign Keys are used throughout the database to maintain valid relationships between entities.

Examples:

- Every Alert references a Detection Rule.
- Every Parsed Event references a Log File.
- Every Report references an Incident.

---

### 3. Scalability

The database structure allows future expansion without significant redesign.

Possible future additions include:

- Threat Intelligence
- IOC Database
- Asset Management
- Case Management
- User-defined Detection Rules

---

### 4. Security

Sensitive information is never stored in plaintext.

Examples:

- Passwords are stored as secure password hashes.
- Audit logs preserve accountability.
- Uploaded evidence remains unchanged within the VFS.

---

### 5. Maintainability

Each table has a single responsibility.

This simplifies development, testing, debugging, and future maintenance.

## 17. Future Improvements

The following enhancements are planned for future versions of CyberShield.

- PostgreSQL support
- Multiple log source connectors
- Real-time log monitoring
- Threat Intelligence integration
- YARA rule support
- Sigma rule support
- Custom detection rule builder
- Email notifications
- WebSocket live dashboard
- AI-assisted alert prioritization
- Multi-factor authentication (MFA)
- REST API authentication using JWT
- Cloud deployment support
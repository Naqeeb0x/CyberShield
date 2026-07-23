# CyberShield V1 System Architecture

## 1. Introduction

The System Architecture document describes the high-level design of CyberShield Version 1.

Its purpose is to explain how different components of the system interact with each other, define the responsibilities of each major module, and provide a blueprint for implementation.

The architecture is designed to be modular, scalable, maintainable, and secure. Each component has a clearly defined responsibility, allowing future features to be added with minimal impact on the existing system.

## 2. High-Level Architecture

CyberShield follows a layered architecture consisting of four primary layers:

1. Presentation Layer (Frontend)
2. Application Layer (Backend)
3. Data Layer (Database)
4. Evidence Layer (Virtual File System)

Each layer has a dedicated responsibility and communicates only with adjacent layers to maintain modularity and separation of concerns.

## 3. System Components

CyberShield Version 1 consists of the following major components:

### 3.1 Presentation Layer (Frontend)

The Presentation Layer provides the graphical user interface through which users interact with the system.

Responsibilities:

- User Login
- Dashboard
- Log Upload
- Log Viewer
- Alert Management
- Incident Management
- Report Viewing
- User Profile

---

### 3.2 Application Layer (Backend)

The Application Layer contains the business logic of CyberShield.

It consists of the following modules:

- Authentication Module
- Log Parser Module
- Detection Engine
- Alert Manager
- Incident Manager
- Report Generator
- Virtual File System (VFS)
- Database Manager

---

### 3.3 Data Layer

The Data Layer stores structured information required by the system.

It is responsible for storing:

- Users
- Uploaded Logs
- Parsed Events
- Alerts
- Incidents
- Reports
- Audit Logs
- Detection Rules

SQLite will be used as the database management system for Version 1.

---

### 3.4 Evidence Layer (Virtual File System)

The Virtual File System (VFS) stores uploaded evidence files while preserving their original contents.

Responsibilities:

- Store original uploaded log files
- Organize evidence by incident
- Preserve file integrity
- Maintain evidence metadata

## 4. Component Interaction

The following diagram illustrates how the major components of CyberShield interact during normal operation.

```

```text
                     +----------------------+
                     |        User          |
                     +----------+-----------+
                                |
                                v
                     +----------------------+
                     |  Frontend (Web UI)   |
                     | HTML / CSS / JS      |
                     +----------+-----------+
                                |
                           HTTP Requests
                                |
                                v
                     +----------------------+
                     |    Flask Backend     |
                     +----------+-----------+
                                |
     ------------------------------------------------------------
     |         |            |           |          |             |
     v         v            v           v          v             v
+---------+ +---------+ +---------+ +---------+ +---------+ +---------+
| Auth    | | Parser  | |Detector | | Alerts  | |Incident | | Reports |
+---------+ +---------+ +---------+ +---------+ +---------+ +---------+
      |          |            |            |            |           |
      +----------+------------+------------+------------+-----------+
                                 |
                                 v
                       +-------------------+
                       | Database Manager  |
                       +---------+---------+
                                 |
                  +--------------+--------------+
                  |                             |
                  v                             v
          +---------------+             +---------------+
          | SQLite DB     |             | Virtual File  |
          |               |             | System (VFS)  |
          +---------------+             +---------------+
```

### Architecture Flow

1. Users interact with the Frontend.
2. The Frontend sends requests to the Flask Backend.
3. The Backend forwards requests to the appropriate module.
4. Modules process data and communicate with the Database Manager.
5. Structured information is stored in SQLite.
6. Original evidence files are stored in the Virtual File System (VFS).
7. Results are returned to the Frontend for display.


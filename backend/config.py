import os

class Config:
    # ==========================
    # Flask Configuration
    # ==========================
    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "CyberShield_V1_Development_Key"
    )

    # ==========================
    # Database Configuration
    # ==========================
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    DATABASE_NAME = "cybershield.db"

    SQLALCHEMY_DATABASE_URI = (
        f"sqlite:///{os.path.join(BASE_DIR, DATABASE_NAME)}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ==========================
    # File Upload Configuration
    # ==========================
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "..", "uploads")

    VFS_FOLDER = os.path.join(BASE_DIR, "..", "vfs")

    MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 50 MB

    ALLOWED_EXTENSIONS = {
        "log",
        "txt",
        "evtx",
        "json",
        "csv"
    }

    # ==========================
    # Application Mode
    # ==========================
    DEBUG = True
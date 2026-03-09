from logging.config import dictConfig
import logging
import os

# diretório de logs
log_path = "log/"

if not os.path.exists(log_path):
    os.makedirs(log_path)

dictConfig({
    "version": 1,
    "formatters": {
        "default": {
            "format": "[%(asctime)s] %(levelname)-4s %(funcName)s() L%(lineno)-4d %(message)s"
        },
        "detailed": {
            "format": "[%(asctime)s] %(levelname)-4s %(funcName)s() L%(lineno)-4d %(message)s - call_trace=%(pathname)s L%(lineno)-4d",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
        "error_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": log_path + "error.log",
            "maxBytes": 10000,
            "backupCount": 3,
            "formatter": "detailed"
        }
    },
    "root": {
        "level": "INFO",
        "handlers": ["console", "error_file"]
    }
})

logger = logging.getLogger(__name__)
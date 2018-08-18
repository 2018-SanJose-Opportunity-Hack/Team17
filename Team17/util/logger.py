# -*- coding: utf-8 -*-
# pylint: disable=unused-wildcard-import

import os
from logging import config
from logging import *

log_levels = {
    "debug" : DEBUG,
    "info" : INFO,
    "warning" : WARNING,
    "error" : ERROR,
    "critical" : CRITICAL
}

env_log_level = (os.environ.get("LOG_LEVEL") or "info").strip()
LOG_LEVEL = log_levels.get(env_log_level.lower())

def get_log_config(label):
    if label == "default":
        return {
            "version": 1,
            "formatters": {
                "default": {
                    "format": "%(asctime)s - %(threadName)s - %(name)s - %(levelname)s - %(message)s"
                }
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "default",
                    "stream": "ext://sys.stdout"
                }
            },
            "root": {
                "level": LOG_LEVEL,
                "handlers": ["console"]
            },
            "loggers": {
            }
        }
    elif label == "flask":
        return {
            "version": 1,
            "formatters": {
                "flask": {"format": "%(asctime)s - %(threadName)s - %(request_id)s - %(name)s - %(levelname)s - %(message)s"}
            },
            "filters": {
                "flask": {
                    "()": "dutalib.logfilters.FlaskLogFilter",
                    "flask": "ext://flask"
                }
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "flask",
                    "filters": ["flask"],
                    "stream": "ext://sys.stdout"
                }
            },
            "root": {
                "level": LOG_LEVEL,
                "handlers": ["console"]
            },
            "loggers": {
            }
        }
    elif label == "multiprocessing":
        return {
            "version": 1,
            "formatters": {
                "default": {"format": "%(asctime)s - %(processName)s - %(name)s - %(levelname)s - %(message)s"}
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "default",
                    "stream": "ext://sys.stdout"
                }
            },
            "root": {
                "level": LOG_LEVEL,
                "handlers": ["console"]
            },
            "loggers": {
            }
        }

env_log_config = (os.environ.get("LOG_CONFIG") or "default").strip()
LOG_CONFIG = get_log_config(env_log_config.lower()) or get_log_config("default")
config.dictConfig(LOG_CONFIG)

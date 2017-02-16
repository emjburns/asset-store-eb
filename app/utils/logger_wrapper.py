import os
import logging.config
import structlog

import yaml

# TODO: Allow for debug logging override by Env var.
def setup_logging(
    default_path='logging.yaml',
    default_level='INFO',
    env_key='LOG_CFG'
):
    """Setup logging configuration

    """
    default_level = _str_to_level(default_level)
    path = os.path.dirname(os.path.abspath(__file__)) + '/' + default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        print("doesnt exist")
        logging.basicConfig(level=default_level)

    #Configure Structlog Wrapper for client use
    structlog.configure(
        processors=[
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            # structlog.processors.JSONRenderer()
            structlog.processors.KeyValueRenderer()
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )


"""
Filter for the stderr stream.
Doesn't print records below ERROR to stderr to avoid dupes.
"""
class StdErrFilter(logging.Filter):
    def filter(self, record):
        return 0 if record.levelno < logging.ERROR else 1

"""
Filter for the stdout stream.
Doesn't print records above WARNING to stdout to avoid dupes.
"""
class StdOutFilter(logging.Filter):
    def filter(self, record):
        return 1 if record.levelno < logging.ERROR else 0

"""
    Convenience function to convert a log level string to the numeric rep.
"""
def _str_to_level(lvl):
    lvl = lvl.strip().lower()
    if lvl == "warn":
        return logging.WARNING
    elif lvl == "info":
        return logging.INFO
    elif lvl == "debug":
        return logging.DEBUG
    elif lvl == "critical":
        return logging.CRITICAL
    elif lvl == "error":
        return logging.ERROR
    else:
        return logging.INFO

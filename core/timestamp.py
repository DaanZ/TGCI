from datetime import datetime, timezone

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def get_timestamp():
    return datetime.now(timezone.utc).strftime(DATETIME_FORMAT)

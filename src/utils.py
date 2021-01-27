from datetime import datetime, date


def get_current_date() -> date:
    return date.today()


def get_current_datetime() -> datetime:
    return datetime.now()


def datetime_to_str(datetime: datetime, datetime_format: str = '%d/%m/%Y') -> str:
    return datetime.strftime(fmt=datetime_format)

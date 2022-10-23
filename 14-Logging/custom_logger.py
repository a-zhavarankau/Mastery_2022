import logging

app_logger = logging.getLogger("app_logger")
app_logger.setLevel("DEBUG")

app_handler = logging.FileHandler(filename="log.txt")
app_logger.addHandler(app_handler)

app_formatter = logging.Formatter(
    fmt="{asctime} - {module} - {levelname} - {message}", style="{"
)
app_handler.setFormatter(app_formatter)


class NotSoImportantTaksFailed(Exception):
    pass


class ImportantTaksFailed(Exception):
    pass


def _very_important_task(data: str):
    pass


def _not_so_important_task(data: str):
    pass


def _load_some_data() -> str:
    return "data"


def run_job():
    data = _load_some_data()
    app_logger.debug(f"Data size: {data.__sizeof__()}")
    app_logger.debug("Important task has been started")

    try:
        _very_important_task(data)
    except ImportantTaksFailed:
        app_logger.error("Important task failure", exc_info=True)

    app_logger.debug("Important task has been ended")
    app_logger.debug("Not important task has been started")

    try:
        _not_so_important_task(data)
    except NotSoImportantTaksFailed:
        app_logger.error("Not important task failure", exc_info=True)

    app_logger.debug("Not important task has been ended")


if __name__ == "__main__":
    run_job()

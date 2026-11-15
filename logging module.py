import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.info("This is a info.")

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.debug("The developer is debugging.")

logging.basicConfig(
    filename="app.log",
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.warning("This is a warning.")

logging.basicConfig(
    filename="app.log",
    level=logging.CRITICAL,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.critical("The code got crased.")

logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.error("This is a error.")
try:
    10 / 0
except Exception:
    logging.exception("Error occurred")






import logging

# Basic Logging Config (min level, log filename, write over mode, format(time - level - msg))
logging.basicConfig(level=logging.DEBUG, filename="log.txt", filemode="w", 
                    format="%(asctime)s - %(levelname)s - %(message)s")

# # Different Levels of Debugging
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")

# # Printing out variables in logs
# x = 2
# logging.debug(f"the value of x is {x}")

# try:
#     1/0
# except ZeroDivisionError as e:
#     logging.error("ZeroDivisionError", exc_info=True)
#     logging.exception("ZeroDivisionError")

# Custom Loggers
logger = logging.getLogger(__name__)
# logger = logging.getLogger("name")

# Setup File Handler
handler = logging.FileHandler('test.log')

# Create and Assign Formatter for Handler
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("Test Custom Logger")
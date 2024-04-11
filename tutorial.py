import logging

logging.basicConfig(level=logging.DEBUG, filename="log.txt", filemode="w")

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
# -- coding: utf-8 --

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('krpano')

def test_log():
    logger.info("start test_log")

    try:
        logger.info("do test...")
        raise TypeError
    except Exception:
        logger.error("simple caused exception")
        logger.error("traceback caused exception", exc_info=True)
    finally:
        logger.info("finish test...")

    logger.info("end test_log")


test_log()
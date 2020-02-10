import logging


def main():
    """  testing logger """
    logger.info("starting")


if __name__ == "__main__":
    """ this should be in the program's main/start/run function """
    import logging.config

    logging.config.fileConfig("logging.conf")
    logger = logging.getLogger(__name__)
    main()

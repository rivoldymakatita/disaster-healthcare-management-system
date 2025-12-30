import logging
from logging.handlers import RotatingFileHandler


class Logger:
    """
    Konfigurasi logging terpusat untuk sistem.
    """

    @staticmethod
    def get_logger(nama_logger="sistem_kesehatan"):
        logger = logging.getLogger(nama_logger)

        # Hindari duplikasi handler
        if logger.handlers:
            return logger

        logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "[%(levelname)s] %(asctime)s - %(message)s",
            datefmt="%d-%m-%Y %H:%M:%S"
        )

        file_handler = RotatingFileHandler(
            "aplikasi.log",
            maxBytes=1_000_000,
            backupCount=3,
            encoding="utf-8"
        )
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger

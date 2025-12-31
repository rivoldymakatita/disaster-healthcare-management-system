# src/utils/logger.py
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


def get_logger(
    name: str,
    log_to_file: bool = True,
    level: int = logging.INFO
) -> logging.Logger:
    """
    Mendapatkan logger yang sudah terkonfigurasi dengan format dan handler konsisten.

    Args:
        name (str): Biasanya __name__ dari modul pemanggil.
        log_to_file (bool, optional): Jika True, log juga ditulis ke logs/app.log (rotating). Default: True.
        level (int, optional): Level logging (misal: logging.INFO, logging.DEBUG). Default: logging.INFO.

    Returns:
        logging.Logger: Objek logger yang sudah terkonfigurasi.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = False

    if logger.hasHandlers():
        logger.handlers.clear()

    fmt = logging.Formatter(
        fmt="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(fmt)
    logger.addHandler(console_handler)

    # Optional file handler (rotating)
    if log_to_file:
        logs_dir = Path("logs")
        logs_dir.mkdir(parents=True, exist_ok=True)

        file_handler = RotatingFileHandler(
            logs_dir / "app.log",
            maxBytes=1_000_000,  # ~1 MB
            backupCount=3,
            encoding="utf-8",
        )
        file_handler.setLevel(level)
        file_handler.setFormatter(fmt)
        logger.addHandler(file_handler)

    return logger

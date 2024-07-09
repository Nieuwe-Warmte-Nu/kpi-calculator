#  Copyright (c) 2024 Deltares / TNO.
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""Setup logging for this python application."""

from enum import Enum
import logging
from typing import Optional
import sys

import coloredlogs


class LogLevel(Enum):
    """Loglevel enum."""

    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR

    @staticmethod
    def parse(value: str) -> "LogLevel":
        """
        Parses a given string for LogLevel's.

        Parameters
        ----------
        value : str
                user provided string containing the requested log level

        Returns
        -------
        LogLevel
            Loglevel for this logger
        """
        lowered = value.lower()

        if lowered == "debug":
            result = LogLevel.DEBUG
        elif lowered == "info":
            result = LogLevel.INFO
        elif lowered in ["warning", "warn"]:
            result = LogLevel.WARNING
        elif lowered in ["err", "error"]:
            result = LogLevel.ERROR
        else:
            raise ValueError(f"Value {value} is not a valid log level.")

        return result


LOG_LEVEL: Optional[LogLevel] = None


def setup_logging(log_level: LogLevel, colors: bool = True) -> None:
    """
    Initializes logging.

    Parameters
    ----------
    log_level : LogLevel
        The LogLevel for this logger.
    """
    global LOG_LEVEL
    root_logger = logging.getLogger()
    root_logger.info("Will use log level:", str(log_level))
    root_logger.setLevel(log_level.value)
    LOG_LEVEL = log_level
    if colors:
        coloredlogs.install(log_level.value, logger=root_logger)
    else:
        log_handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            fmt="%(asctime)s [%(threadName)s][%(filename)s:%(lineno)d][%(levelname)s]: %(message)s"
        )
        log_handler.setFormatter(formatter)
        root_logger.addHandler(log_handler)
    pass

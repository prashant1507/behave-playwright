import configparser

from pycommons.lang.stringutils import StringUtils
from utils.docker_compose_actions import start_docker_compose, stop_docker_compose
from utils.helper_utils import prepare_dirs, execute_command_using_popen
from utils.preapre_details_file import prepare_details_file
from utils.reporting.generate_report import generate_allure_report
from helpers.constants.framework_constants import FrameworkConstants as Fc

import logging

def logs():
    logger = logging.getLogger()
    if not logger.hasHandlers():
        logger.handlers.clear()
        logging.basicConfig(
            level=logging.INFO,
            format="%(message)s"
        )
    return logger

def start_tests(log) -> None:
    prepare_details_file()
    details_ini = configparser.ConfigParser()
    details_ini.read(Fc.details_file)
    tags = details_ini.get("general", "tags")
    prepare_dirs()
    # start_docker_compose(log)
    command = (
        f"behavex {Fc.features} -c {Fc.conf_behavex} "
        f"--parallel-processes 2 --parallel-delay 1000 "
        f"--parallel-scheme scenario --show-progress-bar"
    )
    process = execute_command_using_popen(command)

    try:
        while True:
            output = process.stdout.readline()
            if output == StringUtils.EMPTY and process.poll() is not None:
                break
            if output:
                log.info(output.strip())
    except KeyboardInterrupt:
        log.error("Process terminated by user.")
        process.terminate()
        raise
    finally:
        generate_allure_report(log)
        # stop_docker_compose(log)

def main():
    log = logs()
    try:
        start_tests(log)
    except Exception as e:
        log.error(f"An unexpected error occurred: {e}")
        raise

if __name__ == "__main__":
    main()

import os

from pycommons.lang.stringutils import StringUtils
from utils.docker_compose_actions import start_docker_compose, stop_docker_compose
from utils.helper_utils import prepare_dirs, execute_command_using_popen
from utils.prepare_details_file import prepare_details_file
from utils.reporting.generate_report import generate_allure_report
from helpers.constants.framework_constants import FrameworkConstants as Fc
from utils.helper_utils import read_file

import logging

def logs():
    logger = logging.getLogger()
    logger.handlers.clear()
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s"
    )
    return logger



def main():
    process = None
    log = logs()
    prepare_details_file()
    # Read and print the output line by line
    try:
        details = read_file(Fc.details_file)
        tags = details["tags"]
        prepare_dirs()
        # start_docker_compose(log)
        process = execute_command_using_popen(f"behavex {Fc.features} -c {Fc.conf_behavex} --parallel-processes 2 --parallel-delay 1000 --parallel-scheme scenario --show-progress-bar -t={tags}")
        while True:
            output = process.stdout.readline()
            if output == StringUtils.EMPTY and process.poll() is not None:
                break
            if output:
                log.info(output.strip())
    except KeyboardInterrupt:
        log.error("Process terminated by user.")
        process.terminate()
    finally:
        generate_allure_report(log)
        # stop_docker_compose(log)

if __name__ == "__main__":
    main()
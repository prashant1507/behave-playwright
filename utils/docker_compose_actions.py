import configparser
import subprocess
import sys
import time

from helpers.constants.framework_constants import FrameworkConstants as Fc
from utils.helper_utils import execute_command_using_run

details = configparser.ConfigParser()
details.read(Fc.details_file)

def stop_docker_compose(logger):
    if details.getboolean("general", "start_docker_compose"):
        logger.info("Stopping Docker Compose if Running")
        execute_command_using_run(f"sshpass -p {details.get("general", "password_for_sshpass")} sudo docker-compose -f {Fc.docker_compose_file} down")
        time.sleep(5)


def start_docker_compose(logger):
    if details.getboolean("general", "start_docker_compose"):
        try:
            stop_docker_compose(logger)
            logger.info("Starting Docker Compose")
            execute_command_using_run(f"sshpass -p {details.get("general", "password_for_sshpass")} sudo docker-compose -f {Fc.docker_compose_file} up --remove-orphans -d")
            logger.info("Waiting for all containers to be healthy")
            while not all_services_healthy():
                logger.info("Containers are still starting up. Waiting for 5 seconds")
                time.sleep(2)
            time.sleep(5)
            logger.info("All containers are up and running!")
        except subprocess.CalledProcessError as e:
            logger.info(f"An error occurred while starting Docker Compose: {e}")
            sys.exit(1)


def all_services_healthy():
    result = execute_command_using_run(f"sshpass -p {details.get("general", "password_for_sshpass")} sudo docker-compose -f {Fc.docker_compose_file} ps")
    output = result.stdout
    services_status = [line for line in output.splitlines() if "Up" in line or "healthy" in line]
    services_total = [line for line in output.splitlines() if "Exit" not in line and "Name" not in line and "--" not in line]
    return len(services_status) == len(services_total) and len(services_total) > 0

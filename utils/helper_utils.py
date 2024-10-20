import json
import subprocess
import os
import shutil

from helpers.constants.framework_constants import FrameworkConstants as Fc


def prepare_dirs():
    dir_structure = [
        Fc.reports_parent_dir, Fc.allure_json_dir, 
        Fc.allure_html_dir, Fc.html_dir, 
        Fc.logs_dir, Fc.json_dir, 
        Fc.pretty_dir, Fc.rerun_dir, Fc.screenshots_dir
    ]

    details = read_file(Fc.details_file)
    if details["delete_old_reports"]:
        for subdir in dir_structure:
            delete_dir(subdir)
            create_dir(subdir)


def execute_command_using_run(command):
    return subprocess.run(
        command.split(), capture_output=True, text=True, check=True
    )

def execute_command_using_popen(command):
    return subprocess.Popen(
        command.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1
    )


def create_dir(folder):
    dir_to_create = os.path.abspath(folder)
    os.makedirs(dir_to_create, exist_ok=True)
    return dir_to_create

def delete_dir(folder):
    dir_to_create = os.path.abspath(folder)
    shutil.rmtree(dir_to_create, ignore_errors=True)
    return dir_to_create


def read_file(path):
    with open(path, "r") as f:
        return json.load(f)

import datetime

from utils.helper_utils import execute_command_using_run
from helpers.constants.framework_constants import FrameworkConstants as Fc
from utils.send_report_on_email import send_report, details


def generate_allure_report(logger):
    logger.info("Generating Report")
    set_environment_variables()
    current_time = datetime.datetime.now()
    file_name = current_time.strftime("%d_%m_%y-%H_%M_%S_%f")[:-3]
    report = f"{Fc.allure_html_dir}/{file_name}"
    execute_command_using_run(f"allure generate {Fc.allure_json_dir} --report-dir {report} --clean --report-name Test_Report --single-file")
    logger.info(f"HTML output report is located at: {report}/index.html")
    send_report(logger, report)
    return f"{report}/index.html"

def set_environment_variables():
    environment_data = {
        "URL": details["url"],
        "Browser": details["browser"]
    }

    with open(f"{Fc.allure_json_dir}/environment.properties", "w") as file:
        for key, value in environment_data.items():
            file.write(f"{key}={value}\n")
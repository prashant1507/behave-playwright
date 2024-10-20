import configparser
import datetime

import allure
from behave.runner import Context
from behavex_images import image_attachments
from behavex_images.image_attachments import AttachmentsCondition
from playwright.sync_api import Page

from helpers.constants.framework_constants import FrameworkConstants as Fc
from utils.elk import add_in_elk
from utils.helper_utils import read_file
from utils.reporting.logger import get_logs
from utils.reporting.screenshots import attach_screenshot_in_report
from utils.browser_utils import prepare_browser, test_tracing


def before_all(context: Context):
    current_time = datetime.datetime.now()
    file_name = current_time.strftime("%d_%m_%y-%H_%M_%S_%f")[:-3]
    global logger
    logger = get_logs(f"{Fc.logs_dir}/{file_name}.txt")
    # start_docker_compose(logger)
    image_attachments.set_attachments_condition(context, AttachmentsCondition.ALWAYS)
    context.details = configparser.ConfigParser()
    context.details.read(Fc.details_file)


def before_feature(context: Context, feature):
    logger.info(f"Feature file: {feature.filename}")
    logger.info(f"Number of Scenarios: {len(feature.scenarios)}")
    formatted_tags = " ".join([f"@{tag}" for tag in feature.tags])
    if formatted_tags:
        logger.info(f"{formatted_tags}")
    logger.info(f"Feature: {feature.name}")

def before_scenario(context, scenario):
    formatted_tags = " ".join([f"@{tag}" for tag in scenario.tags])
    if formatted_tags:
        logger.info(f"{formatted_tags}")
    logger.info(f"Scenario: {scenario.name}")

    if scenario.feature.background:
        background = scenario.feature.background
        for step in background.steps:
            logger.info(f"{step.keyword} {step.name}")

    for step in scenario.steps:
        logger.info(f"{step.keyword} {step.name}")
    prepare_browser(context)


def after_step(context: Context, step):
    current_time = datetime.datetime.now()
    file_name = current_time.strftime("%d_%m_%y-%H_%M_%S_%f")[:-3]
    page: Page = context.page
    page.wait_for_load_state()
    page.screenshot(path=f"{Fc.screenshots_dir}/{file_name}.png")
    attach_screenshot_in_report(f"{Fc.screenshots_dir}/{file_name}.png")
    image_attachments.attach_image_file(context, f"{Fc.screenshots_dir}/{file_name}.png")

def after_scenario(context, scenario):
    try:
        logger.info(f"Scenario status: {scenario.status}")
        test_id = " ".join([tag for tag in scenario.tags])
        summary = str(scenario.name).split("--")[0].strip()
        status = str(scenario.status).split(".")[1].capitalize()
        author = "user_1"
        add_in_elk(context, logger, test_id, summary, status, author)
        test_tracing(context, False)
        allure.dynamic.title("Scenario status")
        allure.dynamic.link("https://www.link.com", test_id)
        allure.dynamic.issue(f"https://www.issue.com/{test_id}", test_id)
        allure.dynamic.testcase(f"https://www.testcase.com/{test_id}", test_id)

    finally:
        context.page.close()
        context.browser.close()
        context.playwright.stop()

def after_feature(context, feature):
    logger.info(f"Feature Status: {feature.status}")

# def after_all(context):
#     try:
#         generate_allure_report(logger)
#     finally:
#         stop_docker_compose(logger)

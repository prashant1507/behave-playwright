import datetime

from playwright.sync_api import sync_playwright
from utils.helper_utils import read_file
from helpers.constants.framework_constants import FrameworkConstants as Fc

details = read_file(Fc.details_file)

def prepare_browser(context):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=details["headless"], args=["--start-maximized"])
    context.browser_context = browser.new_context()
    test_tracing(context, True)
    context.page = context.browser_context.new_page()
    context.page.set_viewport_size({"width": 1920, "height": 1080})
    context.browser = browser
    context.playwright = playwright

def test_tracing(context, flag):
    if details["allow_tracing"]:
        if flag:
            context.browser_context.tracing.start(screenshots=True, snapshots=True)
        else:
            current_time = datetime.datetime.now()
            file_name = current_time.strftime("%d_%m_%y-%H_%M_%S_%f")[:-3]
            context.browser_context.tracing.stop(path = f"{Fc.test_trace_dir}/{file_name}.zip")

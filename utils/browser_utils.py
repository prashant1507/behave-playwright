import datetime

from playwright.sync_api import sync_playwright
from helpers.constants.framework_constants import FrameworkConstants as Fc

def prepare_browser(context):
    try:
        playwright = sync_playwright().start()
        browser = playwright.chromium.launch(
            headless=context.details.getboolean("general", "headless"),
            args=["--start-maximized"]
        )
        context.browser_context = browser.new_context()
        test_tracing(context, True)
        context.page = context.browser_context.new_page()
        context.page.set_viewport_size({"width": 1920, "height": 1080})
        context.browser = browser
        context.playwright = playwright

    except Exception as e:
        context.playwright.stop()
        raise RuntimeError(f"Failed to prepare browser: {e}")


def test_tracing(context, flag) -> None:
    if context.details.getboolean("general", "allow_tracing"):
        if flag:
            context.browser_context.tracing.start(screenshots=True, snapshots=True)
        else:
            current_time = datetime.datetime.now()
            file_name = current_time.strftime("%d_%m_%y-%H_%M_%S_%f")[:-3]
            trace_zip_path = f"{Fc.test_trace_dir}/{file_name}.zip"
            
            try:
                context.browser_context.tracing.stop(path=trace_zip_path)
            except Exception as e:
                raise RuntimeError(f"Failed to stop tracing and save the file: {e}")

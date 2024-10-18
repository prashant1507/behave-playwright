import logging
import allure

class AllureLoggingHandler(logging.Handler):

    def emit(self, record):
        log(record.levelname, record.getMessage())

def log(level_name, message):
    with allure.step(f"Log ({level_name}) {message}"):
        # if level_name.lower() == "error":
        #     self.attach_screenshot_in_report()
        if level_name.lower() == "info":
            assert True
        else:
            assert False


def get_logs(log_file):
    logger = logging.getLogger()
    if logger.hasHandlers():
        logger.handlers.clear()
    ## To print in console
    # logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)s)", datefmt='%d/%m/%Y %I:%M:%S %p')

    ## To print log in allure report as well
    # allure_handler = AllureLoggingHandler()
    filehandler = logging.FileHandler(log_file, mode="w")
    formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(module)s: %(funcName)s: %(message)s',
                                  datefmt='%d/%m/%Y %I:%M:%S %p')
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.setLevel(logging.INFO)
    # logger.addHandler(allure_handler)
    return logger

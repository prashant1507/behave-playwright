import allure


def attach_screenshot_in_report(path):
    allure.attach.file(
        source=path,
        attachment_type=allure.attachment_type.PNG,
        extension=".png",
        name="Screenshot"
    )

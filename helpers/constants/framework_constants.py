
import os.path


class FrameworkConstants:

    reports_parent_dir = os.path.abspath("reports")
    resources = os.path.abspath("resources")
    tests_dir = os.path.abspath("tests")

    
    allure_json_dir = os.path.join(reports_parent_dir, "allure_json")
    allure_html_dir = os.path.join(reports_parent_dir, "allure_html")
    html_dir = os.path.join(reports_parent_dir, "html")
    logs_dir = os.path.join(reports_parent_dir, "logs")
    json_dir = os.path.join(reports_parent_dir, "json")
    pretty_dir = os.path.join(reports_parent_dir, "pretty")
    rerun_dir = os.path.join(reports_parent_dir, "rerun")
    screenshots_dir = os.path.join(reports_parent_dir, "screenshots")
    test_trace_dir = os.path.join(reports_parent_dir, "test_traces")


    docker_compose_file = os.path.join(resources, "docker-compose.yml")
    details_file = os.path.join(resources, "details.ini")
    behave_ini = os.path.abspath("behave.ini")
    conf_behavex = os.path.abspath("conf_behavex.cfg")

    features = os.path.join(tests_dir, "features")

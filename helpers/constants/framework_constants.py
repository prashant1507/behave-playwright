
import os.path


class FrameworkConstants:

    reports_parent_dir = os.path.abspath("reports")
    allure_json_dir = os.path.abspath(f"{reports_parent_dir}/allure_json")
    allure_html_dir = os.path.abspath(f"{reports_parent_dir}/allure_html")
    html_dir = os.path.abspath(f"{reports_parent_dir}/html")
    logs_dir = os.path.abspath(f"{reports_parent_dir}/logs")
    json_dir = os.path.abspath(f"{reports_parent_dir}/json")
    pretty_dir = os.path.abspath(f"{reports_parent_dir}/pretty")
    rerun_dir = os.path.abspath(f"{reports_parent_dir}/rerun")
    screenshots_dir = os.path.abspath(f"{reports_parent_dir}/screenshots")
    test_trace_dir = os.path.abspath(f"{reports_parent_dir}/test_traces")

    resources = os.path.abspath("resources")

    docker_compose_file = os.path.abspath("resources/docker-compose.yml")
    details_file = os.path.abspath(f"{resources}/details.json")
    behave_ini = os.path.abspath("behave.ini")
    conf_behavex = os.path.abspath("conf_behavex.cfg")

    features = os.path.abspath("tests/features")

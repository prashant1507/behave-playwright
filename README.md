
**Python Test Framework with Behave, Playwright, and BehaveX**

A robust test automation framework built with Python, utilizing Behave for BDD, Playwright for browser automation, and BehaveX for parallel execution. The framework supports Allure and BehaveX HTML for reporting, and integrates seamlessly with Elasticsearch and Kibana for advanced test result analysis and visualization.

# Setup
1. Execute `pip3 install -r requirements.tx`
2. Set up allure-report
   ```
      # Linux
    Download from https://allurereport.org/docs/install-for-linux/
    Execute: sudo dpkg -i allure_*_all.deb
    Execute: allure --version
   ```
   Ref Link: https://allurereport.org/docs/install/
3. Execute `playwright install` (To install PLaywright browsers)
4. Setup `resources/details.json` as
   ```
      delete_old_reports: true [false]
      start_docker_compose: false [/true] (if false then framwork assumes selenium is running already. Required only if PLaywright is ruuning on Selenium)
      password_for_sshpass: "passowrd" (this has no affect but can be useful if anyone want to start docker-compose where sudo is required)
      headless: true [/false]
      allow_tracing: true [/false]
      tags: "" (Provide specifi tag like tags: "@QA-1")
      add_in_elk: false [/true] (if true then framework assuemes elastic search is running)
                  - if add_in_elk is true the set elk_url: "https://elk.com"
      send_report_on_email: true [/false]
                  - if send_report_on_email is true the provide below:
                        - token: "" (Check Notes -> 'Create Gmail Key Password' to generate Token)
                        - sender_email: ""
                        - receiver_email: ""
      selenium_host_ip: "" (Selenium host - required only if PLaywright is ruuning on Selenium)
      browser: "Chrome" [/"Firefox"]
      url: "https://www.saucedemo.com"      
   ```

# Start Tests
1. Execute `python3 runner.py`


# Helpers
1. Check all behave options `behave -h`
2. Check all allure options `allure -h`
3. Check all playwright options `playwright -h`
4. Execute `allure serve FOLDER_PATH` to start and create allure-report

# Notes:
1. Test is using "https://www.saucedemo.com"
2. Test will be executed in parallel scenario by scenario
3. Create Gmail Key Password
   ```
   1. Goto: https://myaccount.google.com/apppasswords
   2. Enter App Name
   3. Copy generated password
   4. Provide in resources/details.json
   ```
4. The test runs on local browsers. But docker support is also available (Refer `start_docker_compose()` in [runner.py](runner.py))
5. Reports will be available as below:
     - Allure: `reports/allure_report`
     - Behavex HTML: `report/html`
6. Refer [behave.ini](behave.ini) for all settings

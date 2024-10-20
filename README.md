
# Setup
1. Execute `pip3 install -r requirements.tx`
2. Set up allure-report
   ``` 
    Download from https://allurereport.org/docs/install-for-linux/
    Execute: sudo dpkg -i allure_*_all.deb
    Execute: allure --version
   ```
3. Execute `playwright install`
4. Setup `resources/details.json` as
   ```
      # TO DO
   ```

# Start Tests
1. Execute `python3 runner.py`


# Helpers
1. Check all behave options `behave -h`
2. Check all allure options `allure -h`
3. Check all playwright options `playwright -h`
4. Execute `allure serve FOLDER_PATH` to start and create allure-report

# Notes:
1. Test will be executed in parallel scenario by scenario
2. Create Gmail Key Password
   ```
   1. Goto: https://myaccount.google.com/apppasswords
   2. Enter App Name
   3. Copy generated password
   4. Provide in resources/details.json
   ```

cd C:\elecproduvt
behave -f allure_behave.formatter:AllureFormatter -o ./allure_reports ./features
behave --junit --junit-directory jreports features/ElecrProduct.feature
behave -f json.pretty -o json_reports features/ElecrProduct.feature
allure serve allure_reports

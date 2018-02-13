A. Pre reqs:
1. Install chrome, firefox and safari
2. Enable "Allow Remote Automation" for safari

B. Before running test go to project folder and run below commands to start selenium server.
1. java -jar ../Selenium/selenium-server-standalone-3.6.0.jar -host http://localhost -port 4444 -role hub

2. java -Dwebdriver.gecko.driver="../Selenium/geckodriver" -Dwebdriver.chrome.driver="../Selenium/chromedriver" -jar ../Selenium/selenium-server-standalone-3.6.0.jar -role webdriver -hub http://localhost:4444/grid/register -debug -port 5556 -browser browserName=firefox,maxInstances=5,platform=MAC -browser browserName=chrome,maxInstances=5,platform=MAC -browser browserName=safari,maxInstances=5,platform=MAC

If tests are needed to run on different platform, change "platform" in above command

C. Run tests
1. To execute tests run parallel.sh bash file. (Command to run: bash parallel.sh)

2. The format of command to execute test on one browser instance is as below:
python <filename> <browser> <search_term>
-> browser is mandatory input
-> search term is not mandatory. If search term is not provided "Instawork" is taken as default search term

Testing:
1. To fail the test case to check if instawork.com is coming as first result or not provide sumairmeghani as search result. e.g. python FirstTest.py chrome sumairmeghani

2. To check if test case to check across the pages work try SaureenShah
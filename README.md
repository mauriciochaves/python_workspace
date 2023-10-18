
<p align="center">
    <h1 align="center">Installation and Usage</h1>
</p>
<p align="center">


## Installation

* [Appium-Python-Client](https://pypi.org/project/Appium-Python-Client/)
* [Selenium-WebDriver](https://www.seleniumhq.org/)
* [Webdriver Manager](https://pypi.org/project/webdriver-manager/)
* [Requests](https://requests-docs-pt.readthedocs.io/pt_BR/latest/user/quickstart.html)
* [Behave](https://behave.readthedocs.io/en/latest/)
* [PyHamcrest](https://github.com/hamcrest/PyHamcrest)
* Generate Report [allure-behave](https://pypi.org/project/allure-behave/)
* [scoop](https://github.com/lukesampson/scoop)


```
pip install -r requirements.txt
```


## Comand lines


Windows (PowerShell)
```powershell
1. Set-ExecutionPolicy RemoteSigned -scope CurrentUser
2. Type in "Y" and click on "ENTER"
3. iex (new-object net.webclient).downloadstring('https://get.scoop.sh')
4. scoop install allure
```


Linux (Ubuntu)
```Terminal
sudo apt-get install allure
```


## Usage
Run Tests
```behave
behave -f allure_behave.formatter:AllureFormatter -o allure-results ./features
```


Server
```allure
allure serve allure-results
```


HTML file

Open html file in <b>allure-html\index.html</b> with Firefox or Edge

Open with Chrome follow the orientation [How to launch html using Chrome at “--allow-file-access-from-files” mode?](https://stackoverflow.com/questions/18586921/how-to-launch-html-using-chrome-at-allow-file-access-from-files-mode)

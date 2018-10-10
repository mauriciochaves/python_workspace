# Selenium Page Object Pattern example  - YourLogo website.

## Description:
Page Object Pattern, implementation base on the __http://automationpractice.com/index.php__ webpage.

### Tests were implemented and run on:

* System: Linux Ubuntu 16.04 LTS
* Browsers: Firefox Quantum 58.0.2, Chrome 64.0.3282.167 (both 64-bit)
* Selenium WebDriver: 3.9.0
* Python: 3.6

### To Run Tests - Linux Ubuntu way:

1.Clone/Download project: https://github.com/MaBlaGit/YourLogoAutomated.git

2.Install __virtualenvwrapper__
```
 $ pip install virtualenvwrapper
```
3.Run virtualenvwrapper and create hermetic virtualenv for the project

```
$ source /usr/local/bin/virtualenvwrapper.sh
$ mkvirtualenv --python=/usr/bin/python3.6 name-of-virtualenv
$ workon name-of-virtualenv
```

4.Go to  __YourLogoAutomated__ folder and add project to PYTHONPATH of current active virtualenv

```
$ add2virtualenv .
```
5.Install requred modules

```
$ make deps
```

6.Download drivers, unpack, make executable and copy to /usr/local/bin:

__geckodriver__: https://github.com/mozilla/geckodriver/releases

__chromedriver__: https://sites.google.com/a/chromium.org/chromedriver/

(example below shows how add to path __geckodriver__)

```
tar -xvzf geckodriver-v0.11.1-linux64.tar.gz
rm geckodriver-v0.11.1-linux64.tar.gz
chmod +x geckodriver
cp geckodriver /usr/local/bin/
```

### Running tests

In order to run tests go to __tests__ package, open __Terminal__ and enter command
```
$ python3.6 search_product.py
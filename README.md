
<p align="center">
    <h1 align="center">Installation and Usage</h1>
</p>
<p align="center">


## Installation

* Generate Report [allure-behave](https://pypi.org/project/allure-behave/)
* [scoop](https://github.com/lukesampson/scoop)


```
pip install -r requirements.txt
```

## Comand lines

Windows (PowerShell)
```powershell
iex (new-object net.webclient).downloadstring('https://get.scoop.sh')
scoop install allure
```

Linux (Ubuntu)
```Terminal
sudo apt-get install allure
```


## Usage
Run Tests
```behave
behave -f allure_behave.formatter:AllureFormatter -o allure_results ./features
allure serve allure_results
```

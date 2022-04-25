<h1 align="center">
  Module Counterparty UI Tests PY manual
</h1>
<p align="center">
  <img src="https://hackr.io/tutorials/learn-docker/logo/logo-docker?ver=1603206033"/>
  <img src="https://opencollective-production.s3-us-west-1.amazonaws.com/dfc89fd0-ff85-11e7-a77e-87408754420f.png"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Pytest_logo.svg/200px-Pytest_logo.svg.png"/>
  <img src="https://seleniumbase.io/img/green_logo.png"/>
</p>

___
<h2 align="center">
  Docker
</h2>


> env.py for docker
>
> ```
> cp env.development.py env.py
> ```

> Build and run images pytest and selenium-chrome in docker
>
> ```
> docker run --rm pk-ui-test-py /usr/local/bin/pytest [Path from test or marker]
> ```

> Build image pytest in docker
>
> ```
> docker build -t=pk-ui-test-py -f Dockerfile . 
> ```

> Pull image selenium/chrome and selenoid/firefox
>
> ``` 
> docker pull selenoid/chrome:latest
> docker pull selenoid/firefox:88.0
> ```

> **Example:**
>
> Run pytest and send result test in Allure
>
> ```
> docker run --rm [pk-ui-test-py image] /usr/local/bin/pytest -m=[Marker] --alluredir=allure_reports & python SendAllureReport.py
> ```

___

<h2 align="center">
  Allure-Report
</h2>


> **Example:**
>
> Send result tests to Allure-Report
>
> ```
> python SendAllureReport.py
> ```

> **Clear logs after tests**
>
> Method for delete logs after tests
>
> ```
> python ClearLogs.py
> ```

___
<h2 align="center">
  PyTest
</h2>

> **Parameters PyTest:**
>
> * `-m=[Marker name]` - Select marker test.
> * `-n=[Number of threads] `- Multithreading.
> * `--alluredir=[Name dir]`- Create allure report. Default name dir 'allure_reports'.
> * `--reruns=[Numbers restart test]`- Restart fail tests

> **Default parameter PyTest** \
> Parameters are written in the "pytest.ini" file "addopts" item
>  * `--capture=no` - Do not output full trace logs
>  * `-p no:cacheprovider` - Don't save cache
>  * `--pdbcls=IPython.terminal.debugger:TerminalPdb` - Output debug logs
>  * `--alluredir=allure_reports` - Create an allure-reports report in the allure_reports folder
>  * `--reruns=1` - Restart tests 1 time

> ### List markers:
>
> * `smoke` - Smoke tests
> * `api_check` - Api check tests
> * `functional` - Functional tests

> ### List tests:
>
> > **Smoke:**
> > * `testMainPage` - Main page test

> **Example:**
>
> Run all tests in 5 flow and restart fail test 1 time
>
> ```
> pytest -n=5 -m=smoke --reruns=1
> ```
>
> Run all tests in 5 flow with the creation a report in folder allure_reports
>
> ```
> pytest -n=5 --alluredir=allure_reports
> ```
>
> Run group tests in 5 flow with the creation a report in folder allure_reports
>
> ```
> pytest -n=5 -m=smoke --alluredir=allure_reports
> ```

___
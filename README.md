# How to run Selenium automation tests on Hypertest (using PyUnit framework)

Download the concierge binary corresponding to the host operating system. It is recommended to download the binary in the project's Parent Directory.

* Mac: https://downloads.lambdatest.com/concierge/darwin/concierge
* Linux: https://downloads.lambdatest.com/concierge/linux/concierge
* Windows: https://downloads.lambdatest.com/concierge/windows/concierge.exe

[Note - The current project has concierge for Windows. Irrespective of the host OS, the concierge will auto-update whenever there is a new version on the server]

## Running tests in PyUnit using the Matrix strategy

Matrix YAML file (pyunit_hypertest_matrix_sample.yaml) in the repo contains the following configuration:

```yaml
globalTimeout: 90
testSuiteTimeout: 90
testSuiteStep: 90
```

Global timeout, testSuite timeout, and testSuite timeout are set to 90 minutes.
 
The target platform is set to Windows. Please set the *[os]* key to *[win]* in case the tests have to be executed on the macOS platform. 

```yaml
os: [win]
```

The environment variables LT_USERNAME and LT_ACCESS_KEY are declared in the *env* array. It contains two key:value pairs where we have set the required environment variables.

```yaml
env:
  LT_USERNAME: LAMBDATEST_USERNAME
  LT_ACCESS_KEY: LAMBDATEST_ACCESS_KEY
```

Python files in the 'tests' folder contain the 'tests' that will be run in parallel on the Hypertest grid

```bash
files: ["tests/lt_sample_todo.py", "tests/lt_selenium_playground.py"]
```

Content under the *pre* directive is the pre-condition that will be run before the tests are executed on Hypertest grid

```bash
pip3 install -r requirements.txt
```

All the required packages are also installed in this step using *pip3 install*. Please modify *requirements.txt* as per the project requirements.

The *testSuites* object contains a list of commands (that can be presented in an array). In the current YAML file, commands to be run for executing the tests are put in an array (with a '-' preceding each item). In the current YAML file, Python command is used to run tests in *.py* files. The files are mentioned as array to *files* key are executed on Hypertest grid.

```yaml
testSuites:
  - python3 -s  $files
```

The [user_name and access_key of LambdaTest](https://accounts.lambdatest.com/detail/profile) is appended to the *concierge* command using the *--user* and *--key* command-line options. The CLI option *--config* is used for providing the custom Hypertest YAML file (e.g. pyunit_hypertest_matrix_sample.yaml). Run the following command on the terminal to trigger the tests in Python files on the Hypertest grid.

```bash
./concierge --user "${ YOUR_LAMBDATEST_USERNAME()}" --key "${ YOUR_LAMBDATEST_ACCESS_KEY()}" --config pyunit_hypertest_matrix_sample.yaml --verbose
```

Visit [Hypertest Automation Dashboard](https://automation.lambdatest.com/hypertest) to check the status of execution

## Running tests using PyUnit using the Auto-Split strategy

Auto-Split YAML file (pyunit_hypertest_autosplit_sample.yaml) in the repo contains the following configuration:

```yaml
globalTimeout: 90
testSuiteTimeout: 90
testSuiteStep: 90
```

Global timeout, testSuite timeout, and testSuite timeout are set to 90 minutes.
 
The *runson* key determines the platform (or operating system) on which the tests would be executed. Here we have set the target OS as Windows.

```yaml
runson: win
```

Auto-split is set to true in the YAML file.

```yaml
autosplit: true
```

Retry on failure is set to False and the concurrency (i.e. number of parallel sessions) is set to 2. If the test execution fails (at the first shot), further attempts for execution would not be made. 

```yaml
retryOnFailure: false
concurrency: 2
```

Content under the *pre* directive is the pre-condition that will be run before the tests are executed on Hypertest grid.

```bash
pip3 install -r requirements.txt
```

All the required packages are also installed in this step using *pip3 install*. Please modify *requirements.txt* as per the project requirements.

The *testDiscoverer* contains the command that gives details of the tests that are a part of the project. Here, we are fetching the list of Python files that would be further executed using the *value* passed in the *testRunnerCommand*

```bash
grep -nri 'class' tests -ir --include=\*.py | sed 's/:.*//'
```

Running the above command on the terminal will give a list of Python files that are located in the Project folder:

* tests/lt_selenium_playground.py
* tests/lt_sample_todo.py

The *testRunnerCommand* contains the command that is used for triggering the test. The output fetched from the *testDiscoverer* command acts as an input to the *testRunner* command.

```yaml
testRunnerCommand: python3 $test
```

Run the following command on the terminal to trigger the tests in Python files on the Hypertest grid.

```bash
./concierge --user "${ YOUR_LAMBDATEST_USERNAME()}" --key "${ YOUR_LAMBDATEST_ACCESS_KEY()}" --config pyunit_hypertest_autosplit_sample.yaml --verbose
```

Visit [Hypertest Automation Dashboard](https://automation.lambdatest.com/hypertest) to check the status of execution

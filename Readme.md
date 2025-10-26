Integration Testing and Load Testing Project
This project demonstrates **integration testing** using Python along with **load testing** of a web application using **Apache JMeter**. It includes example test plans, scripts, and instructions to run performance tests and generate reports.

## Project Structure
integration_test/
├── app.py # simple website code
├── MyLoadTest.jmx # JMeter test plan
├── results.jtl # Raw JMeter results
├── html_report/ # Generated HTML report from JMeter
├── README.md # Project documentation
└── python_scripts/ # Python integration test scripts

## Prerequisites
- **Java 8+** (required for JMeter)  
- **Apache JMeter 5.6.3+**  
- **Python 3.8+** (for integration scripts)

## Installation

**Download and install JMeter:**

## 1. NON-GUI Mode 

```bash
wget https://dlcdn.apache.org/jmeter/binaries/apache-jmeter-5.6.3.tgz
tar -xvzf apache-jmeter-5.6.3.tgz
sudo mv apache-jmeter-5.6.3 /opt/jmeter
echo 'export PATH=/opt/jmeter/bin:$PATH' >> ~/.bashrc
source ~/.bashrc

```
## 2 . GUI Mode
- **Download from: https://jmeter.apache.org/download_jmeter.cgi**

- **Extract and run jmeter.bat (Windows) or jmeter.sh (Linux/Mac).**

## Running JMeter Load Test
**1.Non-GUI Mode**
**jmeter -n -t MyLoadTest.jmx -l results.jtl -e -o ./html_report**

**GUI Mode**
1. Double click on /bin/jmeter.bat # for windows
2. cd apache-jmeter-5.6.3/bin
sh jmeter.sh # On macOS/Linux

Create a Test Plan
add Thread Group, configure and monitor
├── HTTP request/HTTP Header Manager
├── View Results Tree
├── Graph results
├── Summary Report
└── MyLoadTest.jmx / save the results

If you want an HTML performance report later:
run:
- jmeter -n -t MyLoadTest.jmx -l results.jtl -e -o ./html_report

Then open html_report/index.html in your browser







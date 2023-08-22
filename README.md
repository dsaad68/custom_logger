# Custom Logger Library
This library provides a customizable logger with support for additional attributes, stream and file logging, as well as integration with Azure Application Insights.

## Features
1. Custom Attributes: Using the CustomLogFilter class, you can add any number of custom attributes to log records.
2. Stream and File Logging: The Logger class allows you to enable or disable stream and file handlers for logging.
3. Azure Application Insights Integration: By providing an Azure connection string, you can enable logging to Azure App Insights.

## Usage

You can create a logger object with optional parameters for stream handling, file handling, log levels, and custom dimensions:

```python
logger = Logger(username="Tester", OS="Windows", local="local", custom_dimensions={'job_id': 2020}, file_handler=True)
logger.get_logger()
logging.info("Testing!")

# [2023-08-22 18:28:10] - [INFO] - [Tester] - [Windows] - [local] - [{'job_id': 2020}] - (custom_logger.py).<module>(166) - Testing!
```

It can affect all the log messages generated within imported modules:

```python
import helper

logger = Logger(username="Tester", OS="Windows", local="local", custom_dimensions={'job_id': 2020}, file_handler=True)
logger.get_logger()

helper.do()

# [2023-08-22 18:30:59] - [INFO] - [Tester] - [Windows] - [local] - [{'job_id': 2020}] - (helper.py).do(7) - HELLO
```

## Dependencies
This library uses AzureLogHandler from OpenCensus for Azure Application Insights integration:
* `opencensus`
* `opencensus-context`
* `opencensus-ext-azure`
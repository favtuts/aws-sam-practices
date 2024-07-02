# AWS SAM Practices
Practices on AWS SAM

* https://tuts.heomi.net/a-practical-introduction-to-aws-sam-a-comprehensive-guide-for-cloud-engineers/

# First SAM Application

```bash
$ Sam init


Which template source would you like to use?
        1 - AWS Quick Start Templates
        2 - Custom Template Location
Choice: 1

Choose an AWS Quick Start application template
        1 - Hello World Example
        2 - Data processing
        3 - Hello World Example with Powertools for AWS Lambda
        4 - Multi-step workflow
        5 - Scheduled task
        6 - Standalone function
        7 - Serverless API
        8 - Infrastructure event management
        9 - Lambda Response Streaming
        10 - Serverless Connector Hello World Example
        11 - Multi-step workflow with Connectors
        12 - GraphQLApi Hello World Example
        13 - Full Stack
        14 - Lambda EFS example
        15 - DynamoDB Example
        16 - Machine Learning
Template: 1

Use the most popular runtime and package type? (Python and zip) [y/N]: y

Would you like to enable X-Ray tracing on the function(s) in your application?  [y/N]: n

Would you like to enable monitoring using CloudWatch Application Insights?
For more info, please view https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.html [y/N]: n

Would you like to set Structured Logging in JSON format on your Lambda functions?  [y/N]: y
Structured Logging in JSON format might incur an additional cost. View https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html#monitoring-cloudwatchlogs-pricing for more details

Project name [sam-app]: hello-world

    -----------------------
    Generating application:
    -----------------------
    Name: hello-world
    Runtime: python3.9
    Architectures: x86_64
    Dependency Manager: pip
    Application Template: hello-world
    Output Directory: .
    Configuration file: hello-world/samconfig.toml
    
    Next steps can be found in the README file at hello-world/README.md
        

Commands you can use next
=========================
[*] Create pipeline: cd hello-world && sam pipeline init --bootstrap
[*] Validate SAM template: cd hello-world && sam validate
[*] Test Function in the Cloud: cd hello-world && sam sync --stack-name {stack-name} --watch
```

# Building RESTful API

```bash
$ sam init

You can preselect a particular runtime or package type when using the `sam init` experience.
Call `sam init --help` to learn more.

Which template source would you like to use?
        1 - AWS Quick Start Templates
        2 - Custom Template Location
Choice: 1

Choose an AWS Quick Start application template
        1 - Hello World Example
        2 - Data processing
        3 - Hello World Example with Powertools for AWS Lambda
        4 - Multi-step workflow
        5 - Scheduled task
        6 - Standalone function
        7 - Serverless API
        8 - Infrastructure event management
        9 - Lambda Response Streaming
        10 - Serverless Connector Hello World Example
        11 - Multi-step workflow with Connectors
        12 - GraphQLApi Hello World Example
        13 - Full Stack
        14 - Lambda EFS example
        15 - DynamoDB Example
        16 - Machine Learning
Template: 1

Use the most popular runtime and package type? (Python and zip) [y/N]: y

Would you like to enable X-Ray tracing on the function(s) in your application?  [y/N]: n

Would you like to enable monitoring using CloudWatch Application Insights?
For more info, please view https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.html [y/N]: n

Would you like to set Structured Logging in JSON format on your Lambda functions?  [y/N]: y
Structured Logging in JSON format might incur an additional cost. View https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html#monitoring-cloudwatchlogs-pricing for more details

Project name [sam-app]: restfulapi-app

    -----------------------
    Generating application:
    -----------------------
    Name: restfulapi-app
    Runtime: python3.9
    Architectures: x86_64
    Dependency Manager: pip
    Application Template: hello-world
    Output Directory: .
    Configuration file: restfulapi-app/samconfig.toml
    
    Next steps can be found in the README file at restfulapi-app/README.md
        

Commands you can use next
=========================
[*] Create pipeline: cd restfulapi-app && sam pipeline init --bootstrap
[*] Validate SAM template: cd restfulapi-app && sam validate
[*] Test Function in the Cloud: cd restfulapi-app && sam sync --stack-name {stack-name} --watch
```

# Data Processing Pipeline

Create a serverless data processing pipeline that triggers Lambda functions on S3 events, processes data, and stores results in DynamoDB.

Create a new directory for your project and navigate into it.
```bash
$ sam init

You can preselect a particular runtime or package type when using the `sam init` experience.
Call `sam init --help` to learn more.

Which template source would you like to use?
        1 - AWS Quick Start Templates
        2 - Custom Template Location
Choice: 1

Choose an AWS Quick Start application template
        1 - Hello World Example
        2 - Data processing
        3 - Hello World Example with Powertools for AWS Lambda
        4 - Multi-step workflow
        5 - Scheduled task
        6 - Standalone function
        7 - Serverless API
        8 - Infrastructure event management
        9 - Lambda Response Streaming
        10 - Serverless Connector Hello World Example
        11 - Multi-step workflow with Connectors
        12 - GraphQLApi Hello World Example
        13 - Full Stack
        14 - Lambda EFS example
        15 - DynamoDB Example
        16 - Machine Learning
Template: 1

Use the most popular runtime and package type? (Python and zip) [y/N]: y

Would you like to enable X-Ray tracing on the function(s) in your application?  [y/N]: n

Would you like to enable monitoring using CloudWatch Application Insights?
For more info, please view https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.html [y/N]: n

Would you like to set Structured Logging in JSON format on your Lambda functions?  [y/N]: y
Structured Logging in JSON format might incur an additional cost. View https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html#monitoring-cloudwatchlogs-pricing for more details

Project name [sam-app]: s3-lambda-dynamodb-pipeline

    -----------------------
    Generating application:
    -----------------------
    Name: s3-lambda-dynamodb-pipeline
    Runtime: python3.9
    Architectures: x86_64
    Dependency Manager: pip
    Application Template: hello-world
    Output Directory: .
    Configuration file: s3-lambda-dynamodb-pipeline/samconfig.toml
    
    Next steps can be found in the README file at s3-lambda-dynamodb-pipeline/README.md
        

Commands you can use next
=========================
[*] Create pipeline: cd s3-lambda-dynamodb-pipeline && sam pipeline init --bootstrap
[*] Validate SAM template: cd s3-lambda-dynamodb-pipeline && sam validate
[*] Test Function in the Cloud: cd s3-lambda-dynamodb-pipeline && sam sync --stack-name {stack-name} --watch
```
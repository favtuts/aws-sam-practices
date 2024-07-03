# DATA PROCESSING PIPELINE
* https://tuts.heomi.net/a-practical-introduction-to-aws-sam-a-comprehensive-guide-for-cloud-engineers/


## Build the Application
```bash
$ sam build
Starting Build use cache
Manifest file is changed (new hash: 3298f13049d19cffaa37ca931dd4d421) or dependency folder (.aws-sam/deps/56913e5e-8f42-4d23-985b-c54e4b25ab94)
is missing for (ProcessDataFunction), downloading dependencies and copying/building source
Building codeuri: /home/tvt/techspace/aws/sam/aws-sam-practices/s3-lambda-dynamodb-pipeline/process_data runtime: python3.9 metadata: {}
architecture: x86_64 functions: ProcessDataFunction
 Running PythonPipBuilder:CleanUp
 Running PythonPipBuilder:ResolveDependencies
 Running PythonPipBuilder:CopySource
 Running PythonPipBuilder:CopySource

Build Succeeded

Built Artifacts  : .aws-sam/build
Built Template   : .aws-sam/build/template.yaml

Commands you can use next
=========================
[*] Validate SAM template: sam validate
[*] Invoke Function: sam local invoke
[*] Test Function in the Cloud: sam sync --stack-name {{stack-name}} --watch
[*] Deploy: sam deploy --guided
```

## Deploy the Application
```bash
$ sam deploy --guided --profile tvt_admin

Configuring SAM deploy
======================

        Looking for config file [samconfig.toml] :  Found
        Reading default arguments  :  Success

        Setting default arguments for 'sam deploy'
        =========================================
        Stack Name [s3-lambda-dynamodb-pipeline]:
        AWS Region [us-east-1]:
        #Shows you resources changes to be deployed and require a 'Y' to initiate deploy
        Confirm changes before deploy [Y/n]: y
        #SAM needs permission to be able to create roles to connect to the resources in your template
        Allow SAM CLI IAM role creation [Y/n]: y
        #Preserves the state of previously provisioned resources when an operation fails
        Disable rollback [y/N]: y
        Save arguments to configuration file [Y/n]: y
        SAM configuration file [samconfig.toml]:
        SAM configuration environment [default]:

        Looking for resources needed for deployment:

        Managed S3 bucket: aws-sam-cli-managed-default-samclisourcebucket-qeasky7sjge6
        A different default S3 bucket can be set in samconfig.toml and auto resolution of buckets turned off by setting resolve_s3=False

        Parameter "stack_name=s3-lambda-dynamodb-pipeline" in [default.deploy.parameters] is defined as a global parameter
[default.global.parameters].
        This parameter will be only saved under [default.global.parameters] in
/home/tvt/techspace/aws/sam/aws-sam-practices/s3-lambda-dynamodb-pipeline/samconfig.toml.

        Saved arguments to config file
        Running 'sam deploy' for future deployments will use the parameters saved above.
        The above parameters can be changed by modifying samconfig.toml
        Learn more about samconfig.toml syntax at
        https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-config.html

        Uploading to s3-lambda-dynamodb-pipeline/2b8af50e94fb7f7563fccda82ecf085e  560126 / 560126  (100.00%)

        Deploying with following values
        ===============================
        Stack name                   : s3-lambda-dynamodb-pipeline
        Region                       : us-east-1
        Confirm changeset            : True
        Disable rollback             : True
        Deployment s3 bucket         : aws-sam-cli-managed-default-samclisourcebucket-qeasky7sjge6
        Capabilities                 : ["CAPABILITY_IAM"]
        Parameter overrides          : {}
        Signing Profiles             : {}

Initiating deployment
=====================

        Uploading to s3-lambda-dynamodb-pipeline/e710a0cb137e3dfb49a6634d72041b61.template  4889 / 4889  (100.00%)


Waiting for changeset to be created..

CloudFormation stack changeset
---------------------------------------------------------------------------------------------------------------------------------------------
Operation                           LogicalResourceId                   ResourceType                        Replacement
---------------------------------------------------------------------------------------------------------------------------------------------
+ Add                               CustomS3NotificationFunctionRole    AWS::IAM::Role                      N/A
+ Add                               CustomS3NotificationFunction        AWS::Lambda::Function               N/A
+ Add                               CustomS3Notification                Custom::S3Notification              N/A
+ Add                               DynamoDBTable                       AWS::DynamoDB::Table                N/A
+ Add                               LambdaInvokePermission              AWS::Lambda::Permission             N/A
+ Add                               ProcessDataFunctionRole             AWS::IAM::Role                      N/A
+ Add                               ProcessDataFunction                 AWS::Lambda::Function               N/A
+ Add                               S3Bucket                            AWS::S3::Bucket                     N/A
---------------------------------------------------------------------------------------------------------------------------------------------


Changeset created successfully. arn:aws:cloudformation:us-east-1:475797023758:changeSet/samcli-deploy1719972057/de20831e-07b1-49e9-99c7-1dfb4b79b82f


Previewing CloudFormation changeset before deployment
======================================================
Deploy this changeset? [y/N]: y

2024-07-03 09:01:16 - Waiting for stack create/update to complete

CloudFormation events from stack operations (refresh every 5.0 seconds)
---------------------------------------------------------------------------------------------------------------------------------------------
ResourceStatus                      ResourceType                        LogicalResourceId                   ResourceStatusReason
---------------------------------------------------------------------------------------------------------------------------------------------
CREATE_IN_PROGRESS                  AWS::CloudFormation::Stack          s3-lambda-dynamodb-pipeline         User Initiated
CREATE_IN_PROGRESS                  AWS::S3::Bucket                     S3Bucket                            -
CREATE_IN_PROGRESS                  AWS::DynamoDB::Table                DynamoDBTable                       -
CREATE_IN_PROGRESS                  AWS::DynamoDB::Table                DynamoDBTable                       Resource creation Initiated
CREATE_IN_PROGRESS                  AWS::S3::Bucket                     S3Bucket                            Resource creation Initiated
CREATE_COMPLETE                     AWS::DynamoDB::Table                DynamoDBTable                       -
CREATE_COMPLETE                     AWS::S3::Bucket                     S3Bucket                            -
CREATE_IN_PROGRESS                  AWS::IAM::Role                      ProcessDataFunctionRole             -
CREATE_IN_PROGRESS                  AWS::IAM::Role                      CustomS3NotificationFunctionRole    -
CREATE_IN_PROGRESS                  AWS::IAM::Role                      CustomS3NotificationFunctionRole    Resource creation Initiated
CREATE_IN_PROGRESS                  AWS::IAM::Role                      ProcessDataFunctionRole             Resource creation Initiated
CREATE_COMPLETE                     AWS::IAM::Role                      CustomS3NotificationFunctionRole    -
CREATE_COMPLETE                     AWS::IAM::Role                      ProcessDataFunctionRole             -
CREATE_IN_PROGRESS                  AWS::Lambda::Function               CustomS3NotificationFunction        -
CREATE_IN_PROGRESS                  AWS::Lambda::Function               ProcessDataFunction                 -
CREATE_IN_PROGRESS                  AWS::Lambda::Function               CustomS3NotificationFunction        Resource creation Initiated
CREATE_IN_PROGRESS                  AWS::Lambda::Function               CustomS3NotificationFunction        Eventual consistency check
                                                                                                            initiated
CREATE_IN_PROGRESS                  AWS::Lambda::Function               ProcessDataFunction                 Resource creation Initiated
CREATE_IN_PROGRESS                  AWS::Lambda::Function               ProcessDataFunction                 Eventual consistency check
                                                                                                            initiated
CREATE_IN_PROGRESS                  AWS::Lambda::Permission             LambdaInvokePermission              -
CREATE_IN_PROGRESS                  AWS::Lambda::Permission             LambdaInvokePermission              Resource creation Initiated
CREATE_COMPLETE                     AWS::Lambda::Permission             LambdaInvokePermission              -
CREATE_COMPLETE                     AWS::Lambda::Function               CustomS3NotificationFunction        -
CREATE_COMPLETE                     AWS::Lambda::Function               ProcessDataFunction                 -
CREATE_IN_PROGRESS                  Custom::S3Notification              CustomS3Notification                -
CREATE_IN_PROGRESS                  Custom::S3Notification              CustomS3Notification                Resource creation Initiated
CREATE_COMPLETE                     Custom::S3Notification              CustomS3Notification                -
CREATE_COMPLETE                     AWS::CloudFormation::Stack          s3-lambda-dynamodb-pipeline         -
---------------------------------------------------------------------------------------------------------------------------------------------

CloudFormation outputs from deployed stack
---------------------------------------------------------------------------------------------------------------------------------------------
Outputs
---------------------------------------------------------------------------------------------------------------------------------------------
Key                 DynamoDBTableName
Description         Name of the DynamoDB table
Value               s3-lambda-dynamodb-pipeline-table

Key                 LambdaFunction
Description         ARN of the Lambda function
Value               arn:aws:lambda:us-east-1:475797023758:function:s3-lambda-dynamodb-pipeline-ProcessDataFunction-xHtenZVdoPsx

Key                 S3BucketName
Description         Name of the S3 bucket
Value               s3-lambda-dynamodb-pipeline-bucket
---------------------------------------------------------------------------------------------------------------------------------------------


Successfully created/updated stack - s3-lambda-dynamodb-pipeline in us-east-1
```


## Test the Pipeline

Create a sample `test.json` file and add the following content.
```json
{
  "message": "This is a test message for the Lambda function inorder to test the data processing pipeline."
}
```

Then upload a file to the S3 bucket
```bash
$ aws s3 cp test.json s3://s3-lambda-dynamodb-pipeline-bucket/ --profile tvt_admin
upload: ./test.json to s3://s3-lambda-dynamodb-pipeline-bucket/test.json
```

Check the DynamoDB table to verify that the processed data has been stored.


## Clean deployed stack

```bash
$ sam delete --stack-name "s3-lambda-dynamodb-pipeline"
```


# s3-lambda-dynamodb-pipeline

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- hello_world - Code for the application's Lambda function.
- events - Invocation events that you can use to invoke the function.
- tests - Unit tests for the application code. 
- template.yaml - A template that defines the application's AWS resources.

The application uses several AWS resources, including Lambda functions and an API Gateway API. These resources are defined in the `template.yaml` file in this project. You can update the template to add AWS resources through the same deployment process that updates your application code.

If you prefer to use an integrated development environment (IDE) to build and test your application, you can use the AWS Toolkit.  
The AWS Toolkit is an open source plug-in for popular IDEs that uses the SAM CLI to build and deploy serverless applications on AWS. The AWS Toolkit also adds a simplified step-through debugging experience for Lambda function code. See the following links to get started.

* [CLion](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [GoLand](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [IntelliJ](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [WebStorm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [Rider](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [PhpStorm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [PyCharm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [RubyMine](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [DataGrip](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [VS Code](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/welcome.html)
* [Visual Studio](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/welcome.html)

## Deploy the sample application

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

To use the SAM CLI, you need the following tools.

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 installed](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

To build and deploy your application for the first time, run the following in your shell:

```bash
sam build --use-container
sam deploy --guided
```

The first command will build the source of your application. The second command will package and deploy your application to AWS, with a series of prompts:

* **Stack Name**: The name of the stack to deploy to CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
* **AWS Region**: The AWS region you want to deploy your app to.
* **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
* **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modifies IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
* **Save arguments to samconfig.toml**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.

You can find your API Gateway Endpoint URL in the output values displayed after deployment.

## Use the SAM CLI to build and test locally

Build your application with the `sam build --use-container` command.

```bash
s3-lambda-dynamodb-pipeline$ sam build --use-container
```

The SAM CLI installs dependencies defined in `hello_world/requirements.txt`, creates a deployment package, and saves it in the `.aws-sam/build` folder.

Test a single function by invoking it directly with a test event. An event is a JSON document that represents the input that the function receives from the event source. Test events are included in the `events` folder in this project.

Run functions locally and invoke them with the `sam local invoke` command.

```bash
s3-lambda-dynamodb-pipeline$ sam local invoke HelloWorldFunction --event events/event.json
```

The SAM CLI can also emulate your application's API. Use the `sam local start-api` to run the API locally on port 3000.

```bash
s3-lambda-dynamodb-pipeline$ sam local start-api
s3-lambda-dynamodb-pipeline$ curl http://localhost:3000/
```

The SAM CLI reads the application template to determine the API's routes and the functions that they invoke. The `Events` property on each function's definition includes the route and method for each path.

```yaml
      Events:
        HelloWorld:
          Type: Api
          Properties:
            Path: /hello
            Method: get
```

## Add a resource to your application
The application template uses AWS Serverless Application Model (AWS SAM) to define application resources. AWS SAM is an extension of AWS CloudFormation with a simpler syntax for configuring common serverless application resources such as functions, triggers, and APIs. For resources not included in [the SAM specification](https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md), you can use standard [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) resource types.

## Fetch, tail, and filter Lambda function logs

To simplify troubleshooting, SAM CLI has a command called `sam logs`. `sam logs` lets you fetch logs generated by your deployed Lambda function from the command line. In addition to printing the logs on the terminal, this command has several nifty features to help you quickly find the bug.

`NOTE`: This command works for all AWS Lambda functions; not just the ones you deploy using SAM.

```bash
s3-lambda-dynamodb-pipeline$ sam logs -n HelloWorldFunction --stack-name "s3-lambda-dynamodb-pipeline" --tail
```

You can find more information and examples about filtering Lambda function logs in the [SAM CLI Documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-logging.html).

## Tests

Tests are defined in the `tests` folder in this project. Use PIP to install the test dependencies and run tests.

```bash
s3-lambda-dynamodb-pipeline$ pip install -r tests/requirements.txt --user
# unit test
s3-lambda-dynamodb-pipeline$ python -m pytest tests/unit -v
# integration test, requiring deploying the stack first.
# Create the env variable AWS_SAM_STACK_NAME with the name of the stack we are testing
s3-lambda-dynamodb-pipeline$ AWS_SAM_STACK_NAME="s3-lambda-dynamodb-pipeline" python -m pytest tests/integration -v
```

## Cleanup

To delete the sample application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```bash
sam delete --stack-name "s3-lambda-dynamodb-pipeline"
```

## Resources

See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.

Next, you can use AWS Serverless Application Repository to deploy ready to use Apps that go beyond hello world samples and learn how authors developed their applications: [AWS Serverless Application Repository main page](https://aws.amazon.com/serverless/serverlessrepo/)

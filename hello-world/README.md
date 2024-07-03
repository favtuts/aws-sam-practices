# Hello World Application
* https://tuts.heomi.net/a-practical-introduction-to-aws-sam-a-comprehensive-guide-for-cloud-engineers/

# Test Locally

Run the application locally to test it:
```
$ sam local start-api
```

Then navigate to `http://127.0.0.1:3000/hello` in your browser to see the output.

# Deploy the application

Package the Application
```
$ sam package --output-template-file hello-world-packaged.yaml --s3-bucket tvt-artifacts-bucket --profile tvt_admin
```

Deploy the Application
```
$ sam deploy --template-file hello-world-packaged.yaml --stack-name hello-world-stack --capabilities CAPABILITY_IAM
```


You may see the error:
```
Cannot use both --resolve-s3 and --s3-bucket parameters in non-guided deployments
```
Fix: 
```
What needs to change: Delete line "resolve_s3=true" under [default.package.parameters] in the file samconfig.toml .
Of course, it seems like it would be best to do this AFTER your initial SAM setup / AFTER you have an active S3 bucket for your SAM.
```


To build and deploy your application for the first time, run the following in your shell:
```bash
$ sam build --use-container
``

Deploy to AWS
```bash
$ sam deploy --guided --profile tvt_admin

Configuring SAM deploy
======================

        Looking for config file [samconfig.toml] :  Found
        Reading default arguments  :  Success

        Setting default arguments for 'sam deploy'
        =========================================
        Stack Name [hello-world]: hello-world-stack
        AWS Region [us-east-1]: 
        #Shows you resources changes to be deployed and require a 'Y' to initiate deploy
        Confirm changes before deploy [Y/n]: y
        #SAM needs permission to be able to create roles to connect to the resources in your template
        Allow SAM CLI IAM role creation [Y/n]: y
        #Preserves the state of previously provisioned resources when an operation fails
        Disable rollback [y/N]: y
        HelloWorldFunction has no authentication. Is this okay? [y/N]: y
        Save arguments to configuration file [Y/n]: y
        SAM configuration file [samconfig.toml]: 
        SAM configuration environment [default]: 

        Looking for resources needed for deployment:
        Creating the required resources...
        Successfully created!

        Managed S3 bucket: aws-sam-cli-managed-default-samclisourcebucket-qeasky7sjge6
        A different default S3 bucket can be set in samconfig.toml and auto resolution of buckets turned off by setting resolve_s3=False

        Saved arguments to config file
        Running 'sam deploy' for future deployments will use the parameters saved above.
        The above parameters can be changed by modifying samconfig.toml
        Learn more about samconfig.toml syntax at 
        https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-config.html

        Uploading to hello-world-stack/44cebbc6d696d8f1c2fd63aa59e45908  560123 / 560123  (100.00%)

        Deploying with following values
        ===============================
        Stack name                   : hello-world-stack
        Region                       : us-east-1
        Confirm changeset            : True
        Disable rollback             : True
        Deployment s3 bucket         : aws-sam-cli-managed-default-samclisourcebucket-qeasky7sjge6
        Capabilities                 : ["CAPABILITY_IAM"]
        Parameter overrides          : {}
        Signing Profiles             : {}

Initiating deployment
=====================

        Uploading to hello-world-stack/ced2f1a78d3653cde973192eef106eaa.template  1258 / 1258  (100.00%)


Waiting for changeset to be created..

CloudFormation stack changeset
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Operation                                   LogicalResourceId                           ResourceType                                Replacement                               
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
+ Add                                       HelloWorldFunctionHelloWorldPermissionPro   AWS::Lambda::Permission                     N/A                                       
                                            d                                                                                                                                 
+ Add                                       HelloWorldFunctionRole                      AWS::IAM::Role                              N/A                                       
+ Add                                       HelloWorldFunction                          AWS::Lambda::Function                       N/A                                       
+ Add                                       ServerlessRestApiDeployment47fc2d5f9d       AWS::ApiGateway::Deployment                 N/A                                       
+ Add                                       ServerlessRestApiProdStage                  AWS::ApiGateway::Stage                      N/A                                       
+ Add                                       ServerlessRestApi                           AWS::ApiGateway::RestApi                    N/A                                       
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Changeset created successfully. arn:aws:cloudformation:us-east-1:475797023758:changeSet/samcli-deploy1719908683/49d448ef-a7a7-4d82-a3f8-b14417afb4fa


Previewing CloudFormation changeset before deployment
======================================================
Deploy this changeset? [y/N]: y

2024-07-02 15:24:59 - Waiting for stack create/update to complete

CloudFormation events from stack operations (refresh every 5.0 seconds)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ResourceStatus                              ResourceType                                LogicalResourceId                           ResourceStatusReason                      
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
CREATE_IN_PROGRESS                          AWS::CloudFormation::Stack                  hello-world-stack                           User Initiated                            
CREATE_IN_PROGRESS                          AWS::IAM::Role                              HelloWorldFunctionRole                      -                                         
CREATE_IN_PROGRESS                          AWS::IAM::Role                              HelloWorldFunctionRole                      Resource creation Initiated               
CREATE_COMPLETE                             AWS::IAM::Role                              HelloWorldFunctionRole                      -                                         
CREATE_IN_PROGRESS                          AWS::Lambda::Function                       HelloWorldFunction                          -                                         
CREATE_IN_PROGRESS                          AWS::Lambda::Function                       HelloWorldFunction                          Resource creation Initiated               
CREATE_IN_PROGRESS                          AWS::Lambda::Function                       HelloWorldFunction                          Eventual consistency check initiated      
CREATE_IN_PROGRESS                          AWS::ApiGateway::RestApi                    ServerlessRestApi                           -                                         
CREATE_IN_PROGRESS                          AWS::ApiGateway::RestApi                    ServerlessRestApi                           Resource creation Initiated               
CREATE_COMPLETE                             AWS::ApiGateway::RestApi                    ServerlessRestApi                           -                                         
CREATE_IN_PROGRESS                          AWS::Lambda::Permission                     HelloWorldFunctionHelloWorldPermissionPro   -                                         
                                                                                        d                                                                                     
CREATE_IN_PROGRESS                          AWS::ApiGateway::Deployment                 ServerlessRestApiDeployment47fc2d5f9d       -                                         
CREATE_IN_PROGRESS                          AWS::Lambda::Permission                     HelloWorldFunctionHelloWorldPermissionPro   Resource creation Initiated               
                                                                                        d                                                                                     
CREATE_COMPLETE                             AWS::Lambda::Permission                     HelloWorldFunctionHelloWorldPermissionPro   -                                         
                                                                                        d                                                                                     
CREATE_IN_PROGRESS                          AWS::ApiGateway::Deployment                 ServerlessRestApiDeployment47fc2d5f9d       Resource creation Initiated               
CREATE_COMPLETE                             AWS::ApiGateway::Deployment                 ServerlessRestApiDeployment47fc2d5f9d       -                                         
CREATE_COMPLETE                             AWS::Lambda::Function                       HelloWorldFunction                          -                                         
CREATE_IN_PROGRESS                          AWS::ApiGateway::Stage                      ServerlessRestApiProdStage                  -                                         
CREATE_IN_PROGRESS                          AWS::ApiGateway::Stage                      ServerlessRestApiProdStage                  Resource creation Initiated               
CREATE_COMPLETE                             AWS::ApiGateway::Stage                      ServerlessRestApiProdStage                  -                                         
CREATE_COMPLETE                             AWS::CloudFormation::Stack                  hello-world-stack                           -                                         
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

CloudFormation outputs from deployed stack
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Outputs                                                                                                                                                                      
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Key                 HelloWorldFunctionIamRole                                                                                                                                
Description         Implicit IAM Role created for Hello World function                                                                                                       
Value               arn:aws:iam::475797023758:role/hello-world-stack-HelloWorldFunctionRole-BXy8epFe2wIJ                                                                     

Key                 HelloWorldApi                                                                                                                                            
Description         API Gateway endpoint URL for Prod stage for Hello World function                                                                                         
Value               https://lp0poifrb9.execute-api.us-east-1.amazonaws.com/Prod/hello/                                                                                       

Key                 HelloWorldFunction                                                                                                                                       
Description         Hello World Lambda Function ARN                                                                                                                          
Value               arn:aws:lambda:us-east-1:475797023758:function:hello-world-stack-HelloWorldFunction-wuhIGTq7rThQ                                                         
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Successfully created/updated stack - hello-world-stack in us-east-1
```


Delete deployment
```
$ sam delete --stack-name "hello-world-stack" --profile tvt_admin
        Are you sure you want to delete the stack hello-world-stack in the region us-east-1 ? [y/N]: y
        Are you sure you want to delete the folder hello-world-stack in S3 which contains the artifacts? [y/N]: y
        - Deleting S3 object with key hello-world-stack/44cebbc6d696d8f1c2fd63aa59e45908
        - Deleting S3 object with key hello-world-stack/ced2f1a78d3653cde973192eef106eaa.template
        - Deleting Cloudformation stack hello-world-stack

Deleted successfully
```

# hello-world

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
hello-world$ sam build --use-container
```

The SAM CLI installs dependencies defined in `hello_world/requirements.txt`, creates a deployment package, and saves it in the `.aws-sam/build` folder.

Test a single function by invoking it directly with a test event. An event is a JSON document that represents the input that the function receives from the event source. Test events are included in the `events` folder in this project.

Run functions locally and invoke them with the `sam local invoke` command.

```bash
hello-world$ sam local invoke HelloWorldFunction --event events/event.json
```

The SAM CLI can also emulate your application's API. Use the `sam local start-api` to run the API locally on port 3000.

```bash
hello-world$ sam local start-api
hello-world$ curl http://localhost:3000/
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
hello-world$ sam logs -n HelloWorldFunction --stack-name "hello-world" --tail
```

You can find more information and examples about filtering Lambda function logs in the [SAM CLI Documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-logging.html).

## Tests

Tests are defined in the `tests` folder in this project. Use PIP to install the test dependencies and run tests.

```bash
hello-world$ pip install -r tests/requirements.txt --user
# unit test
hello-world$ python -m pytest tests/unit -v
# integration test, requiring deploying the stack first.
# Create the env variable AWS_SAM_STACK_NAME with the name of the stack we are testing
hello-world$ AWS_SAM_STACK_NAME="hello-world" python -m pytest tests/integration -v
```

## Cleanup

To delete the sample application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```bash
sam delete --stack-name "hello-world"
```

## Resources

See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.

Next, you can use AWS Serverless Application Repository to deploy ready to use Apps that go beyond hello world samples and learn how authors developed their applications: [AWS Serverless Application Repository main page](https://aws.amazon.com/serverless/serverlessrepo/)

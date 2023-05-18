# AWS Serverless service cookiecutter (Python)

[![license](https://img.shields.io/github/license/ran-isenberg/cookiecutter-serverless-python)](https://github.com/ran-isenberg/cookiecutter-serverless-python/blob/master/LICENSE)
![PythonSupport](https://img.shields.io/static/v1?label=python&message=3.10&color=blue?style=flat-square&logo=python)
![version](https://img.shields.io/github/v/release/ran-isenberg/cookiecutter-serverless-python)
![github-star-badge](https://img.shields.io/github/stars/ran-isenberg/cookiecutter-serverless-python.svg?style=social)
![issues](https://img.shields.io/github/issues/ran-isenberg/cookiecutter-serverless-python)

![logo](https://github.com/ran-isenberg/cookiecutter-serverless-python/blob/main/media/banner.png?raw=true)


This project can serve as a cookiecutter template for new Serverless services - CDK deployment code, pipeline and handler are covered with best practices built in.
<br></br>
The project is based on my [AWS Lambda Cookbook template project](https://github.com/ran-isenberg/aws-lambda-handler-cookbook):

[![license](https://img.shields.io/github/license/ran-isenberg/aws-lambda-handler-cookbook)](https://github.com/ran-isenberg/aws-lambda-handler-cookbook/blob/master/LICENSE)
![PythonSupport](https://img.shields.io/static/v1?label=python&message=3.10&color=blue?style=flat-square&logo=python)
[![codecov](https://codecov.io/gh/ran-isenberg/aws-lambda-handler-cookbook/branch/main/graph/badge.svg?token=P2K7K4KICF)](https://codecov.io/gh/ran-isenberg/aws-lambda-handler-cookbook)
![version](https://img.shields.io/github/v/release/ran-isenberg/aws-lambda-handler-cookbook)
![github-star-badge](https://img.shields.io/github/stars/ran-isenberg/aws-lambda-handler-cookbook.svg?style=social)
![issues](https://img.shields.io/github/issues/ran-isenberg/aws-lambda-handler-cookbook)


**[📜Documentation](https://ran-isenberg.github.io/aws-lambda-handler-cookbook/)** | **[Blogs website](https://www.ranthebuilder.cloud)**
> **Contact details | ran.isenberg@ranthebuilder.cloud**
<br></br>
## **Prerequisites**

* **Docker** - install [Docker](https://www.docker.com/). Required for the Lambda layer packaging process.
* **[AWS CDK](cdk.md)** - Required for synth & deploying the AWS Cloudformation stack.
* Python 3.10
* [poetry](https://pypi.org/project/poetry/) - Make sure to run ``poetry config --local virtualenvs.in-project true`` so all dependencies are installed in the project '.venv' folder.
* For Windows based machines, use the Makefile_windows version (rename to Makefile). Default Makefile is for Mac/Linux.
* Cookiecutter - install with pip/brew ``brew install cookiecutter`` or ``pip install cookiecutter``
<br></br>
## Getting Started

```
cookiecutter gh:ran-isenberg/cookiecutter-serverless-python
```

Follow the guide:

![logo](https://github.com/ran-isenberg/cookiecutter-serverless-python/blob/main/media/howto.png?raw=true)
<br></br>

```
cd {new repo folder}
git init
```


Now you can setup your developer environment and deploy to AWS. Run the following commands:

```
make dev
poetry install
make pr
```

Make 'pr' will run all checks, synth, file formatters , unit tests, deploy to AWS and run integration and E2E tests.


For more information head over to project documentation pages at [https://ran-isenberg.github.io/aws-lambda-handler-cookbook](https://ran-isenberg.github.io/aws-lambda-handler-cookbook/)

The documentation provides information about CDK deployment, makefile commands, testing methodology and more.

<br></br>
## Serverless Service - The Order service

- This project provides a working orders service where customers can create orders of items.

- The project deploys an API GW with an AWS Lambda integration under the path POST /api/orders/ and stores data in a DynamoDB table.


![design](https://github.com/ran-isenberg/cookiecutter-serverless-python/blob/main/media/design.png?raw=true)
<br></br>

### **Features**

- Python Serverless service with a recommended file structure.
- CDK infrastructure with infrastructure tests and security tests.
- CI/CD pipelines based on Github actions that deploys to AWS with python linters, complexity checks and style formatters.
- Makefile for simple developer experience.
- The AWS Lambda handler embodies Serverless best practices and has all the bells and whistles for a proper production ready handler.
- AWS Lambda handler uses [AWS Lambda Powertools](https://awslabs.github.io/aws-lambda-powertools-python/).
- AWS Lambda handler 3 layer architecture: handler layer, logic layer and data access layer
- Features flags and configuration based on AWS AppConfig
- Unit, infrastructure, security, integration and E2E tests.
<br></br>

## CDK Deployment
The CDK code create an API GW with a path of /api/orders which triggers the lambda on 'POST' requests.

The AWS Lambda handler uses a Lambda layer optimization which takes all the packages under the [packages] section in the Pipfile and downloads them in via a Docker instance.

This allows you to package any custom dependencies you might have, just add them to the Pipfile under the [packages] section.
<br></br>
## Serverless Best Practices
The AWS Lambda handler will implement multiple best practice utilities.

Each utility is implemented when a new blog post is published about that utility.

The utilities cover multiple aspect of a production-ready service, including:

- [Logging](https://www.ranthebuilder.cloud/post/aws-lambda-cookbook-elevate-your-handler-s-code-part-1-logging)
- [Observability: Monitoring and Tracing](https://www.ranthebuilder.cloud/post/aws-lambda-cookbook-elevate-your-handler-s-code-part-2-observability)
- [Observability: Business KPIs Metrics](https://www.ranthebuilder.cloud/post/aws-lambda-cookbook-elevate-your-handler-s-code-part-3-business-domain-observability)
- [Environment Variables](https://www.ranthebuilder.cloud/post/aws-lambda-cookbook-environment-variables)
- [Input Validation](https://www.ranthebuilder.cloud/post/aws-lambda-cookbook-elevate-your-handler-s-code-part-5-input-validation)
- [Dynamic Configuration & feature flags](https://www.ranthebuilder.cloud/post/aws-lambda-cookbook-part-6-feature-flags-configuration-best-practices)
- [Start Your AWS Serverless Service With Two Clicks](https://www.ranthebuilder.cloud/post/aws-lambda-cookbook-part-7-how-to-use-the-aws-lambda-cookbook-github-template-project)
- [CDK Best practices](https://github.com/ran-isenberg/aws-lambda-handler-cookbook)

<br></br>
### Makefile Commands
#### **Creating a Developer Environment**

1. Run ``make dev``
2. Run ``poetry install``

<br></br>
#### **Deploy CDK**

Create a cloudformation stack by running ``make deploy``.
<br></br>
#### **Unit Tests**

Unit tests can be found under the ``tests/unit`` folder.

You can run the tests by using the following command: ``make unit``.

<br></br>
#### **Integration Tests**

Make sure you deploy the stack first as these tests trigger your lambda handler LOCALLY but they can communicate with AWS services.

These tests allow you to debug in your IDE your AWS Lambda function.

Integration tests can be found under the ``tests/integration`` folder.

You can run the tests by using the following command: ``make integration``.
<br></br>
#### **E2E Tests**

Make sure you deploy the stack first.

E2E tests can be found under the ``tests/e2e`` folder.

These tests send a 'POST' message to the deployed API GW and trigger the Lambda function on AWS.

The tests are run automatically by: ``make e2e``.
<br></br>
#### **Deleting the stack**

CDK destroy can be run with ``make destroy``.
<br></br>
#### **Preparing Code for PR**

Run ``make pr``. This command will run all the required checks, pre commit hooks, linters, code formats, flake8 and tests, so you can be sure GitHub's pipeline will pass.

The command auto fixes errors in the code for you.

If there's an error in the pre-commit stage, it gets auto fixed. However, are required to run ``make pr`` again so it continues to the next stages.

Be sure to commit all the changes that ``make pr`` does for you.

<br></br>
## Code Contributions
Code contributions are welcomed. Read this [guide.](https://github.com/ran-isenberg/aws-lambda-handler-cookbook/blob/main/CONTRIBUTING.md)
<br></br>
## Code of Conduct
Read our code of conduct [here.](https://github.com/ran-isenberg/aws-lambda-handler-cookbook/blob/main/CODE_OF_CONDUCT.md)
<br></br>
## Connect
* Email: [ran.isenberg@ranthebuilder.cloud](mailto:ran.isenberg@ranthebuilder.cloud)
* Blog Website [RanTheBuilder](https://www.ranthebuilder.cloud)
* LinkedIn: [ranisenberg](https://www.linkedin.com/in/ranisenberg/)
* Twitter: [IsenbergRan](https://twitter.com/IsenbergRan)
<br></br>
## Credits
* [AWS Lambda Powertools (Python)](https://github.com/awslabs/aws-lambda-powertools-python)
<br></br>
## License
This library is licensed under the MIT License. See the [LICENSE](https://github.com/ran-isenberg/aws-lambda-handler-cookbook/blob/main/LICENSE) file.

# Shifty-API
Back-end CRUD logic for managing shifts and users in Shifty applications. Written in Python 3 with 
Serverless Framework for AWS.
## Prerequisites
Your development environment will need to have the following installed:
- [Python 3.6](https://www.python.org/downloads/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)
- [Serverless Framework](https://serverless.com/framework/) (version 1.17.0 or higher)
### Recommendations
The instructions below assume a Linux development environment. Unless you know what you're doing,
it is strongly advised to develop in a Linux environment.
   If you are stuck with Windows, consider [Ubuntu on Windows](https://msdn.microsoft.com/en-us/commandline/wsl/about).
## Installation
- Create a directory/folder to clone the project into.
- Run `virtualenv .` in that directory and then `sounds bin/activate`. Now the dependencies 
you install will be isolated to this project.
  - Run `deactivate` to escape your virtual environment.
- Run `pip install -r requirements.txt` in the directory you cloned into to install the 
project dependencies.
## Deployment
- Simply use the `serverless deploy` command in the directory you cloned into. 
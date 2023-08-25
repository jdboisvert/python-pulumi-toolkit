# Development set up
This document describes how to set up your development environment for this project.

# Set up
1. Install [Pulumi](https://www.pulumi.com/docs/get-started/install/)
2. Install [Python 3.9+](https://www.python.org/downloads/)

## Virtual env using pyenv
```shell
# install pyenv (if necessary)
brew install pyenv pyenv-virtualenv
echo """
export PYENV_VIRTUALENV_DISABLE_PROMPT=1
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
""" > ~/.zshrc
source ~/.zshrc

# create a virtualenv
pyenv install 3.11.0
pyenv virtualenv 3.11.0 python_pulumi_toolkit
pyenv activate python_pulumi_toolkit

# install dependencies
pip install -U pip
pip install -r requirements.txt
```

## Pulumi Playground
There is a directory called `pulumi-playground` that contains a Pulumi project that can be used to test the components in this library. To use this you will need to create a Pulumi account and create a new stack. Note if you plan to use this directory you will need to change the `Pulumi.<stack name>.yaml` file to point to your stack. 

I added this more as a way to quickly test the components in this library (odds are as this grows it will be removed).

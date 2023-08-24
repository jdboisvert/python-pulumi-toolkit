# python-pulumi-toolkit
A collection of Pulumi resources wrapped in a portable and reusable SDK. 

## Set up
1. Install [Pulumi](https://www.pulumi.com/docs/get-started/install/)
2. Install [Python 3.9+](https://www.python.org/downloads/)

### Virtual env using pyenv
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
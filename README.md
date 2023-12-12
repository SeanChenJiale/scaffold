# scaffold
A project scaffold for Python
## Requirements
Create A Python Scaffold
This lab demonstrates an important concept in Cloud computing, building repeatable development environments that allow for Continuous Integration and Continuous Development.

Open a terminal in Visual Studio Code.

cd into the projects directory:  cd /home/coder/project

Install virtualenv:  python3 -m pip install virtualenv

Create a virtualenv: /home/coder/.local/bin/virtualenv VENV

Source the virtualenv (activate it):  source VENV/bin/activate

cd into scaffold:  cd /home/coder/project/scaffold

install software:  make install

Run lint:  make lint

rRun tests:  make test

Experiment on your own with breaking a test or adding a bad variable and run make lint or make test.

Note: We recommend that you open this notebook in the most updated version Google Chrome for the most consistent experience.

  
```
ssh-keygen -t rsa  
cat /home/ec2-user//.ssh/id_rsa.pub
# the string is within the public key section of the image below
# touch file_name
# make lint
```

## Sample images  
![image](https://github.com/SeanChenJiale/scaffold/assets/153470046/342703db-08e1-4ee1-9b2b-37cba73cc8ae) 
![image](https://github.com/SeanChenJiale/scaffold/assets/153470046/df8a5791-7d7f-4b0d-9bb1-f632c6f16ecb)



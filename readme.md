
# Welcome to AI Hub Workshop Simulation hands-on session

In this session we will introduce CARLA briefly.

Note: Required OS for this session is ubuntu. If you are on windows, you can follow the instructions from presentor's screen.
Please clone the repo

```bash
git clone https://github.com/golnazraja/aihub_simulators_workshop.git
```

And switch to the master branch

```bash
cd aihub_simulators_workshop/
git checkout master
```
Please prepare a virtual environment for this workshop to avoid conflict.
Install **Python 3.7** (other python versions can cause conflict) 

you can try virtual environment in **ubuntu** as bellow
(Conda and miniconda environments will also work)

```bash
sudo apt install python3.7 python3-venv python3.7-venv
python3.7 -m venv py37-venv
. py37-venv/bin/activate
```
Then switch to the repository directory and install the requirements via pip

```bash
pip install -r requirements.txt
```

And Done!

Now we can run the codes together during the workshop.
Note: During the session you have to connect to our local server through WiFi to be in the network of our CARLA server.

Codes during the workshop:

Introduction to CARLA:
```bash
python intro.py
```

```bash
python hands_on.py
```


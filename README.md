## Start the server
Run `pip install -r requirement.txt`
Run `bash run_tutorial.sh`
Connect to the website using the URL given in the terminal (look for something like “Starting ASGI/Daphne version 4.2.1 development server at http://localhost:[PORT]/”)

## Add the experiment to the webserver
Go to the admin page on the website
Login using 'admin' as username and 'password' as password
Go the Experiments and add a new experiment with the following information:
* Name `Frozen lake`
* Type `reward`
* Description `Reward-based experiment using the TAMER algorithm.`
* Inputs listened `["ArrowUp", "ArrowDown"]`
* Agent available to play `[["agent_0", "Agent"]]`
* Number of users `1`
* Link `frozen`
* Target FPS `0.8`
* Train `True`
You can now see a new experiment appeared on the home page

## Setup the experiment on the runner
Open the file `runner/experiments/frozen/environment.py` and implement the functions `input_mapping`
Open the file `runner/experiments/frozen/agent.py` and implement the functions `sample`, `predict` and `train`

## Try it
Now you have to train the agent by giving it positive and negative feedback!

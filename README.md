# Python-APP
A pod scanner application that will scan through the pods and return the pods in a designated POD_STATUS. The status would be a parameter to this program, passed in via an environment variable POD_STATUS.  The program would produce a list of all pods in the specified state.

# Installation

Prerequisites
* Python3
* Kubernetes
* Helm

Running the app
1. git clone https://github.com/rowlandr71/Python-APP.git
2. cd Python-APP
3. Ensure that the KubeConfig loads from local. uncomment ```bash config.load_kube_config()``` and comment out ```bash config.load_incluster_config()```
4. Install the dependencies and execute the script.
```bash
pip install Kubernetes
pip install Flask
python3 pod_scanner.py
```
5. Access the a

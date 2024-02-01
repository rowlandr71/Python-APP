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
4. Set the POD_STATUS as environment variables
   ```bash
   export POD_STATUS=Running
   ```
5. Install the dependencies and execute the script.
    ```bash
    pip install Kubernetes
    pip install Flask
    python3 pod_scanner.py
    ```
6. Access the web app over the browser using ```bash http://localhost:5000 ```

# Screenshot 

![alt text](https://github.com/rowlandr71/Python-APP/blob/main/Screenshot%20.png)

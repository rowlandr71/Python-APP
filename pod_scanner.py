import os
from flask import Flask, jsonify
from kubernetes import client, config

app = Flask(__name__)

def get_pods_with_status(api_instance, namespace, pod_status):
    pods = api_instance.list_namespaced_pod(namespace)
    matching_pods = [pod.metadata.name for pod in pods.items if pod.status.phase == pod_status]
    return matching_pods

@app.route("/")
def index():
    # # Load Kubernetes configuration from default location
    # config.load_kube_config()

    # Set the namespace from environment variable or use 'default' as default
    namespace = os.getenv("NAMESPACE", "default")

    # Set the pod status from environment variable or use 'running' as default
    pod_status = os.getenv("POD_STATUS", "Running")

    # Create Kubernetes API client
    api_instance = client.CoreV1Api()

    # Get pods with the specified status
    matching_pods = get_pods_with_status(api_instance, namespace, pod_status)

    # provides a json response
    response_data = {"namespace": namespace, "pod_status": pod_status, "matching_pods": matching_pods}
    return jsonify(response_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
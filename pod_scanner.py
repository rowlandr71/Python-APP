import os
from flask import Flask, render_template
from kubernetes import client, config

app = Flask(__name__)

def get_pods_with_status(api_instance, pod_status, pod_namespace=None):
    pods = api_instance.list_pod_for_all_namespaces(watch=False)
    matching_pods = [pod.metadata.name for pod in pods.items if pod.status.phase == pod_status]
    
    if pod_namespace is not None:
        matching_pods = [pod for pod in matching_pods if pod.metadata.namespace == pod_namespace]
    
    matching_pod_namespaces = {pod.metadata.name: pod.metadata.namespace for pod in pods.items if pod.metadata.name in matching_pods}
    
    return matching_pods, matching_pod_namespaces

@app.route("/")
def index():
    # Load Kubernetes configuration from default location
    config.load_incluster_config()
    # config.load_kube_config()

    # Set the pod status from environment variable or use 'Running' as default
    pod_status = os.getenv("POD_STATUS", "Running")

    # Set the pod namespace from environment variable (optional)
    pod_namespace = os.getenv("POD_NAMESPACE", None)

    # Create Kubernetes API client
    api_instance = client.CoreV1Api()

    # Get pods with the specified status and namespace
    matching_pods, matching_pod_namespaces = get_pods_with_status(api_instance, pod_status, pod_namespace)

    # Render the HTML template
    return render_template("index.html", matching_pods=matching_pod_namespaces)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
from kubernetes import client, config
from alert_manager import send_slack_alert
import json

# Load Kubernetes configuration
config.load_kube_config()

# Create Kubernetes API client
v1 = client.CoreV1Api()

# Fetch all pods from all namespaces
pods = v1.list_pod_for_all_namespaces()

print("\n=== Unhealthy Pods Report ===\n")

unhealthy_pods = []

# Iterate through all pods
for pod in pods.items:

    namespace = pod.metadata.namespace
    pod_name = pod.metadata.name

    if not pod.status.container_statuses:
        continue

    for container in pod.status.container_statuses:

        status = None

        # Waiting state
        if container.state.waiting:
            status = container.state.waiting.reason

        # Terminated state
        elif container.state.terminated:
            status = container.state.terminated.reason

        # Ignore successful completed jobs
        if status and status != "Completed":

            pod_data = {
                "namespace": namespace,
                "pod": pod_name,
                "container": container.name,
                "status": status,
                "restarts": container.restart_count
            }

            unhealthy_pods.append(pod_data)

            print(f"Namespace : {namespace}")
            print(f"Pod       : {pod_name}")
            print(f"Container : {container.name}")
            print(f"Status    : {status}")
            print(f"Restarts  : {container.restart_count}")
            print("-" * 60)

# No unhealthy pods found
if not unhealthy_pods:
    print("No unhealthy pods found.")

# Generate JSON report
with open("reports/unhealthy_pods.json", "w") as file:
    json.dump(unhealthy_pods, file, indent=4)

print("\nJSON report generated:")
print("reports/unhealthy_pods.json")

# Send Slack Alert
if unhealthy_pods:

    message = "🚨 Kubernetes Health Alert\n\n"

    for pod in unhealthy_pods:

        message += (
            f"Namespace: {pod['namespace']}\n"
            f"Pod: {pod['pod']}\n"
            f"Container: {pod['container']}\n"
            f"Status: {pod['status']}\n"
            f"Restarts: {pod['restarts']}\n\n"
        )

    response_code = send_slack_alert(message)

    print(f"\nSlack alert sent. HTTP Status Code: {response_code}")
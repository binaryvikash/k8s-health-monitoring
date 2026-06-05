from kubernetes import client, config

# Load kubeconfig from local machine
config.load_kube_config()

v1 = client.CoreV1Api()

print("\n=== Kubernetes Health Report ===\n")

pods = v1.list_pod_for_all_namespaces()

for pod in pods.items:

    pod_name = pod.metadata.name
    namespace = pod.metadata.namespace
    phase = pod.status.phase

    print(
        f"Namespace: {namespace:<15} "
        f"Pod: {pod_name:<35} "
        f"Phase: {phase}"
    )
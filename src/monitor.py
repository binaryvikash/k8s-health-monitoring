from kubernetes import client, config

config.load_kube_config()

v1 = client.CoreV1Api()

pods = v1.list_pod_for_all_namespaces()

print("\n=== Unhealthy Pods Report ===\n")

unhealthy_found = False

for pod in pods.items:

    namespace = pod.metadata.namespace
    pod_name = pod.metadata.name

    if not pod.status.container_statuses:
        continue

    for container in pod.status.container_statuses:

        if container.state.waiting:
            unhealthy_found = True

            print(f"Namespace : {namespace}")
            print(f"Pod       : {pod_name}")
            print(f"Status    : {container.state.waiting.reason}")
            print("-" * 50)

        elif container.state.terminated:
            unhealthy_found = True

            print(f"Namespace : {namespace}")
            print(f"Pod       : {pod_name}")
            print(f"Status    : {container.state.terminated.reason}")
            print("-" * 50)

if not unhealthy_found:
    print("No unhealthy pods found.")
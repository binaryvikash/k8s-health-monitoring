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

        status = None

        if container.state.waiting:
            status = container.state.waiting.reason

        elif container.state.terminated:
            status = container.state.terminated.reason

        if status and status != "Completed":

            unhealthy_found = True

            print(f"Namespace : {namespace}")
            print(f"Pod       : {pod_name}")
            print(f"Container : {container.name}")
            print(f"Status    : {status}")
            print(f"Restarts  : {container.restart_count}")
            print("-" * 60)

if not unhealthy_found:
    print("No unhealthy pods found.")
# Kubernetes Health Monitoring Utility

A Python-based Kubernetes monitoring utility that connects to a Kubernetes cluster using the Kubernetes Python SDK and identifies unhealthy workloads.

## Features

* Connects to Kubernetes clusters using kubeconfig
* Lists pods across all namespaces
* Displays pod health status
* Detects unhealthy pods
* Foundation for automated alerting and reporting

## Tech Stack

* Python
* Kubernetes
* Docker Desktop Kubernetes
* Kubernetes Python SDK

## Project Structure

```text
k8s-health-monitoring/
│
├── manifests/
│   └── broken-pod.yaml
│
├── src/
│   └── monitor.py
│
├── screenshots/
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Future Enhancements

* Detect CrashLoopBackOff
* Detect ImagePullBackOff
* Slack notifications
* Email alerts
* Docker containerization
* Kubernetes deployment

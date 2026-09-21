# AIOps Hybrid Cloud Infrastructure

A progressive infrastructure project combining virtualization, monitoring,
Infrastructure as Code, cloud infrastructure, and intelligent operations.

## Objective

The goal is to build a small hybrid infrastructure environment starting
from a local virtual machine and progressively extending it to AWS.

The project focuses on:

- Infrastructure and virtualization
- System monitoring and observability
- Infrastructure as Code
- Hybrid cloud infrastructure
- Infrastructure resilience
- Intelligent monitoring and AIOps

## Architecture

The project starts with a local infrastructure:

Windows Host
    ↓
VMware Workstation
    ↓
Vagrant
    ↓
Ubuntu Linux VM
    ↓
Node Exporter
    ↓
Prometheus
    ↓
Grafana

The next phase will connect the local environment with AWS infrastructure:

Local Infrastructure ↔ AWS EC2

## Technologies

- VMware Workstation
- Vagrant
- Ubuntu Linux
- Prometheus
- Node Exporter
- Grafana
- Terraform
- AWS EC2
- Python

## Project Phases

### Phase 1 — Local Infrastructure
- Create an Ubuntu virtual machine with Vagrant
- Configure the virtual environment
- Verify network connectivity

### Phase 2 — Monitoring
- Install Node Exporter
- Collect system metrics with Prometheus
- Visualize metrics with Grafana

### Phase 3 — Cloud Infrastructure
- Provision AWS infrastructure with Terraform
- Create and manage an EC2 instance
- Understand Infrastructure as Code

### Phase 4 — Hybrid Cloud
- Connect the local infrastructure with AWS
- Monitor both environments
- Study infrastructure communication and availability

### Phase 5 — AIOps
- Detect abnormal infrastructure behavior
- Analyze monitoring data
- Identify potential failures
# AIOps Hybrid Cloud Infrastructure

A progressive infrastructure project combining virtualization, monitoring,
Infrastructure as Code, cloud infrastructure, and intelligent operations.

## Objective

The goal is to build a small hybrid infrastructure environment starting
from a local virtual machine and progressively extending it to AWS.

The project focuses on:

- Infrastructure and virtualization
- System monitoring and observability
- Infrastructure as Code
- Hybrid cloud infrastructure
- Infrastructure resilience
- Intelligent monitoring and AIOps

## Architecture

The project starts with a local infrastructure:

Windows Host
    ↓
VMware Workstation
    ↓
Vagrant
    ↓
Ubuntu Linux VM
    ↓
Node Exporter
    ↓
Prometheus
    ↓
Grafana

The next phase will connect the local environment with AWS infrastructure:

Local Infrastructure ↔ AWS EC2

## Technologies

- VMware Workstation
- Vagrant
- Ubuntu Linux
- Prometheus
- Node Exporter
- Grafana
- Terraform
- AWS EC2
- Python

## Project Phases

### Phase 1 — Local Infrastructure
- Create an Ubuntu virtual machine with Vagrant
- Configure the virtual environment
- Verify network connectivity

### Phase 2 — Monitoring
- Install Node Exporter
- Collect system metrics with Prometheus
- Visualize metrics with Grafana

### Phase 3 — Cloud Infrastructure
- Provision AWS infrastructure with Terraform
- Create and manage an EC2 instance
- Understand Infrastructure as Code

### Phase 4 — Hybrid Cloud
- Connect the local infrastructure with AWS
- Monitor both environments
- Study infrastructure communication and availability

### Phase 5 — AIOps
- Detect abnormal infrastructure behavior
- Analyze monitoring data
- Identify potential failures
- Support infrastructure operations with intelligent analysis

## Current Status

Completed:

- Local Ubuntu VM created with Vagrant
- Prometheus Node Exporter installed
- Prometheus configured for monitoring
- Grafana installed
- Monitoring dashboards created

In progress:

- Terraform and AWS EC2
- Hybrid infrastructure architecture

Future:

- Centralized monitoring
- Failure detection
- Anomaly detection
- AIOps capabilities

## Repository Structure

```text
architecture/     Architecture and design
vagrant/          Local virtualization configuration
monitoring/       Prometheus and Grafana configuration
terraform/        Infrastructure as Code
scripts/          Automation scripts
docs/             Project documentation

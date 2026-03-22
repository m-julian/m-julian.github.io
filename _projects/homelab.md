---
layout: page
title: Homelab
description: Homelab setup
img: assets/img/homelab_setup.jpg
importance: 1
category: learning
related_publications: false
---

I've always wanted to learn more about computer networking, as well as running a variety of services such as jellyfin, kubernetes, OPNSense, etc. Recently, I purchased two small form factor PCs to experiment with and learn more.

Hardware:
- HP ProDesk, i5 8500t, 32GB ram
- Lenovo M920q, i5 8500t, 16GB ram, Intel I350-T4 Quad Port RJ45
- Two NVMe drives for containers and VMs
- Two intel enterprise SSDs for proxmox and storage
- Netgear GS308E managed switch

Currently running proxmox on both machines, with the plan to add a third machine for high-availability at some point.

Services:
- jellyfin
- samba
- Ubuntu VM
- k3s Kubernetes cluster
- tailscale
- OPNSense

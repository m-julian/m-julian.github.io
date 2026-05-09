---
layout: post
title: Training a Simple Neural Network Manually
date: 2026-05-09 00:00:01
description: Training a neural network with gradients evaluated manually. Gradients are verified against PyTorch's autograd.
tags: [math, neural-networks, machine-learning, pytorch]
categories: [tutorials]
---

This notebook trains a simple neural network to fit the function $f(\mathbf{x}) = \sin(x_1) + 2\cos(x_2)$ using the equations for backpropagation derived in my previous posts ([1]({% post_url neural_networks/2026-04-26-backpropagation %}), [2]({% post_url neural_networks/2026-05-02-backpropagation-vectorized %})), and verifies the gradients against PyTorch's autograd engine.
{::nomarkdown}
{% jupyter_notebook "/jupyter_notebooks/neural_networks/theory/backpropagation_pytorch.ipynb" %}
{:/nomarkdown}

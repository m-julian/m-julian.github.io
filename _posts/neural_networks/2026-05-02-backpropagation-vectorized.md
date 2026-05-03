---
layout: post
title: Vectorized Forward and Backward Pass in a Simple Neural Network
date: 2026-05-01 00:00:01
description: Vectorized forward and backward passes
tags: [math, neural-networks, machine-learning]
categories: [tutorials]
---

This notebook verctorizes the derivations in my [previous post]({% post_url neural_networks/2026-04-26-backpropagation %}), for a simple neural network. Vecotization significantly boosts performance, since NN calculations are heavily parallel, which is why GPUs are heavily utilized in ML.

{::nomarkdown}
{% jupyter_notebook "/jupyter_notebooks/neural_networks/theory/nn_backpropagation_vectorized.ipynb" %}
{:/nomarkdown}

---
layout: post
title: How to publish a jupyter notebook on Github pages with Jekyll
date: 2024-10-05 14:51:30
description: Contains instructions and information for setting up jupyter notebook support on Github pages websites with Jekyll.
---

# Adding Jupyter Notebook Support to GitHub Pages

Jupyter notebook support is added with the `jekyll-jupyter-notebook` Ruby gem from

```text
https://github.com/red-data-tools/jekyll-jupyter-notebook
```

Install this gem, and then you will be able to add jupyter notebooks to your GitHub pages. To use the extension, make a new Markdown post, and then link to a Jupyter notebook that is contained somewhere else in the source code of the GitHub website.

Linking is done by:

```text
{percentage jupyter_notebook "path_to_notebook.ipynb" percentage}
```
where `percentage` above needs to be replaced by `%`, so that it is proper liquid code. This will insert the Jupyter notebook into the new post.

# Support for Latex Equations Numbering in Jupyter Notebook

So far, the easiest way I have found to insert Latex and being able to reference equations is by following [this StackOverflow comment](https://stackoverflow.com/a/57900511/11699003)

```latex
\begin{equation*}
\mathbf{r} \equiv \begin{bmatrix}
y \\
\theta
\end{bmatrix}
\label{eq:vector_ray} \tag{1}
\end{equation*}

Vector **r** is defined by equation $\eqref{eq:vector_ray}$
```

Note that this only works in Jupyter because it uses MathJax. The VSCode latex rendered uses Katex, so it will note be able to render these properly. Since MathJax is also used for the rendering of the equations in the [al-folio Jekyll theme](https://github.com/alshedivat/al-folio), then it should render the equations fine.
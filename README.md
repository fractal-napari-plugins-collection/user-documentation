# Fractal Analytics Platform / Napari Plugin Collection
## User Documentation

This repository contains the documentation for the napari plugins developed for the Fractal Analytics Platform (https://github.com/fractal-analytics-platform).

The pre-build documentation is available in the following formats:
- [HTML](https://fractal-napari-plugins-collection.github.io/user-documentation/)


### Generate Documentation From Source

The documentation is written in [reStructuredText](https://docutils.sourceforge.io/rst.html) which can be translated into various output formats (e.g. HTML, LaTeX, ...) using [Sphinx](https://www.sphinx-doc.org/).

Prerequisites:
- Python 3.7 or later
- MiKTeX 2.9 or later (optional)

    Note: to generate PDF files a TeX distribution, e.g. [MiKTeX](https://miktex.org/), is required.

Required Python packages:
- Sphinx >= 4.0.0
- sphinx-rtd-theme >= 0.5.2

The HTML documentation can be generated using the following commands:

```
sphinx-build -b html ./src/docs ./docs
```

The PDF documentation can be generated using the following commands:

```
mkdir latex-docs
sphinx-build -b latex ./src/docs ./latex-docs
CD ./latex-docs
pdflatex fap_napari_plugins.tex
pdflatex fap_napari_plugins.tex
```


### GitHub Pages

Given the documentation was build as HTML output and stored in ./docs, it can be directly published as GitHub Pages.
Please refer to the [GitHub Pages documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages) for further details.


### Migration

This documentation can easily be migrated/adapted into other repositories which already hold related source code in ./src.
Following, an example of a common project structure for software with a Sphinx documentation:

```
+ my-repository
  + .github
  | + workflows        # GitHub workflows
  + docs               # pre-compiled documentation
  + src
  | + component-1      # source code for component-1
  | + component-2      # source code for component-2
  | + docs             # source for the documentation
  + tests              # unit tests
  + .gitignore
  + LICENSE
  + README.md
  + ...                # project dependend files, e.g. setup.py or project.sln
```


## Copyright
Copyright (c) 2021, Friedrich Miescher Institute for Biomedical Research & University of Zurich. All rights reserved.
Licensed under BSD 3-Clause - see ./LICENSE

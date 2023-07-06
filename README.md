# Gymnasium environment template
This projects helps scaffolding your own Gymnasium environment.
For more explanation on how to create our own environment, see the [Gymnasium documentation](https://gymnasium.farama.org/tutorials/gymnasium_basics/environment_creation/).

## Setup

### Recommended solution
1. Install `pipx` following the [pipx documentation](https://pypa.github.io/pipx/installation/).
2. Then install Copier:
```{sh}
pipx install copier
```

### Alternative solutions

Install Copier with Pip or Conda:
```{sh}
pip install copier
```
or
```{sh}
conda install -c conda-forge copier
```

## How to generate your environment


You can check that `Copier` has been correctly installed by running the following command, which should output a version number:

```
copier --version
```

Then you can just run the following command and replace the string `path/to/directory` by the path to the directory where you want to create your new project.

```
copier https://github.com/Farama-Foundation/gymnasium-env-template.git "path/to/directory"
```

Answer the questions, and when it's finished you should get a project structure 🌳 like the following:

```
.
├── LICENSE
├── README.md
├── environment.yml
├── .gitlab-ci.yml
├── .flake8
├── .gitignore
├── config/
├── data/
├── docs/
├── notebooks/
├── src/
└── tests/
```

## Contributing
If you would like to contribute, follow these steps:
- Fork this repository
- Clone your fork
- Set up pre-commit via `pre-commit install`
- Check you files manually with `pre-commit run -a`

PRs may require accompanying PRs in [the documentation repo](https://github.com/Farama-Foundation/Gymnasium/tree/main/docs).


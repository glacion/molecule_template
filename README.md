# Molecule Template

A template for using [molecule](https://ansible.readthedocs.io/projects/molecule/)
to develop ansible roles. To be an example, this role installs itself.

## Features

- GitHub [Actions](https://github.com/features/actions)
  workflow for testing and releasing to ansible galaxy
- [pre-commit](https://pre-commit.com) configuration for linting project files
  - ansible:
    [ansible-lint](https://ansible.readthedocs.io/projects/lint) linting,
    [yamlfix](https://lyz-code.github.io/yamlfix/) formatting
  - jinja:
    [jinjalint](https://github.com/motet-a/jinjalint) linting
  - markdown:
    [pymarkdown](https://github.com/jackdewinter/pymarkdown) linting
  - python:
    [flake8](https://flake8.pycqa.org/en/latest) linting,
    [black](https://github.com/psf/black) formatting
- [molecule-qemu](https://github.com/andreygubarev/molecule-qemu)
  configured for testing with x86_64 and aarch64 platforms.
  This example uses my [fork](https://github.com/glacion/molecule-qemu) with added features.
  See these for configuring the VMs for molecule.
- [pytest-testinfra](https://github.com/pytest-dev/pytest-testinfra)
  for testing state with python.

## Requirements

- python3
- qemu-system-x86_64, qemu-system-aarch64, mkisofs, qemu-img for running molecule instances,
  see [molecule-qemu](https://github.com/andreygubarev/molecule-qemu) for details.
  Additionally see [workflow](.github/workflows/release.yml) for setting up for ubuntu 22.04.

## Setting up

Replace `my_role` with your desired role name and `my_username` with your GitHub username.

- Retrieve this repository(or fork it)

  ```bash
  curl -LO https://github.com/glacion/molecule_template/archive/refs/heads/main.tar.gz
  tar -xvf main.tar.gz --strip-components=1 --one-top-level=my_role
  ```

- Initialize git, python, and pre-commit

  ```bash
  git init
  python3 -m venv .venv
  source .venv/bin/activate
  pip install .
  pre-commit install
  ```

- Make necessary metadata changes

  - Author information in [README](./README.md), galaxy [metadata](./meta/main.yml)
  - `namespace` field in galaxy [metadata](./meta/main.yml) to your github username.
  - `include_role` in converge [playbook](./molecule/default/converge.yml) playbook
    as `my_username/my_role`

- Run a full cycle of molecule

  ```bash
  molecule test
  ```

- Create a repository on GitHub
- Retrieve your API key from [galaxy](https://galaxy.ansible.com/me/preferences)
- Save this API key as a Repository secret in your repository under the name of `GALAXY_API_KEY`
  [settings](https://docs.github.com/en/actions/security-guides/encrypted-secrets)

- Push your repository

  ```bash
  git add .
  git commit -m 'initial commit'
  git tag 0.0.0
  git remote add origin git@github.com/my_username/my_role
  git push -u origin main --tags
  ```

If everything is set up correctly, GitHub Actions will run tests and publish your role to galaxy.
In order to release a new version, create a new tag like `git tag 0.1.0` and push with `git push --tags`.
This will additionally create a new release in GitHub with the changes from the previous tag,
consider using [conventional commits](https://www.conventionalcommits.org/en/v1.0.0) for a better changelog.

## License

BSD

## Author Information

Can Güvendiren <can@glacion.com>

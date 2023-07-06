from pathlib import Path
import shutil
import importlib
import pip
import os

from copier import run_copy
import yaml
import toml
import gymnasium

ROOT_LOC = Path(__file__).resolve().parent
TEMPLATE_LOC = ROOT_LOC.joinpath("template-test")
COPIER_FILE = ROOT_LOC.joinpath("copier.yml")


def get_yaml_dict(yaml_file):
    with open(yaml_file) as fid:
        copier_vars = yaml.safe_load(fid)
    return copier_vars


class GenerateTemplate:
    def __enter__(self):
        copier_vars = get_yaml_dict(COPIER_FILE)
        template_vars = {
            "environment_name": copier_vars.get("environment_name").get("default"),
        }

        # Generate a template
        run_copy(
            src_path=str(ROOT_LOC),
            dst_path=str(TEMPLATE_LOC),
            data=template_vars,
            cleanup_on_error=True,
        )

    def __exit__(self, exc_type, exc_value, traceback):
        # Remove the template
        shutil.rmtree(TEMPLATE_LOC)


def test_template_copy():
    with GenerateTemplate():
        path_list_to_check = [
            TEMPLATE_LOC.joinpath("src"),
            TEMPLATE_LOC.joinpath("LICENSE"),
            TEMPLATE_LOC.joinpath("README.md"),
            TEMPLATE_LOC.joinpath("pyproject.toml"),
        ]
        for item in path_list_to_check:
            assert Path.exists(item)


def test_Readme_templating():
    with GenerateTemplate():
        Readme_loc = TEMPLATE_LOC.joinpath("README.md")
        with open(Readme_loc, "r") as fid:
            file_content = fid.read()
        copier_vars = get_yaml_dict(COPIER_FILE)
        env_name = copier_vars.get("environment_name").get("default")
        assert f"cd {env_name}" in file_content


def test_pyproject_templating():
    with GenerateTemplate():
        environment_loc = TEMPLATE_LOC.joinpath("pyproject.toml")
        env_vars = toml.load(environment_loc)
        copier_vars = get_yaml_dict(COPIER_FILE)
        env_name = copier_vars.get("environment_name").get("default")
        assert env_vars.get("project").get("name") == str(env_name)


def test_run_env():
    with GenerateTemplate():
        environment_loc = TEMPLATE_LOC.joinpath("pyproject.toml")
        env_vars = toml.load(environment_loc)
        env_name = env_vars.get("project").get("name")

        os.chdir(TEMPLATE_LOC)
        pip.main(["uninstall", env_name, "-y"])
        pip.main(["install", "-e", "."])
        importlib.import_module(env_name)  # , package=None)
        from gymnasium.wrappers import FlattenObservation

        env = gymnasium.make("{env_name}/GridWorld-v0")
        wrapped_env = FlattenObservation(env)
        assert wrapped_env.reset() == ([3, 0, 3, 3], {})
        pip.main(["uninstall", env_name, "-y"])

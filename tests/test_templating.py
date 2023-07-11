import toml  # type: ignore
from pathlib import Path

from utils import GenerateTemplate, TEMPLATE_LOC, COPIER_FILE, get_yaml_dict


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

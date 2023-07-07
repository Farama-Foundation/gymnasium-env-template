import importlib
import pip
import os
from test_templating import GenerateTemplate, TEMPLATE_LOC

import toml
import gymnasium


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

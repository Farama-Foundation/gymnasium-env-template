import yaml  # type: ignore
from pathlib import Path
from copier import run_copy
import shutil

ROOT_LOC = Path(__file__).resolve().parent.parent
TEMPLATE_LOC = ROOT_LOC.joinpath("template-test")
COPIER_FILE = ROOT_LOC.joinpath("copier.yml")


def get_yaml_dict(yaml_file):
    with open(yaml_file) as fid:
        copier_vars = yaml.safe_load(fid)
    return copier_vars


class GenerateTemplate:
    def __init__(self, project_license="None"):
        self.project_license = project_license

    def __enter__(self):
        copier_vars = get_yaml_dict(COPIER_FILE)
        template_vars = {
            "environment_name": copier_vars.get("environment_name").get("default"),
            "project_license": self.project_license,
        }

        # Generate a template
        run_copy(
            src_path=str(ROOT_LOC),
            dst_path=str(TEMPLATE_LOC),
            data=template_vars,
            cleanup_on_error=True,
            # defaults=True,
        )

    def __exit__(self, exc_type, exc_value, traceback):
        # Remove the template
        shutil.rmtree(TEMPLATE_LOC)

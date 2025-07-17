import subprocess
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def run_command(*cmd_args, **cmd_kwargs):
    try:
        return subprocess.check_output(*cmd_args, **cmd_kwargs).decode("utf-8")
    except subprocess.CalledProcessError as e:
        print(e.returncode)
        print(e.output.decode("utf-8"))
        raise

def go_mod_init():
    print("Running go mod init...")
    module_name = "{{ cookiecutter.go_module }}"
    run_command(
        f"cd {PROJECT_DIRECTORY} && go mod init {module_name}",
        stderr=subprocess.STDOUT,
        shell=True,
    )

def go_mod_tidy():
    """Run 'go mod tidy' to generate go.mod imports and go.sum file"""
    print("Running go mod tidy...")
    run_command(
        f"cd {PROJECT_DIRECTORY} && go mod tidy",
        stderr=subprocess.STDOUT,
        shell=True,
    )

def mise_trust():
    print("Running mise trust...")
    run_command(
        f"cd {PROJECT_DIRECTORY} && mise trust",
        stderr=subprocess.STDOUT,
        shell=True,
    )

def mise_install():
    """Run 'mise install' to install dependencies"""
    print("Running mise install...")
    run_command(
        f"cd {PROJECT_DIRECTORY} && mise install",
        stderr=subprocess.STDOUT,
        shell=True,
    )

def main():
    mise_trust()
    mise_install()
    go_mod_init()
    go_mod_tidy()


if __name__ == "__main__":
    main()

from engine.core import Version, Config
from engine.shell.core import Say

def main():
    Say(f"Running {Config.name} Server v{Version.Release}")
    Say("(c) Gugu Software - 2024")
    Say("Addons:")
    for k, v in Version.Using.items():
        Say(f"- {k}@{v}")
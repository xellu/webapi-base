from engine.shell.core import Say, Shell

def main(command=None):
    if command:
        for cmd in Shell.commands:
            if cmd.command == command.lower():
                cmd_args = cmd.command
                for arg in cmd.args:
                    cmd_args += f" <{arg.name}>" if arg.require else f" [{arg.name}]"
                
                Say(f"Showing help for {cmd.command}")
                Say(f"Usage: {cmd_args}")
                Say(f"- {cmd.description}")
                
    else:
        Say(f"Available commands ({len(Shell.commands)}):")
        Say(f"Use 'help <command>' to show help for a specific command")
        
        for cmd in Shell.commands:
            cmd_args = cmd.command
            for arg in cmd.args:
                cmd_args += f" <{arg.name}>" if arg.require else f" [{arg.name}]"
            
            Say(f" {cmd_args} -> {cmd.description}")
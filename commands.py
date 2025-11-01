from movement_system import handle_go
from item_system import get_item



COMMANDS = {
    "go" : handle_go,
    "get" : get_item,
    "take" : get_item,
}

def process_cmd(cmd_text, game):
    for cmd_name, handler in COMMANDS.items():
        if cmd_text.startswith(cmd_name):
            return handler(cmd_text, game)
    return "Unknown command"
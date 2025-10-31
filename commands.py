
def handle_go(cmd,game):
    parts = cmd.split()
    if len(parts) < 2:
        return "Go where?"
    direction = parts[1].lower()
    area_index = game["current_area"]
    print(area_index)
    current_area = game["areas"][area_index]
    if direction in current_area["exits"]:
        game["previous_area"] = game["current_area"]
        game["current_area"] = current_area["exits"][direction]
        return f"You go {direction} to {game['current_area']}"
    else:
        return f"You can't go {direction}"


COMMANDS = {
    "go" : handle_go,
}

def process_cmd(cmd_text, game):
    for cmd_name, handler in COMMANDS.items():
        if cmd_text.startswith(cmd_name):
            return handler(cmd_text, game)
    return "Unknown command"
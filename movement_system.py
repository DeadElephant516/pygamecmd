
def handle_go(cmd,game):
    parts = cmd.split()
    if len(parts) < 2:
        return "Go where?"
    direction = parts[1].lower()
    area_data = game["current_area"]

    current_area = game["areas"][area_data]
    if direction in current_area["exits"]:
        game["previous_area"] = game["current_area"]
        game["current_area"] = current_area["exits"][direction]
        return f"You go {direction} to {game['current_area']}"
    else:
        return f"You can't go {direction}"
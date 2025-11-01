
def get_item(cmd,game):
        parts = cmd.split()
        if len(parts) < 2:
            return "Get What?" if parts[0].lower() == "get" else "Take what?"

        item_name = "_".join(parts[1:]).lower()
        area_data = game["current_area"]
        current_area = game["areas"][area_data]

        if item_name in current_area["items"]:
            inv = game["inventory"]
            inv.append(item_name)
            current_area["items"].remove(item_name)
            return f"You picked up {item_name}"
        else:
            return "There is nothing like that here"
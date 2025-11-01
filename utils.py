
def show_nearby_items(game):
    area_data = game["current_area"]
    current_area = game["areas"][area_data]
    items = current_area["items"]
    if items:
        pretty_items = [item.replace("_", " ") for item in items]
        return f"Items: {', '.join(pretty_items)}"
    else:
        return "No items here"


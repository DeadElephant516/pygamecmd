
def show_nearby_items(game):
    area_data = game["current_area"]
    current_area = game["areas"][area_data]
    items = current_area["items"]
    if items:
        item_name_format = [item.replace("_", " ") for item in items]
        return f"Items: {', '.join(item_name_format)}"
    else:
        return "No items here"

def display_inv(cmd,game):
    inv = game["inventory"]
    inv_format = [i.replace("_"," ") for i in inv]
    return f"Inventory: {', '.join(inv_format)}"
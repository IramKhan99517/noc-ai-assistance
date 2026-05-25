
def get_section(section_name):
    with open("SOP_data.txt", "r") as file:
        data = file.read()

    start = data.find(f"[{section_name}]")
    if start == -1:
        return "SOP section not found."

    end = data.find("[", start + 1)
    if end == -1:
        return data[start:]

    return data[start:end]



def mock_ai_engine(question):
    q = question.lower()

    if "pos" in q:
        return get_section("POS_DOWN")

    elif "network" in q or "offline" in q:
        return get_section("Store_Network_Down")

    elif "setup" in q or "go-live" in q:
        return get_section("Store_Setup")

    return "No SOP matched. Please try POS, Network, or Setup keywords."


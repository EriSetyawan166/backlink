with open("blogspot_links.txt", "r") as file:
    lines = file.readlines()

with open("preprocessed_links.txt", "w") as file:
    for line in lines:
        if "translate" not in line and "webcache" not in line:
            file.write(line)

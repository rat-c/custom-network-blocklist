def remove_duplicates(file_path):
    lines_seen = set()
    with open(file_path, "r") as file:
        lines = file.readlines()
    with open(file_path, "w") as file:
        for line in lines:
            if line not in lines_seen:
                file.write(line)
                lines_seen.add(line)

file_path = "blocklist.txt"
remove_duplicates(file_path)

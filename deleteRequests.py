

# create a function
def delete():
    file_path = "C:/Users/Jeremiah/OneDrive/Documents/CODE/TwitchMarkov/jbooogieLogs.txt"

    with open(file_path, "r", encoding="latin-1") as f:
        lines = f.readlines()

    with open(file_path, "w", encoding="latin-1") as f:
        for line in lines:
            if "has been added to the queue" not in line:
                f.write(line)


delete()

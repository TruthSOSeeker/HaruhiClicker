def save_game(stored_score, clicker_bought_status, clicker_level_status):
    with open("game_save.txt", "w") as file:
        file.write(f"{stored_score}\n")
        file.write(f"{clicker_bought_status}\n")
        file.write(f"{clicker_level_status}\n")
    print(f"Score: {stored_score}, Clicker bought: {clicker_bought_status}, Clicker Level: {clicker_level_status}")
def load_game():
    try:
        with open("game_save.txt", "r") as file:
            lines = file.readlines()
            stored_score = int(lines[0])
            clicker_bought_status = lines[1].strip() == "True"
            clicker_level_status = int(lines[2])
        load_check = True
        print("hi") #I added this to check if the code was being run. I did see "hi" printed on the terminal, so this code is running.
        return stored_score, clicker_bought_status, clicker_level_status,load_check

    except FileNotFoundError:
        print("File not found")
        load_check = False
        return None, None, None, load_check
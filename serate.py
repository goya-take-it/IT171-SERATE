annie = 0
ruth = 0
treasure_x = 5
treasure_y = 3
game_running = True

print(f"Find the treasure at ({treasure_x}, {treasure_y})!")

while game_running:
    move = input("Enter move (up/down/left/right): ").lower()

# update player based on move
    if move == "up" or move == "w":
        ruth += 1
    elif move == "down" or move == "s":
        ruth -= 1
    elif move == "left" or move == "a":
        annie -= 1
    elif move == "right" or move == "d":
        annie += 1
    elif move == "quit" or move == "q":
        print("Game exited.")
        break
    else:
        print("Oop- invalid move! \nYou can also use (w/a/s/d) keys. Try again ^^")
        continue

    print(f"Player position: ({player_x}, {player_y})")

    # check if player has reached the treasure
    if annie == treasure_x and ruth == treasure_y:
        print("You found the treasure! You win!")
        game_running = False
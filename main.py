from env import environment

def main():
    game = environment((500, 500), 20)

    # main game loop:
    while True:
        game.game_step()

main()

# issues/additions:
# fruit spawns inside of snake sometimes
# add a grid to the background
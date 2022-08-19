green_duration = int(input())
free_window_duration = int(input())
command = input()
END_COMMAND = 'END'
GREEN_COMMAND = 'green'
total_cars_passed = []

while True:
    command = input()
    if command == END_COMMAND:
        if len(command) >= green_duration:
            total_cars_passed.append(command)
        print("Everyone is safe.")
        print(f"{len(total_cars_passed)} total cars passed the crossroads.")
        break


#
    # else:
    #     if command == END_COMMAND:
    #
##########################
##########################
##########################

            # print("A crash happened!")
            # print(f"{car} was hit at {character_hit}.")

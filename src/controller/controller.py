import time


def stopwatch():
    while True:
        command = input("Start, stop, reset, or quit: \n")
        if (command == "start"):
            start = time.time()
            print(start)
        elif (command == "stop"):
            total = round(time.time() - start)
            print(total)
            stopwatch()
        elif (command == "reset'"):
            stopwatch()
        elif (command == "quit"):
            break
        else:
            break


stopwatch()




import os
import time

PROGRAM_VERSION = "1.0.0"

def main():
    printout = "Installed version = "+PROGRAM_VERSION
    print(printout)

    timestamp = time.strftime("%Y-%m-%d %H%M%S")
    filename = "logs/"+timestamp+".txt"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write(printout)

if __name__ == "__main__":
    main()
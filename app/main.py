import json

from system import get_system_info


def main():

    system_info = get_system_info()

    with open("data/system.json", "w") as file:
        json.dump(system_info, file, indent=4)
        file.write("\n")

    print(system_info)

if __name__ == "__main__":
    main()

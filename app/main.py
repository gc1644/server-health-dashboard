import json

from system import (
    get_hostname,
    get_os,
    get_kernel,
    get_cpu_usage,
    get_memory_usage,
    get_disk_usage,
)


def main():

    system_info = {
        "system": {
            "hostname": get_hostname(),
            "os": get_os(),
            "kernel": get_kernel(),
        },
        "usage": {
            "cpu": get_cpu_usage(),
            "memory": get_memory_usage(),
            "disk": get_disk_usage(),
        },
    }

    with open("data/system.json", "w") as file:
        json.dump(system_info, file, indent=4)
        file.write("\n")

    print(system_info)

if __name__ == "__main__":
    main()

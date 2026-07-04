from system import ( 
    get_hostname,
    get_os,
    get_kernel,
    get_cpu_usage,
    get_memory_usage,
    get_disk_usage,
)

def main():
    hostname = get_hostname()
    print(f"Hostname: {hostname}")

    os_name = get_os()
    print(f"OS: {os_name}")

    kernel = get_kernel()
    print(f"Kernel: {kernel}")

    cpu_usage = get_cpu_usage()
    print(f"CPU: {cpu_usage}%")

    memory_usage = get_memory_usage()
    print(f"Memory: {memory_usage}%")

    disk_usage = get_disk_usage()
    print(f"Disk: {disk_usage}%")

if __name__ == "__main__":
    main()

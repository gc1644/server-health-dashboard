from system import get_hostname, get_os, get_kernel

def main():
    hostname = get_hostname()
    print(f"Hostname: {hostname}")

    os_name = get_os()
    print(f"OS: {os_name}")

    kernel = get_kernel()
    print(f"Kernel: {kernel}")

if __name__== "__main__":
    main()

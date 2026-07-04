import platform
import psutil

def get_hostname():
    return platform.node()

def get_os():
    return platform.system()

def get_kernel():
    return platform.release()

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    return psutil.virtual_memory().percent

def get_disk_usage():
    return psutil.disk_usage("/").percent

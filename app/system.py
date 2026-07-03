import platform

def get_hostname():
    return platform.node()

def get_os():
    return platform.system()

def get_kernel():
    return platform.release()

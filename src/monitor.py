import platform
import subprocess
import time


def ping_host(host="8.8.8.8"):
    """"Ping host once and returns reponse time in ms, or return None if unable"""
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]

    try:
        start_time = time.time()
        output = subprocess.run(command, capture_output = True, check = False)
        duration = round((time.time() - start_time) * 1000, 2)

        if output.returncode == 0:
            return duration
        return None
    except (FileNotFoundError, OSError) as e:
        print(f"Error pinging host: {e}")
        return None

if __name__ == "__main__":
    print("Testing...")
    latency = ping_host("8.8.8.8")
    if latency:
        print(f"Ping successful, latency: {latency} ms")
    else:
        print("Ping unsuccessful. Host unreachable.")
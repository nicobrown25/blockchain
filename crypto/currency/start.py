import subprocess
import time


def start_scripts():
    try:
        process1 = subprocess.Popen(
            ["python", "./node_controller_gui.py"])
        process2 = subprocess.Popen(
            ["python", "./wallet_gui.py"])
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        process1.terminate()
        process2.terminate()


if __name__ == "__main__":
    start_scripts()

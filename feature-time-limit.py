import signal

def timeout_handler(signum, frame):
    raise TimeoutError

signal.signal(signal.SIGALRM, timeout_handler)

try:
    signal.alarm(10)  # 10 second limit
    row = int(input("Enter row: "))
    signal.alarm(0)
except TimeoutError:
    print("Too slow! Turn skipped.")

import threading
import time

# Initialize semaphores
a = threading.Semaphore(1)  # Allow Process 1 to start
b = threading.Semaphore(0)  # Block Process 2 initially
c = threading.Semaphore(0)  # Block Process 3 initially

def process1():
    a.acquire()
    print("H", end="", flush=True)
    time.sleep(0.5)
    
    print("E", end="", flush=True)
    time.sleep(0.5)

    b.release()  # Signal Process 2 to run first L

def process2():
    b.acquire()
    print("L", end="", flush=True)
    time.sleep(0.5)

    b.release()  # Signal itself to run second L
    b.acquire()

    print("L", end="", flush=True)
    time.sleep(0.5)

    c.release()  # Signal Process 3

def process3():
    c.acquire()
    print("O", end="\n", flush=True)  # Print "O" and move to a new line
    time.sleep(1)

    a.release()  # Restart the cycle

# Create and start threads
t1 = threading.Thread(target=process1)
t2 = threading.Thread(target=process2)
t3 = threading.Thread(target=process3)

t1.start()
t2.start()
t3.start()

# Wait for threads to complete
t1.join()
t2.join()
t3.join()

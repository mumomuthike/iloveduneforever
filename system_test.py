# system_test.py

import json
import threading
import time
import random
from datetime import datetime
from urllib.request import urlopen


# -------------------------------
# Utility Functions
# -------------------------------
def log(message):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")


def read_write_file_test():
    log("Running file I/O test...")
    data = {
        "name": "Faith",
        "role": "Software Engineer",
        "skills": ["Python", "SQL", "Flutter"]
    }

    # Write to file
    with open("test_data.json", "w") as f:
        json.dump(data, f, indent=4)

    # Read from file
    with open("test_data.json", "r") as f:
        loaded = json.load(f)

    log(f"Loaded data: {loaded}")


# -------------------------------
# Class Test
# -------------------------------
class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

    def random_operation(self, a, b):
        op = random.choice(["add", "multiply"])
        if op == "add":
            return self.add(a, b)
        return self.multiply(a, b)


# -------------------------------
# API Test (no Flask)
# -------------------------------
def api_test():
    log("Running API test (public API)...")
    try:
        response = urlopen("https://api.github.com")
        data = json.loads(response.read())

        log(f"GitHub API status: {response.status}")
        log(f"Current user URL: {data.get('current_user_url')}")
    except Exception as e:
        log(f"API test failed: {e}")


# -------------------------------
# Threading Test
# -------------------------------
def worker(name):
    for i in range(3):
        log(f"{name} working... {i}")
        time.sleep(1)


def threading_test():
    log("Running threading test...")
    t1 = threading.Thread(target=worker, args=("Thread-1",))
    t2 = threading.Thread(target=worker, args=("Thread-2",))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    log("Threads completed.")


# -------------------------------
# Performance Test
# -------------------------------
def performance_test():
    log("Running performance test...")
    start = time.time()

    total = sum(i * i for i in range(1_000_000))

    end = time.time()
    log(f"Computed sum: {total}")
    log(f"Time taken: {end - start:.4f} seconds")


# -------------------------------
# Main Runner
# -------------------------------
def main():
    log("Starting system test...\n")

    # File test
    read_write_file_test()

    # Class test
    log("Running class test...")
    calc = Calculator()
    log(f"5 + 10 = {calc.add(5, 10)}")
    log(f"6 * 7 = {calc.multiply(6, 7)}")
    log(f"Random op (3, 4): {calc.random_operation(3, 4)}")

    # API test
    api_test()

    # Threading
    threading_test()

    # Performance
    performance_test()

    log("\nAll tests completed successfully!")


if __name__ == "__main__":
    main()
# test_script.py

def greet(name):
    return f"Hello, {name}! Your Python environment is working."

def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    print(greet("Faith"))
    
    result = add_numbers(5, 7)
    print(f"5 + 7 = {result}")
    
    # Simple loop test
    print("Counting from 1 to 5:")
    for i in range(1, 6):
        print(i)
# Import the Add function, and assert that it works correctly.
from main import Add

def TestAdd():
        assert Add(4,6) == 10
        print("Add operation successful.")

if __name__ == '__main__':
        TestAdd()
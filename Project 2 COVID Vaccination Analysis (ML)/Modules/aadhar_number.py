# Column 1 : Aadhar Number Generation
import random

def Aadhar_Number():
    """Generates a random 12-digit Aadhar-like number as a string."""
    return "".join([str(random.randint(0, 9)) for _ in range(12)])

if __name__ == '__main__':
    print(Aadhar_Number())
        
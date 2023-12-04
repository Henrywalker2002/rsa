import time
from rsa import RSA

def time_measure_decorator(func):
    # write code can measure time here
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("time measure: ", end - start)
    return wrapper
    
@time_measure_decorator
def main():
    rsa = RSA()
    byte = rsa.encode("hello world")
    text = rsa.decode(byte)
    

if __name__ == "__main__":
    main()
    
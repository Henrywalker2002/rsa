import time
from rsa import RSA

def time_measure_decorator(func):
    # write code can measure time here
    def wrapper(*args, **kwargs):
        start = time.time() * 1000
        func(*args, **kwargs)
        end = time.time()* 1000
        print(f"Thời gian chạy: {end - start} miliseconds")
    return wrapper
    
@time_measure_decorator
def main():
    rsa = RSA(1024)
    message = "Do Not Abuse The Dead, For They Have Reached The Result Of What They Have Done"
    byte = rsa.encode(message)
    text = rsa.decode(byte)
    if(text == message):
        print("Giải mã thành công.")
    else:
        print("Lỗi trong quá trình giải mã.")
    

if __name__ == "__main__":
    main()
    
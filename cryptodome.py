from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import time
# Tạo khóa RSA
key = RSA.generate(1024)

# Đo thời gian tạo khóa
start_time = time.time() * 1000
public_key = key.publickey()

# Chuỗi cần mã hóa
message = b"Do Not Abuse The Dead, For They Have Reached The Result Of What They Have Done"

# Mã hóa
cipher = PKCS1_OAEP.new(public_key)
encrypted_message = cipher.encrypt(message)

decipher = PKCS1_OAEP.new(key)
decrypted_message = decipher.decrypt(encrypted_message)
end_time = time.time() * 1000
print(f"Thời gian chạy: {end_time - start_time} miliseconds")

# Kiểm tra kết quả
if message == decrypted_message:
    print("Giải mã thành công.")
else:
    print("Lỗi trong quá trình giải mã.")

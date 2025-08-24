username = input("ป้อนขื่อผู้ใช้ : ")
password = input("ป้อนรหัสผ่าน : ")

# !! and
if username == "admin" and password == "12345678":
    pass
    print("เข้าสู่ระบบสำเร็จ")
else:
    
    print("ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")

# !! not
# if not username == "admin":
#     print("ชื่อผู้ใช้ไม่ถูกต้อง")
# else:
#     print("เข้าสู่ระบบสำเร็จ")



# !! or
# if username == "admin" or password == "12345678":
#     print("รหัสผ่านไม่ถูกต้อง")
# else:
#     print("เข้าสู่ระบบสำเร็จ")
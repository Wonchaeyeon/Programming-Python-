f=open("data.bin","wb")

byte_arr = bytes([255,0,127])  # RGB컬러 값
f.write(byte_arr)

f.close()
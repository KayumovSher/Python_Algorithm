byte = int(input("Faylning hajmi (byte) larda berilgan -> "))

k_byte = byte // 1024
q_byte = byte % 1024

print("Kiritilgan hajm byte = {}, kilobyte = {}, qoldiq byte = {}".format(byte,k_byte,q_byte))
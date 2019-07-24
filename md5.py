import md5

data = input("Masukkan kata : ")
enkripsiData = md5.new(data).hexdigest()

print(enkripsiData)
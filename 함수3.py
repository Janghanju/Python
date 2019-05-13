
신호등 = input("녹색등인가? YES or NO : ")

while 신호등 != "YES":
    print("기다린다")
    신호등 = input("녹색등인가? YES or NO :")
    if 신호등 == "YES":
        break
    
print("건넌다")

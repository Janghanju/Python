input_id = input("아이디를 입력하세요. \n")

members = ["a", "b", "c", "d", "e", "f"]   #real_egoing = "egoing"
                                           #real_k8805 = "k8805"

for member in members:
    if member == input_id:
        print("Hello!, "+member)
        import sys
        sys.exit()

print("Who are you?")

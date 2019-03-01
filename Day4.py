value=[0,"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
list = ["apples", "Bananas", "batman"]
def get_reciept(list):
    total = 0
    list = [s.lower() for s in list]
    for item in list:
        word_total=0
        for letter in item:
            word_total += value.index(letter)
        print(item , word_total)
        total += word_total
    print("total =",total)
get_reciept(list)

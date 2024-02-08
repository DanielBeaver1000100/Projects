def spin(array=[],num=2):
    holder=""
    for i in range(num-1):
        holder=array[0]
        array.pop(0)
        array.append(holder)
    return array
def main():
    I=["E","K","M","F","L","G","D","Q","V","Z","N","T","O","W","Y","H","X","U","S","P","A","I","B","R","C","J"]
    print(I)
    I=spin(I,2)
    print()
    print(I)


main()
    
    

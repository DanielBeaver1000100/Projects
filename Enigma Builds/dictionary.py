def main():
    dic={"HI":"HELLO"}
    print(dic['HI'])
    try:
        dic["HI"]
    except:
        print("Not a Key")
    else:
        print("Key")
    key=str(input('Enter the  letter for the plug: ')).strip().upper()
    val=str(input('Enter the connecting letter to the plug: ')).strip().upper()
    dic.update({key:val})
    dic.update({val:key})
    
    key=str(input('Enter the  letter for the plug: ')).strip().upper()
    try:
        dic[key]
    except:
        print("key")
    else:
        print("Not a valid")
    val=str(input('Enter the connecting letter to the plug: ')).strip().upper()
    
    try:
        dic[val]
    except:
        print("key")
    else:
        print("Not a valid")

    
main()
    

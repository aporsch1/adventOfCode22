def main():
    with open("day6.txt", "r") as f:
        transmission = string(f.readlines())
    for i in range(len(transmission)-1):
        substring = transmission[i:i+14]
        if(len(set(substring))==14):
            print(i+14)
            break    
main()

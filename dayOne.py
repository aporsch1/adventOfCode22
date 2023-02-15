def main():
    with open("Calories.txt","r") as f:
        lines = f.readlines()
        calories = [entry.strip() for entry in lines]
    elf_sums=[]
    current_sum = 0
    for entry in calories:
         if entry != '':
             current_sum += int(entry)
         elif entry == '':
             elf_sums.append(current_sum)
             current_sum = 0
    elf_sums.append(current_sum)
    max_cals = max(elf_sums)
    print(max_cals)
    elf_sums.sort(reverse=True)
    print(elf_sums[0]+elf_sums[1]+elf_sums[2])
main()







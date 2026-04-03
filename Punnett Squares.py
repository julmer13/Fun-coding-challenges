#def things
def generate_matrix(First_allele_list, Second_allele_list):
    matrix = []
    for side_allele in First_allele_list:
        row = []
        for top_allele in Second_allele_list:

            if side_allele.isupper() or not top_allele.isupper():
                row.append("  " + side_allele + top_allele + "  ")
            else:
                row.append("  " + top_allele + side_allele + "  ")

        matrix.append(row)    
    
    return matrix

def add_box(matrix, number_of_alleles):
    new_matrix = list(matrix)

    for i in range(0, len(matrix), 1):
        new_matrix.insert(i * 4, [(make_colors("  ", "white")) * ((number_of_alleles * 4) - 1)])
        new_matrix.insert((i * 4) + 1, ["      "] * (number_of_alleles))
        new_matrix.insert((i * 4) + 3, ["      "] * (number_of_alleles))

    new_matrix.append([(make_colors("  ", "white")) * ((number_of_alleles * 4) - 1)])

    for square in new_matrix:
        square.append(" ")
        square.insert(0, " ")

    return new_matrix

def calculate_probabilities(matrix):

    flat_list = [genotype.strip() for row in matrix for genotype in row]
    total = len(flat_list)

    counts = {}
    for g in flat_list:
        counts[g] = counts.get(g, 0) + 1

    sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)

    print(end="\n")
    for g, count in sorted_counts:
        percentage = (count / total) * 100
        print(f"{g}: {count}/{total} ({percentage:.1f}%)")


def make_colors(text, color):
    colors = { 
        "white":"\33[47m",
        "reset": "\033[0m",
    }
    return f"{colors[color]}{text}{colors['reset']}"

print("\033c", end="")

try:
    while True:
        
        both_allele = input("Enter the letters for the alleles split by spaces (i.e. HH Hh): ").split(" ")

        First_allele_list = list(both_allele[0])
        Second_allele_list = list(both_allele[1])

        matrix = generate_matrix(First_allele_list, Second_allele_list)

        matrix = add_box(matrix, len(Second_allele_list))

        row = ["       "]
        for element in Second_allele_list:
            row.append(element)
            row.append("       ")

        print("\033c", end="")

        print("".join(row))

        for gene in range(len(matrix)):
            if (gene - 2) % 4 == 0:
                index = (gene - 2) // 4

                if index < len(First_allele_list):
                    allele = First_allele_list[index]
                    print(f"{allele} {(make_colors('  ', 'white')).join(matrix[gene])}")
                
                else:
                    print(f"  {(make_colors('  ', 'white')).join(matrix[gene])}")

            else:
                print(f"  {(make_colors('  ', 'white')).join(matrix[gene])}")
        
        raw_matrix = generate_matrix(First_allele_list, Second_allele_list)
        calculate_probabilities(raw_matrix)

        print("\n", end="")

except KeyboardInterrupt:
    print("Program ended")        
from player_permutation.permutation import Permutation

# Clear the output file
open('outputPS7.txt', 'w').close()

# Initialize the permutation object
permutation = Permutation()

# Read the input file and parse the data
permutation.read_file("inputPS7.txt")

# Calculate permutation
perms = permutation.assign()


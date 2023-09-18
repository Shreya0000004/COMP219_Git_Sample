# Open the input file in read mode
with open("sample_data1.txt", "r") as file:
    # Read and print each line from the file
    for line in file:
        print(line.strip())  # Strip newline characters for cleaner output



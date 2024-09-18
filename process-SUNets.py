import sys

def main():
    if len(sys.argv) != 3:
        print("ERROR: WRONG # ARGS\nExample usage: python process-SUNets.py input.txt output.txt")
        return
    input_fn = sys.argv[1]
    output_fn = sys.argv[2]

    with open(input_fn, 'r') as file:
        lines = file.readlines()
        new_lines = ["Email Address\n"]
        for line in lines:
            line = line.strip()
            # A little bit of extra checking in case some weird directories/files pulled in
            if line.isalnum() and line.lower() == line:
                new_lines.append(line + "@stanford.edu\n")
        
    with open(output_fn, 'w+') as file:
        file.writelines(new_lines)


if __name__ == "__main__":
    main()
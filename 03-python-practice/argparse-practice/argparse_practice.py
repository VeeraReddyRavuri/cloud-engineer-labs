import argparse

def main():

    parser = argparse.ArgumentParser(description="This is a practice parser")

    parser.add_argument("-R", "--required", required=True, help="This is a required argument")
    parser.add_argument("-O", "--optional", type=int, default=100, help="This is an optional integer argument")
    parser.add_argument("-B", "--boolean", action="store_true", help="This is a boolean argument")

    args = parser.parse_args()

    print(f"The required argument is: {args.required}")
    print(f"The optional argument is: {args.optional}")
    print(f"The booelan argument is: {args.boolean}")

    
if __name__ == "__main__":
    main()
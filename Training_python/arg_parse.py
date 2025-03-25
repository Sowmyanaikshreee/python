import argparse
if __name__ == "__main__":
    parser= argparse.ArgumentParser()
    parser.add_argument("number1", help = "first no")
    parser.add_argument("number2", help = "second no")
    parser.add_argument("operation", help = " operation")

    args = parser.parse_args()

  
    print(args.number2)
    print(args.number1)
    print(args.operation)

import os

def test():

    # print the text in ./test
    with open("./test", "r") as f:

        print(f.read())

    print(f"Done!")

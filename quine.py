quine = """
def main():
    quine = '''
    def main():
        quine = \"""
        {0}
        \""".format(quine)
        print(quine)

    main()

if __name__ == "__main__":
    main()
"""

def main():
    print(quine.format(quine))

if __name__ == "__main__":
    main()

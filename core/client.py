from core.strCon import strConstants

def main() -> None:
    print("Hello World!")

def entry() -> None:
    raise RuntimeError(strConstants.INCORRECT_USAGE)

if __name__ == "__main__":
    entry()

from enum import StrEnum

class strConstants(StrEnum):
    SUCCESS = "success"
    FAILURE = "failure"
    VERSION_INCOMPATIBILITY = "Please use Python version 3.9 or higher."
    INCORRECT_USAGE = "dat aint how u use ts boa💔"
    MIN_BIT_SIZE = "Bit size must be at least 2."

def entry() -> None:
    raise RuntimeError(strConstants.INCORRECT_USAGE)

if __name__ == "__main__":
    entry()

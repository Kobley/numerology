import sys
import core.client as client
from core.strCon import strConstants

def entry() -> None:
    if sys.version_info.major < 3:
        raise RuntimeError(strConstants.VERSION_INCOMPATIBILITY)
    elif sys.version_info.minor < 9:
        raise RuntimeError(strConstants.VERSION_INCOMPATIBILITY)

    client.main()

if __name__ == "__main__":
    entry()

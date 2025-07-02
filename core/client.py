from core.strCon import strConstants
from core.commands.primeCmd import PrimeCommand

from cleo.application import Application

application: Application = Application(name="numerology", version="1.0.0")
application.add(PrimeCommand())

def main() -> None:
    application.run()

def entry() -> None:
    raise RuntimeError(strConstants.INCORRECT_USAGE)

if __name__ == "__main__":
    entry()

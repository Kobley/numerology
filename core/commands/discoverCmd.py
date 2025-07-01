from cleo.commands.command import Command
from cleo.helpers import argument, option
# discover command to find types of number, main cmd, with optionals like bit size, contains certain substring, etc
# other cmds like gen fib gen prime etc, maybe with same optionals, maybe not
# or maybe split up types and add specific optionals for each type say if its fib, add optional for prime check too. or if its prime, add optional for twin prime check too.
class GreetCommand(Command):
    name = "greet"
    description = "Greets someone"
    arguments = [
        argument(
            "type",
            description="what type of number to discover? [fibonacci, prime, twin prime, safe prime, ]"
        )
    ]
    options = [
        option(
            "yell",
            "y",
            description="If set, the task will yell in uppercase letters",
            flag=True
        )
    ]

    def handle(self):
        name = self.argument("name")

        if name:
            text = f"Hello {name}"
        else:
            text = "Hello"

        if self.option("yell"):
            text = text.upper()

        self.line(text)
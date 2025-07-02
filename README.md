 # numerology
  python tool built to find special numbers.

> [!WARNING]  
> still in development, nothing below is final nor finished.

## usage
> ```md
> $ python .\main.py
> Numerology (version 1.0.0)
> 
> Usage:
>   command [options] [arguments]
> 
> Options:
>   -h, --help            Display help for the given command. When no command is given display help for the list command.
>   -q, --quiet           Do not output any message.
>   -V, --version         Display this application version.
>       --ansi            Force ANSI output.
>       --no-ansi         Disable ANSI output.
>   -n, --no-interaction  Do not ask any interactive question.
>   -v|vv|vvv, --verbose  Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug.
> 
> Available commands:
>   help   Displays help for a command.
>   list   Lists commands.
>   prime  find a prime number with specific properties
> ```

## example command usage

### detail on specific command
> ```md
> $ python .\main.py help prime
> 
> Description:
>   find a prime number with specific properties
> 
> Usage:
>   prime [options] [--] [<type> [<search>]]
> 
> Arguments:
>   type                       what type of prime to discover? [standard, fib, twin, safe] [default: "standard"]
>   search                     what search method to use? [standard, rand] [default: "standard"]
> 
> Options:
>   -p, --palindrome           number found must be a palindrome
>   -l, --length=LENGTH        number must be this many digits long [default: "6"]
>   -s, --substring=SUBSTRING  number found must contain given digits
>   -h, --help                 Display help for the given command. When no command is given display help for the list command.
>   -q, --quiet                Do not output any message.
>   -V, --version              Display this application version.
>       --ansi                 Force ANSI output.
>       --no-ansi              Disable ANSI output.
>   -n, --no-interaction       Do not ask any interactive question.
>   -v|vv|vvv, --verbose       Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug.
> ```

### standard prime generation
> ```md
> $ python .\main.py prime standard rand
> Searching for a standard prime number....
> Found the number: 446647
> ```
> standard prime generation but with the randomized approach

### fibonacci prime with specifications
> ```md
> $ python .\main.py prime fib rand -s 8008 -l 5
> Searching for a fibonacci prime number...
>  0/3 [>---------------------------]   0%
> ```
> fibonacci prime randomized search with digit substring of 8008 and max bit size 5

### randomized prime with specifications
> ```md
> $ python .\main.py prime standard rand -s 69 -l 6 -p
> Searching for a standard prime number....
> Found a prime canidate with substring: 76963...
> Found a prime canidate with substring: 173969...
> Found a prime canidate with substring: 812699...
> Found a prime canidate with substring: 772697...
> Found a prime canidate with substring: 211693...
> (many more entries)
> Found a prime canidate with substring: 96769...
> Found a palindrome prime canidate: 96769...
> Found the number: 96769
> ```
> standard randomized prime search with max bit size of 6, must be a palindrome, and must contain the digits 69

## this project is licensed with the GNU GPLv3 license.
> ### below is a summary.

The GNU General Public License version 3 (GPLv3) is a free software license designed to ensure that software remains free and open for all users. It allows anyone to use, study, modify, and distribute the software, provided that any distributed versions, including modified ones, are also licensed under GPLv3, ensuring that derivative works remain free. The license includes protections against patent claims and prohibits the use of hardware restrictions to prevent users from running modified versions of the software. This strong copyleft license ensures that the freedoms granted by the original software are preserved in all copies and derivative works.

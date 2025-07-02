from cleo.commands.command import Command
from cleo.helpers import argument, option
from core.algorithms import alg
import sys
sys.set_int_max_str_digits(32768)

class PrimeCommand(Command):
    name = "prime"
    description = "find a prime number with specific properties"
    arguments = [
        argument(
            "type",
            description="what type of prime to discover? [standard, fib, twin, safe]",
            optional=True,
            default="standard",
        ),
        argument(
            "search",
            description="what search method to use? [standard, rand]",
            optional=True,
            default="standard"
        )
    ]
    options = [
        option(
            "palindrome",
            "p",
            description="number found must be a palindrome",
            flag=True
        ),
        option(
            "length",
            "l",
            description="number must be this many digits long",
            flag=False,
            default="6"
        ),
        option(
            "substring",
            "s",
            description="number found must contain given digits",
            flag=False
        )
    ]

    def handle(self):
        num_type = self.argument("type")
        search_type = self.argument("search")
        substring = self.option("substring")
        length = self.option("length")
        palindrome = self.option("palindrome")

        if num_type == "standard":
            self.line("Searching for a standard prime number....")
            
            if search_type == "standard":
                
                canidate:int = 3
                while True:
                    if alg.miller_rabin(canidate):
                        
                        if length:
                            if len(str(canidate)) == int(length):
                                # self.line(f"Found a prime canidate with length: {canidate}...")
                                pass
                            else:
                                canidate = alg.next_prime(canidate)
                                continue
                        
                        if substring:
                            if alg.contains_digit_substring(canidate, substring):
                                self.line(f"Found a prime canidate with substring: {canidate}...")
                            else:
                                canidate = alg.next_prime(canidate)
                                continue
                        
                        if palindrome:
                            if alg.is_palindromic(canidate) and len(str(canidate)) >= 4:
                                self.line(f"Found a palindrome prime canidate: {canidate}...")
                            else:
                                canidate = alg.next_prime(canidate)
                                continue
                        
                        self.line(f"Found the number: {canidate}")
                        break
                    canidate += 2
            elif search_type == "rand":
                # progress = self.progress_bar(3)
                while True:
                    # progress.start()
                    rand_canidate:int = alg.rand_prime(alg.digits_to_bits(int(length)))
                    
                    if alg.miller_rabin(rand_canidate):
                        # progress.advance()
                        
                        if substring:
                            if alg.contains_digit_substring(rand_canidate, substring):
                                self.line(f"Found a prime canidate with substring: {rand_canidate}...")
                                # progress.advance()
                            else:
                                continue
                        
                        if palindrome:
                            if alg.is_palindromic(rand_canidate) and len(str(rand_canidate)) >= 4:
                                self.line(f"Found a palindrome prime canidate: {rand_canidate}...")
                                # progress.advance()
                            else:
                                continue
                        
                        # progress.finish()
                        # self.line("\n")
                        self.line(f"Found the number: {rand_canidate}")
                        break
                
        elif num_type == "fib":
            self.line("Searching for a fibonacci prime number...")
            if search_type == "standard":
                
                fib_canidate:int = 3
                while True:
                    if alg.miller_rabin(fib_canidate) and alg.miller_rabin(alg.nth_fib(fib_canidate)):
                        fib_num:int = alg.nth_fib(fib_canidate)
                        
                        if length:
                            if len(str(fib_num)) >= int(length):
                                self.line(f"Found a prime fibonacci canidate with length: {len(str(fib_num))}...")
                            else:
                                fib_canidate = alg.next_prime(fib_canidate)
                                continue
                        
                        if substring:
                            if alg.contains_digit_substring(fib_num, substring):
                                self.line(f"Found a prime fibonacci canidate with substring: {fib_num}...")
                            else:
                                fib_canidate = alg.next_prime(fib_canidate)
                                continue
                        
                        if palindrome:
                            if alg.is_palindromic(fib_num) and len(str(fib_num)) >= 4:
                                self.line(f"Found a palindrome prime fibonacci canidate: {fib_num}...")
                            else:
                                fib_canidate = alg.next_prime(fib_canidate)
                                continue
                        
                        self.line(f"Found the number: {fib_num}")
                        self.line(f"With prime index: {fib_canidate}")
                        break
                    fib_canidate = alg.next_prime(fib_canidate)
                    
            elif search_type == "rand":
                progress = self.progress_bar(3)
                rand_fib_canidate:int = 0
                while True:
                    progress.start()
                    rand_fib_canidate = alg.nth_fib(alg.rand_prime(alg.digits_to_bits(int(length))))
                    
                    if True:
                        progress.advance()
                        if substring:
                            if alg.contains_digit_substring(rand_fib_canidate, substring):
                                # self.line(f"Found a prime fibonacci canidate with substring: {rand_fib_canidate}...")
                                progress.advance()
                            else:
                                rand_fib_canidate = alg.next_prime(rand_fib_canidate)
                                continue
                        
                        if palindrome:
                            if alg.is_palindromic(rand_fib_canidate) and len(str(rand_fib_canidate)) >= 4:
                                # self.line(f"Found a palindrome prime fibonacci canidate: {rand_fib_canidate}...")
                                progress.advance()
                            else:
                                rand_fib_canidate = alg.next_prime(rand_fib_canidate)
                                continue
                        
                        break
                progress.finish()
                self.line("\n")
                self.line(f"Found the number: {rand_fib_canidate}")
                
        elif num_type == "twin":
            self.line("Searching for a twin prime number...")
            if search_type == "standard":
                pass
            elif search_type == "rand":
                pass
                
        elif num_type == "safe":
            self.line("Searching for a safe prime number...")
            if search_type == "standard":
                pass
            elif search_type == "rand":
                pass
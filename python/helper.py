import os
import functools
import time


class Helper:
    """
    Helper functions to handle IO stuff
    """

    def get_number(self, low: int, high: int, message: str) -> int:
        num = -1
        while not (num >= low and num <= high):
            try:
                num = (int)(input(message))
                if os.name == "nt":
                    os.system("cls")
                else:
                    os.system("clear")
            except ValueError as _:
                if os.name == "nt":
                    os.system("cls")
                else:
                    os.system("clear")
                print(f"The number should be from {low} to {high}")
        return num

    def get_int(self, prompt: str):
        while True:
            try:
                return (int)(input(prompt))
            except ValueError as _:
                print("Your answer should be a whole number")

    def verbose(self, fun):
        @functools.wraps(fun)
        def timer(*args, **kwargs):
            print(f"Running {fun.__name__}")
            start_time = time.perf_counter_ns()
            try:
                result = fun(*args, **kwargs)
            finally:
                stop_time = time.perf_counter_ns()
                duration_ns = stop_time - start_time
                duration_ms = duration_ns / 1_000_000
                print(f"{fun.__name__} completed in {duration_ms}ms")
            timer.__doc__ = fun.__doc__
            timer.__name__ = fun.__doc__
            return result

        return timer

    def printf(fmt: str, *args):
        done = False
        start: int = 0
        tup_idx: int = 0
        while not done:
            i = fmt.find("%s", start)
            if i == -1:
                done = True
            else:
                word: str = str(args[tup_idx])
                tup_idx += 1
                fmt = fmt[:i] + word + fmt[i + 2 :]
                start = i + 1 + len(word)
        print(fmt)

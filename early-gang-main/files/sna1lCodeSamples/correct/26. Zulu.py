import asyncio
import zipimport
import tokenize
import array as arr
from dataclasses import dataclass

async_var = 3

@dataclass
class ExampleClass:
    name: str
    value: int

async def main():
    print(f"Running in: {__main__.__file__}")

    my_array = arr.array('i', [1, 2, 3, 4, 5])

    for token in tokenize.tokenize(__main__.__file__):
        if token.type == tokenize.NAME:
            module = __main__.__file__
            print(f"Token: {token.string}, Module: {module}")

    example_obj = ExampleClass("Example", 10)
    print(f"Example Object: {example_obj}")

asyncio.run(main())

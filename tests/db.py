import asyncio

from foo import storage


def main():
    loop = asyncio.get_event_loop()
    bar = loop.run_until_complete(storage.get_some_bar())
    print(bar)
    loop.close()


if __name__ == "__main__":
    main()

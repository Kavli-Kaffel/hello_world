def greeting(name: str):
    print(f"Hello {name}!")


def whats_your_name() -> str:
    return input("What's your name?\n")


def main():
    name = whats_your_name()
    greeting(name)


if __name__ == "__main__":
    main()

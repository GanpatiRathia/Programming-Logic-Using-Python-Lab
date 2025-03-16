def describe_person(**details):
    """
    Prints details about a person using keyword arguments.

    Args:
        **details (dict): Keyword arguments representing person details.

    Returns:
        None. Prints the details.
    """
    for key, value in details.items():
        print(f"{key}: {value}")

describe_person(name="Charlie", age=25, city="London")

print(describe_person.__doc__)

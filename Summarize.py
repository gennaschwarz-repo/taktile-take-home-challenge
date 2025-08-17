def add(data):
    """Function that summarized cols x and y"""

    data["sum"] = data["a"] + data["b"]

    return data


if __env:  # indicates we are running on Taktile
    data = add(data)

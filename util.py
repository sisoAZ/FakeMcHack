def sort_args(text) -> list:
    result = []
    if " " not in text and "　" not in text:
        result.append(text)
        return result
    if " " in text:
        return text.split(" ")
    if "　" in text:
        return text.split("　")
    return result
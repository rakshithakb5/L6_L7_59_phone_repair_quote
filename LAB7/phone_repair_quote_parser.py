def mask_imei(imei):
    """
    Removes dashes and spaces, then hides all but the last four digits.
    Returns an empty string for non-string input. Values of four characters
    or fewer are fully masked so nothing leaks.
    """
    if not isinstance(imei, str):
        return ""
    imei = imei.replace('-', '').replace(' ', '')
    if len(imei) <= 4:
        return '*' * len(imei)
    return '*' * (len(imei) - 4) + imei[-4:]

def parse_parts_order(text):
    """
    Parses 'screen x1; battery x2' into a {part: quantity} dictionary.
    Malformed items (no 'x', empty part name, non-numeric or zero quantity)
    are skipped. Non-string input gives an empty dictionary.
    """
    order = {}
    if not isinstance(text, str):
        return order
    for item in text.split(';'):
        if 'x' not in item:
            continue
        part, qty = item.rsplit('x', 1)
        part = part.strip()
        if not part:
            continue
        try:
            quantity = int(qty.strip())
        except ValueError:
            continue
        if quantity <= 0:
            continue
        order[part] = quantity
    return order

def parse_model(text):
    """
    Splits 'Brand Model name' into a (brand, model) tuple.
    Returns ('', '') for non-string or blank input and (Brand, '') when
    only one word is given.
    """
    if not isinstance(text, str):
        return ("", "")
    words = text.strip().split(None, 1)
    if not words:
        return ("", "")
    brand = words[0].title()
    model = words[1].strip() if len(words) > 1 else ""
    return brand, model

def main():
    print("==== Running mask_imei ====")
    value = input("Enter an IMEI number (e.g. 35-209900-176148-1): ")
    print("Masked IMEI:", mask_imei(value))

    print("\n==== Running parse_parts_order ====")
    value = input("Enter parts and quantities as PART xQTY separated by ; (e.g. screen x1; battery x2): ")
    print("Parts order:", parse_parts_order(value))

    print("\n==== Running parse_model ====")
    value = input("Enter the phone brand and model (e.g. Samsung Galaxy S23): ")
    print("Brand and model:", parse_model(value))

if __name__ == "__main__":
    main()

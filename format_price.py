import re
import argparse

def is_number(val):
    return isinstance(val, int) or isinstance(val, float)

def format_price(price):
    price_precision = 2
    try:
        price = price if is_number(price) else float(str(price))
    except ValueError:
        return None

    str_price = '{:,}'.format(round(price, price_precision))
    str_price = str_price.replace(',', ' ')
    str_price = re.sub(r'(.+)(\.0+)$',r'\1',string=str_price)
    return str_price

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Price formatter'
    )
    parser.add_argument('price', help="Price to format", type=float)
    args = parser.parse_args()
    print(format_price(args.price))

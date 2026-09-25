"""Simple command-line currency converter.

Rates are represented as units of each currency per 1 USD. Update the table
when you need newer rates.
"""

from __future__ import annotations

import argparse


RATES_PER_USD = {
    "AUD": 1.53,
    "CAD": 1.36,
    "EUR": 0.92,
    "GBP": 0.79,
    "INR": 83.10,
    "JPY": 149.50,
    "USD": 1.00,
}


def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
    """Convert an amount between supported currencies."""
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    if from_currency not in RATES_PER_USD:
        raise ValueError(f"Unsupported source currency: {from_currency}")
    if to_currency not in RATES_PER_USD:
        raise ValueError(f"Unsupported target currency: {to_currency}")

    amount_in_usd = amount / RATES_PER_USD[from_currency]
    return amount_in_usd * RATES_PER_USD[to_currency]


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert an amount between currencies.")
    parser.add_argument("amount", type=float, help="Amount to convert")
    parser.add_argument("from_currency", help="Source currency code, such as USD")
    parser.add_argument("to_currency", help="Target currency code, such as INR")
    args = parser.parse_args()

    if args.amount < 0:
        parser.error("amount must be zero or greater")

    try:
        converted_amount = convert_currency(
            args.amount, args.from_currency, args.to_currency
        )
    except ValueError as error:
        parser.error(str(error))

    print(
        f"{args.amount:.2f} {args.from_currency.upper()} = "
        f"{converted_amount:.2f} {args.to_currency.upper()}"
    )


if __name__ == "__main__":
    main()
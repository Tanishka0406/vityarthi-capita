# vityarthi-capita

## Currency converter

Convert between the supported currencies from the command line:

```bash
python3 currency_converter.py 100 USD INR
```

Supported currencies: `AUD`, `CAD`, `EUR`, `GBP`, `INR`, `JPY`, and `USD`.

The exchange rates are stored in `currency_converter.py` as rates relative to
USD. Update `RATES_PER_USD` when you need current rates.

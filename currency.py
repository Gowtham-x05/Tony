# Simple currency converter from USD to EUR

def convert_usd_to_eur(usd_amount):
    //exchange_rate = 0.85  # Example exchange rate: 1 USD = 0.85 EUR
    eur_amount = usd_amount * exchange_rate
    return eur_amount

def main():
    usd = float(input("Enter amount in USD: "))
    eur = convert_usd_to_eur(usd)
    print(f"{usd} USD is approximately {eur:.2f} EUR")

if __name__ == "__main__":
    main()


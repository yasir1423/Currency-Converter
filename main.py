import requests
def get_exchange_rate():
    try:
        #Using a free and open exchange-rate open AI
        url="https://api.exchangerate-api.com/v4/latest/USD"
        response=requests.get(url)
        #Check if API request was successful
        if response.status_code!=200:
            raise Exception("Error fetching exchange rates!")
        data=response.json()
        return data["rates"]
    except requests.exceptions.ConnectionError:
        print("Error: No internet connection!!!")
        return None
    except Exception as e:
        print("Error",e)
        return None
def convert_currency(amount,from_currency,to_currency,rates):
    from_currency=from_currency.upper()
    to_currency=to_currency.upper()
    #Check if currency codes exist
    if from_currency not in rates:
        print(f"Error:'{from_currency}' is not a valid currency code.")
        return None
    if to_currency not in rates:
        print(f"Error:'{to_currency} is not a valid currency code.")
        return None
    #Convert amount into USD first and then to target currency
    usd_amount=amount/rates[from_currency]
    converted_amount=usd_amount*rates[to_currency]
    return converted_amount
#Main program
rates=get_exchange_rate()
if rates:
    print("===Live Currency Convertor===")
    try:
        amount=float(input("Enter amount:"))
        from_currency=input("Convert from(e.g:USD,PKR,EUR):")
        to_currency=input("Convert to(e.g:USD,PKR,EUR):")
        result=convert_currency(amount,from_currency,to_currency,rates)
        if result is not None:
            print(f"{amount}{from_currency.upper()}={result:.2f}{to_currency.upper()}")
    except ValueError:
        print("Error!!!Please enter a valid number.")
'''List of some Important currency Codes
USD - United States Dollar
EUR - Euro (Eurozone)
GBP - British Pound Sterling (United Kingdom)
JPY - Japanese Yen (Japan)
CNY - Chinese Yuan (China)
INR - Indian Rupee (India)
CAD - Canadian Dollar (Canada)
AUD - Australian Dollar (Australia)
CHF - Swiss Franc (Switzerland)
HKD - Hong Kong Dollar (Hong Kong)
SGD - Singapore Dollar (Singapore)
NZD - New Zealand Dollar (New Zealand)
ZAR - South African Rand (South Africa)
RUB - Russian Ruble (Russia)
BRL - Brazilian Real (Brazil)
MXN - Mexican Peso (Mexico)
KRW - South Korean Won (South Korea)'''

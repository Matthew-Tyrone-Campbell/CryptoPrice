import requests

api_key_file = open("/home/matthew/Code/API Keys/CoinRanking.txt")
API_KEY = api_key_file.readline().strip()
api_key_file.close()

URL = 'https://api.coinranking.com/v2/coin/{uuid}/price'
UUID_CODES = {'Doge':'a91GCGd_u96cF', 'Bitcoin':'Qwsogvtv82FCd', 'Ethereum':'razxDUgYGNAdQ'}

HEADER = {
    'Content-Type': 'application/json',
    'x-access-token': f'{API_KEY}'
}
def get_crypto_price(url,header):
    response = requests.get(url,headers=header).json()
    return response['data']['price']

def menu():
    user_response = input("Press Enter to get the latest Crypto prices: ")
    crypto_prices = {}
    if user_response == True:
        print("Program exited")
    else:
        print('Extracting crypto prices ...')
        for x in UUID_CODES:
            crypto_prices[x] = get_crypto_price(URL.format(uuid=UUID_CODES[x]),HEADER)
        for x in crypto_prices:
            print(f'{x}: ${crypto_prices[x]}')
menu()

import requests

api_key_file = open("/home/matthew/Code/API Keys/CoinRanking.txt")
API_KEY = api_key_file.readline().strip()
api_key_file.close()

UUID_CODES = ['a91GCGd_u96cF', 'Qwsogvtv82FCd', 'Qwsogvtv82FCd',]
HEADER = {
    'Content-Type': 'application/json',
    'x-access-token': f'{API_KEY}'
}
def get_crypto_data(header,uuid_codes):
    # The array element variable is the text required to add another uuid code into the url
    # example: https://api.coinranking.com/v2/coins?uuids[]=razxDUgYGNAdQ&uuids[]=Qwsogvtv82FCd
    url_array_element = "{and_symbol}uuids[]={uuid}"
    url = 'https://api.coinranking.com/v2/coins?'
    
    # this adds the different cryptocurriences to the api url. Because of the & needed for additional ones, the first crypto is done outside of the loop
    url = url+url_array_element.format(and_symbol="", uuid=uuid_codes[0])
    for x in range(1, len(uuid_codes)):
        url = url+url_array_element.format(and_symbol="&", uuid=uuid_codes[x])
    response = requests.get(url,headers=header)
    return response

def menu():
    user_response = input("Press Enter to get the latest Crypto prices: ")
    crypto_prices = {}
    if user_response == True:
        print("Program exited")
    else:
        print('Extracting crypto prices ...')
        crypto_data = get_crypto_data(HEADER,UUID_CODES)
        print(crypto_data.text)
menu()

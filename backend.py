import requests

def get_api_key():
    api_key_file = open("/home/matthew/Code/API Keys/CoinRanking.txt")
    API_KEY = api_key_file.readline().strip()
    api_key_file.close()
    return API_KEY

#class for the crypto
class Crypto:
    def __init__(self,api_key):
        self.UUID_CODES = ['a91GCGd_u96cF', 'Qwsogvtv82FCd', 'razxDUgYGNAdQ',]
        self.api_key = api_key
        self.HEADER = {
                    'Content-Type': 'application/json',
                    'x-access-token': f'{self.api_key}'
                    }
        self.crypto_data = {}
    # makes api request and puts results in self.crypto_data
    def get_crypto_data(self):
        # The array element variable is the text required to add another uuid code into the url
        # example: https://api.coinranking.com/v2/coins?uuids[]=razxDUgYGNAdQ&uuids[]=Qwsogvtv82FCd
        url_array_element = "uuids[]={}"
        url = 'https://api.coinranking.com/v2/coins?'
        
        # this adds the different cryptocurriences to the api url. Because of the & needed in the url for additional coins, 
        # the array_element is changed basically on second iteration
        for code in self.UUID_CODES:
            url = url+url_array_element.format(code)
            url_array_element = "&uuids[]={}"
            
        # makes api request and puts it in self.crypto_data, also checks if the request was succesfull
        response = requests.get(url,headers=self.HEADER)
        self.crypto_data = response.json()
        if self.crypto_data["status"] == "error":
            raise RuntimeError(self.crypto_data["message"])
    
    # gets the crypto prices and puts them in a dictionary, with the name of the coin as the key
    def get_crypto_prices(self):
        crypto_coins = self.crypto_data["data"]["coins"]
        prices = {}
        for crypto in crypto_coins:
            prices[crypto["name"]] = round(float(crypto["price"]),3)
        return prices
    
#basic cammand line interface 
def menu(crypto_object):
    # if user presses enter user_response will equal false, and program will continue
    user_response = input("Press Enter to get the latest Crypto prices: ")
    if user_response == True:
        print("Program exited")
    else:
        print('Extracting crypto prices ...')
        try:
            crypto_object.get_crypto_data()
            prices = crypto_object.get_crypto_prices()
            for x in prices:
                print(f"{x}: ${prices[x]}")
        except RuntimeError as error:
            print(error)   
if __name__ == '__main__':
    menu(Crypto(get_api_key()))

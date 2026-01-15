#The url_crypto_query is the text required to query different cryptocurrencies using the api endpoint

import requests

def get_api_key():
    api_key_file = open("/home/matthew/Code/API Keys/CoinRanking.txt")
    API_KEY = api_key_file.readline().strip()
    api_key_file.close()
    return API_KEY

class Crypto:
    def __init__(self,api_key):
        self.UUID_CODES = ['a91GCGd_u96cF', 'Qwsogvtv82FCd', 'razxDUgYGNAdQ']
        self.api_key = api_key
        self.HEADER = {
                    'Content-Type': 'application/json',
                    'x-access-token': f'{self.api_key}'
                    }
        self.crypto_data = {}

    # makes api request and turns it into a dictionary, also checks if api request was successfull
    def crypto_api_request(self):
        url_crypto_query = "uuids[]={}"
        url = 'https://api.coinranking.com/v2/coins?'
        
        # adds the different cryptocurriences to the api url, note the change in the '&' for every crypto
        for code in self.UUID_CODES:
            url = url+url_crypto_query.format(code)
            url_crypto_query = "&uuids[]={}"
            
        # makes api request and returns it. also checks if the request was succesfull
        response = requests.get(url,headers=self.HEADER).json()
        if response["status"] == "error":
            raise RuntimeError(self.crypto_data["message"])
        return response
    
    #takes the cryptocurrencies from the api response and puts them in self.crypto_data as a dictionary
    def process_data(self, response):
        cryptos = {}
        for crypto in response["data"]["coins"]:
            cryptos[crypto["name"]] = crypto
        return cryptos
    
    def assign_crypto_data(self):
        self.crypto_data = self.process_data(self.crypto_api_request())
        
    def get_crypto_price(self,cryptocurrency):
        price = round(float(self.crypto_data[cryptocurrency]['price']),2)
        price = str(price)
        return price

    def get_crypto_logo(self,cryptocurrency):
        return self.crypto_data[cryptocurrency]["iconUrl"]

    def get_crypto_change(self, cryptocurrency):
        return self.crypto_data[cryptocurrency]["change"]

    def get_crypto_initials(self,cryptocurrency):
        return self.crypto_data[cryptocurrency]["symbol"]
    
#basic cammand line interface 
def menu():
    # if user presses enter user_response will equal false, and program will continue
    user_response = input("Press Enter to get the latest Crypto prices: ")
    if user_response == True:
        print("Program exited")
    else:
        print('Extracting crypto prices ...')
        crypto_object = Crypto(get_api_key())
        crypto_object.assign_crypto_data()
        try:
            for crypto in crypto_object.crypto_data:
                price = crypto_object.get_crypto_price(crypto)
                change = crypto_object.get_crypto_change(crypto)
                print(f"{crypto}: ${price}, change: {change}%")
        except RuntimeError as error:
            print(error)   
if __name__ == '__main__':
    menu()
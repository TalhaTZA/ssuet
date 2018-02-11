import requests
import matplotlib.pyplot as plt


class Graph():
    def __init__(self, *args, **kwargs):
        pass
    
    def setUrl(self,name_of_cryptocurrency='BTC',currreny_to_covert_into='USD'):
        self.name=name_of_cryptocurrency.upper()
        self.convert=currreny_to_covert_into.upper()
        self.url=('https://min-api.cryptocompare.com/data/histominute?fsym={}&tsym={}&limit=60&aggregate=3&e=CCCAGG').format(self.name,self.convert)
        self.getJsonData()

    def getJsonData(self):
        self.response=requests.get(self.url)
        self.json_response=self.response.json()
        self.data=self.json_response['Data']
        self.getTimeAndPrice()
    
    def getTimeAndPrice(self):
        self.list_price=[]
        self.list_time=[]
        for element in self.data:
            self.list_time.append(element['time'])
            self.list_price.append(element['close'])
        self.makeGraph()
    
    def makeGraph(self):
        plt.plot(self.list_time,self.list_price)
        plt.title('CHART OF {}'.format(self.name))
        plt.xlabel('time in milliseconds')
        plt.ylabel('price in {}'.format(self.convert.lower()))
        plt.show()

def main():
    btc=Graph()
    btc.setUrl('BTC','USD')

    eth=Graph()
    eth.setUrl('ETH','USD')


if __name__ in ('__main__'):
    main()

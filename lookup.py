import requests

def openURL(coinName):
    #https://api.coinmarketcap.com/v1/ticker/bitcoin/
    print(coinName,":")
    try:
        url = "https://api.coinmarketcap.com/v1/ticker/"+coinName+"/"
        r = requests.get(url)
        data = r.json()
        print("got url")
    except:
        pass

    currLst = data[0]
    return currLst
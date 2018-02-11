import requests

def openURL(coinName):
    #https://api.coinmarketcap.com/v1/ticker/bitcoin/
    try:
        url = "https://api.coinmarketcap.com/v1/ticker/"+coinName+"/"
        print(url)
        r = requests.get(url)
        data = r.json()
    except:
        pass

    return data

def getData(coinName):
    currLst = openURL(coinName)

    return currLst[0]


def search(coinName):
    currDict = getData(coinName)

    return currDict

print(search("bitcoin"))
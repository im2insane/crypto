import requests

def openURL(coinName):
    #https://api.coinmarketcap.com/v1/ticker/bitcoin/
    try:
        url = "https://api.coinmarketcap.com/v1/ticker/"+coinName+"/"
        r = requests.get(url)
        data = r.json()
    except:
        pass

    currLst = data[0]

    for keys in currLst:
        if currLst[keys] == "null":
            currLst[keys] = "0"

    return currLst

# def formatStr(numStr):
#     print(type(numStr))
#     numStr = int(numStr)
#     print(type(numStr))
#     numStr ="{0:,.0f}".format(numStr)
#     print(type(numStr))
#     print(numStr)
#     pass
#
# str = "1223456789"
# formatStr(str)

######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_WiFi"
    oIndex = "USR-C322"
    hexID = "SZKRFUSRC322"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'USR-C322', 'kicadSymbolFootprint': 'RF_WiFi:USR-C322', 'kicadSymbolDatasheet': 'https://www.usriot.com/download/WIFI/USR-C322%20User%20Manual%20V2.3.pdf', 'kicadSymbolki_keywords': 'WiFi IEEE802.11 b/g/n', 'kicadSymbolki_description': '802.11 b/g/n Wi-Fi Module', 'kicadSymbolki_fp_filters': 'USR?C322*'}])
    newPart['name'].append('RF_WiFi : USR-C322')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


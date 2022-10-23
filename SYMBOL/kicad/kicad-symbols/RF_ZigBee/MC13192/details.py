
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_ZigBee"
    oIndex = "MC13192"
    hexID = "SZKRFZIGBEEMC13192"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MC13192', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.nxp.com/products/no-longer-manufactured/2.4-ghz-low-power-transceiver-for-802.15.4:MC13192', 'kicadSymbolki_keywords': 'ZIGBEE', 'kicadSymbolki_description': '2.4 GHz, Low Power Transceiver for 802.15.4 (Zigbee controller)'}])
    newPart['name'].append('MC13192')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


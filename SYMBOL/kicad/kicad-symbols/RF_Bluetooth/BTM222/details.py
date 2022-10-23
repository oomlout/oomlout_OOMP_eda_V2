
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Bluetooth"
    oIndex = "BTM222"
    hexID = "SZKRFBLUETOOTHBTM222"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BTM222', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.tme.eu/de/Document/b90358c53cd65c9b10d2914f55812666/btm222_datasheet.pdf', 'kicadSymbolki_keywords': 'Bluetooth BT SPP Module', 'kicadSymbolki_description': 'Bluetooth SPP Module, UART, Class 1'}])
    newPart['name'].append('BTM222')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


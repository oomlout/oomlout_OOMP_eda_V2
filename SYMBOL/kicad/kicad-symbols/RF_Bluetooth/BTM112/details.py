
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Bluetooth"
    oIndex = "BTM112"
    hexID = "SZKRFBLUETOOTHBTM112"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BTM112', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.sparkfun.com/datasheets/Wireless/Bluetooth/BTM112_wATcommands.pdf', 'kicadSymbolki_keywords': 'Bluetooth BT SPP Module', 'kicadSymbolki_description': 'Bluetooth SPP Module, UART, Class 2'}])
    newPart['name'].append('RF_Bluetooth : BTM112')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart



######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Bluetooth"
    oIndex = "BL652"
    hexID = "SZKRFBLUETOOTHBL652"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BL652', 'kicadSymbolFootprint': 'RF_Module:Laird_BL652', 'kicadSymbolDatasheet': 'http://cdn.lairdtech.com/home/brandworld/files/Datasheet%20-%20BL652.pdf', 'kicadSymbolki_keywords': 'Bluetooth Nordic nRF52', 'kicadSymbolki_description': 'Bluetooth module', 'kicadSymbolki_fp_filters': 'Laird*BL652*'}])
    newPart['name'].append('RF_Bluetooth : BL652')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


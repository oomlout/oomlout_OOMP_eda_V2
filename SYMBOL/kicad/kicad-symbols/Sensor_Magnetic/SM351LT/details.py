
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Magnetic"
    oIndex = "SM351LT"
    hexID = "SZKSENMAGNETICSM351LT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SM351LT', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23', 'kicadSymbolDatasheet': 'https://sensing.honeywell.com/honeywell-sensing-nanopower-series-product-sheet-50095501-a-en.pdf', 'kicadSymbolki_keywords': 'Hall Effect Switch Sensor', 'kicadSymbolki_description': 'Hall Effect Switch, SOT-23', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Sensor_Magnetic : SM351LT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


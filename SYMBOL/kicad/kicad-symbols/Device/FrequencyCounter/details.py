
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "FrequencyCounter"
    hexID = "SZKDEVICEFREQUENCYCOUNTER"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'MES', 'kicadSymbolValue': 'FrequencyCounter', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'frequency counter', 'kicadSymbolki_description': 'Frequency counter'}])
    newPart['name'].append('Device : FrequencyCounter')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


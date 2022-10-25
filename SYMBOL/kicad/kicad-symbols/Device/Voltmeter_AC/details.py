
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "Voltmeter_AC"
    hexID = "SZKDEVICEVOLTMETERAC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'MES', 'kicadSymbolValue': 'Voltmeter_AC', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'voltmeter AC', 'kicadSymbolki_description': 'AC voltmeter'}])
    newPart['name'].append('Device : Voltmeter_AC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


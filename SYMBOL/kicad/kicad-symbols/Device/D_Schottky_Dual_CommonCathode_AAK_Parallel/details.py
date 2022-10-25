
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "D_Schottky_Dual_CommonCathode_AAK_Parallel"
    hexID = "SZKDEVICEDSCHOTTKYDUALCOONCATHODEAAKPARALLEL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'D_Schottky_Dual_CommonCathode_AAK_Parallel', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': 'Dual Schottky diode, common anode on pin 1'}])
    newPart['name'].append('Device : D_Schottky_Dual_CommonCathode_AAK_Parallel')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


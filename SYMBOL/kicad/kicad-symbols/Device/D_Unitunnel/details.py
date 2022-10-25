
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "D_Unitunnel"
    hexID = "SZKDEVICEDUNITUNNEL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'D_Unitunnel', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'unitunnel diode', 'kicadSymbolki_description': 'Unitunnel diode', 'kicadSymbolki_fp_filters': 'TO-???* *_Diode_* *SingleDiode* D_*'}])
    newPart['name'].append('Device : D_Unitunnel')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


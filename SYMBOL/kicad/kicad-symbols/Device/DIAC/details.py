
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "DIAC"
    hexID = "SZKDEVICEDIAC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'DIAC', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'AC diode DIAC', 'kicadSymbolki_description': 'Diode for alternating current', 'kicadSymbolki_fp_filters': 'TO-???* *_Diode_* *SingleDiode* D_*'}])
    newPart['name'].append('Device : DIAC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


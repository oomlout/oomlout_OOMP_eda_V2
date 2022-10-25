
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "R_Pack04"
    hexID = "SZKDEVICERPACK4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'RN', 'kicadSymbolValue': 'R_Pack04', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'R network parallel topology isolated', 'kicadSymbolki_description': '4 resistor network, parallel topology', 'kicadSymbolki_fp_filters': 'DIP* SOIC* R*Array*Concave* R*Array*Convex*'}])
    newPart['name'].append('Device : R_Pack04')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


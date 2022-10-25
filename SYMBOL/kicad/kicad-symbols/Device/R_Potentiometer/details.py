
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "R_Potentiometer"
    hexID = "SZKDEVICERPOTENTIOMETER"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'RV', 'kicadSymbolValue': 'R_Potentiometer', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'resistor variable', 'kicadSymbolki_description': 'Potentiometer', 'kicadSymbolki_fp_filters': 'Potentiometer*'}])
    newPart['name'].append('Device : R_Potentiometer')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


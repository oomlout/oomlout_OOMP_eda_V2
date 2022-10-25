
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "R_Potentiometer_Trim_US"
    hexID = "SZKDEVICERPOTENTIOMETERTRIMUS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'RV', 'kicadSymbolValue': 'R_Potentiometer_Trim_US', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'resistor variable trimpot trimmer', 'kicadSymbolki_description': 'Trim-potentiometer, US symbol', 'kicadSymbolki_fp_filters': 'Potentiometer*'}])
    newPart['name'].append('Device : R_Potentiometer_Trim_US')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


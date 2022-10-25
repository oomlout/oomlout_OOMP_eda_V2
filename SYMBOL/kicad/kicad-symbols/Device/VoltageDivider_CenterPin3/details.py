
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "VoltageDivider_CenterPin3"
    hexID = "SZKDEVICEVOLTAGEDIVIDERCENTERPIN3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'RN', 'kicadSymbolValue': 'VoltageDivider_CenterPin3', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'R network voltage divider', 'kicadSymbolki_description': 'Voltage divider, center on pin 3', 'kicadSymbolki_fp_filters': 'R?Array?SIP* SOT?23'}])
    newPart['name'].append('Device : VoltageDivider_CenterPin3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


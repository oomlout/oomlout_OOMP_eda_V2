
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "VoltageDivider_CenterPin1"
    hexID = "SZKDEVICEVOLTAGEDIVIDERCENTERPIN1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'RN', 'kicadSymbolValue': 'VoltageDivider_CenterPin1', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'R network voltage divider', 'kicadSymbolki_description': 'Voltage divider, center on pin 1', 'kicadSymbolki_fp_filters': 'R?Array?SIP* SOT?23'}])
    newPart['name'].append('Device : VoltageDivider_CenterPin1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart



######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "RJ45_LED_Shielded"
    hexID = "SZKCNRJ45LSHED"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '8P8C_LED_Shielded', 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'RJ45_LED_Shielded', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': '8P8C RJ female connector led', 'kicadSymbolki_description': 'RJ connector, 8P8C (8 positions 8 connected), two LEDs, Shielded', 'kicadSymbolki_fp_filters': '8P8C* RJ45*'}])
    newPart['name'].append('Connector : RJ45_LED_Shielded')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


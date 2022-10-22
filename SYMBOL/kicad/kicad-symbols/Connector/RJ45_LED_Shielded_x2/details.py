
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "RJ45_LED_Shielded_x2"
    hexID = "SZKCNRJ45LSHEDX2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '8P8C_LED_Shielded_x2', 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'RJ45_LED_Shielded_x2', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': '8P8C RJ female connector led', 'kicadSymbolki_description': 'RJ connector, 8P8C (8 positions 8 connected), two LEDs, Shielded, two ports', 'kicadSymbolki_fp_filters': '8P8C*02* RJ45*02*'}])
    newPart['name'].append('RJ45_LED_Shielded_x2')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


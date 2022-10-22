
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "CoaxialSwitch_Testpoint"
    hexID = "SZKCNCOAXIALSWITCHTP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'TP', 'kicadSymbolValue': 'CoaxialSwitch_Testpoint', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': ' Coaxial Switch RF testpoint', 'kicadSymbolki_description': 'Subminiature Coaxial Switch testpoint', 'kicadSymbolki_fp_filters': 'CoaxialSwitch*'}])
    newPart['name'].append('CoaxialSwitch_Testpoint')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


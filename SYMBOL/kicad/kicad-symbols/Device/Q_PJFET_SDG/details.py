
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "Q_PJFET_SDG"
    hexID = "SZKDEVICEQPJFETSDG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'Q_PJFET_SDG', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'transistor PJFET P-JFET', 'kicadSymbolki_description': 'P-JFET transistor, source/drain/gate'}])
    newPart['name'].append('Q_PJFET_SDG')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart



######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_HCS12"
    oIndex = "MC9S12DT256"
    hexID = "SZKMCUNXPHCS12MC9S12DT256"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MC9S12DT256', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/fact-sheet/MC9S12DT256FS.pdf', 'kicadSymbolki_keywords': 'HCS12 MCU', 'kicadSymbolki_description': 'HCS12 Microcontroller'}])
    newPart['name'].append('MC9S12DT256')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


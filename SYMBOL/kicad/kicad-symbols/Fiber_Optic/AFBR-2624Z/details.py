
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Fiber_Optic"
    oIndex = "AFBR-2624Z"
    hexID = "SZKFIBEROPTICAFBR2624Z"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'AFBR-2624Z', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://docs.broadcom.com/docs/AV02-4369EN', 'kicadSymbolki_keywords': 'fiber optic receiver', 'kicadSymbolki_description': 'Versatile Link Fiber Optic Receiver', 'kicadSymbolki_fp_filters': 'Broadcom*AFBR*16xxZ*'}])
    newPart['name'].append('AFBR-2624Z')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


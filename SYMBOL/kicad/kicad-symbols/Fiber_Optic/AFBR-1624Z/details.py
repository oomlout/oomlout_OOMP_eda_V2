
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Fiber_Optic"
    oIndex = "AFBR-1624Z"
    hexID = "SZKFIBEROPTICAFBR1624Z"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'AFBR-1624Z', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://docs.broadcom.com/docs/AV02-4369EN', 'kicadSymbolki_keywords': 'Fiber optic transmitter', 'kicadSymbolki_description': 'Versatile Link Fiber Optic Transmitter', 'kicadSymbolki_fp_filters': 'Broadcom*AFBR*16xxZ*'}])
    newPart['name'].append('Fiber_Optic : AFBR-1624Z')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


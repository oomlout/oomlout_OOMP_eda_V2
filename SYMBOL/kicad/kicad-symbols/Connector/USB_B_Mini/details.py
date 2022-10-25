
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "USB_B_Mini"
    hexID = "SZKCNUBM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'USB_B_Micro', 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'USB_B_Mini', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'connector USB mini', 'kicadSymbolki_description': 'USB Mini Type B connector', 'kicadSymbolki_fp_filters': 'USB*'}])
    newPart['name'].append('Connector : USB_B_Mini')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


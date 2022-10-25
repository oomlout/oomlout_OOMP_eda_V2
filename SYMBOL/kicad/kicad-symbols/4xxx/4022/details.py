
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "4xxx"
    oIndex = "4022"
    hexID = "SZK4XXX422"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '4022', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.intersil.com/content/dam/Intersil/documents/cd40/cd4017bms-22bms.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'CMOS CNT CNT8', 'kicadSymbolki_description': 'Johnson Counter (8 states)', 'kicadSymbolki_fp_filters': 'DIP?16*'}])
    newPart['name'].append('4xxx : 4022')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


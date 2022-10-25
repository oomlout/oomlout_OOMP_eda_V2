
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "4xxx"
    oIndex = "4002"
    hexID = "SZK4XXX42"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '4002', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.intersil.com/content/dam/Intersil/documents/cd40/cd4000bms-01bms-02bms-25bms.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'CMOS Nor4', 'kicadSymbolki_description': 'Dual  4 input NOR gate', 'kicadSymbolki_fp_filters': 'DIP?14*'}])
    newPart['name'].append('4xxx : 4002')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


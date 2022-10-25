
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Character"
    oIndex = "SA39-12SRWA"
    hexID = "SZKDICHARACTERSA3912SRWA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SA39-12EWA', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SA39-12SRWA', 'kicadSymbolFootprint': 'Display_7Segment:Sx39-1xxxxx', 'kicadSymbolDatasheet': 'http://www.kingbrightusa.com/images/catalog/SPEC/sa39-12srwa.pdf', 'kicadSymbolki_keywords': 'display LED 7-segment', 'kicadSymbolki_description': 'Single digit 7 segment display, super bright red, common anode', 'kicadSymbolki_fp_filters': 'S?39?1*'}])
    newPart['name'].append('Display_Character : SA39-12SRWA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


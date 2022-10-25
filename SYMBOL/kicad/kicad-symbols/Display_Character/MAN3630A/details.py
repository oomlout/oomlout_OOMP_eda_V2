
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Character"
    oIndex = "MAN3630A"
    hexID = "SZKDICHARACTERMAN363A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAN3630A', 'kicadSymbolFootprint': 'Display_7Segment:MAN3630A', 'kicadSymbolDatasheet': 'https://www.digchip.com/datasheets/parts/datasheet/161/MAN3640A-pdf.php', 'kicadSymbolki_keywords': 'display LED 7-segment', 'kicadSymbolki_description': 'Overflow 7 segment orange LED common anode', 'kicadSymbolki_fp_filters': '*MAN3630A*'}])
    newPart['name'].append('Display_Character : MAN3630A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart



######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Character"
    oIndex = "MAN3640A"
    hexID = "SZKDICHARACTERMAN364A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAN3640A', 'kicadSymbolFootprint': 'Display_7Segment:MAN3610A', 'kicadSymbolDatasheet': 'https://www.digchip.com/datasheets/parts/datasheet/161/MAN3640A-pdf.php', 'kicadSymbolki_keywords': 'display LED 7-segment', 'kicadSymbolki_description': 'Single digit 7 segment orange LED common anode right hand decimal', 'kicadSymbolki_fp_filters': 'MAN3610A*'}])
    newPart['name'].append('Display_Character : MAN3640A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


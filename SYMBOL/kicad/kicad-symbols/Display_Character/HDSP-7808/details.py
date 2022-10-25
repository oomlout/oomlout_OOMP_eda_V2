
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Character"
    oIndex = "HDSP-7808"
    hexID = "SZKDICHARACTERHDSP788"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HDSP-7808', 'kicadSymbolFootprint': 'Display_7Segment:HDSP-7807', 'kicadSymbolDatasheet': 'https://docs.broadcom.com/docs/AV02-2553EN', 'kicadSymbolki_keywords': 'display LED 7-segment', 'kicadSymbolki_description': '+-1 overflow 7 segment green, common cathode', 'kicadSymbolki_fp_filters': 'HDSP?7807*'}])
    newPart['name'].append('Display_Character : HDSP-7808')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


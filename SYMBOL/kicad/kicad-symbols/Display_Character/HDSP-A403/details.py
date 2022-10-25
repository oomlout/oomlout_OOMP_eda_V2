
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Character"
    oIndex = "HDSP-A403"
    hexID = "SZKDICHARACTERHDSPA43"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HDSP-A403', 'kicadSymbolFootprint': 'Display_7Segment:HDSP-A401', 'kicadSymbolDatasheet': 'https://docs.broadcom.com/docs/AV02-2553EN', 'kicadSymbolki_keywords': 'display LED 7-segment', 'kicadSymbolki_description': 'One digit 7 segment orange, common cathode', 'kicadSymbolki_fp_filters': 'HDSP?A401*'}])
    newPart['name'].append('Display_Character : HDSP-A403')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


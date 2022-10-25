
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Character"
    oIndex = "HDSP-7501"
    hexID = "SZKDICHARACTERHDSP751"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'HDSP-A151', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HDSP-7501', 'kicadSymbolFootprint': 'Display_7Segment:HDSP-A151', 'kicadSymbolDatasheet': 'https://docs.broadcom.com/docs/AV02-2553EN', 'kicadSymbolki_keywords': 'display LED 7-segment', 'kicadSymbolki_description': 'One digit 7 segment high efficiency red, common anode', 'kicadSymbolki_fp_filters': 'HDSP?A151*'}])
    newPart['name'].append('Display_Character : HDSP-7501')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


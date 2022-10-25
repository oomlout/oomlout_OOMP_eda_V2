
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Graphic"
    oIndex = "OLED-128O064D"
    hexID = "SZKDIGRAPHICOL128O64D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'DS', 'kicadSymbolValue': 'OLED-128O064D', 'kicadSymbolFootprint': 'Display:OLED-128O064D', 'kicadSymbolDatasheet': 'https://www.vishay.com/docs/37902/oled128o064dbpp3n00000.pdf', 'kicadSymbolki_keywords': 'display oled', 'kicadSymbolki_description': 'OLED display 128x64', 'kicadSymbolki_fp_filters': 'OLED?128O064D*'}])
    newPart['name'].append('Display_Graphic : OLED-128O064D')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


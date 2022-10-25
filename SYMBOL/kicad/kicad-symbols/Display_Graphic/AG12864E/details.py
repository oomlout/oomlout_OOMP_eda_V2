
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Graphic"
    oIndex = "AG12864E"
    hexID = "SZKDIGRAPHICAG12864E"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'DS', 'kicadSymbolValue': 'AG12864E', 'kicadSymbolFootprint': 'Display:AG12864E', 'kicadSymbolDatasheet': 'https://www.digchip.com/datasheets/parts/datasheet/1121/AG-12864E-pdf.php', 'kicadSymbolki_keywords': 'display LCD graphic', 'kicadSymbolki_description': 'Graphics Display 128x64px,  8b parallel, 1/64 Duty, 3.3V or 5V VDD', 'kicadSymbolki_fp_filters': '*AG12864E*'}])
    newPart['name'].append('Display_Graphic : AG12864E')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


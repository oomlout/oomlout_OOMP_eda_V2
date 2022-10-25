
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Graphic"
    oIndex = "EA_DOGM128X-6"
    hexID = "SZKDIGRAPHICEADOGM128X6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'EA_DOGM128X-6', 'kicadSymbolFootprint': 'Display:EA_DOGM128-6', 'kicadSymbolDatasheet': 'https://www.lcd-module.de/eng/pdf/grafik/dogm128e.pdf', 'kicadSymbolki_keywords': 'display LCD graphic', 'kicadSymbolki_description': 'EA DOGM128X-6 Graphical Display 128x64 optional backlight SPI 3.0-3.3V', 'kicadSymbolki_fp_filters': 'EA*DOGM128*6*'}])
    newPart['name'].append('Display_Graphic : EA_DOGM128X-6')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


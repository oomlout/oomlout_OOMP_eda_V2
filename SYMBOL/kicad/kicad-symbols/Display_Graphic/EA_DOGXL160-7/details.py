
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Graphic"
    oIndex = "EA_DOGXL160-7"
    hexID = "SZKDIGRAPHICEADOGXL167"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'EA_DOGXL160-7', 'kicadSymbolFootprint': 'Display:EA_DOGXL160-7', 'kicadSymbolDatasheet': 'http://www.lcd-module.com/eng/pdf/grafik/dogxl160-7e.pdf', 'kicadSymbolki_keywords': 'display LCD graphic', 'kicadSymbolki_description': 'EA DOGXL160-7 Graphical Display 160x104 no back light I2C SPI 2.7-3.3V', 'kicadSymbolki_fp_filters': 'EA*DOGXL160*7*'}])
    newPart['name'].append('Display_Graphic : EA_DOGXL160-7')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


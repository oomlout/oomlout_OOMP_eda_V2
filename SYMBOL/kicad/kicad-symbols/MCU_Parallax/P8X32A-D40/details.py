
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Parallax"
    oIndex = "P8X32A-D40"
    hexID = "SZKMCUPARALLAXP8X32AD4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'P8X32A-D40', 'kicadSymbolFootprint': 'Package_DIP:DIP-40_W15.24mm', 'kicadSymbolDatasheet': 'https://www.parallax.com/sites/default/files/downloads/P8X32A-Propeller-Datasheet-v1.4.0_0.pdf', 'kicadSymbolki_keywords': 'microcontroller multicore Parallax Propeller DIP', 'kicadSymbolki_description': 'Parallax Propeller 8 core, 32 bit, 80 MHz microcontroller, 3.3VDC, 40-pin DIP', 'kicadSymbolki_fp_filters': 'DIP*40*W15.24mm*'}])
    newPart['name'].append('P8X32A-D40')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


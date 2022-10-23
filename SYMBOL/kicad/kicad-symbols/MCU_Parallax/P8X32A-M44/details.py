
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Parallax"
    oIndex = "P8X32A-M44"
    hexID = "SZKMCUPARALLAXP8X32AM44"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'P8X32A-M44', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-44-1EP_9x9mm_P0.65mm_EP7.5x7.5mm', 'kicadSymbolDatasheet': 'https://www.parallax.com/sites/default/files/downloads/P8X32A-Propeller-Datasheet-v1.4.0_0.pdf', 'kicadSymbolki_keywords': 'microcontroller multicore Parallax Propeller QFN', 'kicadSymbolki_description': 'Parallax Propeller 8 core, 32 bit, 80 MHz microcontroller, 3.3VDC, 44-pin QFN', 'kicadSymbolki_fp_filters': 'QFN*44*1EP*9x9mm*P0.65mm*'}])
    newPart['name'].append('P8X32A-M44')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


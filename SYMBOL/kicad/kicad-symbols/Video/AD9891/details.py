
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Video"
    oIndex = "AD9891"
    hexID = "SZKVIDEOAD9891"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD9891', 'kicadSymbolFootprint': 'Package_BGA:BGA-64_9.0x9.0mm_Layout10x10_P0.8mm', 'kicadSymbolDatasheet': 'https://www.analog.com/static/imported-files/data_sheets/AD9891_9895.pdf', 'kicadSymbolki_keywords': 'CCD Signal Processor', 'kicadSymbolki_description': 'CCD Signal Processor, 20MHz 10bits, CSPBGA-64', 'kicadSymbolki_fp_filters': 'BGA*9.0x9.0mm*Layout10x10*P0.8mm*'}])
    newPart['name'].append('AD9891')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


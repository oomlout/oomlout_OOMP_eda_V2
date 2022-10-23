
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_RAM"
    oIndex = "IS61C5128AS-25HLI"
    hexID = "SZKMEMORYRAMIS61C5128AS25HLI"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IS61C5128AS-25HLI', 'kicadSymbolFootprint': 'Package_SO:TSOP-I-32_11.8x8mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.issi.com/WW/pdf/61-64C5128AL.pdf', 'kicadSymbolki_keywords': 'SRAM MEMORY', 'kicadSymbolki_description': '512K x 8 HIGH-SPEED CMOS STATIC RAM, 25ns, STSOP I-32', 'kicadSymbolki_fp_filters': 'TSOP*11.8x8mm*P0.5mm*'}])
    newPart['name'].append('IS61C5128AS-25HLI')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


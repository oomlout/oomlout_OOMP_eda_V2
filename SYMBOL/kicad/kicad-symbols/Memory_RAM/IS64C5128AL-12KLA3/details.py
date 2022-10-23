
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_RAM"
    oIndex = "IS64C5128AL-12KLA3"
    hexID = "SZKMEMORYRAMIS64C5128AL12KLA3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IS61C5128AL-10KLI', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IS64C5128AL-12KLA3', 'kicadSymbolFootprint': 'Package_SO:SOJ-36_10.16x23.49mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.issi.com/WW/pdf/61-64C5128AL.pdf', 'kicadSymbolki_keywords': 'SRAM MEMORY', 'kicadSymbolki_description': '512K x 8 HIGH-SPEED CMOS STATIC RAM, 12ns, SOJ-36', 'kicadSymbolki_fp_filters': 'SOJ*10.16x23.49mm*P1.27mm*'}])
    newPart['name'].append('IS64C5128AL-12KLA3')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


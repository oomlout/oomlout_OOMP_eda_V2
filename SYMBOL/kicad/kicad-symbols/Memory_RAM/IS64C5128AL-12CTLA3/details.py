
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_RAM"
    oIndex = "IS64C5128AL-12CTLA3"
    hexID = "SZKMEMORYRAMIS64C5128AL12CTLA3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IS61C5128AL-10TLI', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IS64C5128AL-12CTLA3', 'kicadSymbolFootprint': 'Package_SO:TSOP-II-44_10.16x18.41mm_P0.8mm', 'kicadSymbolDatasheet': 'http://www.issi.com/WW/pdf/61-64C5128AL.pdf', 'kicadSymbolki_keywords': 'SRAM MEMORY', 'kicadSymbolki_description': '512K x 8 HIGH-SPEED CMOS STATIC RAM, 12ns, TSOP II-44', 'kicadSymbolki_fp_filters': 'TSOP*10.16x18.41mm*P0.8mm*'}])
    newPart['name'].append('IS64C5128AL-12CTLA3')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


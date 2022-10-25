
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_RAM"
    oIndex = "IS61C5128AL-10TLI"
    hexID = "SZKMEMORYRAMIS61C5128AL1TLI"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IS61C5128AL-10TLI', 'kicadSymbolFootprint': 'Package_SO:TSOP-II-44_10.16x18.41mm_P0.8mm', 'kicadSymbolDatasheet': 'http://www.issi.com/WW/pdf/61-64C5128AL.pdf', 'kicadSymbolki_keywords': 'SRAM MEMORY', 'kicadSymbolki_description': '512K x 8 HIGH-SPEED CMOS STATIC RAM, 10ns, TSOP II-44', 'kicadSymbolki_fp_filters': 'TSOP*10.16x18.41mm*P0.8mm*'}])
    newPart['name'].append('Memory_RAM : IS61C5128AL-10TLI')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


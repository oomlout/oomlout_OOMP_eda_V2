
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_RAM"
    oIndex = "IS61C5128AS-25QLI"
    hexID = "SZKMEMORYRAMIS61C5128AS25QLI"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IS61C5128AS-25QLI', 'kicadSymbolFootprint': 'Package_SO:SSOP-32_11.305x20.495mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.issi.com/WW/pdf/61-64C5128AL.pdf', 'kicadSymbolki_keywords': 'SRAM MEMORY', 'kicadSymbolki_description': '512K x 8 HIGH-SPEED CMOS STATIC RAM, 25ns, SOP-32', 'kicadSymbolki_fp_filters': 'SSOP*11.305x20.495mm*P1.27mm*'}])
    newPart['name'].append('Memory_RAM : IS61C5128AS-25QLI')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


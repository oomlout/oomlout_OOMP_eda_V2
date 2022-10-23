
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_UniqueID"
    oIndex = "DS2401P"
    hexID = "SZKMEMORYUNIQUEIDDS241P"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DS2401P', 'kicadSymbolFootprint': 'Package_SO_J-Lead:TSOC-6_3.76x3.94mm_P1.27mm', 'kicadSymbolDatasheet': 'http://pdfserv.maximintegrated.com/en/ds/DS2401.pdf', 'kicadSymbolki_keywords': 'OneWire 1-Wire 1Wire Maxim Dallas ID', 'kicadSymbolki_description': 'Silicon Serial Number, TSOC-6', 'kicadSymbolki_fp_filters': 'TSOC*'}])
    newPart['name'].append('DS2401P')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


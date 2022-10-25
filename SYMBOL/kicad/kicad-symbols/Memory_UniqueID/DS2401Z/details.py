
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_UniqueID"
    oIndex = "DS2401Z"
    hexID = "SZKMEMORYUNIQUEIDDS241Z"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DS2401Z', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-223', 'kicadSymbolDatasheet': 'http://pdfserv.maximintegrated.com/en/ds/DS2401.pdf', 'kicadSymbolki_keywords': 'OneWire 1-Wire 1Wire Maxim Dallas ID', 'kicadSymbolki_description': 'Silicon Serial Number, SOT-223', 'kicadSymbolki_fp_filters': 'SOT?223*'}])
    newPart['name'].append('Memory_UniqueID : DS2401Z')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


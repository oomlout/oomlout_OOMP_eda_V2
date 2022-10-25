
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Intel"
    oIndex = "80C186XL"
    hexID = "SZKMCUINTEL8C186XL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'M80C186XL', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '80C186XL', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://datasheets.chipdb.org/Intel/x86/8018x/datashts/27243104.PDF', 'kicadSymbolki_keywords': 'MPRO', 'kicadSymbolki_description': '16-Bit High-Integration Embedded Processor', 'kicadSymbolki_fp_filters': 'PLCC* PGA*Layout11x11*P2.54mm* LCC*'}])
    newPart['name'].append('MCU_Intel : 80C186XL')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart



######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_ROM"
    oIndex = "XCF08P"
    hexID = "SZKMEMORYROMXCF8P"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'XCF08P', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.xilinx.com/support/documentation/data_sheets/ds123.pdf', 'kicadSymbolki_keywords': 'PROM FLASH', 'kicadSymbolki_description': 'Platform Flash In-System PROM'}])
    newPart['name'].append('Memory_ROM : XCF08P')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


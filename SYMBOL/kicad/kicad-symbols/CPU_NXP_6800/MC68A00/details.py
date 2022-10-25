
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "CPU_NXP_6800"
    oIndex = "MC68A00"
    hexID = "SZKCPUNXP68MC68A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MC6800', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MC68A00', 'kicadSymbolFootprint': 'Package_DIP:DIP-40_W15.24mm', 'kicadSymbolDatasheet': 'http://pdf.datasheetcatalog.com/datasheet/motorola/MC68A00L.pdf', 'kicadSymbolki_keywords': 'MCU', 'kicadSymbolki_description': '8-Bit Microprocessing unit 1.5MHz, DIP-40', 'kicadSymbolki_fp_filters': 'DIP*W15.24mm*'}])
    newPart['name'].append('CPU_NXP_6800 : MC68A00')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


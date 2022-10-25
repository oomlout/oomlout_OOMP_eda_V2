
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "GPU"
    oIndex = "MC68B45"
    hexID = "SZKGPUMC68B45"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MC6845', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MC68B45', 'kicadSymbolFootprint': 'Package_DIP:DIP-40_W15.24mm', 'kicadSymbolDatasheet': 'http://pdf.datasheetcatalog.com/datasheet_pdf/motorola/MC6845L_and_MC6845P.pdf', 'kicadSymbolki_keywords': 'CRT controller', 'kicadSymbolki_description': 'CRT Controller 2MHz, DIP-40', 'kicadSymbolki_fp_filters': 'DIP*W15.24mm*'}])
    newPart['name'].append('GPU : MC68B45')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


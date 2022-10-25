
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "CPU"
    oIndex = "Z80CPU"
    hexID = "SZKCPUZ8CPU"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'Z80CPU', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'www.zilog.com/manage_directlink.php?filepath=docs/z80/um0080', 'kicadSymbolki_keywords': 'Z80 CPU uP', 'kicadSymbolki_description': '8-bit General Purpose Microprocessor, DIP-40', 'kicadSymbolki_fp_filters': 'DIP* PDIP*'}])
    newPart['name'].append('CPU : Z80CPU')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


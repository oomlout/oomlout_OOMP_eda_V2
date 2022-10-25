
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "B380C2300-1500B"
    hexID = "SZKDIODEBRIDGEB38C2315B"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'B40C2300-1500B', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'B380C2300-1500B', 'kicadSymbolFootprint': 'Diode_THT:Diode_Bridge_19.0x3.5x10.0mm_P5.0mm', 'kicadSymbolDatasheet': 'https://diotec.com/tl_files/diotec/files/pdf/datasheets/b40c2300.pdf', 'kicadSymbolki_keywords': 'rectifier acdc', 'kicadSymbolki_description': 'Silicon Bridge Rectifier, 380V Vrms, 1.5A If, pins=-A+A, SIL-package', 'kicadSymbolki_fp_filters': 'D*Bridge*19.0x3.5x10.0mm*P5.0mm*'}])
    newPart['name'].append('Diode_Bridge : B380C2300-1500B')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


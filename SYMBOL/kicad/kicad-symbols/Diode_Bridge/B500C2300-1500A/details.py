
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "B500C2300-1500A"
    hexID = "SZKDIODEBRIDGEB5C2315A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'B40C2300-1500A', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'B500C2300-1500A', 'kicadSymbolFootprint': 'Diode_THT:Diode_Bridge_19.0x3.5x10.0mm_P5.0mm', 'kicadSymbolDatasheet': 'https://diotec.com/tl_files/diotec/files/pdf/datasheets/b40c2300.pdf', 'kicadSymbolki_keywords': 'rectifier acdc', 'kicadSymbolki_description': 'Silicon Bridge Rectifier, 500V Vrms, 1.5A If, pins=-AA+, SIL-package', 'kicadSymbolki_fp_filters': 'D*Bridge*19.0x3.5x10.0mm*P5.0mm*'}])
    newPart['name'].append('B500C2300-1500A')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


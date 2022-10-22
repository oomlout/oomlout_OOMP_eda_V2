
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "B40C3x00-2200A"
    hexID = "SZKDIODEBRIDGEB4C3X22A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'B40C5000-3x00A', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'B40C3x00-2200A', 'kicadSymbolFootprint': 'Diode_THT:Diode_Bridge_32.0x5.6x17.0mm_P10.0mm_P7.5mm', 'kicadSymbolDatasheet': 'https://diotec.com/tl_files/diotec/files/pdf/datasheets/b40c3700', 'kicadSymbolki_keywords': 'rectifier acdc', 'kicadSymbolki_description': 'Silicon Bridge Rectifier, 40V Vrms, 2.2A If, pins=-AA+, SIL-package', 'kicadSymbolki_fp_filters': 'D*Bridge*32.0x5.6x17.0mm*P10.0mm*P7.5mm*'}])
    newPart['name'].append('B40C3x00-2200A')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart



######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface"
    oIndex = "S5933_PQ160"
    hexID = "SZKINTERFACES5933PQ16"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'S5933_PQ160', 'kicadSymbolFootprint': 'Package_QFP:PQFP-160_28x28mm_P0.65mm', 'kicadSymbolDatasheet': 'http://datasheet.datasheetarchive.com/originals/distributors/Datasheets-35/DSA-684194.pdf', 'kicadSymbolki_keywords': 'PCI 2.1 Compliant Master/Slave Device', 'kicadSymbolki_description': 'PCI 2.1 Compliant Master/Slave Device, PQFP-160', 'kicadSymbolki_fp_filters': 'PQFP*28x28mm*P0.65mm*'}])
    newPart['name'].append('S5933_PQ160')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


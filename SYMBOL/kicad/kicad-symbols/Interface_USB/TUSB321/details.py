
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "TUSB321"
    hexID = "SZKINTERFACEUTU321"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TUSB321', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_X2QFN-12_1.6x1.6mm_P0.4mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tusb321.pdf', 'kicadSymbolki_keywords': 'USB CC PD VCONN', 'kicadSymbolki_description': 'USB Type-C Configuration Channel Logic and Port Control with VCONN, X2QFN-12', 'kicadSymbolki_fp_filters': 'Texas?X2QFN*1.6x1.6mm*P0.4mm*'}])
    newPart['name'].append('TUSB321')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


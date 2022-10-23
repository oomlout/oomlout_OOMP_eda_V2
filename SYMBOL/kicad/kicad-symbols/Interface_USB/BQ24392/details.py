
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "BQ24392"
    hexID = "SZKINTERFACEUBQ24392"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BQ24392', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_R-PUQFN-N10', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/bq24392.pdf', 'kicadSymbolki_keywords': 'USB BC detector charger', 'kicadSymbolki_description': 'Dual SPST USB 2.0 High Speed Switch with USB Battery Charging Specification Revision 1.2 Detection, UQFN-10', 'kicadSymbolki_fp_filters': 'Texas*R*PUQFN*'}])
    newPart['name'].append('BQ24392')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


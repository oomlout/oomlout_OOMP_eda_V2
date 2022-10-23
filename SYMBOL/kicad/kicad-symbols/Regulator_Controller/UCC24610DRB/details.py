
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "UCC24610DRB"
    hexID = "SZKREGULATORCONTROLLERUCC2461DRB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'UCC24610DRB', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_DRB0008A', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ucc24610.pdf', 'kicadSymbolki_keywords': 'synchronous rectifier controller', 'kicadSymbolki_description': 'GREEN Rectifier Controller Device, 600kHz, DFN-8', 'kicadSymbolki_fp_filters': 'Texas*DRB*'}])
    newPart['name'].append('UCC24610DRB')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


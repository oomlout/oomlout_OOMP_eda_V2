
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "LMG5200"
    hexID = "SZKPOWERMANAGEMENTLMG52"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'LMG5200', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_MOF0009A', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lmg5200.pdf', 'kicadSymbolki_keywords': 'Dual N-Channel GaN MOSFET', 'kicadSymbolki_description': '80-V, 10-A GaN Half-Bridge Power Stage, MOF0009A', 'kicadSymbolki_fp_filters': 'Texas*MOF0009A*'}])
    newPart['name'].append('LMG5200')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


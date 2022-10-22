
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "OPA569DWP"
    hexID = "SZKAMPLIFIEROPERATIONALOPA569DWP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'OPA569DWP', 'kicadSymbolFootprint': 'Package_SO:SO-20-1EP_7.52x12.825mm_P1.27mm_EP6.045x12.09mm_Mask3.56x4.47mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/opa569.pdf', 'kicadSymbolki_keywords': 'opamp single high current', 'kicadSymbolki_description': 'Rail-to-Rail I/O, 2A, Power Amplifier, SO-20', 'kicadSymbolki_fp_filters': 'SO*1EP*7.52x12.825mm*P1.27mm*'}])
    newPart['name'].append('OPA569DWP')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


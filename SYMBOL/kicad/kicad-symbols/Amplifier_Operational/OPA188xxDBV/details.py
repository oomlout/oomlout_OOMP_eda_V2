
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "OPA188xxDBV"
    hexID = "SZKAMPLIFIEROPERATIONALOPA188XXDBV"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AD8603', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'OPA188xxDBV', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TSOT-23-5', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/opa188.pdf', 'kicadSymbolki_keywords': 'single opamp zero-drift', 'kicadSymbolki_description': 'Zero-Drift, Precision, Low-Noise, Rail-to-Rail Output, 36-V Operational Amplifier, TSOT-23-5', 'kicadSymbolki_fp_filters': 'TSOT*23*'}])
    newPart['name'].append('OPA188xxDBV')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


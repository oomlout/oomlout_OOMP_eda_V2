
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "OPA4340EA"
    hexID = "SZKAMPLIFIEROPERATIONALOPA434EA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LTC6082xGN', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'OPA4340EA', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/opa340.pdf', 'kicadSymbolki_keywords': 'quad opamp', 'kicadSymbolki_description': 'Quad Single-Supply, Rail-to-Rail Operational Amplifier, MicroAmplifier Series, SSOP-16', 'kicadSymbolki_fp_filters': 'SSOP*3.9x4.9mm*P0.635mm* SOIC*3.9x9.9mm*P1.27mm* QSOP*3.9x4.9mm*P0.635mm*'}])
    newPart['name'].append('OPA4340EA')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


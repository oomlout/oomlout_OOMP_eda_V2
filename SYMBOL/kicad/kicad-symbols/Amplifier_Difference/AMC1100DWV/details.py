
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Difference"
    oIndex = "AMC1100DWV"
    hexID = "SZKAMPLIFIERDIFFERENCEAMC11DWV"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AMC1100DWV', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_7.5x5.85mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/amc1100.pdf', 'kicadSymbolki_keywords': 'isolated difference amplifier', 'kicadSymbolki_description': 'Fully-Differential Isolation Amplifier, Fixed Gain = 8, UL1577/IEC60747-5-2 Approved, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*7.5x5.85mm*P1.27mm*'}])
    newPart['name'].append('AMC1100DWV')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


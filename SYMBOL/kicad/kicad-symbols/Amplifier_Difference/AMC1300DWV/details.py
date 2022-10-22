
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Difference"
    oIndex = "AMC1300DWV"
    hexID = "SZKAMPLIFIERDIFFERENCEAMC13DWV"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AMC1100DWV', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AMC1300DWV', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_7.5x5.85mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/amc1300.pdf', 'kicadSymbolki_keywords': 'isolated difference amplifier', 'kicadSymbolki_description': 'Precision, ±250-mV Input, Reinforced Isolated Amplifier, Fixed Gain = 8.2, UL1577/VDE V 0884-11 Approved, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*7.5x5.85mm*P1.27mm*'}])
    newPart['name'].append('AMC1300DWV')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


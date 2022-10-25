
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Difference"
    oIndex = "LM733H"
    hexID = "SZKAMPLIFIERDIFFERENCELM733H"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM733CH', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM733H', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-5-10', 'kicadSymbolDatasheet': 'http://www.soemtron.org/downloads/disposals/lm733cn.pdf', 'kicadSymbolki_keywords': 'single differential video opamp', 'kicadSymbolki_description': 'Single Differential Amplifier, TO-5-10', 'kicadSymbolki_fp_filters': 'TO?5*'}])
    newPart['name'].append('Amplifier_Difference : LM733H')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart



######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "LM675"
    hexID = "SZKAMPLIFIEROPERATIONALLM675"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM675', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-5_P3.4x3.7mm_StaggerOdd_Lead3.8mm_Vertical', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm675.pdf', 'kicadSymbolki_keywords': 'single opamp', 'kicadSymbolki_description': 'Power Operational Amplifier, TO-220-5', 'kicadSymbolki_fp_filters': 'TO?220?5*StaggerOdd*'}])
    newPart['name'].append('Amplifier_Operational : LM675')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


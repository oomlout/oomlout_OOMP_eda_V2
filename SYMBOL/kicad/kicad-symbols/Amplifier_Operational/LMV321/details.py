
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "LMV321"
    hexID = "SZKAMPLIFIEROPERATIONALLMV321"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LMV321', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lmv324.pdf', 'kicadSymbolki_keywords': 'single opamp', 'kicadSymbolki_description': 'Low-Voltage Rail-to-Rail Output Operational Amplifiers, SOT-23-5/SC-70-5', 'kicadSymbolki_fp_filters': 'SOT?23* *SC*70*'}])
    newPart['name'].append('Amplifier_Operational : LMV321')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


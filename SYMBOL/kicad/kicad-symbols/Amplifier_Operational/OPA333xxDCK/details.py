
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "OPA333xxDCK"
    hexID = "SZKAMPLIFIEROPERATIONALOPA333XXDCK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LMV321', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'OPA333xxDCK', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/opa333.pdf', 'kicadSymbolki_keywords': 'single opamp', 'kicadSymbolki_description': 'Single 1.8V, microPower, CMOS Operational Amplifiers, Zero-Drift Series, SC-70-5', 'kicadSymbolki_fp_filters': 'SOT?23* *SC*70*'}])
    newPart['name'].append('Amplifier_Operational : OPA333xxDCK')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


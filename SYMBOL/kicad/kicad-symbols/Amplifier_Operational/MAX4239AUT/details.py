
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "MAX4239AUT"
    hexID = "SZKAMPLIFIEROPERATIONALMAX4239AUT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX4238AUT', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX4239AUT', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-6', 'kicadSymbolDatasheet': 'http://datasheets.maximintegrated.com/en/ds/MAX4238-MAX4239.pdf', 'kicadSymbolki_keywords': 'single opamp', 'kicadSymbolki_description': 'Ultra-Low Offset/Drift, Low-Noise, Precision Amplifiers, SOT-23-6', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Amplifier_Operational : MAX4239AUT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


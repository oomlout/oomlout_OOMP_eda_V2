
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Current"
    oIndex = "MAX4081F"
    hexID = "SZKAMPLIFIERCURRENTMAX481F"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX4081F', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://datasheets.maximintegrated.com/en/ds/MAX4080-MAX4081.pdf', 'kicadSymbolki_keywords': 'current sense amplifier', 'kicadSymbolki_description': '76V, High-Side, Current-Sense Amplifiers with Voltage Output, Bidirectional, 5V/V Gain, SOIC-8/uMAX-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* MSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Amplifier_Current : MAX4081F')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


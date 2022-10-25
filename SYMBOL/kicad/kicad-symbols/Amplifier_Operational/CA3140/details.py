
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "CA3140"
    hexID = "SZKAMPLIFIEROPERATIONALCA314"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CA3130', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CA3140', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.intersil.com/content/dam/intersil/documents/ca31/ca3140-a.pdf', 'kicadSymbolki_keywords': 'single opamp', 'kicadSymbolki_description': '4.5MHz, BiMOS Operational Amplifier with MOSFET Input/Bipolar Output, DIP-8/SOIC-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Amplifier_Operational : CA3140')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


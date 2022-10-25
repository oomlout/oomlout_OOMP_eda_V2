
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "OP279"
    hexID = "SZKAMPLIFIEROPERATIONALOP279"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'OP279', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/OP179_279.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'dual opamp', 'kicadSymbolki_description': 'Dual Rail-to-Rail High Output Current Operational Amplifiers, SOIC-8/TSSOP-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* TSSOP*4.4x3mm*P0.65mm*'}])
    newPart['name'].append('Amplifier_Operational : OP279')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


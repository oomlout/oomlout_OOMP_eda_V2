
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "MC33179"
    hexID = "SZKAMPLIFIEROPERATIONALMC33179"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM2902', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MC33179', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/MC33178-D.PDF', 'kicadSymbolki_keywords': 'quad opamp', 'kicadSymbolki_description': 'Quad Low Power, Low Noise Operational Amplifiers, DIP-14/SOIC-14/SSOP-14', 'kicadSymbolki_fp_filters': 'SOIC*3.9x8.7mm*P1.27mm* DIP*W7.62mm* TSSOP*4.4x5mm*P0.65mm* SSOP*5.3x6.2mm*P0.65mm* MSOP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Amplifier_Operational : MC33179')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart



######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "TSV994"
    hexID = "SZKAMPLIFIEROPERATIONALTSV994"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM2902', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TSV994', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/tsv994.pdf', 'kicadSymbolki_keywords': 'quad opamp', 'kicadSymbolki_description': 'Quad Rail-to-rail, 20 MHz GBP, operational amplifiers, SOIC-14/TSSOP-14', 'kicadSymbolki_fp_filters': 'SOIC*3.9x8.7mm*P1.27mm* DIP*W7.62mm* TSSOP*4.4x5mm*P0.65mm* SSOP*5.3x6.2mm*P0.65mm* MSOP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Amplifier_Operational : TSV994')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart



######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "TSV912IDT"
    hexID = "SZKAMPLIFIEROPERATIONALTSV912IDT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM2904', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TSV912IDT', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'www.st.com/resource/en/datasheet/tsv911.pdf', 'kicadSymbolki_keywords': 'dual opamp', 'kicadSymbolki_description': 'Dual rail-to-rail input/output 8 MHz operational amplifiers, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* DIP*W7.62mm* TO*99* OnSemi*Micro8* TSSOP*3x3mm*P0.65mm* TSSOP*4.4x3mm*P0.65mm* MSOP*3x3mm*P0.65mm* SSOP*3.9x4.9mm*P0.635mm* LFCSP*2x2mm*P0.5mm* *SIP* SOIC*5.3x6.2mm*P1.27mm*'}])
    newPart['name'].append('Amplifier_Operational : TSV912IDT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


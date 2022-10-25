
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "TSV912IQ2T"
    hexID = "SZKAMPLIFIEROPERATIONALTSV912IQ2T"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TSV912IQ2T', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8-1EP_2x2mm_P0.5mm_EP1.05x1.75mm', 'kicadSymbolDatasheet': 'www.st.com/resource/en/datasheet/tsv911.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'dual opamp', 'kicadSymbolki_description': 'Dual rail-to-rail input/output 8 MHz operational amplifiers, DFN-8', 'kicadSymbolki_fp_filters': 'DFN*2x2mm*P0.5mm*'}])
    newPart['name'].append('Amplifier_Operational : TSV912IQ2T')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart



######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "LM358_DFN"
    hexID = "SZKAMPLIFIEROPERATIONALLM358DFN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TSV912IQ2T', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM358_DFN', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8-1EP_2x2mm_P0.5mm_EP1.05x1.75mm', 'kicadSymbolDatasheet': 'www.st.com/resource/en/datasheet/lm358.pdf', 'kicadSymbolki_keywords': 'dual opamp', 'kicadSymbolki_description': 'Low-Power, Dual Operational Amplifiers, DFN-8', 'kicadSymbolki_fp_filters': 'DFN*2x2mm*P0.5mm*'}])
    newPart['name'].append('Amplifier_Operational : LM358_DFN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


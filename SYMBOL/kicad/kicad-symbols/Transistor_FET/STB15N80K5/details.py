
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "STB15N80K5"
    hexID = "SZKTRANSISTORFETSTB15N8K5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'STB15N80K5', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-2', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/stb15n80k5.pdf', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '14A Id, 800V Vds, N-Channel MOSFET, 375mOhm Ron, D2PAK', 'kicadSymbolki_fp_filters': 'TO?263*'}])
    newPart['name'].append('Transistor_FET : STB15N80K5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


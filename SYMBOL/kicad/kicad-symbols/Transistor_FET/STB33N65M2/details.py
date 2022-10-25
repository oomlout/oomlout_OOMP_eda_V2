
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "STB33N65M2"
    hexID = "SZKTRANSISTORFETSTB33N65M2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STB15N80K5', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'STB33N65M2', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-2', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/stb33n65m2.pdf', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '24A Id, 650V Vds, N-Channel MDmesh M2 MOSFET, 140mOhm Ron, D2PAK', 'kicadSymbolki_fp_filters': 'TO?263*'}])
    newPart['name'].append('Transistor_FET : STB33N65M2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart



######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "STS2DNE60"
    hexID = "SZKTRANSISTORFETSTS2DNE6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'FDS6890A', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'STS2DNE60', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/CD00001537.pdf', 'kicadSymbolki_keywords': 'Dual N-Channel MOSFET', 'kicadSymbolki_description': '2A Id, 60V Vds, Dual N-Channel MOSFET, 180mOhm Ron, SO-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Transistor_FET : STS2DNE60')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


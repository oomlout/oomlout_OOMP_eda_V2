
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Comparator"
    oIndex = "LMV339"
    hexID = "SZKCOMPARATORLMV339"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM339', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LMV339', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/lmv331.pdf', 'kicadSymbolki_keywords': 'cmp open collector', 'kicadSymbolki_description': 'Quad General-Purpose Low-Voltage Comparator, SOIC-14/TSSOP-14', 'kicadSymbolki_fp_filters': 'SOIC*3.9x8.7mm*P1.27mm* TSSOP*4.4x5mm*P0.65mm*'}])
    newPart['name'].append('Comparator : LMV339')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


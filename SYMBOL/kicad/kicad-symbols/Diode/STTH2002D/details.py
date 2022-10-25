
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "STTH2002D"
    hexID = "SZKDIODESTTH22D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'STTH2002D', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-2_Vertical', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/stth2002.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': '200V 20A Ultrafast Recovery Diode, TO-220', 'kicadSymbolki_fp_filters': 'TO?220*2*'}])
    newPart['name'].append('Diode : STTH2002D')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


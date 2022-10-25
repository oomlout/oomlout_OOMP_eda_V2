
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "2N7000"
    hexID = "SZKTRANSISTORFET2N7"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': '2N7000', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-92_Inline', 'kicadSymbolDatasheet': 'https://www.vishay.com/docs/70226/70226.pdf', 'kicadSymbolki_keywords': 'N-Channel MOSFET Logic-Level', 'kicadSymbolki_description': '0.2A Id, 200V Vds, N-Channel MOSFET, 2.6V Logic Level, TO-92', 'kicadSymbolki_fp_filters': 'TO?92*'}])
    newPart['name'].append('Transistor_FET : 2N7000')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


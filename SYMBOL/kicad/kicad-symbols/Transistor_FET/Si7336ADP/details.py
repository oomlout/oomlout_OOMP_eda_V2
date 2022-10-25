
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "Si7336ADP"
    hexID = "SZKTRANSISTORFETSI7336ADP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'Si7336ADP', 'kicadSymbolFootprint': 'Package_SO:PowerPAK_SO-8_Single', 'kicadSymbolDatasheet': 'https://www.vishay.com/docs/73152/si7336adp.pdf', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '30A Id, 30V Vds, 2.4mOhm Ron, PowerPAK-8', 'kicadSymbolki_fp_filters': 'PowerPAK*SO*Single*'}])
    newPart['name'].append('Transistor_FET : Si7336ADP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


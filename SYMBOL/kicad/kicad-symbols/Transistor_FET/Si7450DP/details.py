
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "Si7450DP"
    hexID = "SZKTRANSISTORFETSI745DP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'Si7336ADP', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'Si7450DP', 'kicadSymbolFootprint': 'Package_SO:PowerPAK_SO-8_Single', 'kicadSymbolDatasheet': 'https://www.vishay.com/docs/71432/si7450dp.pdf', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '5.3A Id, 200V Vds, 80mOhm Ron, PowerPAK-8', 'kicadSymbolki_fp_filters': 'PowerPAK*SO*Single*'}])
    newPart['name'].append('Transistor_FET : Si7450DP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart



######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "PMN48XP"
    hexID = "SZKTRANSISTORFETPMN48XP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'PMN48XP', 'kicadSymbolFootprint': 'Package_SO:TSOP-6_1.65x3.05mm_P0.95mm', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/PMN48XP.pdf', 'kicadSymbolki_keywords': 'P-Channel MOSFET', 'kicadSymbolki_description': '-4.1A Id, -20V Vds, P-Channel Power MOSFET, 48mOhm Ron, SC-74-6', 'kicadSymbolki_fp_filters': 'TSOP*1.65x3.05mm*P0.95mm*'}])
    newPart['name'].append('Transistor_FET : PMN48XP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


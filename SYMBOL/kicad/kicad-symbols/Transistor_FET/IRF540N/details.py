
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF540N"
    hexID = "SZKTRANSISTORFETIRF54N"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BUZ11', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF540N', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-3_Vertical', 'kicadSymbolDatasheet': 'http://www.irf.com/product-info/datasheets/data/irf540n.pdf', 'kicadSymbolki_keywords': 'HEXFET N-Channel MOSFET', 'kicadSymbolki_description': '33A Id, 100V Vds, HEXFET N-Channel MOSFET, TO-220', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('Transistor_FET : IRF540N')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


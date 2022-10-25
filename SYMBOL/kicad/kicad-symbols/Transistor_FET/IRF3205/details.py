
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF3205"
    hexID = "SZKTRANSISTORFETIRF325"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BUZ11', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF3205', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-3_Vertical', 'kicadSymbolDatasheet': 'http://www.irf.com/product-info/datasheets/data/irf3205.pdf', 'kicadSymbolki_keywords': 'Single N-Channel HEXFET Power MOSFET', 'kicadSymbolki_description': '110A Id, 55V Vds, Single N-Channel HEXFET Power MOSFET, 8mOhm Ron, TO-220AB', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('Transistor_FET : IRF3205')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


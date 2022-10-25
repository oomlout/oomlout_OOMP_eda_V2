
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRLIZ44N"
    hexID = "SZKTRANSISTORFETIRLIZ44N"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRLIZ44N', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220F-3_Vertical', 'kicadSymbolDatasheet': 'http://www.irf.com/product-info/datasheets/data/irliz44n.pdf', 'kicadSymbolki_keywords': 'N-Channel HEXFET MOSFET Logic-Level', 'kicadSymbolki_description': '30A Id, 55V Vds, 22mOhm Rds, N-Channel HEXFET Power MOSFET, TO-220AB', 'kicadSymbolki_fp_filters': 'TO?220F*'}])
    newPart['name'].append('Transistor_FET : IRLIZ44N')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


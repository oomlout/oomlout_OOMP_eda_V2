
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "FDG6335N"
    hexID = "SZKTRANSISTORFETFDG6335N"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'FDG1024NZ', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'FDG6335N', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'kicadSymbolDatasheet': 'http://www.gneic.com/product/datasheet/FDG6335N-1122853.pdf', 'kicadSymbolki_keywords': 'Dual N-Channel MOSFET', 'kicadSymbolki_description': '0.7A Id, 20V Vds, Dual N-Channel MOSFET, 300mOhm Ron, SC-70-6', 'kicadSymbolki_fp_filters': 'SOT?363*'}])
    newPart['name'].append('Transistor_FET : FDG6335N')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


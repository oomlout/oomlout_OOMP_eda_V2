
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "FDN340P"
    hexID = "SZKTRANSISTORFETFDN34P"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TP0610T', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'FDN340P', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/FDN340P-D.PDF', 'kicadSymbolki_keywords': 'P-Channel MOSFET', 'kicadSymbolki_description': '2A Id, 20V Vds, P-Channel MOSFET, 70mOhm Ron, SOT-23', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Transistor_FET : FDN340P')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


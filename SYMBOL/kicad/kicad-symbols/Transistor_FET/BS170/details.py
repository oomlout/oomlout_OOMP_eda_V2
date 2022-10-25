
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "BS170"
    hexID = "SZKTRANSISTORFETBS17"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BS107', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BS170', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-92_Inline', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/BS170-D.PDF', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '0.5A Id, 60V Vds, N-Channel MOSFET, TO-92', 'kicadSymbolki_fp_filters': 'TO?92*'}])
    newPart['name'].append('Transistor_FET : BS170')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


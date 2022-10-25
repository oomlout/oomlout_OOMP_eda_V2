
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "C3M0120100J"
    hexID = "SZKTRANSISTORFETC3M121J"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'C3M0065090J', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'C3M0120100J', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-7_TabPin8', 'kicadSymbolDatasheet': 'https://www.wolfspeed.com/media/downloads/957/C3M0120100J.pdf', 'kicadSymbolki_keywords': 'N-Channel SiC MOSFET', 'kicadSymbolki_description': '22A Id, 1000V Vds, 120mOhm, N-Channel SiC MOSFET, TO-263-7', 'kicadSymbolki_fp_filters': 'TO?263*TabPin8*'}])
    newPart['name'].append('Transistor_FET : C3M0120100J')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart



######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "C3M0120090D"
    hexID = "SZKTRANSISTORFETC3M129D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'C3M0065090D', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'C3M0120090D', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-247-3_Vertical', 'kicadSymbolDatasheet': 'https://www.wolfspeed.com/media/downloads/824/C3M0120090D.pdf', 'kicadSymbolki_keywords': 'N-Channel SiC MOSFET', 'kicadSymbolki_description': '23A Id, 900V Vds, 120mOhm, N-Channel SiC MOSFET, TO-247', 'kicadSymbolki_fp_filters': 'TO?247*'}])
    newPart['name'].append('Transistor_FET : C3M0120090D')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


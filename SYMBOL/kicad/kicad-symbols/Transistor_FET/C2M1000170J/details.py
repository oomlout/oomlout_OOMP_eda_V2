
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "C2M1000170J"
    hexID = "SZKTRANSISTORFETC2M117J"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'C3M0065090J', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'C2M1000170J', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-7_TabPin8', 'kicadSymbolDatasheet': 'https://www.wolfspeed.com/media/downloads/820/C2M1000170J.pdf', 'kicadSymbolki_keywords': 'N-Channel SiC MOSFET', 'kicadSymbolki_description': '5.3A Id, 1700V Vds, 1000mOhm, N-Channel SiC MOSFET, TO-263-7', 'kicadSymbolki_fp_filters': 'TO?263*TabPin8*'}])
    newPart['name'].append('Transistor_FET : C2M1000170J')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


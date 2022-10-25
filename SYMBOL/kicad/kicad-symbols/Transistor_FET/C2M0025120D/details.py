
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "C2M0025120D"
    hexID = "SZKTRANSISTORFETC2M2512D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'C3M0065090D', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'C2M0025120D', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-247-3_Vertical', 'kicadSymbolDatasheet': 'https://www.wolfspeed.com/media/downloads/161/C2M0025120D.pdf', 'kicadSymbolki_keywords': 'N-Channel SiC MOSFET', 'kicadSymbolki_description': '90A Id, 1200V Vds, 25mOhm, N-Channel SiC MOSFET, TO-247', 'kicadSymbolki_fp_filters': 'TO?247*'}])
    newPart['name'].append('Transistor_FET : C2M0025120D')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


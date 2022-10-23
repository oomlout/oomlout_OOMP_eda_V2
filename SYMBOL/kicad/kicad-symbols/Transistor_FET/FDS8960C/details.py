
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "FDS8960C"
    hexID = "SZKTRANSISTORFETFDS896C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IRF7309IPBF', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'FDS8960C', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.mouser.fr/datasheet/2/308/FDS8960C-D-1808807.pdf', 'kicadSymbolki_keywords': 'Dual N-Channel P-Channel MOSFET', 'kicadSymbolki_description': '7A Id, 35V Vds, Dual N and P Channel MOSFET, 24mOhm Ron, 10V Vgs, SO8L', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('FDS8960C')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart



######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "FDMC8032L"
    hexID = "SZKTRANSISTORFETFDMC832L"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'FDMC8032L', 'kicadSymbolFootprint': 'Package_SON:Fairchild_DualPower33-6_3x3mm', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/FDMC8032L-D.PDF', 'kicadSymbolki_keywords': 'Dual N-Channel MOSFET', 'kicadSymbolki_description': '7A Id, 40V Vds, Dual N-Channel MOSFET, 20mOhm Ron, Power33 Package', 'kicadSymbolki_fp_filters': 'Fairchild*DualPower33*3x3mm*'}])
    newPart['name'].append('FDMC8032L')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


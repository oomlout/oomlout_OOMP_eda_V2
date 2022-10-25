
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "AON6411"
    hexID = "SZKTRANSISTORFETAON6411"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'AON6411', 'kicadSymbolFootprint': 'Package_DFN_QFN:AO_DFN-8-1EP_5.55x5.2mm_P1.27mm_EP4.12x4.6mm', 'kicadSymbolDatasheet': 'http://www.aosmd.com/res/data_sheets/AON6411.pdf', 'kicadSymbolki_keywords': 'P-Channel MOSFET', 'kicadSymbolki_description': 'P-Channel MOSFET, -85A Id, -20V Vds, DFN-8', 'kicadSymbolki_fp_filters': 'AO*DFN*8*1EP*5.55x5.2mm*P1.27mm*EP4.12x4.6mm*'}])
    newPart['name'].append('Transistor_FET : AON6411')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


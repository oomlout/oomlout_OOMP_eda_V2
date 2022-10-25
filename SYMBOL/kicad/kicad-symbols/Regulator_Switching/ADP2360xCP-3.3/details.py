
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "ADP2360xCP-3.3"
    hexID = "SZKREGULATORSWITCHINGADP236XCP33"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ADP2360xCP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADP2360xCP-3.3', 'kicadSymbolFootprint': 'Package_CSP:LFCSP-WD-8-1EP_3x3mm_P0.65mm_EP1.6x2.44mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADP2360.pdf', 'kicadSymbolki_keywords': 'Step-Down Buck Regulator', 'kicadSymbolki_description': 'High Efficiency Buck Regulator, Vin 60V, Vout 3.3V, 50mA, LFCSP-8', 'kicadSymbolki_fp_filters': 'LFCSP*1EP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Regulator_Switching : ADP2360xCP-3.3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


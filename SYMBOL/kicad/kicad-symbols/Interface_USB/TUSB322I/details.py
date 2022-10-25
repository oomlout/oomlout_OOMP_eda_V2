
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "TUSB322I"
    hexID = "SZKINTERFACEUTU322I"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TUSB322I', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_X2QFN-12_1.6x1.6mm_P0.4mm', 'kicadSymbolDatasheet': 'www.ti.com/lit/ds/symlink/tusb322i.pdf', 'kicadSymbolki_keywords': 'USB VCONN PD CC', 'kicadSymbolki_description': 'USB Type-C Configuration Channel Logic and Port Control with VCONN, X2QFN-12', 'kicadSymbolki_fp_filters': 'Texas?X2QFN*1.6x1.6mm*P0.4mm*'}])
    newPart['name'].append('Interface_USB : TUSB322I')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


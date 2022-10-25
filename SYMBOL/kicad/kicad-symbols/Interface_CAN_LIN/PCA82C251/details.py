
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_CAN_LIN"
    oIndex = "PCA82C251"
    hexID = "SZKINTERFACECANLINPCA82C251"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PCA82C251', 'kicadSymbolFootprint': 'Package_SO:SO-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.nxp.com/documents/data_sheet/PCA82C251.pdf', 'kicadSymbolki_keywords': 'BUS CAN', 'kicadSymbolki_description': 'CAN Transceiver for 24V Systems, SO-8', 'kicadSymbolki_fp_filters': 'SO*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Interface_CAN_LIN : PCA82C251')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


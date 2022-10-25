
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "ISL3298xxRT"
    hexID = "SZKINTERFACEUARTISL3298XXRT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ISL3298xxRT', 'kicadSymbolFootprint': 'Package_DFN_QFN:TDFN-8-1EP_3x2mm_P0.5mm_EP1.80x1.65mm', 'kicadSymbolDatasheet': 'https://www.renesas.com/sg/en/www/doc/datasheet/isl3295e-98e.pdf', 'kicadSymbolki_keywords': 'RS485 RS422 transceiver', 'kicadSymbolki_description': 'RS485, RS422, 20Mbps Transceiver, 3.0V to 7V, Low-Power, TDFN-8', 'kicadSymbolki_fp_filters': 'TDFN*1EP*3x2mm*P0.5mm*'}])
    newPart['name'].append('Interface_UART : ISL3298xxRT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


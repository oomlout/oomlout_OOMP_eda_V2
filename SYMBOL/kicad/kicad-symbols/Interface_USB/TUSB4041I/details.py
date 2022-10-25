
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "TUSB4041I"
    hexID = "SZKINTERFACEUTU441I"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TUSB4041I', 'kicadSymbolFootprint': 'Package_QFP:HTQFP-64-1EP_10x10mm_P0.5mm_EP8x8mm_Mask4.4x4.4mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tusb4041i.pdf', 'kicadSymbolki_keywords': 'USB2.0 hub', 'kicadSymbolki_description': 'four port USB 2.0 Hub', 'kicadSymbolki_fp_filters': 'HTQFP*10x10mm*P0.5mm*'}])
    newPart['name'].append('Interface_USB : TUSB4041I')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


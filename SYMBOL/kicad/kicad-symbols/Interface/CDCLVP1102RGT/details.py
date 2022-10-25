
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface"
    oIndex = "CDCLVP1102RGT"
    hexID = "SZKINTERFACECDCLVP112RGT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CDCLVP1102RGT', 'kicadSymbolFootprint': 'Package_DFN_QFN:VQFN-16-1EP_3x3mm_P0.5mm_EP1.6x1.6mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/cdclvp1102.pdf', 'kicadSymbolki_keywords': 'Clock Buffer LVDS', 'kicadSymbolki_description': 'Two-LVPECL Output, High-Performance Clock Buffer, VQFN-16', 'kicadSymbolki_fp_filters': 'VQFN*1EP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Interface : CDCLVP1102RGT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


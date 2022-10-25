
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "FPGA_Lattice"
    oIndex = "ICE40UL1K-SWG16"
    hexID = "SZKFPGALATTICEICE4UL1KSWG16"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ICE40UL1K-SWG16', 'kicadSymbolFootprint': 'Package_CSP:WLCSP-16_1.409x1.409mm_P0.35mm', 'kicadSymbolDatasheet': 'https://www.latticesemi.com/view_document?document_id=50945', 'kicadSymbolki_keywords': 'FPGA programmable logic', 'kicadSymbolki_description': 'iCE40 UltraPlus FPGA, 1.2V, WLCSP-16', 'kicadSymbolki_fp_filters': 'WLCSP*1.409x1.409mm*P0.35mm*'}])
    newPart['name'].append('FPGA_Lattice : ICE40UL1K-SWG16')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


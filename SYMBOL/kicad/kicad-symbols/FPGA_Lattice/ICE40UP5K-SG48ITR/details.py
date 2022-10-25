
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "FPGA_Lattice"
    oIndex = "ICE40UP5K-SG48ITR"
    hexID = "SZKFPGALATTICEICE4UP5KSG48ITR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ICE40UP5K-SG48ITR', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-48-1EP_7x7mm_P0.5mm_EP5.6x5.6mm', 'kicadSymbolDatasheet': 'http://www.latticesemi.com/Products/FPGAandCPLD/iCE40Ultra', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'FPGA programmable logic', 'kicadSymbolki_description': 'iCE40 UltraPlus FPGA, 5280 LUTs, 1.2V, 48-pin QFN', 'kicadSymbolki_fp_filters': 'QFN*7x7mm*P0.5mm*EP5.6x5.6mm*'}])
    newPart['name'].append('FPGA_Lattice : ICE40UP5K-SG48ITR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


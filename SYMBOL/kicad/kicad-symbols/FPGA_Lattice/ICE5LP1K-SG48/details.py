
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "FPGA_Lattice"
    oIndex = "ICE5LP1K-SG48"
    hexID = "SZKFPGALATTICEICE5LP1KSG48"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ICE40UP5K-SG48ITR', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ICE5LP1K-SG48', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-48-1EP_7x7mm_P0.5mm_EP5.6x5.6mm', 'kicadSymbolDatasheet': 'http://www.latticesemi.com/Products/FPGAandCPLD/iCE40Ultra', 'kicadSymbolki_keywords': 'FPGA programmable logic', 'kicadSymbolki_description': 'iCE40 Ultra FPGA, 1100 LUTs, 1.2V, 48-pin QFN', 'kicadSymbolki_fp_filters': 'QFN*7x7mm*P0.5mm*EP5.6x5.6mm*'}])
    newPart['name'].append('ICE5LP1K-SG48')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart



######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "FPGA_Lattice"
    oIndex = "ICE40HX8K-BG121"
    hexID = "SZKFPGALATTICEICE4HX8KBG121"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ICE40HX8K-BG121', 'kicadSymbolFootprint': 'Package_BGA:BGA-121_9.0x9.0mm_Layout11x11_P0.8mm_Ball0.4mm_Pad0.35mm_NSMD', 'kicadSymbolDatasheet': 'http://www.latticesemi.com/Products/FPGAandCPLD/iCE40', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'FPGA programmable logic', 'kicadSymbolki_description': 'iCE40 HX FPGA, 7680 LUTs, 1.2V, BGA-121', 'kicadSymbolki_fp_filters': 'BGA*9.0x9.0mm*Layout11x11*P0.8mm*Ball0.4mm*'}])
    newPart['name'].append('ICE40HX8K-BG121')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


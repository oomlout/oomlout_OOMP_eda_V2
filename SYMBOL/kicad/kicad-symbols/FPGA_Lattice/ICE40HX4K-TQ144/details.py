
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "FPGA_Lattice"
    oIndex = "ICE40HX4K-TQ144"
    hexID = "SZKFPGALATTICEICE4HX4KTQ144"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ICE40HX4K-TQ144', 'kicadSymbolFootprint': 'Package_QFP:TQFP-144_20x20mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.latticesemi.com/Products/FPGAandCPLD/iCE40', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'FPGA programmable logic', 'kicadSymbolki_description': 'iCE40 HX FPGA, 3520 LUTs, 1.2V, TQFP-144', 'kicadSymbolki_fp_filters': 'TQFP*20x20mm*P0.5mm*'}])
    newPart['name'].append('ICE40HX4K-TQ144')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


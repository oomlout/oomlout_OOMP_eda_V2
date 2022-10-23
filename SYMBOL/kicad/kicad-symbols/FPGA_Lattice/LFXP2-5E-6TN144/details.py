
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "FPGA_Lattice"
    oIndex = "LFXP2-5E-6TN144"
    hexID = "SZKFPGALATTICELFXP25E6TN144"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LFXP2-5E-5TN144', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LFXP2-5E-6TN144', 'kicadSymbolFootprint': 'Package_QFP:TQFP-144_20x20mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.latticesemi.com/view_document?document_id=24635', 'kicadSymbolki_keywords': 'FPGA Lattice XP2', 'kicadSymbolki_description': 'FPGA, 5000 LUTs, 1.2V, TQFP-144', 'kicadSymbolki_fp_filters': 'TQFP*20x20mm*'}])
    newPart['name'].append('LFXP2-5E-6TN144')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


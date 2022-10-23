
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "FPGA_Lattice"
    oIndex = "LFE5UM5G-85F-8BG756x"
    hexID = "SZKFPGALATTICELFE5UM5G85F8BG756X"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LFE5UM5G-85F-8BG756x', 'kicadSymbolFootprint': 'Package_BGA:Lattice_caBGA-756_27.0x27.0mm_Layout32x32_P0.8mm', 'kicadSymbolDatasheet': 'https://www.latticesemi.com/view_document?document_id=50461', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'FPGA programmable logic', 'kicadSymbolki_description': 'ECP5-5G FPGA, 84K LUTs, 1.2V, 5Gbps SERDES, BGA-756', 'kicadSymbolki_fp_filters': 'Lattice*caBGA*27.0x27.0mm*Layout32x32*P0.8mm*'}])
    newPart['name'].append('LFE5UM5G-85F-8BG756x')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


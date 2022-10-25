
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "FPGA_Lattice"
    oIndex = "LFE5U-85F-7BG756x"
    hexID = "SZKFPGALATTICELFE5U85F7BG756X"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LFE5U-85F-8BG756x', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LFE5U-85F-7BG756x', 'kicadSymbolFootprint': 'Package_BGA:Lattice_caBGA-756_27.0x27.0mm_Layout32x32_P0.8mm', 'kicadSymbolDatasheet': 'https://www.latticesemi.com/view_document?document_id=50461', 'kicadSymbolki_keywords': 'FPGA programmable logic', 'kicadSymbolki_description': 'ECP5 FPGA, 84K LUTs, 1.2V, BGA-756', 'kicadSymbolki_fp_filters': 'Lattice*caBGA*27.0x27.0mm*Layout32x32*P0.8mm*'}])
    newPart['name'].append('FPGA_Lattice : LFE5U-85F-7BG756x')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


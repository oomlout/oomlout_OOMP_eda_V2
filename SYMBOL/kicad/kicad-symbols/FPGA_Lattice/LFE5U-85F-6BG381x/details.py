
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "FPGA_Lattice"
    oIndex = "LFE5U-85F-6BG381x"
    hexID = "SZKFPGALATTICELFE5U85F6BG381X"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LFE5U-85F-8BG381x', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LFE5U-85F-6BG381x', 'kicadSymbolFootprint': 'Package_BGA:Lattice_caBGA-381_17.0x17.0mm_Layout20x20_P0.8mm_Ball0.4mm_Pad0.4mm_NSMD', 'kicadSymbolDatasheet': 'https://www.latticesemi.com/view_document?document_id=50461', 'kicadSymbolki_keywords': 'FPGA programmable logic', 'kicadSymbolki_description': 'ECP5 FPGA, 84K LUTs, 1.2V, BGA-381', 'kicadSymbolki_fp_filters': 'Lattice*caBGA*17.0x17.0mm*Layout20x20*P0.8mm*'}])
    newPart['name'].append('FPGA_Lattice : LFE5U-85F-6BG381x')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


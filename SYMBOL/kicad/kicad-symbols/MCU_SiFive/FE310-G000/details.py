
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_SiFive"
    oIndex = "FE310-G000"
    hexID = "SZKMCUSIFIVEFE31G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FE310-G000', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-48-1EP_6x6mm_P0.4mm_EP4.2x4.2mm_ThermalVias', 'kicadSymbolDatasheet': 'https://sifive.cdn.prismic.io/sifive%2Ffeb6f967-ff96-418f-9af4-a7f3b7fd1dfc_fe310-g000-ds.pdf', 'kicadSymbolki_keywords': 'microcontroller RISC-V SiFive', 'kicadSymbolki_description': 'RISC-V MCU, 8KB OTP Program Memory, 8KB ROM, 16KB Instruction Cache, 16KB SRAM, 320MHz, 1.8 and 3.6V, 24 GPIO, QFN-48', 'kicadSymbolki_fp_filters': 'QFN*1EP*6x6mm*P0.4mm*'}])
    newPart['name'].append('MCU_SiFive : FE310-G000')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


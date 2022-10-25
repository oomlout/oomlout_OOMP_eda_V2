
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "DSP_Microchip_DSPIC33"
    oIndex = "DSPIC33FJ64GP804"
    hexID = "SZKDSPMCHIPDSPIC33DSPIC33FJ64GP84"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DSPIC33FJ64GP804', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/70292G.pdf', 'kicadSymbolki_keywords': '16-bit Digital Signal Controller Microchip dsPIC33', 'kicadSymbolki_description': '40MIPS, 64k Flash, 16k SRAM, ECAN, Audio DAC', 'kicadSymbolki_fp_filters': 'QFN?44*1EP*8x8mm*P0.65mm* TQFP?44*10x10mm*P0.8mm*'}])
    newPart['name'].append('DSP_Microchip_DSPIC33 : DSPIC33FJ64GP804')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart



######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "DSP_Microchip_DSPIC33"
    oIndex = "DSPIC33FJ64GP306A-IMR"
    hexID = "SZKDSPMCHIPDSPIC33DSPIC33FJ64GP36AIMR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DSPIC33FJ64GP306A-IMR', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-64-1EP_9x9mm_P0.5mm_EP5.4x5.4mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/70593d.pdf', 'kicadSymbolki_keywords': '16-bit Digital Signal Controller Microchip dsPIC', 'kicadSymbolki_description': '40MIPS, 64k Flash, 16k SRAM, QFN-64', 'kicadSymbolki_fp_filters': 'QFN*9x9mm*P0.5mm*'}])
    newPart['name'].append('DSP_Microchip_DSPIC33 : DSPIC33FJ64GP306A-IMR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


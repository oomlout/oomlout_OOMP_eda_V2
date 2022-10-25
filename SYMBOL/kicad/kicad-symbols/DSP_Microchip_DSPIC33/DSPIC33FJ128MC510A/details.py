
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "DSP_Microchip_DSPIC33"
    oIndex = "DSPIC33FJ128MC510A"
    hexID = "SZKDSPMCHIPDSPIC33DSPIC33FJ128MC51A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'DSPIC33FJ256MC710A', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DSPIC33FJ128MC510A', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/70594C.pdf', 'kicadSymbolki_keywords': '16-bit Digital Signal Controller Microchip dsPIC', 'kicadSymbolki_description': 'High-Performance, 16-bit Digital Signal Controller, 40MIPS, 128k Flash, 8k SRAM, TQFP-100', 'kicadSymbolki_fp_filters': 'TQFP*12x12mm*P0.4mm* TQFP*14x14mm*P0.5mm*'}])
    newPart['name'].append('DSP_Microchip_DSPIC33 : DSPIC33FJ128MC510A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart



######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "DSP_Microchip_DSPIC33"
    oIndex = "DSPIC33FJ64MC802-xSP"
    hexID = "SZKDSPMCHIPDSPIC33DSPIC33FJ64MC82XSP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DSPIC33FJ64MC802-xSP', 'kicadSymbolFootprint': 'Package_DIP:DIP-28_W7.62mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/70291G.pdf', 'kicadSymbolki_keywords': '16-bit Digital Signal Controller Microchip dsPIC', 'kicadSymbolki_description': '40 MIPS, 64k Flash, 16k SRAM, DIP-28', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('DSP_Microchip_DSPIC33 : DSPIC33FJ64MC802-xSP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


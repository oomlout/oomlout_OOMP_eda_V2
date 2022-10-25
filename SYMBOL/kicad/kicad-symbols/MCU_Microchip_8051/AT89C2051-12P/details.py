
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_8051"
    oIndex = "AT89C2051-12P"
    hexID = "SZKMCUMCHIP851AT89C25112P"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AT89C2051-12P', 'kicadSymbolFootprint': 'Package_DIP:DIP-20_W7.62mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/doc0368.pdf', 'kicadSymbolki_keywords': 'MCS-51 8bit Flash Microcontroller', 'kicadSymbolki_description': '12MHz, 2kB Flash, 128B SRAM, DIP-20', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('MCU_Microchip_8051 : AT89C2051-12P')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


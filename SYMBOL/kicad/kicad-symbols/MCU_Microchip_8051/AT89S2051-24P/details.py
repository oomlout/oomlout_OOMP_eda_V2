
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_8051"
    oIndex = "AT89S2051-24P"
    hexID = "SZKMCUMCHIP851AT89S25124P"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AT89C2051-12P', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AT89S2051-24P', 'kicadSymbolFootprint': 'Package_DIP:DIP-20_W7.62mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/doc3390.pdf', 'kicadSymbolki_keywords': 'MCS-51 8bit Flash Microcontroller', 'kicadSymbolki_description': '24MHz, 2kB Flash, 256B SRAM, DIP-20', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('MCU_Microchip_8051 : AT89S2051-24P')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


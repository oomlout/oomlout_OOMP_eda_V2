
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC12"
    oIndex = "PIC12CR509A-ISN"
    hexID = "SZKMCUMCHIPPIC12PIC12CR59AISN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC12CR509A-IP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC12CR509A-ISN', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/devicedoc/40139e.pdf', 'kicadSymbolki_keywords': '8-Bit CMOS Microcontroller', 'kicadSymbolki_description': 'PIC12CR509A, 1024W ROM, 41B SRAM, SO8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('MCU_Microchip_PIC12 : PIC12CR509A-ISN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


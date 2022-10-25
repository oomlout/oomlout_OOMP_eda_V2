
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Module"
    oIndex = "Sipeed-M1"
    hexID = "SZKMCUMOSIPEEDM1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'A', 'kicadSymbolValue': 'Sipeed-M1', 'kicadSymbolFootprint': 'Module:Sipeed-M1', 'kicadSymbolDatasheet': 'https://dl.sipeed.com/MAIX/HDK/Sipeed-M1&M1W/Specifications', 'kicadSymbolki_keywords': 'AI Kendryte K210 RISC-V', 'kicadSymbolki_description': 'AI accelerated RISC-V microcontroller', 'kicadSymbolki_fp_filters': 'Sipeed*M1*'}])
    newPart['name'].append('MCU_Module : Sipeed-M1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


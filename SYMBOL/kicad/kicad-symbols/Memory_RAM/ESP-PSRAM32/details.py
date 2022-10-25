
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_RAM"
    oIndex = "ESP-PSRAM32"
    hexID = "SZKMEMORYRAMESPPSRAM32"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ESP-PSRAM32', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.espressif.com/sites/default/files/documentation/esp-psram32_datasheet_en.pdf', 'kicadSymbolki_keywords': '32 Mbit serial pseudo SRAM MEMORY', 'kicadSymbolki_description': '32 Mbit serial pseudo SRAM device organized as 4Mx8 bits, 1.8 VCC, SOIC8 (SOP8)', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm?P1.27mm*'}])
    newPart['name'].append('Memory_RAM : ESP-PSRAM32')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


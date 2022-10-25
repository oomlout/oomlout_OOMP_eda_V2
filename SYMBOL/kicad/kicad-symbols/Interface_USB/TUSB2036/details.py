
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "TUSB2036"
    hexID = "SZKINTERFACEUTU236"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TUSB2036', 'kicadSymbolFootprint': 'Package_QFP:LQFP-32_7x7mm_P0.8mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tusb2036.pdf', 'kicadSymbolki_keywords': '2-Port, 3-Port, 3.3V, EEPROM, Full Speed, Hub, Texas Instruments, USB1.1', 'kicadSymbolki_description': '2- or 3-Port USB1.1 HUB with optional serial EEPROM', 'kicadSymbolki_fp_filters': 'LQFP*7x7mm*P0.8mm*'}])
    newPart['name'].append('Interface_USB : TUSB2036')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


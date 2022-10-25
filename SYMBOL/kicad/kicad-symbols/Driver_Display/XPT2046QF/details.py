
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Display"
    oIndex = "XPT2046QF"
    hexID = "SZKDRIVERDIXPT246QF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'XPT2046QF', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-16-1EP_4x4mm_P0.65mm_EP2.1x2.1mm', 'kicadSymbolDatasheet': 'http://www.xptek.cn/uploadfile/download/201707171401161883.pdf', 'kicadSymbolki_keywords': 'Single-supply, 12bit, 4 ch, touch screen driver, 2.2 - 5.25 VDD, -40 to +85 C, QSPI, SPI, 3-wire serial interface, QFN-16', 'kicadSymbolki_description': 'Single-supply, 12bit, 4 ch, touch screen driver, 2.2 - 5.25 VDD, -40 to +85 C, QSPI, SPI, 3-wire serial interface, QFN-16', 'kicadSymbolki_fp_filters': '*QFN*1EP*4x4mm*P0.65mm*'}])
    newPart['name'].append('Driver_Display : XPT2046QF')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


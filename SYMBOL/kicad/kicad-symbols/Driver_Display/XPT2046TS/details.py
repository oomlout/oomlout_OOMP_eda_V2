
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Display"
    oIndex = "XPT2046TS"
    hexID = "SZKDRIVERDIXPT246TS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'XPT2046TS', 'kicadSymbolFootprint': 'Package_SO:TSSOP-16_4.4x5mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.xptek.cn/uploadfile/download/201707171401161883.pdf', 'kicadSymbolki_keywords': 'Single-supply, 12bit, 4 ch, touch screen driver, 2.2 - 5.25 VDD, -40 to +85 C, QSPI, SPI, 3-wire serial interface, TSSOP-16', 'kicadSymbolki_description': 'Single-supply, 12bit, 4 ch, touch screen driver, 2.2 - 5.25 VDD, -40 to +85 C, QSPI, SPI, 3-wire serial interface, TSSOP-16', 'kicadSymbolki_fp_filters': '*TSSOP*4.4x5mm*P0.65mm*'}])
    newPart['name'].append('Driver_Display : XPT2046TS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


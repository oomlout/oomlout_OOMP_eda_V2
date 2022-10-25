
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Display"
    oIndex = "ADS7843E"
    hexID = "SZKDRIVERDIADS7843E"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADS7843E', 'kicadSymbolFootprint': 'Package_SO:SSOP-16_3.9x4.9mm_P0.635mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ads7843.pdf', 'kicadSymbolki_keywords': 'Single-supply, 12bit, 4 ch, touch screen driver, 2.2 - 5.25 VDD, -40 to +85 C, QSPI, SPI, 3-wire serial interface, SSOP-16', 'kicadSymbolki_description': 'Single-supply, 12bit, 4 ch, touch screen driver, 2.2 - 5.25 VDD, -40 to +85 C, QSPI, SPI, 3-wire serial interface, SSOP-16', 'kicadSymbolki_fp_filters': '*SSOP*3.9x4.9mm*P0.635mm*'}])
    newPart['name'].append('Driver_Display : ADS7843E')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


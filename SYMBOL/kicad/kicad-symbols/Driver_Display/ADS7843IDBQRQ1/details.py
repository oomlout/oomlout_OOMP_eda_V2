
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Display"
    oIndex = "ADS7843IDBQRQ1"
    hexID = "SZKDRIVERDIADS7843IDBQRQ1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ADS7843E', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADS7843IDBQRQ1', 'kicadSymbolFootprint': 'Package_SO:SSOP-16_3.9x4.9mm_P0.635mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ads7843-q1.pdf', 'kicadSymbolki_keywords': 'Single-supply, 12bit, 4 ch, touch screen driver, 2.2 - 5.25 VDD, -40 to +125 C, QSPI, SPI, 3-wire serial interface, SSOP-16', 'kicadSymbolki_description': 'Single-supply, 12bit, 4 ch, touch screen driver, 2.2 - 5.25 VDD, -40 to +125 C, QSPI, SPI, 3-wire serial interface, SSOP-16', 'kicadSymbolki_fp_filters': '*SSOP*3.9x4.9mm*P0.635mm*'}])
    newPart['name'].append('ADS7843IDBQRQ1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


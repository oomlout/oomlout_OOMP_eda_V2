
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_AM_FM"
    oIndex = "SA636DK"
    hexID = "SZKRFAMFMSA636DK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SA636DK', 'kicadSymbolFootprint': 'Package_SO:SSOP-20_4.4x6.5mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/SA636.pdf', 'kicadSymbolki_keywords': 'Low-voltage, monolithic, FM, IF, RSSI', 'kicadSymbolki_description': 'Low-voltage, high performance, monolithic FM IF system with high-speed RSSI, SSOP-20', 'kicadSymbolki_fp_filters': 'SSOP*4.4x6.5mm*P0.65mm*'}])
    newPart['name'].append('RF_AM_FM : SA636DK')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


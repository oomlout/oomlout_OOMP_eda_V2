
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Mixer"
    oIndex = "AD831AP"
    hexID = "SZKRFMIXERAD831AP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD831AP', 'kicadSymbolFootprint': 'Package_LCC:PLCC-20', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD831.pdf', 'kicadSymbolki_keywords': 'mixer rf', 'kicadSymbolki_description': 'Doubly Balanced monolithic Mixer, 500 MHz BW, +24 dBm, IP3, LNA and LO driver, PLCC-20', 'kicadSymbolki_fp_filters': 'PLCC*'}])
    newPart['name'].append('RF_Mixer : AD831AP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


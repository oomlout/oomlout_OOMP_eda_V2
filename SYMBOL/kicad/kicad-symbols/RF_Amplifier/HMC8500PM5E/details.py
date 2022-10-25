
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Amplifier"
    oIndex = "HMC8500PM5E"
    hexID = "SZKRFAMPLIFIERHMC85PM5E"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'HMC1099PM5E', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HMC8500PM5E', 'kicadSymbolFootprint': 'Package_CSP:LFCSP-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/HMC8500PM5E.pdf', 'kicadSymbolki_keywords': 'RF Amplifier', 'kicadSymbolki_description': '10 W (40 dBm), 0.01 GHz to 2.8 GHz, GaN Power Amplifier, LFCSP-32', 'kicadSymbolki_fp_filters': 'LFCSP*1EP*5x5mm*P0.5mm*'}])
    newPart['name'].append('RF_Amplifier : HMC8500PM5E')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


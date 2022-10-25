
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "Filter_EMI_LL_1423"
    hexID = "SZKDEVICEFILEMILL1423"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'FL', 'kicadSymbolValue': 'Filter_EMI_LL_1423', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'EMI filter common-mode choke', 'kicadSymbolki_description': 'EMI 2-inductor filter, pin-connections 1-4 and 2-3', 'kicadSymbolki_fp_filters': 'Bourns*SRF0905*'}])
    newPart['name'].append('Device : Filter_EMI_LL_1423')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


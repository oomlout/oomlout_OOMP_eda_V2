
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_ZigBee"
    oIndex = "MW-R-DP-W"
    hexID = "SZKRFZIGBEEMWRDPW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TWE-L-DP-W', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MW-R-DP-W', 'kicadSymbolFootprint': 'Package_DIP:DIP-28_W15.24mm', 'kicadSymbolDatasheet': 'https://www.mono-wireless.com/jp/products/TWE-Lite-DIP/MW-PDS-TWELITEDIP-JP.pdf', 'kicadSymbolki_keywords': 'TWELITE', 'kicadSymbolki_description': 'NXP JN5164/JN5169 breakout module, DIP', 'kicadSymbolki_fp_filters': 'DIP*28*W15.24mm*'}])
    newPart['name'].append('RF_ZigBee : MW-R-DP-W')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


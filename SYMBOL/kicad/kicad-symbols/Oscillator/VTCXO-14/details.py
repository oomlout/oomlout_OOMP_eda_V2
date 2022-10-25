
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "VTCXO-14"
    hexID = "SZKOCSVTCXO14"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'OCXO-14', 'kicadSymbolReference': 'X', 'kicadSymbolValue': 'VTCXO-14', 'kicadSymbolFootprint': 'Oscillator:Oscillator_DIP-14', 'kicadSymbolDatasheet': 'http://www.golledge.com/pdf/products/tcxos/gtxos14.pdf', 'kicadSymbolki_keywords': 'Crystal Clock Oscillator', 'kicadSymbolki_description': 'Voltage-Controlled Crystal Clock Oscillator, DIP14-style metal package', 'kicadSymbolki_fp_filters': 'Oscillator*DIP*14*'}])
    newPart['name'].append('Oscillator : VTCXO-14')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


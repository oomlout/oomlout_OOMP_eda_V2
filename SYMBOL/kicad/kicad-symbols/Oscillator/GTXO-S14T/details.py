
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "GTXO-S14T"
    hexID = "SZKOCSGTXOS14T"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'DGOF5S3', 'kicadSymbolReference': 'X', 'kicadSymbolValue': 'GTXO-S14T', 'kicadSymbolFootprint': 'Oscillator:Oscillator_DIP-14', 'kicadSymbolDatasheet': 'http://www.golledge.com/pdf/products/tcxos/gtxos14.pdf', 'kicadSymbolki_keywords': 'Crystal Clock Oscillator', 'kicadSymbolki_description': '3.3 & 5V Stratum 3 Sinewave TCXO, DIP14-style metal package', 'kicadSymbolki_fp_filters': 'Oscillator*DIP*14*'}])
    newPart['name'].append('Oscillator : GTXO-S14T')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


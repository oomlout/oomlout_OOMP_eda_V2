
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "VC-81"
    hexID = "SZKOCSVC81"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'X', 'kicadSymbolValue': 'VC-81', 'kicadSymbolFootprint': 'Oscillator:Oscillator_DIP-8', 'kicadSymbolDatasheet': 'http://www.scsiglobal.com/Hosonic/Documents/SCSI-VC-81&83.pdf', 'kicadSymbolki_keywords': 'Crystal Clock Oscillator', 'kicadSymbolki_description': 'Voltage-Controlled Crystal Clock Oscillator, DIP8-style metal package', 'kicadSymbolki_fp_filters': 'Oscillator*DIP*8*'}])
    newPart['name'].append('Oscillator : VC-81')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


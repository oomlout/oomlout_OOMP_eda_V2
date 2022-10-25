
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "OCXO-14"
    hexID = "SZKOCSOCXO14"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'X', 'kicadSymbolValue': 'OCXO-14', 'kicadSymbolFootprint': 'Oscillator:Oscillator_DIP-14', 'kicadSymbolDatasheet': 'http://www.petermann-technik.de/fileadmin/petermann/pdf/crystal-oscillators/OCXO-14_PETERMANN-TECHNIK.pdf', 'kicadSymbolki_keywords': 'Crystal Clock Oscillator', 'kicadSymbolki_description': 'Voltage-Controlled Crystal Clock Oscillator, DIP14-style metal package', 'kicadSymbolki_fp_filters': 'Oscillator*DIP*14*'}])
    newPart['name'].append('Oscillator : OCXO-14')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


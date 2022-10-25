
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "CSD16301Q2"
    hexID = "SZKTRANSISTORFETCSD1631Q2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'CSD16301Q2', 'kicadSymbolFootprint': 'Package_SON:Texas_DQK', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/csd16301q2.pdf', 'kicadSymbolki_keywords': 'NexFET Power MOSFET N-MOS', 'kicadSymbolki_description': '5A Id, 25V Vds, NexFET N-Channel Power MOSFET, 19mOhm Ron, SON-6', 'kicadSymbolki_fp_filters': 'Texas*DQK*'}])
    newPart['name'].append('Transistor_FET : CSD16301Q2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


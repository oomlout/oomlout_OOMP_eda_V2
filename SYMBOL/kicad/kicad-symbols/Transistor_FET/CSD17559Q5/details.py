
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "CSD17559Q5"
    hexID = "SZKTRANSISTORFETCSD17559Q5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CSD17578Q5A', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'CSD17559Q5', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TDSON-8-1', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/gpn/csd17559q5', 'kicadSymbolki_keywords': 'NexFET Power MOSFET N-MOS', 'kicadSymbolki_description': '100A Id, 30V Vds, NexFET N-Channel Power MOSFET, 1.15mOhm Ron, 39nC Qg(typ), SON8 5x6mm', 'kicadSymbolki_fp_filters': 'TDSON*'}])
    newPart['name'].append('Transistor_FET : CSD17559Q5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


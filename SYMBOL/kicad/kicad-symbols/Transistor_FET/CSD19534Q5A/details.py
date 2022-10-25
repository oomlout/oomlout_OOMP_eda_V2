
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "CSD19534Q5A"
    hexID = "SZKTRANSISTORFETCSD19534Q5A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CSD17578Q5A', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'CSD19534Q5A', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TDSON-8-1', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/gpn/csd19534q5a', 'kicadSymbolki_keywords': 'NexFET Power MOSFET N-MOS', 'kicadSymbolki_description': '50A Id, 100V Vds, NexFET N-Channel Power MOSFET, 15.1mOhm Ron, 17nC Qg(typ), SON8 5x6mm', 'kicadSymbolki_fp_filters': 'TDSON*'}])
    newPart['name'].append('Transistor_FET : CSD19534Q5A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart



######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "CSD19537Q3"
    hexID = "SZKTRANSISTORFETCSD19537Q3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'CSD19537Q3', 'kicadSymbolFootprint': 'Package_SON:VSON-8_3.3x3.3mm_P0.65mm_NexFET', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/csd19537q3.pdf', 'kicadSymbolki_keywords': 'NexFET Power MOSFET N-MOS', 'kicadSymbolki_description': '50A Id, 100V Vds, NexFET N-Channel Power MOSFET, 13mOhm Ron, Qg Typ 16.0nC, VSON8 3.3x3.3mm', 'kicadSymbolki_fp_filters': 'VSON*3.3x3.3mm*P0.65mm*NexFET*'}])
    newPart['name'].append('Transistor_FET : CSD19537Q3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


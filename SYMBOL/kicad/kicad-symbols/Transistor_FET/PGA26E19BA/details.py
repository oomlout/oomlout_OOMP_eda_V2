
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "PGA26E19BA"
    hexID = "SZKTRANSISTORFETPGA26E19BA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PGA26E07BA', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'PGA26E19BA', 'kicadSymbolFootprint': 'Package_DFN_QFN:Panasonic_HSON-8_8x8mm_P2.00mm', 'kicadSymbolDatasheet': 'https://industrial.panasonic.com/content/data/SC/ds/ds4/PGA26E19BA_E.pdf', 'kicadSymbolki_keywords': 'N-Channel GaN MOSFET', 'kicadSymbolki_description': '13A Id, 600V Vds, 140mOhm, N-Channel GaN MOSFET, DFN-8', 'kicadSymbolki_fp_filters': 'Panasonic*HSON*8x8mm*P2.00mm*'}])
    newPart['name'].append('Transistor_FET : PGA26E19BA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart



######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "PGA26E07BA"
    hexID = "SZKTRANSISTORFETPGA26E7BA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'PGA26E07BA', 'kicadSymbolFootprint': 'Package_DFN_QFN:Panasonic_HSON-8_8x8mm_P2.00mm', 'kicadSymbolDatasheet': 'https://industrial.panasonic.com/content/data/SC/ds/ds4/PGA26E07BA_E.pdf', 'kicadSymbolki_keywords': 'N-Channel GaN MOSFET', 'kicadSymbolki_description': '26A Id, 600V Vds, 56mOhm, N-Channel GaN MOSFET, DFN-8', 'kicadSymbolki_fp_filters': 'Panasonic*HSON*8x8mm*P2.00mm*'}])
    newPart['name'].append('Transistor_FET : PGA26E07BA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


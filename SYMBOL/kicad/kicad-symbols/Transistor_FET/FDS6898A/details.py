
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "FDS6898A"
    hexID = "SZKTRANSISTORFETFDS6898A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'FDS6890A', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'FDS6898A', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/FDS6898A-D.PDF', 'kicadSymbolki_keywords': 'Dual N-Channel MOSFET', 'kicadSymbolki_description': '9.4A Id, 20V Vds, Dual N-Channel MOSFET, 14mOhm Ron, SO-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Transistor_FET : FDS6898A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


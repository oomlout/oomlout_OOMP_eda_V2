
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "FDS6630A"
    hexID = "SZKTRANSISTORFETFDS663A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IRF8721PBF-1', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'FDS6630A', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/FDS6630A-D.pdf', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '6.5A Id, 30V Vds, N-Channel MOSFET, 38mOhm Ron, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Transistor_FET : FDS6630A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


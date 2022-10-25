
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "FDS6930B"
    hexID = "SZKTRANSISTORFETFDS693B"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'FDS6890A', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'FDS6930B', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/FDS6930B-D.PDF', 'kicadSymbolki_keywords': 'Dual N-Channel MOSFET', 'kicadSymbolki_description': '5.5A Id, 30V Vds, Dual N-Channel Logic Level MOSFET, 38mOhm Ron, SO-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Transistor_FET : FDS6930B')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


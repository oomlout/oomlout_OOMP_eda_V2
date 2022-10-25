
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "FDMT800120DC"
    hexID = "SZKTRANSISTORFETFDMT812DC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'FDMT80060DC', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'FDMT800120DC', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:PQFN_8x8', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/FDMT800120DC-D.pdf', 'kicadSymbolki_keywords': 'dual-cool-powertrench MOSFET fairchild', 'kicadSymbolki_description': '20A Id, 120V Vds, N-Channel Dual cool 88 PowerTrench MOSFET, 4.2mOhm Ron, 107nC Qgmax, -55 to 150 °C, 8x8mm MLP', 'kicadSymbolki_fp_filters': 'PQFN*8x8*'}])
    newPart['name'].append('Transistor_FET : FDMT800120DC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart



######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "FDMT800152DC"
    hexID = "SZKTRANSISTORFETFDMT8152DC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'FDMT80060DC', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'FDMT800152DC', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:PQFN_8x8', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/FDMT800152DC-D.pdf', 'kicadSymbolki_keywords': 'dual-cool-powertrench MOSFET fairchild', 'kicadSymbolki_description': '13A Id, 150V Vds, N-Channel Dual Cool PowerTrench MOSFET, 9.0mOhm Ron, 83nC Qgmax, -55 to 150 °C, 8x8mm MLP', 'kicadSymbolki_fp_filters': 'PQFN*8x8*'}])
    newPart['name'].append('Transistor_FET : FDMT800152DC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


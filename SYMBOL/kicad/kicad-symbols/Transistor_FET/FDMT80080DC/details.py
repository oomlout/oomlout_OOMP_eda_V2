
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "FDMT80080DC"
    hexID = "SZKTRANSISTORFETFDMT88DC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'FDMT80060DC', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'FDMT80080DC', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:PQFN_8x8', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/FDMT80080DC-D.pdf', 'kicadSymbolki_keywords': 'dual-cool-powertrench MOSFET fairchild', 'kicadSymbolki_description': '36A Id, 80V Vds, N-Channel Dual Cool PowerTrench MOSFET, 1.35mOhm Ron, 273nC Qgmax, -55 to 150 °C, 8x8mm MLP', 'kicadSymbolki_fp_filters': 'PQFN*8x8*'}])
    newPart['name'].append('FDMT80080DC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


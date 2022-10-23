
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "FDMT80060DC"
    hexID = "SZKTRANSISTORFETFDMT86DC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'FDMT80060DC', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:PQFN_8x8', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/FDMT80060DC-D.pdf', 'kicadSymbolki_keywords': 'PowerTrench Power MOSFET N-MOS', 'kicadSymbolki_description': '43A Id, 60V Vds, PowerTrench N-Channel Power MOSFET, 6.9mOhm Ron, Qg (typ) 7.9nC 8x8mm MLP', 'kicadSymbolki_fp_filters': 'PQFN*8x8*'}])
    newPart['name'].append('FDMT80060DC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


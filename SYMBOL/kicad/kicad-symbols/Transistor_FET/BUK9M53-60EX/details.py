
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "BUK9M53-60EX"
    hexID = "SZKTRANSISTORFETBUK9M536EX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BUK9M53-60EX', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:LFPAK33', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/BUK9M53-60E.pdf', 'kicadSymbolki_keywords': 'Power MOSFET N-MOS', 'kicadSymbolki_description': '17A Id, 60V Vds, N-Channel TrenchMOS MOSFET, 46mOhm Ron, 6nC Qqd, -55 to 175 °C, LFPAK33', 'kicadSymbolki_fp_filters': 'LFPAK33*'}])
    newPart['name'].append('BUK9M53-60EX')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


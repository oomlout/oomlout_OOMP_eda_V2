
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "BUK9M52-40EX"
    hexID = "SZKTRANSISTORFETBUK9M524EX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BUK9M53-60EX', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BUK9M52-40EX', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:LFPAK33', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/BUK9M52-40E.pdf', 'kicadSymbolki_keywords': 'Power MOSFET N-MOS', 'kicadSymbolki_description': '17.6A Id, 40V Vds, N-Channel TrenchMOS MOSFET, 40mOhm Ron, 4.5nC Qqd, -55 to 175 °C, LFPAK33', 'kicadSymbolki_fp_filters': 'LFPAK33*'}])
    newPart['name'].append('Transistor_FET : BUK9M52-40EX')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


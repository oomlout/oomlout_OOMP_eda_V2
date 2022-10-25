
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay_SolidState"
    oIndex = "TLP141G"
    hexID = "SZKRELAYSOLIDSTATETLP141G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLP141G', 'kicadSymbolFootprint': 'Package_SO:MFSOP6-5_4.4x3.6mm_P1.27mm', 'kicadSymbolDatasheet': 'http://datasheet.octopart.com/TLP141G(U,F)-Toshiba-datasheet-134958.pdf', 'kicadSymbolki_keywords': 'OptoThyristor DC Optocoupler', 'kicadSymbolki_description': 'DC Optocoupler Thyristor Based, Vdrm 400V, It 150mA, Viso 2500V, MFSOP6', 'kicadSymbolki_fp_filters': 'MFSOP6*4.4x3.6mm*P1.27mm*'}])
    newPart['name'].append('Relay_SolidState : TLP141G')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart



######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "IRS2113M"
    hexID = "SZKDRIVERFETIRS2113M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IRS2113M', 'kicadSymbolFootprint': 'Package_DFN_QFN:Infineon_MLPQ-16-14-1EP_4x4mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irs2113mpbf.pdf?fileId=5546d462533600a40153567676a227b7', 'kicadSymbolki_keywords': 'Gate Driver', 'kicadSymbolki_description': 'High- and Low-Side Driver, 600V, 2.5/2.5A, MLPQ-14', 'kicadSymbolki_fp_filters': 'Infineon*MLPQ*EP*4x4mm*P0.5mm*'}])
    newPart['name'].append('Driver_FET : IRS2113M')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


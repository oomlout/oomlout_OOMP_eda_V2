
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "IRS21844M"
    hexID = "SZKDRIVERFETIRS21844M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IRS21844M', 'kicadSymbolFootprint': 'Package_DFN_QFN:Infineon_MLPQ-16-14-1EP_4x4mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irs21844mpbf.pdf?fileId=5546d462533600a401535676dfb027de', 'kicadSymbolki_keywords': 'Gate Driver', 'kicadSymbolki_description': 'Half-Bridge Driver, 600V, 1.9/2.3A, MLPQ-14', 'kicadSymbolki_fp_filters': 'Infineon*MLPQ*EP*4x4mm*P0.5mm*'}])
    newPart['name'].append('IRS21844M')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


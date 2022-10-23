
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LTC3638"
    hexID = "SZKREGULATORSWITCHINGLTC3638"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC3638', 'kicadSymbolFootprint': 'Package_SO:Linear_MSOP-12-16-1EP_3x4mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/3638fa.pdf', 'kicadSymbolki_keywords': 'buck dc-dc switcher switching', 'kicadSymbolki_description': '250mA High efficiency 140V step-down converter, MSOP-16(12)', 'kicadSymbolki_fp_filters': 'Linear*MSOP*12*16*EP*3x4mm*P0.5mm*'}])
    newPart['name'].append('LTC3638')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


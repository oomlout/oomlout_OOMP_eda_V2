
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LTC3639"
    hexID = "SZKREGULATORSWITCHINGLTC3639"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LTC3638', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC3639', 'kicadSymbolFootprint': 'Package_SO:Linear_MSOP-12-16-1EP_3x4mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/3639fd.pdf', 'kicadSymbolki_keywords': 'buck dc-dc switcher switching', 'kicadSymbolki_description': '100mA High efficiency 150V syncrhonous step-down converter, MSOP-16(12)', 'kicadSymbolki_fp_filters': 'Linear*MSOP*12*16*EP*3x4mm*P0.5mm*'}])
    newPart['name'].append('LTC3639')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


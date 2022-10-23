
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LT3757EMSE"
    hexID = "SZKREGULATORSWITCHINGLT3757EMSE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT3757EMSE', 'kicadSymbolFootprint': 'Package_SO:MSOP-10-1EP_3x3mm_P0.5mm_EP1.68x1.88mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/3757Afe.pdf', 'kicadSymbolki_keywords': 'Boost flyback SEPIC inverting DC/DC regulator', 'kicadSymbolki_description': 'Boost, flyback, SEPIC and inverting regulator. MSOP-10', 'kicadSymbolki_fp_filters': 'MSOP*EP*3x3mm*P0.5mm*'}])
    newPart['name'].append('LT3757EMSE')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart



######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "LTC3892-1"
    hexID = "SZKREGULATORCONTROLLERLTC38921"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC3892-1', 'kicadSymbolFootprint': 'Package_SO:TSSOP-28-1EP_4.4x9.7mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/38921fc.pdf', 'kicadSymbolki_keywords': 'switching buck converter regulator dual-output', 'kicadSymbolki_description': '60V dual 2-phase synchronous step-down DC/DC controller, forced continuous conduction mode, TSSOP-28', 'kicadSymbolki_fp_filters': 'TSSOP*1EP*4.4x9.7mm*P0.65mm*'}])
    newPart['name'].append('LTC3892-1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart



######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "LTC7810"
    hexID = "SZKREGULATORCONTROLLERLTC781"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC7810', 'kicadSymbolFootprint': 'Package_QFP:LQFP-48-1EP_7x7mm_P0.5mm_EP3.6x3.6mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/LTC7810.pdf', 'kicadSymbolki_keywords': 'switching buck converter regulator dual-output', 'kicadSymbolki_description': '150V dual 2-phase synchronous step-down DC/DC controller, LQPF-48', 'kicadSymbolki_fp_filters': 'LQFP?48?1EP*7x7mm*P0.5mm*EP3.6x3.6mm*'}])
    newPart['name'].append('LTC7810')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


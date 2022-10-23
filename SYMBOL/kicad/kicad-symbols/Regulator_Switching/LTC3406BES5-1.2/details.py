
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LTC3406BES5-1.2"
    hexID = "SZKREGULATORSWITCHINGLTC346BES512"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC3406BES5-1.2', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TSOT-23-5', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/3406b12fs.pdf', 'kicadSymbolki_keywords': 'Regulator step-down', 'kicadSymbolki_description': '600mA Synchronous Step-Down Regulator, 1.5MHz, Fixed 1.2V Output Voltage, Burst Mode Disabled, ThinSOT-23', 'kicadSymbolki_fp_filters': 'TSOT?23*'}])
    newPart['name'].append('LTC3406BES5-1.2')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart



######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LTC3442"
    hexID = "SZKREGULATORSWITCHINGLTC3442"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC3442', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-12-1EP_3x4mm_P0.5mm_EP1.7x3.3mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/3442fb.pdf', 'kicadSymbolki_keywords': 'Micropower Synchronous Buck-Boost DC/DC Converter', 'kicadSymbolki_description': 'Micropower Synchronous Buck-Boost DC/DC Converter with Automatic Burst Mode Operation, DFN-12', 'kicadSymbolki_fp_filters': 'DFN*EP*3x4mm*P0.5mm*'}])
    newPart['name'].append('Regulator_Switching : LTC3442')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


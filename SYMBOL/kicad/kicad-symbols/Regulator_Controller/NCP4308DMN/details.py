
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "NCP4308DMN"
    hexID = "SZKREGULATORCONTROLLERNCP438DMN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NCP4308DMN', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8-1EP_4x4mm_P0.8mm_EP2.39x2.21mm', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/NCP4308-D.PDF', 'kicadSymbolki_keywords': 'synchronous rectifier controller', 'kicadSymbolki_description': 'Synchronous Rectifier Controller, 4A/8A, 4V UVLO, DFN-8', 'kicadSymbolki_fp_filters': 'DFN*1EP*4x4mm*P0.8mm*EP2.39x2.21mm*'}])
    newPart['name'].append('Regulator_Controller : NCP4308DMN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


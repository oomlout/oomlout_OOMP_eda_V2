
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "XC6206PxxxMR"
    hexID = "SZKREGULATORLINEARXC626PXXXMR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'APE8865N-12-HF-3', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'XC6206PxxxMR', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23', 'kicadSymbolDatasheet': 'https://www.torexsemi.com/file/xc6206/XC6206.pdf', 'kicadSymbolki_keywords': 'Torex LDO Voltage Regulator Fixed Positive', 'kicadSymbolki_description': 'Positive 60-250mA Low Dropout Regulator, Fixed Output, SOT-23', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Regulator_Linear : XC6206PxxxMR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


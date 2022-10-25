
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LTC3886"
    hexID = "SZKREGULATORSWITCHINGLTC3886"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC3886', 'kicadSymbolFootprint': 'Package_DFN_QFN:Linear_UGK52_QFN-46-52', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/LTC3886-3886-1.pdf', 'kicadSymbolki_keywords': 'step down switch manager I2C telemetry fault current sense', 'kicadSymbolki_description': '60V dual output buck output with digital power system management, UKG52(46)', 'kicadSymbolki_fp_filters': 'Linear*UGK52*QFN*46*52*'}])
    newPart['name'].append('Regulator_Switching : LTC3886')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


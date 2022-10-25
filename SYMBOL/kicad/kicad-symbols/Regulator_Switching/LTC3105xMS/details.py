
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LTC3105xMS"
    hexID = "SZKREGULATORSWITCHINGLTC315XMS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC3105xMS', 'kicadSymbolFootprint': 'Package_SO:MSOP-12_3x4mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/3105fb.pdf', 'kicadSymbolki_keywords': 'Solar MPPT Maximum Power Point Control Converter Step-Up', 'kicadSymbolki_description': '400mA Step-Up DC/DC Converter with Maximum Power Point Control and 250mV Start-Up, MSOP-12', 'kicadSymbolki_fp_filters': 'MSOP*3x4mm*0.65mm*'}])
    newPart['name'].append('Regulator_Switching : LTC3105xMS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


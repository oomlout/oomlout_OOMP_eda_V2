
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "ADA4870ARRZ"
    hexID = "SZKAMPLIFIEROPERATIONALADA487ARRZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADA4870ARRZ', 'kicadSymbolFootprint': 'Package_SO:HSOP-20-1EP_11.0x15.9mm_P1.27mm_SlugDown_ThermalVias', 'kicadSymbolDatasheet': 'www.analog.com/media/en/technical-documentation/data-sheets/ADA4870.pdf', 'kicadSymbolki_keywords': 'single opamp', 'kicadSymbolki_description': 'High Speed, High Voltage, 1A Output Drive Amplifier, PSOP-20', 'kicadSymbolki_fp_filters': 'HSOP*1EP*11.0x15.9mm*P1.27mm*SlugDown*'}])
    newPart['name'].append('Amplifier_Operational : ADA4870ARRZ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


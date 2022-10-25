
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "APE1707M-HF"
    hexID = "SZKREGULATORSWITCHINGAPE177MHF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'APE1707M-33-HF', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'APE1707M-HF', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://files.remont-aud.net/baza/dc_dc/data/APE1707.pdf', 'kicadSymbolki_keywords': 'Adjustable 2A 150KHz PWM Buck DC/DC', 'kicadSymbolki_description': '2A, 150KHz PWM Buck DC/DC Converter, adjustable output voltage, SO-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Regulator_Switching : APE1707M-HF')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


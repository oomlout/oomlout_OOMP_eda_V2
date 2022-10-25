
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "LM3478MA"
    hexID = "SZKREGULATORCONTROLLERLM3478MA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM3478MA', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/gpn/lm3478', 'kicadSymbolki_keywords': 'Boost flyback SEPIC DC-DC controller', 'kicadSymbolki_description': '2.97~40V Wide Input Range Boost/SEPIC/Flyback DC-DC Controller, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC-8*3.9x4.9mm_P1.27mm*'}])
    newPart['name'].append('Regulator_Controller : LM3478MA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


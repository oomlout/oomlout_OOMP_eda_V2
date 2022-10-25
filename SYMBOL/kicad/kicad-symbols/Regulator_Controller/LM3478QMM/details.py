
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "LM3478QMM"
    hexID = "SZKREGULATORCONTROLLERLM3478Q"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM3478MA', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM3478QMM', 'kicadSymbolFootprint': 'Package_SO:VSSOP-8_3.0x3.0mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/gpn/lm3478q-q1', 'kicadSymbolki_keywords': 'Boost flyback SEPIC DC-DC controller Automotive', 'kicadSymbolki_description': '2.97~40V Wide Input Range Boost/SEPIC/Flyback DC-DC Controller, AEC-Q100 Qualified, VSSOP-8', 'kicadSymbolki_fp_filters': 'VSSOP-8_3.0x3.0mm_P0.65mm*'}])
    newPart['name'].append('Regulator_Controller : LM3478QMM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


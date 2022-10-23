
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "LM3478MM"
    hexID = "SZKREGULATORCONTROLLERLM3478"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM3478MA', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM3478MM', 'kicadSymbolFootprint': 'Package_SO:VSSOP-8_3.0x3.0mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/gpn/lm3478', 'kicadSymbolki_keywords': 'Boost flyback SEPIC DC-DC controller', 'kicadSymbolki_description': '2.97~40V Wide Input Range Boost/SEPIC/Flyback DC-DC Controller, VSSOP-8', 'kicadSymbolki_fp_filters': 'VSSOP-8_3.0x3.0mm_P0.65mm*'}])
    newPart['name'].append('LM3478MM')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


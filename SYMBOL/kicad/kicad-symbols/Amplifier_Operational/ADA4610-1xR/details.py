
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "ADA4610-1xR"
    hexID = "SZKAMPLIFIEROPERATIONALADA4611XR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'OPA333xxD', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADA4610-1xR', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADA4610-1_4610-2_4610-4.pdf', 'kicadSymbolki_keywords': 'single opamp', 'kicadSymbolki_description': 'Low Noise, Precision, Rail-to-Rail Output, JFET Single Op Amp, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Amplifier_Operational : ADA4610-1xR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart



######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "Si8241CB"
    hexID = "SZKAMPLIFIERAUDIOSI8241CB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'Si8241BB', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'Si8241CB', 'kicadSymbolFootprint': 'Package_SO:SOIC-16_3.9x9.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/NCD5702-D.PDF', 'kicadSymbolki_keywords': 'class d gate driver', 'kicadSymbolki_description': 'Class D Audio Driver With Precision Dead-Time Generator, 10V UVLO, +/-750V, +0.5/-0.5A, SOIC-16', 'kicadSymbolki_fp_filters': 'SOIC*3.9x9.9*P1.27mm*'}])
    newPart['name'].append('Amplifier_Audio : Si8241CB')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


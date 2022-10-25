
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "TPS7A7001DDA"
    hexID = "SZKREGULATORLINEARTPS7A71DDA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS7A7001DDA', 'kicadSymbolFootprint': 'Package_SO:TI_SO-PowerPAD-8', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps7a7001.pdf', 'kicadSymbolki_keywords': 'ldo regulator voltage linear', 'kicadSymbolki_description': '2A, Low-Dropout Voltage Regulator, 1.425-6.5V Input, Adjustable Min 0.5V Output, PowerPad SO-8', 'kicadSymbolki_fp_filters': 'TI*SO*PowerPAD*'}])
    newPart['name'].append('Regulator_Linear : TPS7A7001DDA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


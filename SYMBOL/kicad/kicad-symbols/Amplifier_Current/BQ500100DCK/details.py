
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Current"
    oIndex = "BQ500100DCK"
    hexID = "SZKAMPLIFIERCURRENTBQ51DCK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BQ500100DCK', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/bq500100.pdf', 'kicadSymbolki_keywords': 'Current shunt monitor', 'kicadSymbolki_description': '20V High side current sensor, Voltage Output, 50V/V Gain, SC-70-6', 'kicadSymbolki_fp_filters': 'SOT?363*'}])
    newPart['name'].append('Amplifier_Current : BQ500100DCK')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


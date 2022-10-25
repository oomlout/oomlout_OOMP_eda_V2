
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "NCV8114BSN280T1G"
    hexID = "SZKREGULATORLINEARNCV8114BSN28T1G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'NCV8114ASN120T1G', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NCV8114BSN280T1G', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TSOT-23-5', 'kicadSymbolDatasheet': 'https://ru.mouser.com/datasheet/2/308/NCV8114-D-1107616.pdf', 'kicadSymbolki_keywords': 'linear regulator ldo fixed positive', 'kicadSymbolki_description': '300mA, Low Noise, Linear Regulator without output active discharge function, 1.7-5.5V input voltage range, 2.8V fixed positive output, TSOT-23-5', 'kicadSymbolki_fp_filters': 'TSOT?23*'}])
    newPart['name'].append('Regulator_Linear : NCV8114BSN280T1G')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


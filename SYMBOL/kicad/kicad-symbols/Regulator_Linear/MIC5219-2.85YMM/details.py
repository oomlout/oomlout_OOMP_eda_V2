
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "MIC5219-2.85YMM"
    hexID = "SZKREGULATORLINEARMIC5219285Y"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MIC5219-2.5YMM', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MIC5219-2.85YMM', 'kicadSymbolFootprint': 'Package_SO:MSOP-8_3x3mm_P0.65mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/MIC5219-500mA-Peak-Output-LDO-Regulator-DS20006021A.pdf', 'kicadSymbolki_keywords': '500mA ultra-low-noise LDO linear voltage regulator fixed positive', 'kicadSymbolki_description': '500mA low dropout linear regulator, fixed 2.85V output, MSOP-8', 'kicadSymbolki_fp_filters': 'MSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Regulator_Linear : MIC5219-2.85YMM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


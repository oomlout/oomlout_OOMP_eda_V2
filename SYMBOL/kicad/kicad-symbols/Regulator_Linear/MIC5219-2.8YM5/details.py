
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "MIC5219-2.8YM5"
    hexID = "SZKREGULATORLINEARMIC521928YM5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AP131-15', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MIC5219-2.8YM5', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/MIC5219-500mA-Peak-Output-LDO-Regulator-DS20006021A.pdf', 'kicadSymbolki_keywords': '500mA ultra-low-noise LDO linear voltage regulator fixed positive', 'kicadSymbolki_description': '500mA low dropout linear regulator, fixed 2.8V output, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Regulator_Linear : MIC5219-2.8YM5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


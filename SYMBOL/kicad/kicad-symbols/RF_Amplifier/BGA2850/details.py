
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Amplifier"
    oIndex = "BGA2850"
    hexID = "SZKRFAMPLIFIERBGA285"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BGA2866', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BGA2850', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/BGA2850.pdf', 'kicadSymbolki_keywords': 'RF GAIN BLOCK', 'kicadSymbolki_description': 'MIC wideband amplifier, DC-2.2GHz, +24dB @ 950MHz, 5V, SOT-363-6', 'kicadSymbolki_fp_filters': 'SOT*363*'}])
    newPart['name'].append('RF_Amplifier : BGA2850')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart



######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Module"
    oIndex = "Ai-Thinker-Ra-01"
    hexID = "SZKRFMOAITHINKERRA1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'Ai-Thinker-Ra-01', 'kicadSymbolFootprint': 'RF_Module:Ai-Thinker-Ra-01-LoRa', 'kicadSymbolDatasheet': 'http://wiki.ai-thinker.com/_media/lora/docs/c047ps01a1_ra-01_product_specification_v1.1.pdf', 'kicadSymbolki_keywords': 'Ra-01 LoRa', 'kicadSymbolki_description': 'Ai-Thinker Ra-01 410-525 MHz LoRa Module, SPI interface, external antenna', 'kicadSymbolki_fp_filters': 'Ai?Thinker?Ra?01*'}])
    newPart['name'].append('RF_Module : Ai-Thinker-Ra-01')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


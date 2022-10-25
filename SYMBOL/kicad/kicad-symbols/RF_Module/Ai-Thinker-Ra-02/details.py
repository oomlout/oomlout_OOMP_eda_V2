
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Module"
    oIndex = "Ai-Thinker-Ra-02"
    hexID = "SZKRFMOAITHINKERRA2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'Ai-Thinker-Ra-02', 'kicadSymbolFootprint': 'RF_Module:Ai-Thinker-Ra-01-LoRa', 'kicadSymbolDatasheet': 'http://wiki.ai-thinker.com/_media/lora/docs/c048ps01a1_ra-02_product_specification_v1.1.pdf', 'kicadSymbolki_keywords': 'Ra-02 LoRa', 'kicadSymbolki_description': 'Ai-Thinker Ra-02 410-525 MHz LoRa Module, SPI interface, U.FL antenna connector', 'kicadSymbolki_fp_filters': 'Ai?Thinker?Ra?01*'}])
    newPart['name'].append('RF_Module : Ai-Thinker-Ra-02')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


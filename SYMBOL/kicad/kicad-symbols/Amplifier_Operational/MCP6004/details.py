
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "MCP6004"
    hexID = "SZKAMPLIFIEROPERATIONALMCP64"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM2902', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP6004', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/21733j.pdf', 'kicadSymbolki_keywords': 'quad opamp', 'kicadSymbolki_description': '1MHz, Low-Power Op Amp, DIP-14/SOIC-14/TSSOP-14', 'kicadSymbolki_fp_filters': 'SOIC*3.9x8.7mm*P1.27mm* DIP*W7.62mm* TSSOP*4.4x5mm*P0.65mm* SSOP*5.3x6.2mm*P0.65mm* MSOP*3x3mm*P0.5mm*'}])
    newPart['name'].append('MCP6004')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


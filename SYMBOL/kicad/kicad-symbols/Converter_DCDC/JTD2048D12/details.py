
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "JTD2048D12"
    hexID = "SZKCONJTD248D12"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'JTD2024D05', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'JTD2048D12', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_XP_POWER_JTDxxxxxxx_THT', 'kicadSymbolDatasheet': 'https://www.xppower.com/portals/0/pdfs/SF_JTD20.pdf', 'kicadSymbolki_keywords': 'isolated isolation dc-dc converter step-down dual', 'kicadSymbolki_description': 'Isolated 20W 4:1 input DC/DC converter module, 18-75V input voltage, +/-12V output voltage, DIP', 'kicadSymbolki_fp_filters': 'Converter*DCDC*XP?POWER*JTDxxxxxxx*'}])
    newPart['name'].append('JTD2048D12')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


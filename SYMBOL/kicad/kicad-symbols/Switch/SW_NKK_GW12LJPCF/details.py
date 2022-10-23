
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Switch"
    oIndex = "SW_NKK_GW12LJPCF"
    hexID = "SZKSWITCHSWNKKGW12LJPCF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'SW', 'kicadSymbolValue': 'SW_NKK_GW12LJPCF', 'kicadSymbolFootprint': 'Button_Switch_THT:SW_NKK_GW12LJP', 'kicadSymbolDatasheet': 'http://www.nkkswitches.com/pdf/gwillum.pdf', 'kicadSymbolki_keywords': 'switch single-pole double-throw spdt ON-ON illuminated red green', 'kicadSymbolki_description': 'Switch, single pole double throw, illuminated paddle, red and green LEDs', 'kicadSymbolki_fp_filters': 'SW*NKK*GW12LJP*'}])
    newPart['name'].append('SW_NKK_GW12LJPCF')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


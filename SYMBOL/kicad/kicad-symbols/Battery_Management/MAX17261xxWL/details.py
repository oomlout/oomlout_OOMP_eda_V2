
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "MAX17261xxWL"
    hexID = "SZKBATMANAGEMENTMAX17261XXWL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX17261xxWL', 'kicadSymbolFootprint': 'Package_BGA:Maxim_WLP-9_1.595x1.415_Layout3x3_P0.4mm_Ball0.27mm_Pad0.25mm_NSMD', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX17261.pdf', 'kicadSymbolki_keywords': 'Charge pump, battery', 'kicadSymbolki_description': '5.1μA Multi-Cell Fuel Gauge with ModelGauge m5 EZ, WLP-9', 'kicadSymbolki_fp_filters': 'Maxim*WLP*1.595x1.415*Layout3x3*P0.4mm*'}])
    newPart['name'].append('MAX17261xxWL')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


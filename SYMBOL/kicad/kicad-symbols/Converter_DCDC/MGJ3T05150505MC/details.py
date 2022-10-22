
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "MGJ3T05150505MC"
    hexID = "SZKCONMGJ3T51555MC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MGJ3T05150505MC', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_Murata_MGJ3', 'kicadSymbolDatasheet': 'https://power.murata.com/datasheet?/data/power/ncl/kdc_mgj3.pdf', 'kicadSymbolki_keywords': 'DC/DC converter', 'kicadSymbolki_description': '5.2kVDC Isolated 3W Gate Drive, 4.5-9V Vin, +15V/-5V or +15V/-10V or +20V/-5V Vout', 'kicadSymbolki_fp_filters': 'Converter*DCDC*Murata*MGJ3*'}])
    newPart['name'].append('MGJ3T05150505MC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


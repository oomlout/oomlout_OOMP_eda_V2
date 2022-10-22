
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "MGJ2D051505SC"
    hexID = "SZKCONMGJ2D5155SC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MGJ2D051505SC', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_Murata_MGJ2DxxxxxxSC_THT', 'kicadSymbolDatasheet': 'https://power.murata.com/pub/data/power/ncl/kdc_mgj2.pdf', 'kicadSymbolki_keywords': 'DC/DC converter', 'kicadSymbolki_description': '5.2kVDC Isolated 2W Gate Drive, 5V Vin, +15V/-5V Vout', 'kicadSymbolki_fp_filters': 'Converter*DCDC*Murata*MGJ2DxxxxxxSC*'}])
    newPart['name'].append('MGJ2D051505SC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


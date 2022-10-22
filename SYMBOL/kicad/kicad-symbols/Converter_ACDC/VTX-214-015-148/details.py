
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_ACDC"
    oIndex = "VTX-214-015-148"
    hexID = "SZKCONVTX21415148"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'VTX-214-015-103', 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'VTX-214-015-148', 'kicadSymbolFootprint': 'Converter_ACDC:Converter_ACDC_Vigortronix_VTX-214-015-1xx_THT', 'kicadSymbolDatasheet': 'http://www.vigortronix.com/15WattSMPSPCBModuleAC-DC', 'kicadSymbolki_keywords': '48V 15W AC-DC module power supply', 'kicadSymbolki_description': '48V Vigortronix 15W ACDC Converters', 'kicadSymbolki_fp_filters': 'Converter*ACDC*Vigortronix*VTX*214*015*1xx*'}])
    newPart['name'].append('VTX-214-015-148')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


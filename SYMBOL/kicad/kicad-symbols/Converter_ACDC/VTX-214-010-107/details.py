
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_ACDC"
    oIndex = "VTX-214-010-107"
    hexID = "SZKCONVTX214117"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'VTX-214-010-103', 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'VTX-214-010-107', 'kicadSymbolFootprint': 'Converter_ACDC:Converter_ACDC_Vigortronix_VTX-214-010-xxx_THT', 'kicadSymbolDatasheet': 'http://www.vigortronix.com/10WattACDCPCBPowerModule.aspx', 'kicadSymbolki_keywords': '7.5V 10W AC-DC module power supply', 'kicadSymbolki_description': '7.5V Vigortronix 10W ACDC Converters', 'kicadSymbolki_fp_filters': 'Converter*ACDC*Vigortronix*VTX*214*010*xxx*'}])
    newPart['name'].append('VTX-214-010-107')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


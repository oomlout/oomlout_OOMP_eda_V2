
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_ACDC"
    oIndex = "RAC20-05SK"
    hexID = "SZKCONRAC25SK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'RAC20-05SK', 'kicadSymbolFootprint': 'Converter_ACDC:Converter_ACDC_Recom_RAC20-xxSK_THT', 'kicadSymbolDatasheet': 'https://recom-power.com/pdf/Powerline_AC-DC/RAC20-K.pdf', 'kicadSymbolki_keywords': 'ac dc power supply', 'kicadSymbolki_description': '20 Watt Single Output AC/DC power supply 5V 4000mA', 'kicadSymbolki_fp_filters': 'Converter*ACDC*Recom*RAC20*SK*THT*'}])
    newPart['name'].append('RAC20-05SK')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart



######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_ACDC"
    oIndex = "RAC20-12DK"
    hexID = "SZKCONRAC212DK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'RAC20-12DK', 'kicadSymbolFootprint': 'Converter_ACDC:Converter_ACDC_Recom_RAC20-xxDK_THT', 'kicadSymbolDatasheet': 'https://recom-power.com/pdf/Powerline_AC-DC/RAC20-K.pdf', 'kicadSymbolki_keywords': 'ac dc power supply', 'kicadSymbolki_description': '20 Watt Dual Output AC/DC power supply ±12V ±833mA', 'kicadSymbolki_fp_filters': 'Converter*ACDC*Recom*RAC20*DK*THT*'}])
    newPart['name'].append('RAC20-12DK')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


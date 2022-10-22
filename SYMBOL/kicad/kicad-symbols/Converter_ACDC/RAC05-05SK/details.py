
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_ACDC"
    oIndex = "RAC05-05SK"
    hexID = "SZKCONRAC55SK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'RAC05-3.3SK', 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'RAC05-05SK', 'kicadSymbolFootprint': 'Converter_ACDC:Converter_ACDC_RECOM_RAC05-xxSK_THT', 'kicadSymbolDatasheet': 'https://www.recom-power.com/pdf/Powerline-AC-DC/RAC05-K.pdf', 'kicadSymbolki_keywords': 'ac dc power supply', 'kicadSymbolki_description': '5W Single Output EMC Class B 5V 1000mA', 'kicadSymbolki_fp_filters': 'Converter*ACDC*RECOM*RAC05*SK*'}])
    newPart['name'].append('RAC05-05SK')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


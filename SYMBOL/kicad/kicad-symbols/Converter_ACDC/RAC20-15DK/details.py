
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_ACDC"
    oIndex = "RAC20-15DK"
    hexID = "SZKCONRAC215DK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'RAC20-12DK', 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'RAC20-15DK', 'kicadSymbolFootprint': 'Converter_ACDC:Converter_ACDC_Recom_RAC20-xxDK_THT', 'kicadSymbolDatasheet': 'https://recom-power.com/pdf/Powerline_AC-DC/RAC20-K.pdf', 'kicadSymbolki_keywords': 'ac dc power supply', 'kicadSymbolki_description': '20 Watt Dual Output AC/DC power supply ±15V ±670mA', 'kicadSymbolki_fp_filters': 'Converter*ACDC*Recom*RAC20*DK*THT*'}])
    newPart['name'].append('Converter_ACDC : RAC20-15DK')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


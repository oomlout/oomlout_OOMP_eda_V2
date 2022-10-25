
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "ATA00AA18S-L"
    hexID = "SZKCONATAAA18SL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATA00AA18S-L', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_Artesyn_ATA_SMD', 'kicadSymbolDatasheet': 'https://www.artesyn.com/power/assets/ata_series_ds_01apr2015_79c25814fd.pdf', 'kicadSymbolki_keywords': 'DC/DC converter dual', 'kicadSymbolki_description': 'Artesyn 3W Isolated DC/DC Converter Module, ±5V Output Voltage, 9-36V Input Voltage', 'kicadSymbolki_fp_filters': '*Artesyn*ATA*SMD*'}])
    newPart['name'].append('Converter_DCDC : ATA00AA18S-L')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


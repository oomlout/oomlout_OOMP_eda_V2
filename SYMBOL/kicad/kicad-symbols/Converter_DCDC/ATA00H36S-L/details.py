
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "ATA00H36S-L"
    hexID = "SZKCONATAH36SL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATA00F18S-L', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATA00H36S-L', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_Artesyn_ATA_SMD', 'kicadSymbolDatasheet': 'https://www.artesyn.com/power/assets/ata_series_ds_01apr2015_79c25814fd.pdf', 'kicadSymbolki_keywords': 'DC/DC converter single', 'kicadSymbolki_description': 'Artesyn 3W Isolated DC/DC Converter Module, 24V Output Voltage, 18-75V Input Voltage', 'kicadSymbolki_fp_filters': '*Artesyn*ATA*SMD*'}])
    newPart['name'].append('Converter_DCDC : ATA00H36S-L')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart



######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "TPS70248_HTSSOP20"
    hexID = "SZKREGULATORLINEARTPS7248HTSS2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TPS70245_HTSSOP20', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS70248_HTSSOP20', 'kicadSymbolFootprint': 'Package_SO:HTSSOP-20-1EP_4.4x6.5mm_P0.65mm_EP3.4x6.5mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps702.pdf', 'kicadSymbolki_keywords': 'Dual 3.3V 1.5V LDO Regulator 500mA 250mA Voltage Supervisor', 'kicadSymbolki_description': '3.3V 500mA/1.5V 250mA Dual Low Drop-out Regulator with Voltage Supervisor, PowerPAD TSSOP-20', 'kicadSymbolki_fp_filters': 'HTSSOP*4.4x6.5mm*P0.65mm*'}])
    newPart['name'].append('Regulator_Linear : TPS70248_HTSSOP20')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart



######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "EE2-12NUX"
    hexID = "SZKRELAYEE212NUX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'EE2-3NUX', 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'EE2-12NUX', 'kicadSymbolFootprint': 'Relay_SMD:Relay_DPDT_Kemet_EE2_NUX_NKX', 'kicadSymbolDatasheet': 'https://content.kemet.com/datasheets/KEM_R7002_EC2_EE2.pdf', 'kicadSymbolki_keywords': 'signal relay double pole double throw DPDT DC coil non latching', 'kicadSymbolki_description': 'General purpose signal relay, Kemet EE2 Series, DPDT (2 Form C), non-latching, high solder joint reliability SMD, 60W/125VA, 220VDC/250VAC, 2A, 12V DC coil', 'kicadSymbolki_fp_filters': 'Relay*DPDT*Kemet*EE2*NUX*'}])
    newPart['name'].append('Relay : EE2-12NUX')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


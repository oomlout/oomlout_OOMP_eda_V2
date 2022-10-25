
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "EE2-4.5SNUX"
    hexID = "SZKRELAYEE245SNUX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'EE2-3SNUX', 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'EE2-4.5SNUX', 'kicadSymbolFootprint': 'Relay_SMD:Relay_DPDT_Kemet_EE2_NUX_NKX', 'kicadSymbolDatasheet': 'https://content.kemet.com/datasheets/KEM_R7002_EC2_EE2.pdf', 'kicadSymbolki_keywords': 'signal relay double pole double throw DPDT DC coil single coil latching', 'kicadSymbolki_description': 'General purpose signal relay, Kemet EE2 Series, DPDT (2 Form C), single coil latching, high solder joint reliability SMD, 60W/125VA, 220VDC/250VAC, 2A, 4.5V DC coil', 'kicadSymbolki_fp_filters': 'Relay*DPDT*Kemet*EE2*NUX*'}])
    newPart['name'].append('Relay : EE2-4.5SNUX')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


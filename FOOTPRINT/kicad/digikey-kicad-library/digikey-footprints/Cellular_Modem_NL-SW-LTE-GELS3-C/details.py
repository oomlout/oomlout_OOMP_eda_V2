
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "digikey-kicad-library"
    oDesc = "digikey-footprints"
    oIndex = "Cellular_Modem_NL-SW-LTE-GELS3-C"
    hexID = "FZKICADDIGIKEYKICADLIBRARYDIGIKEYFOOTPRINTSCELLULARMODEMNLSWLTEGELS3C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Cellular_Modem_NL-SW-LTE-GELS3-C', 'description': 'http://nimbelink.com/Documentation/Skywire/4G_LTE_Cat_1/30122_NL-SW-LTE-GELS3_Datasheet.pdf', 'tags': None, 'attributeType': None, 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('digikey-footprints : Cellular_Modem_NL-SW-LTE-GELS3-C')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


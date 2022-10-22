
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "digikey-kicad-library"
    oDesc = "digikey-footprints"
    oIndex = "DSUB-9_Receptical_A-DF_09_A_KG-T2S"
    hexID = "FZKICADDIGIKEYKICADLIBRARYDIGIKEYFOOTPRINTSDSUB9RECEPTICALADF9AKGT2S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DSUB-9_Receptical_A-DF_09_A_KG-T2S', 'description': 'http://www.assmann-wsw.com/fileadmin/datasheets/ASS_4888_CO.pdf', 'tags': None, 'attributeType': None, 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('digikey-footprints : DSUB-9_Receptical_A-DF_09_A_KG-T2S')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


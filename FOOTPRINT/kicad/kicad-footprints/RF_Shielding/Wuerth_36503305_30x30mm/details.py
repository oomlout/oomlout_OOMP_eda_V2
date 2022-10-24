
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Shielding"
    oIndex = "Wuerth_36503305_30x30mm"
    hexID = "FZKRFSWUERTH3653353X3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Wuerth_36503305_30x30mm', 'description': 'WE-SHC Shielding Cabinet THT 31x31mm', 'tags': 'Shielding Cabinet', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Shielding.3dshapes/Wuerth_36503305_30x30mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('RF_Shielding : Wuerth_36503305_30x30mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart



######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Dsub"
    oIndex = "DSUB-25_Male_Horizontal_P2.77x2.84mm_EdgePinOffset9.90mm_Housed_MountingHolesOffset11.32mm"
    hexID = "FZKCNDSUBDSUB25MALEHORIZONTALP277X284EDGEPINOFFSET99HOUSEDHOLSOFFSET1132"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DSUB-25_Male_Horizontal_P2.77x2.84mm_EdgePinOffset9.90mm_Housed_MountingHolesOffset11.32mm', 'description': '25-pin D-Sub connector, horizontal/angled (90 deg), THT-mount, male, pitch 2.77x2.84mm, pin-PCB-offset 9.9mm, distance of mounting holes 47.1mm, distance of mounting holes to PCB edge 11.32mm, see https://disti-assets.s3.amazonaws.com/tonar/files/datasheets/16730.pdf', 'tags': '25-pin D-Sub connector horizontal angled 90deg THT male pitch 2.77x2.84mm pin-PCB-offset 9.9mm mounting-holes-distance 47.1mm mounting-hole-offset 47.1mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Dsub.3dshapes/DSUB-25_Male_Horizontal_P2.77x2.84mm_EdgePinOffset9.90mm_Housed_MountingHolesOffset11.32mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Dsub : DSUB-25_Male_Horizontal_P2.77x2.84mm_EdgePinOffset9.90mm_Housed_MountingHolesOffset11.32mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


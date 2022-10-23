
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Dsub"
    oIndex = "DSUB-25_Female_Horizontal_P2.77x2.84mm_EdgePinOffset14.56mm_Housed_MountingHolesOffset15.98mm"
    hexID = "FZKCNDSUBDSUB25FEMALEHORIZONTALP277X284EDGEPINOFFSET1456HOUSEDHOLSOFFSET1598"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DSUB-25_Female_Horizontal_P2.77x2.84mm_EdgePinOffset14.56mm_Housed_MountingHolesOffset15.98mm', 'description': '25-pin D-Sub connector, horizontal/angled (90 deg), THT-mount, female, pitch 2.77x2.84mm, pin-PCB-offset 14.56mm, distance of mounting holes 47.1mm, distance of mounting holes to PCB edge 15.979999999999999mm, see https://disti-assets.s3.amazonaws.com/tonar/files/datasheets/16730.pdf', 'tags': '25-pin D-Sub connector horizontal angled 90deg THT female pitch 2.77x2.84mm pin-PCB-offset 14.56mm mounting-holes-distance 47.1mm mounting-hole-offset 47.1mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Dsub.3dshapes/DSUB-25_Female_Horizontal_P2.77x2.84mm_EdgePinOffset14.56mm_Housed_MountingHolesOffset15.98mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Dsub : DSUB-25_Female_Horizontal_P2.77x2.84mm_EdgePinOffset14.56mm_Housed_MountingHolesOffset15.98mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


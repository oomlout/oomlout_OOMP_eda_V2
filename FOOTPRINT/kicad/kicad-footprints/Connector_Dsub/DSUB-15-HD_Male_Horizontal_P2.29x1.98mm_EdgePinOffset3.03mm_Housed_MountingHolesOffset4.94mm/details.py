
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Dsub"
    oIndex = "DSUB-15-HD_Male_Horizontal_P2.29x1.98mm_EdgePinOffset3.03mm_Housed_MountingHolesOffset4.94mm"
    hexID = "FZKCNDSUBDSUB15HDMALEHORIZONTALP229X198EDGEPINOFFSET33HOUSEDHOLSOFFSET494"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DSUB-15-HD_Male_Horizontal_P2.29x1.98mm_EdgePinOffset3.03mm_Housed_MountingHolesOffset4.94mm', 'description': '15-pin D-Sub connector, horizontal/angled (90 deg), THT-mount, male, pitch 2.29x1.98mm, pin-PCB-offset 3.0300000000000002mm, distance of mounting holes 25mm, distance of mounting holes to PCB edge 4.9399999999999995mm, see https://disti-assets.s3.amazonaws.com/tonar/files/datasheets/16730.pdf', 'tags': '15-pin D-Sub connector horizontal angled 90deg THT male pitch 2.29x1.98mm pin-PCB-offset 3.0300000000000002mm mounting-holes-distance 25mm mounting-hole-offset 25mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Dsub.3dshapes/DSUB-15-HD_Male_Horizontal_P2.29x1.98mm_EdgePinOffset3.03mm_Housed_MountingHolesOffset4.94mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Dsub : DSUB-15-HD_Male_Horizontal_P2.29x1.98mm_EdgePinOffset3.03mm_Housed_MountingHolesOffset4.94mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


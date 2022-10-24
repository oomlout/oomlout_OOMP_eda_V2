
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "MountingEquipment"
    oIndex = "DINRailAdapter_3xM3_PhoenixContact_1201578"
    hexID = "FZKMONDINRAILADAPTER3XM3PHOENIXCONTACT121578"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DINRailAdapter_3xM3_PhoenixContact_1201578', 'description': 'https://www.phoenixcontact.com/online/portal/us?uri=pxc-oc-itemdetail:pid=1201578&library=usen&tab=1', 'tags': 'DIN rail adapter universal three M3 clearance holes', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/MountingEquipment.3dshapes/DINRailAdapter_3xM3_PhoenixContact_1201578.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('MountingEquipment : DINRailAdapter_3xM3_PhoenixContact_1201578')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


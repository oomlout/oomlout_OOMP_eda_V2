
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DIP"
    oIndex = "DIP-6_W7.62mm_Socket"
    hexID = "FZKDIPDIP6W762SO"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DIP-6_W7.62mm_Socket', 'description': '6-lead though-hole mounted DIP package, row spacing 7.62 mm (300 mils), Socket', 'tags': 'THT DIP DIL PDIP 2.54mm 7.62mm 300mil Socket', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/DIP-6_W7.62mm_Socket.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Package_DIP : DIP-6_W7.62mm_Socket')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


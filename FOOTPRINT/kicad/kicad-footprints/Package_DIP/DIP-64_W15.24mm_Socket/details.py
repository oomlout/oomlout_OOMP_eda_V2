
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DIP"
    oIndex = "DIP-64_W15.24mm_Socket"
    hexID = "FZKDIPDIP64W1524SO"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DIP-64_W15.24mm_Socket', 'description': '64-lead though-hole mounted DIP package, row spacing 15.24 mm (600 mils), Socket', 'tags': 'THT DIP DIL PDIP 2.54mm 15.24mm 600mil Socket', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/DIP-64_W15.24mm_Socket.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Package_DIP : DIP-64_W15.24mm_Socket')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart



######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SIP"
    oIndex = "SIP4_Sharp-SSR_P7.62mm_Straight"
    hexID = "FZKSIPSIP4SHARPSSRP762S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SIP4_Sharp-SSR_P7.62mm_Straight', 'description': 'SIP4 Footprint for SSR made by Sharp', 'tags': 'Solid State relais SSR Sharp', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SIP.3dshapes/SIP4_Sharp-SSR_P7.62mm_Straight.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Package_SIP : SIP4_Sharp-SSR_P7.62mm_Straight')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart



######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_PCBEdge"
    oIndex = "4UCON_10156_2x40_P1.27mm_Socket_Horizontal"
    hexID = "FZKCNPCBEDGE4UCON11562X4P127SOHORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': '4UCON_10156_2x40_P1.27mm_Socket_Horizontal', 'description': '4UCON 10156 Card edge socket with 80 contacts (40 each side), through-hole, http://www.4uconnector.com/online/object/4udrawing/10156.pdf', 'tags': '4UCON 10156 Card edge socket with 80 contacts', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_PCBEdge.3dshapes/4UCON_10156_2x40_P1.27mm_Socket_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Connector_PCBEdge : 4UCON_10156_2x40_P1.27mm_Socket_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


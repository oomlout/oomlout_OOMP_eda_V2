
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "WSON-8-1EP_6x5mm_P1.27mm_EP3.4x4.3mm"
    hexID = "FZKSONWSON81EP6X5P127EP34X43"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WSON-8-1EP_6x5mm_P1.27mm_EP3.4x4.3mm', 'description': 'WSON, 8 Pin (http://www.winbond.com/resource-files/w25q32jv%20revg%2003272018%20plus.pdf (page 68)), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'WSON NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/WSON-8-1EP_6x5mm_P1.27mm_EP3.4x4.3mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SON : WSON-8-1EP_6x5mm_P1.27mm_EP3.4x4.3mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


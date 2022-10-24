
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "TDFN-10-1EP_2x3mm_P0.5mm_EP0.9x2mm"
    hexID = "FZKDFNTDFN11EP2X3P5EP9X2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TDFN-10-1EP_2x3mm_P0.5mm_EP0.9x2mm', 'description': 'TDFN, 10 Pin (https://pdfserv.maximintegrated.com/package_dwgs/21-0429.PDF), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'TDFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/TDFN-10-1EP_2x3mm_P0.5mm_EP0.9x2mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : TDFN-10-1EP_2x3mm_P0.5mm_EP0.9x2mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart


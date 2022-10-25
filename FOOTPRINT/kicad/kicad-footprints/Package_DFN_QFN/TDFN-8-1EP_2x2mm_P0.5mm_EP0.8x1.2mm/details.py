
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "TDFN-8-1EP_2x2mm_P0.5mm_EP0.8x1.2mm"
    hexID = "FZKDFNTDFN81EP2X2P5EP8X12"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TDFN-8-1EP_2x2mm_P0.5mm_EP0.8x1.2mm', 'description': 'TDFN, 8 Pin (https://pdfserv.maximintegrated.com/package_dwgs/21-0168.PDF), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'TDFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/TDFN-8-1EP_2x2mm_P0.5mm_EP0.8x1.2mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : TDFN-8-1EP_2x2mm_P0.5mm_EP0.8x1.2mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


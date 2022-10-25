
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "QFN-48-1EP_6x6mm_P0.4mm_EP4.66x4.66mm"
    hexID = "FZKDFNQFN481EP6X6P4EP466X466"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'QFN-48-1EP_6x6mm_P0.4mm_EP4.66x4.66mm', 'description': 'QFN, 48 Pin (https://www.onsemi.com/pub/Collateral/485BA.PDF), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'QFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-48-1EP_6x6mm_P0.4mm_EP4.66x4.66mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : QFN-48-1EP_6x6mm_P0.4mm_EP4.66x4.66mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


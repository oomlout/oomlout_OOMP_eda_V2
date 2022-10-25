
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "WQFN-14-1EP_2.5x2.5mm_P0.5mm_EP1.45x1.45mm"
    hexID = "FZKDFNWQFN141EP25X25P5EP145X145"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WQFN-14-1EP_2.5x2.5mm_P0.5mm_EP1.45x1.45mm', 'description': 'WQFN, 14 Pin (https://www.onsemi.com/pub/Collateral/FUSB302B-D.PDF#page=32), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'WQFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/WQFN-14-1EP_2.5x2.5mm_P0.5mm_EP1.45x1.45mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : WQFN-14-1EP_2.5x2.5mm_P0.5mm_EP1.45x1.45mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


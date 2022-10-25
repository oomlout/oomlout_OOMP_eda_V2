
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_TO_SOT_THT"
    oIndex = "SOD-70_P2.54mm"
    hexID = "FZKSOTSOD7P254"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SOD-70_P2.54mm', 'description': 'Plastic near cylindrical package Sod-70 see: https://www.nxp.com/docs/en/data-sheet/KTY81_SER.pdf  [StepUp generated footprint]', 'tags': 'Sod-70', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_THT.3dshapes/SOD-70_P2.54mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Package_TO_SOT_THT : SOD-70_P2.54mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


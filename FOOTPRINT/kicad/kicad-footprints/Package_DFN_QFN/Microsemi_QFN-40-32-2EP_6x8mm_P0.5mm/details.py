
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "Microsemi_QFN-40-32-2EP_6x8mm_P0.5mm"
    hexID = "FZKDFNMSEMIQFN4322EP6X8P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Microsemi_QFN-40-32-2EP_6x8mm_P0.5mm', 'description': '40-Lead (32-Lead Populated) Plastic Quad Flat, No Lead Package - 6x8x0.9mm Body (https://www.microsemi.com/document-portal/doc_download/131677-pd70224-data-sheet)', 'tags': 'QFN 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Microsemi_QFN-40-32-2EP_6x8mm_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : Microsemi_QFN-40-32-2EP_6x8mm_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


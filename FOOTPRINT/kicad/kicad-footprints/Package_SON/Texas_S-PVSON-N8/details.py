
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "Texas_S-PVSON-N8"
    hexID = "FZKSONTEXASSPVSONN8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_S-PVSON-N8', 'description': '8-Lead Plastic VSON, 3x3mm Body, 0.65mm Pitch, S-PVSON-N8, http://www.ti.com/lit/ds/symlink/opa2333.pdf', 'tags': 'DFN 0.65 S-PVSON-N8', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/Texas_S-PVSON-N8.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SON : Texas_S-PVSON-N8')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


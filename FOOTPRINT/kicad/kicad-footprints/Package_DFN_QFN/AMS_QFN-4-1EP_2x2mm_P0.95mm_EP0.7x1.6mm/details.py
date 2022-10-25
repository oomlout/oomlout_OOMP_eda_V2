
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "AMS_QFN-4-1EP_2x2mm_P0.95mm_EP0.7x1.6mm"
    hexID = "FZKDFNAMSQFN41EP2X2P95EP7X16"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'AMS_QFN-4-1EP_2x2mm_P0.95mm_EP0.7x1.6mm', 'description': 'UFD Package, 4-Lead Plastic QFN (2mm x 2mm), http://ams.com/eng/content/download/950231/2267959/483138', 'tags': 'QFN 0.95', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/AMS_QFN-4-1EP_2x2mm_P0.95mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : AMS_QFN-4-1EP_2x2mm_P0.95mm_EP0.7x1.6mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


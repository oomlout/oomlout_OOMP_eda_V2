
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_QFP"
    oIndex = "PQFP-112_20x20mm_P0.65mm"
    hexID = "FZKQFPPQFP1122X2P65"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PQFP-112_20x20mm_P0.65mm', 'description': 'PQFP, 112 pins, 20mm sq body, 0.65mm pitch (http://cache.freescale.com/files/shared/doc/package_info/98ASS23330W.pdf, http://www.nxp.com/docs/en/application-note/AN4388.pdf)', 'tags': 'PQFP 112', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_QFP.3dshapes/PQFP-112_20x20mm_P0.65mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_QFP : PQFP-112_20x20mm_P0.65mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


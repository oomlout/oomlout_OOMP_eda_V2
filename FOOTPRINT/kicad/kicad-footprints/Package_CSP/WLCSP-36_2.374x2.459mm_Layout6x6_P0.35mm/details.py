
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_CSP"
    oIndex = "WLCSP-36_2.374x2.459mm_Layout6x6_P0.35mm"
    hexID = "FZKCSPWLCSP362374X2459LAYOUT6X6P35"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WLCSP-36_2.374x2.459mm_Layout6x6_P0.35mm', 'description': 'WLCSP-36, https://www.nxp.com/docs/en/package-information/98ASA00604D.pdf', 'tags': 'WLCSP-36', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/WLCSP-36_2.374x2.459mm_Layout6x6_P0.35mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_CSP : WLCSP-36_2.374x2.459mm_Layout6x6_P0.35mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


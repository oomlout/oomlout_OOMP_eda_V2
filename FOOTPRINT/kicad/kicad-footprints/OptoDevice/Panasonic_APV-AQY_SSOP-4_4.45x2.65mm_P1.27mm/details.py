
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "OptoDevice"
    oIndex = "Panasonic_APV-AQY_SSOP-4_4.45x2.65mm_P1.27mm"
    hexID = "FZKOPPAPVAQYSS4445X265P127"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Panasonic_APV-AQY_SSOP-4_4.45x2.65mm_P1.27mm', 'description': 'https://www.panasonic-electric-works.com/cps/rde/xbcr/pew_eu_en/technical_information_photomos_en.pdf', 'tags': 'SSOP4 APV21 AQY22', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/Panasonic_APV-AQY_SSOP-4_4.45x2.65mm_P1.27mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('OptoDevice : Panasonic_APV-AQY_SSOP-4_4.45x2.65mm_P1.27mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


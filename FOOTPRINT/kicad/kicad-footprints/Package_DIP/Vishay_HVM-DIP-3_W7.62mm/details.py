
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DIP"
    oIndex = "Vishay_HVM-DIP-3_W7.62mm"
    hexID = "FZKDIPVISHAYHVMDIP3W762"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Vishay_HVM-DIP-3_W7.62mm', 'description': '3-lead though-hole mounted high-volatge DIP package (based on standard DIP-4), row spacing 7.62 mm (300 mils), see https://www.vishay.com/docs/91361/hexdip.pdf', 'tags': 'THT DIP DIL PDIP 2.54mm 7.62mm 300mil Vishay HVMDIP HEXDIP', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/Vishay_HVM-DIP-3_W7.62mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Package_DIP : Vishay_HVM-DIP-3_W7.62mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


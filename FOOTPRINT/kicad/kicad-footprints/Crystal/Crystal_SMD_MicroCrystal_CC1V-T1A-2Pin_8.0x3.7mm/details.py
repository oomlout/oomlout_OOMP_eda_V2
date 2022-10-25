
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Crystal"
    oIndex = "Crystal_SMD_MicroCrystal_CC1V-T1A-2Pin_8.0x3.7mm"
    hexID = "FZKXXSMMXCC1VT1A2PIN8X37"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Crystal_SMD_MicroCrystal_CC1V-T1A-2Pin_8.0x3.7mm', 'description': 'SMD Crystal MicroCrystal CC1V-T1A series https://www.microcrystal.com/fileadmin/Media/Products/32kHz/Datasheet/CC1V-T1A.pdf, 8.0x3.7mm^2 package', 'tags': 'SMD SMT crystal', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Crystal_SMD_MicroCrystal_CC1V-T1A-2Pin_8.0x3.7mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Crystal : Crystal_SMD_MicroCrystal_CC1V-T1A-2Pin_8.0x3.7mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


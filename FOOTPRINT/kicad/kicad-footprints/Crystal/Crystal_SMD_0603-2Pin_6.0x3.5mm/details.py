
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Crystal"
    oIndex = "Crystal_SMD_0603-2Pin_6.0x3.5mm"
    hexID = "FZKXXSM632PIN6X35"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Crystal_SMD_0603-2Pin_6.0x3.5mm', 'description': 'SMD Crystal SERIES SMD0603/2 http://www.petermann-technik.de/fileadmin/petermann/pdf/SMD0603-2.pdf, 6.0x3.5mm^2 package', 'tags': 'SMD SMT crystal', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Crystal_SMD_0603-2Pin_6.0x3.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Crystal : Crystal_SMD_0603-2Pin_6.0x3.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


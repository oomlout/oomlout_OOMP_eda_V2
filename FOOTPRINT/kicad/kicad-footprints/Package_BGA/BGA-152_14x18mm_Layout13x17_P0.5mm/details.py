
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "BGA-152_14x18mm_Layout13x17_P0.5mm"
    hexID = "FZKBGABGA15214X18LAYOUT13X17P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BGA-152_14x18mm_Layout13x17_P0.5mm', 'description': 'BGA-152_14x18mm_Layout13x17_P0.5mm', 'tags': 'VBGA-152', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/BGA-152_14x18mm_Layout13x17_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : BGA-152_14x18mm_Layout13x17_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


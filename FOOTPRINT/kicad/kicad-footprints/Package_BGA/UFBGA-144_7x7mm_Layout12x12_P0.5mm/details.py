
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "UFBGA-144_7x7mm_Layout12x12_P0.5mm"
    hexID = "FZKBGAUFBGA1447X7LAYOUT12X12P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'UFBGA-144_7x7mm_Layout12x12_P0.5mm', 'description': 'UFBGA-144, 12x12 raster, 7x7mm package, pitch 0.5mm; see section 7.4 of http://www.st.com/resource/en/datasheet/stm32f446ze.pdf', 'tags': 'BGA 144 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/UFBGA-144_7x7mm_Layout12x12_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : UFBGA-144_7x7mm_Layout12x12_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


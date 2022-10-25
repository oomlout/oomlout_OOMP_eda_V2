
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "UFBGA-64_5x5mm_Layout8x8_P0.5mm"
    hexID = "FZKBGAUFBGA645X5LAYOUT8X8P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'UFBGA-64_5x5mm_Layout8x8_P0.5mm', 'description': 'UFBGA-64, 8x8 raster, 5x5mm package, pitch 0.5mm; see section 7.1 of http://www.st.com/resource/en/datasheet/stm32f051t8.pdf', 'tags': 'BGA 64 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/UFBGA-64_5x5mm_Layout8x8_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : UFBGA-64_5x5mm_Layout8x8_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart



######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "UFBGA-201_10x10mm_Layout15x15_P0.65mm"
    hexID = "FZKBGAUFBGA211X1LAYOUT15X15P65"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'UFBGA-201_10x10mm_Layout15x15_P0.65mm', 'description': 'UFBGA-201, 15x15 raster, 10x10mm package, pitch 0.65mm; see section 7.6 of http://www.st.com/resource/en/datasheet/stm32f207vg.pdf', 'tags': 'BGA 201 0.65', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/UFBGA-201_10x10mm_Layout15x15_P0.65mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : UFBGA-201_10x10mm_Layout15x15_P0.65mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


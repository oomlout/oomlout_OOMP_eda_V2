
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Audio"
    oIndex = "Jack_6.35mm_Neutrik_NMJ6HCD2_Horizontal"
    hexID = "FZKCNAUDIOJ635NEUTRIKNMJ6HCD2HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Jack_6.35mm_Neutrik_NMJ6HCD2_Horizontal', 'description': 'M Series, 6.35mm (1/4in) stereo jack, switched, with chrome ferrule and straight PCB pins, https://www.neutrik.com/en/product/nmj6hcd2', 'tags': 'neutrik jack m', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_6.35mm_Neutrik_NMJ6HCD2_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Audio : Jack_6.35mm_Neutrik_NMJ6HCD2_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


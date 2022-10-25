
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Audio"
    oIndex = "Jack_6.35mm_Neutrik_NRJ6HM-1-PRE_Horizontal"
    hexID = "FZKCNAUDIOJ635NEUTRIKNRJ6HM1PREHORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Jack_6.35mm_Neutrik_NRJ6HM-1-PRE_Horizontal', 'description': 'Slim Jacks, 6.35mm (1/4in) stereo jack, metal nose, efficient chassis ground connection, T+R normalling contact, https://www.neutrik.com/en/product/nrj6hm-1-pre', 'tags': 'neutrik jack slim', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_6.35mm_Neutrik_NRJ6HM-1-PRE_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Audio : Jack_6.35mm_Neutrik_NRJ6HM-1-PRE_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


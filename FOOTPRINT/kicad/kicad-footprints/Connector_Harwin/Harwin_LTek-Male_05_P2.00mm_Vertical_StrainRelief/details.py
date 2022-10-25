
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Harwin"
    oIndex = "Harwin_LTek-Male_05_P2.00mm_Vertical_StrainRelief"
    hexID = "FZKCNHARWINHARWINLTEKMALE5P2VERTICALSTRAINRELIEF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Harwin_LTek-Male_05_P2.00mm_Vertical_StrainRelief', 'description': 'Harwin LTek Connector, 5 pins, single row male, vertical entry, strain relief clip', 'tags': 'connector harwin ltek M80', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Harwin.3dshapes/Harwin_LTek-Male_05_P2.00mm_Vertical_StrainRelief.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Harwin : Harwin_LTek-Male_05_P2.00mm_Vertical_StrainRelief')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


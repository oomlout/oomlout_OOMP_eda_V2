
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Converter_DCDC"
    oIndex = "Converter_DCDC_Murata_OKI-78SR_Horizontal"
    hexID = "FZKCONCONMOKI78SRHORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Converter_DCDC_Murata_OKI-78SR_Horizontal', 'description': 'https://power.murata.com/data/power/oki-78sr.pdf', 'tags': '78sr3.3 78sr5 78sr9 78sr12 78srXX', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Converter_DCDC.3dshapes/Converter_DCDC_Murata_OKI-78SR_horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Converter_DCDC : Converter_DCDC_Murata_OKI-78SR_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart



######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_FFC-FPC"
    oIndex = "Molex_502250-2791_2Rows-27Pins-1MP_P0.60mm_Horizontal"
    hexID = "FZKCNFFCFPCMX522527912ROWS27PINS1MPP6HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_502250-2791_2Rows-27Pins-1MP_P0.60mm_Horizontal', 'description': 'Molex Molex 0.30mm Pitch Easy-On BackFlip Type FFC/FPC, 502250-2791, 27 Circuits (http://www.molex.com/pdm_docs/sd/5022502791_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex  top entry', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_FFC-FPC.3dshapes/Molex_502250-2791_2Rows-27Pins-1MP_P0.60mm_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_FFC-FPC : Molex_502250-2791_2Rows-27Pins-1MP_P0.60mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart


# Engineering verification

Checks below apply to the Studio Eight digital design on November 26, 2026. Scope matters here because the enclosure, rendered components and electrical carrier are separate artifacts.

## Enclosure

FreeCAD 1.0.2 imported the STEP assembly as eight valid solids. Each module contributes a lower faceplate, upper faceplate, tray and outer cheek. All 28 distinct solid pairs were intersected. The maximum returned volume was 0.000000 mm³ and no pair exceeded the 0.01 mm³ reporting threshold. This test covers the enclosure pieces. Fit of the complete mechanism, fasteners and harness needs a physical assembly. [STEP](../FADRS-Studio/FADRS-Enclosure.step) · [Pair-by-pair results](evidence/enclosure-check.txt)

To repeat the measurement in the FreeCAD Python console, substitute the path to the STEP file.

```python
import itertools
import Part

solids = Part.read("/path/to/FADRS-Enclosure.step").Solids
print(len(solids), all(solid.isValid() for solid in solids))
volumes = [a.common(b).Volume for a, b in itertools.combinations(solids, 2)]
print(len(volumes), max(volumes), sum(volume > 0.01 for volume in volumes))
```

## Fader clearances

| Nominal check | Inputs | Result |
| --- | --- | ---: |
| Original key-to-case side clearance | 7.50 mm center offset − 3.95 mm switch half-width − 6.50 mm fader case half-width | −2.95 mm |
| Revised key-to-case side clearance | 12.00 − 3.95 − 6.50 mm | 1.55 mm |
| Nearest key to saddle along the travel axis at the top stop | 18.50 mm center offset − 3.75 mm key half-depth − 11.75 mm saddle half-depth | 3.00 mm |

These dimensions describe two different interfaces. The first two rows check the switch body under the panel. The last row checks the visible moving saddle against the key cap. The corresponding parts and panel cuts can be inspected in the [Blender assembly](../FADRS-Studio/FADRS-Studio.blend) and [STEP enclosure](../FADRS-Studio/FADRS-Enclosure.step).

## Single-fader carrier

KiCad 9.0.7 checked the passive breakout for one Bourns PSM01-081A-103B2. ERC returned zero errors and warnings. DRC returned zero violations, unconnected pads and footprint errors. The parity-enabled run reported zero schematic parity issues. [ERC report](evidence/carrier-erc.txt) · [DRC report](evidence/carrier-drc.txt) · [CLI results](evidence/carrier-checks.txt)

From the project root, with KiCad 9 on the path, run the following. The reports are written to the working directory.

```sh
board=FADRS-Studio/Fader-Carrier/Fader-Carrier
kicad-cli sch erc --exit-code-violations -o carrier-erc.txt "$board.kicad_sch"
kicad-cli pcb drc --schematic-parity --exit-code-violations -o carrier-drc.txt "$board.kicad_pcb"
```

## Blender assembly and renders

The device meshes occupy 541.00 × 270.23 × 72.55 mm including the controls, feet and rear connector. A scene inventory checked eight modeled faders, eight channel displays, eight carrier instances, 53 switches and four dual motor drivers. The file reopened with nine packed screen images, four cameras and five studio lights. The hero is the default camera. The four portfolio PNGs came from Cycles with AgX color management. [Scene inventory](evidence/blender-scene.txt) · [Render settings](../FADRS-Studio/render.py)

The portable scene stores 127 panel legends as geometry. Each legend object retains its original string in the `legend_text` custom property. Before and after conversion, a 691 × 460 hero proof rendered with the same settings had identical decoded RGB pixels.

## Work remaining before a hardware demonstration

| Milestone | Evidence to collect |
| --- | --- |
| One physical channel | Check fader pinout and motor tabs against a sample, board fit, saddle retention, full travel and the switch clearance with tolerances. |
| Powered fader control | Measure current under expected loads, tune closed-loop positioning and verify that touch reliably releases the motor. |
| Master and interconnect | Complete the controller, display, USB and power circuits. Check the two-module harness pinout, strain relief and service access. |
| DAW integration | Implement and test firmware with Ableton Live and Studio One, including banking, transport and automation feedback. |
| Complete enclosure | Assemble both modules with the intended materials and fasteners. Check cable fit, access and operation across all eight channels. |

# FADRS Studio Eight

an eight-channel motorized daw controller with a separate master transport. the assembled model measures **541 × 270 × 73 mm** including the rear connector and controls. the deck rises 4.5° from the front edge. the fader bank uses 40 mm channel spacing and 100 mm of travel.

each channel has an oled track name and level display, a rotary encoder, and dedicated record, solo, mute and select keys. the master has a 4.3-inch display, a 68 mm jog wheel with a machined thumb recess, bank and channel navigation, and five transport keys. the marked unity point and the displayed channel levels use the same fader scale.

## open the design

Use Blender 5, a STEP-capable mechanical CAD application and KiCad 9 respectively. Open the KiCad project with its accompanying libraries in the same folder.

| file | contents |
| --- | --- |
| [FADRS-Studio.blend](FADRS-Studio.blend) | editable blender 5 scene. includes the four cameras, five studio lights, nine packed screen images and outlined panel lettering. objects are grouped by channel, master, housing and electronics. |
| [FADRS-Hero.png](FADRS-Hero.png) | 3840 × 2560 three-quarter product render in cycles |
| [FADRS-Panel.png](FADRS-Panel.png) | 3200 × 1980 elevated view of both modules |
| [FADRS-Faders.png](FADRS-Faders.png) | 2880 × 1800 detail of the fader bank |
| [FADRS-Transport.png](FADRS-Transport.png) | 2700 × 1800 detail of the jog wheel and transport |
| [FADRS-Enclosure.step](FADRS-Enclosure.step) | eight separate enclosure solids in assembly position. includes the faceplates, trays and outer cheeks, panel openings, mounting bosses and the inter-module harness passage. units are millimetres. |
| [Fader-Carrier/Fader-Carrier.kicad_pro](Fader-Carrier/Fader-Carrier.kicad_pro) | editable schematic and routed 148 × 25 mm two-layer terminal carrier for one fader. eight instances of its exported board geometry are present in the scene. |
| [render.py](render.py) | renders any of the four views from the packed scene |

the two bays bolt together through the inner walls. the proposed service harness passes between them. the tops combine a pearl powder-coated lower deck with a graphite display band. the outer cheeks are oxblood anodized aluminum. the nickel-finished fader saddles expose a conductive surface for touch sensing.

## component provenance

the early FADRS design selected the Teensy 4.1 and RA8875. a february 2026 schematic snapshot also identified the Bourns PSM01 fader. studio eight carries those choices and the separate master module into a new enclosure and control layout. the original schematic was an early parts study. the diagram and routing included here are for the single-fader carrier.

| component | quantity | geometry represented in the scene |
| --- | ---: | --- |
| bourns PSM01-081A-103B2 | 8 | reconstructed from the manufacturer's 100 mm pc-terminal drawing and the supplied land pattern. the visible saddle is custom. the motor can, pulleys and belt are simplified. [bourns drawing](https://www.bourns.com/docs/product-datasheets/psm.pdf) |
| pjrc teensy 4.1 | 1 | imported community assembly step by zack kummer, distributed in the XenGi teensy footprint library. [model repository](https://github.com/XenGi/teensy.pretty) · [pjrc dimensions](https://www.pjrc.com/teensy/dimensions.html) |
| raio RA8875L3N | 1 | imported 100-pin package step from the project's component cache. its supporting circuit board is a layout envelope. [component record](https://www.snapeda.com/parts/RA8875L3N/Raio/view-part/) |
| adafruit 938 monochrome oled | 8 | adafruit's original module step, with a packed 128 × 64 pixel session image over the active area. [product](https://www.adafruit.com/product/938) · [adafruit cad](https://github.com/adafruit/Adafruit_CAD_Parts) |
| adafruit 1591 touchscreen | 1 | 105.6 × 67 × 4.3 mm package reconstructed from the module dimensions. the session view uses its 480 × 272 pixel resolution. [product and drawing](https://www.adafruit.com/product/1591) |
| e-switch TL1240xQ1Jxxx series | 53 | supplier step mesh used for every switch. lens colors and illuminated states are illustrative. five custom transport key shells sit above the switch actuators. [supplier](https://www.e-switch.com/product/tl1240-series-illuminated-through-hole-tactile-switch/) |
| bourns PEC11R-4220F-S0024 | 8 | shaft, mounting barrel and body envelopes. the fluted caps are custom. [bourns drawing](https://www.bourns.com/docs/product-datasheets/pec11r.pdf) |
| pololu 713 dual motor driver | 4 | original pololu step, one dual driver per two faders. [supplier cad](https://www.pololu.com/product/713/resources) |
| same sky PJ-005A and UJ20-C-V-C-3-SMT-TR | 1 each | supplier step geometry for the barrel jack and usb-c receptacle. the usb-c daughterboard interface is a proposed connection to the teensy. [dc jack](https://www.sameskydevices.com/product/resource/pj-005a.pdf) · [usb-c receptacle](https://www.sameskydevices.com/product/resource/uj20-c-v-c-3-smt-tr.pdf) |
| jst B10B-PHDSS, 10 positions | 2 | kicad step geometry from the related hardware archive. plug bodies and the jumper illustrate the service connection. [jst phd series](https://www.jst-mfg.com/product/pdf/eng/ePHD.pdf) |

the component meshes represent a mix of supplier CAD, community CAD and reconstructions. tessellation, placement, finishes and screen artwork belong to the studio scene. the current enclosure, fader saddles, encoder caps, jog wheel and transport key shells were modeled for FADRS. licensing notices for the reused libraries accompany the source credits. [Adafruit CAD license](../docs/licenses/adafruit-cad-MIT.txt) · [XenGi library license](../docs/licenses/teensy-library-MIT.txt) · [KiCad library terms](https://www.kicad.org/libraries/license/)

## single-channel wiring

the carrier brings the seven numbered RV1 contacts out to two groups of solder pads. these references preserve the supplied land-pattern numbering. trace a terminal through the schematic before assigning it a function in a future controller design.

| solder group | pin 1 | pin 2 | pin 3 | pin 4 |
| --- | --- | --- | --- | --- |
| J1 | T3 | T7 | T6 | — |
| J2 | T2 | T1 | T4 | T5 |

motor tabs A and B connect separately to the intended motor driver. the wire groups take leads from the underside to keep connector bodies out of the travel envelope. [Schematic](Fader-Carrier/Fader-Carrier.kicad_sch) · [PCB](Fader-Carrier/Fader-Carrier.kicad_pcb) · [Board plot](../docs/images/fader-carrier.svg)

## verification and build status

the enclosure step reopens as eight valid solids. pairwise checks found no positive-volume overlaps between them. the channel keys clear the 13 mm fader case by at least 1.55 mm laterally in the nominal model. at full travel, the nearest key and saddle have 3.0 mm of separation along the travel axis.

the carrier preserves the seven numbered pcb contacts and two locating holes from the supplied footprint. its two solder-pad groups break out those seven terminals. the two motor tabs require a separate connection to the driver. kicad 9.0.7 reported zero erc findings, zero drc findings, zero unconnected pads and zero schematic-to-board parity issues.

the full controller is an industrial-design prototype. the master and control electronics, power distribution, firmware, touch response, custom cap retention, physical tolerances and assembly still need bench validation. the screen images show a sample daw session. the parts table identifies modeled components and does not serve as a complete purchasing bom.

[Measurements, raw check results and remaining bench work](../docs/verification.md) · [Portfolio case study and image captions](../docs/portfolio.md)

## render again

open the blend file and press F12 for the hero. from a shell in this folder, run one of the following with blender on your path.

```sh
blender --background FADRS-Studio.blend --python render.py -- --output renders
blender --background FADRS-Studio.blend --python render.py -- --shot transport --preview --output previews
```

Use `--shot hero panel faders transport` to select shots, or omit the option to render all four. The lighting, materials, geometry and cameras are editable. Panel legends are meshes, with their source strings saved in each object’s `legend_text` custom property. The OLED and transport screen images are packed into the scene.

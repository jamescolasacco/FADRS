# FADRS Studio Eight · portfolio case study

## Project card

**FADRS Studio Eight** is a digital prototype for an eight-channel motorized DAW controller. A detachable transport pairs a 68 mm jog wheel with dedicated playback controls, while each channel keeps its track name, level and controls together.

| Field | Detail |
| --- | --- |
| Project | Independent music hardware concept by James Colasacco |
| Discipline | Industrial design, mechanical integration, PCB layout, product visualization |
| Tools | Blender 5.0.1 with Cycles, FreeCAD 1.0.2, KiCad 9.0.7 |
| Scope | Component-based digital assembly, enclosure CAD, one routed fader carrier and four studio renders |
| Target workflows | Mixing and transport in Ableton Live and Studio One. DAW integration is a design target. |
| Contribution | James set the concept and product direction. CAD implementation, PCB layout, rendering and documentation were AI-assisted. Supplier and community model credits are in the [parts reference](../FADRS-Studio/README.md#component-provenance). |

## The design brief

How much of a mix can you read with your hand still on a fader? FADRS gives each of eight tracks a fixed vertical strip. The OLED shows a track name and level, the encoder sits directly below it, and record, solo, mute and select cluster above the fader. A separate master module holds navigation and transport. Its fixed position gives the operator a stable reference when moving to another bank of tracks.

The 100 mm Bourns fader set the depth of the design. The strips sit on 40 mm centers so the controls, labels and mounting points can repeat across the bank. A pearl lower deck makes the fader positions easy to pick out in the render. A graphite band groups the displays and encoders, and oxblood cheeks mark the outside edges of the two-module assembly. These finishes are material proposals.

## The decision worth showing

An earlier layout put the right-hand channel keys just 7.5 mm from the fader centerline. A 13 mm fader case extends 6.5 mm from that line. Adding the 3.95 mm half-width of the switch body put the two nominal envelopes 2.95 mm into each other.

The redesign moved those keys 4.5 mm outward, placing both columns 12 mm from the centerline. The switch carrier gained a U-shaped cutout around the motor and the encoder moved to its own mounting plane. The resulting nominal side clearance is **1.55 mm**, with **3.0 mm** between the nearest key and saddle at the end of travel. This is a geometry result. Checking the complete tolerance stack requires actual parts. [Layout close-up](../FADRS-Studio/FADRS-Faders.png) · [Calculations and checks](verification.md)

## From a strip to a board

A repeatable channel starts under the faceplate. A 148 × 25 mm passive carrier breaks the fader’s seven numbered contacts out to two groups of underside solder pads. The motor tabs run separately to the proposed driver. One editable board supplies the geometry for all eight instances in the Blender assembly. KiCad reported zero electrical-rule and design-rule violations on that board, with zero unconnected pads and zero schematic parity issues. [Board source](../FADRS-Studio/Fader-Carrier/Fader-Carrier.kicad_pcb) · [Test records](verification.md#single-fader-carrier)

![KiCad plot of the long, narrow carrier with one group of signal pads at each end](images/fader-carrier.svg)

## Portfolio paragraph

> I started FADRS to explore how I wanted to mix eight tracks with my hands. Each strip keeps the track name, level, encoder and fader in one line, while a separate transport gives playback and navigation a permanent home. Packaging the parts changed the layout. The first switch position conflicted with the fader body, so the redesign moved the keys outward and gave the motor its own clearance cutout. The digital prototype includes an eight-piece enclosure, a routed single-fader PCB and four Blender studio renders. Physical fit, motor control and DAW integration are the next engineering milestones.

## Image selection

The linked PNGs are the full-resolution originals. The captions can accompany galleries, project cards or slides.

| Image | Caption | Alt text |
| --- | --- | --- |
| [Hero · 3840 × 2560](../FADRS-Studio/FADRS-Hero.png) | Studio Eight brings eight long-throw faders and a dedicated transport into a two-module desktop surface. | Three-quarter render of a pearl and graphite controller with eight silver faders and red side cheeks. |
| [Panel · 3200 × 1980](../FADRS-Studio/FADRS-Panel.png) | Each strip pairs a track display with its encoder, four channel keys and fader. The transport occupies the right module. | Elevated view of the full panel with eight labeled OLEDs at left and a session display above the jog wheel at right. |
| [Fader detail · 2880 × 1800](../FADRS-Studio/FADRS-Faders.png) | The custom saddles sit on 40 mm centers. The switch placement clears the fader case beneath the deck. | Close-up of silver fader saddles at different levels with record, solo, mute and select keys above them. |
| [Transport detail · 2700 × 1800](../FADRS-Studio/FADRS-Transport.png) | A recessed thumb pocket and ridged edge give the proposed 68 mm jog wheel two grip positions. | Close-up of the round jog wheel, playback keys and master session display. |

For a short project card, use the hero and the first paragraph. For a longer case study, follow the hero with the panel view, fader detail and PCB plot. The full controller is at the digital prototype stage. An assembled unit, measured motor or touch performance and tested DAW support are future milestones. [Engineering evidence](verification.md)

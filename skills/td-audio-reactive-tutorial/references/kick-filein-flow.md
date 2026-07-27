# kick.toe File In Peak Speed Flow

Observed compact single-flow audio block under `/project1`:

```text
audiofilein1
  -> audiodevout1
  -> math3(gain 0.5)
       -> analyze1(function maximum)
            -> filter1
                 -> math2(gain 100)
                      -> null6
                 -> speed2
```

## Nodes

| Node | Type | Input | Output | Important Parameters |
| --- | --- | --- | --- | --- |
| `audiofilein1` | `audiofileinCHOP` | none | `audiodevout1`, `math3` | project audio file, `play=True` |
| `audiodevout1` | `audiodeviceoutCHOP` | `audiofilein1` | none | playback monitor |
| `math3` | `mathCHOP` | `audiofilein1` | `analyze1` | `chanop=avg`, `gain=0.5` |
| `analyze1` | `analyzeCHOP` | `math3` | `filter1` | `function=maximum` |
| `filter1` | `filterCHOP` | `analyze1` | `math2`, `speed2` | `type=gauss`, `width=0.2`, `widthunit=seconds`, `timeslice=True` |
| `math2` | `mathCHOP` | `filter1` | `null6` | `gain=100` |
| `null6` | `nullCHOP` | `math2` | none | final envelope output |
| `speed2` | `speedCHOP` | `filter1` | none | cumulative speed/motion output |

## Signal Shapes

- `audiofilein1`: raw stereo audio, 44100 Hz.
- `math3`: stereo averaged into one channel with `chanop=avg`, then scaled by `gain=0.5`, still audio-rate.
- `analyze1`: one 60 FPS peak/maximum control sample.
- `filter1`: smoothed continuous control sample. In the tested project, `width=0.2 seconds`; a recreated node left at `1.0 seconds` will not match.
- `null6`: amplified continuous envelope for downstream parameter control.
- `speed2`: accumulated motion-style driver from the smoothed envelope. Absolute value depends on run time and reset timing.

## Test Result

The block was recreated in `/project1` with test node names. The first attempt differed because:

- The recreated source Math CHOP initially kept two channels. Setting `chanop=avg` matched original `math3`.
- The recreated Filter CHOP initially used TD's default `width=1.0 seconds`. Setting `width=0.2 seconds` matched the learned original parameter.
- The recreated Speed CHOP did not match original `speed2` numerically because `Speed CHOP` is cumulative and the original had been running longer.

## Notes

- Use this flow when a project needs a simple overall-energy envelope plus an accumulated motion driver.
- Keep it separate from `Audio Analysis COMP` workflows, which produce prebuilt channels such as `kick`, `snare`, `low`, `mid`, and `high`.
- Keep it separate from spectrum workflows. Spectrum produces frequency bins or texture data rather than the same kind of control signal as `null6`.

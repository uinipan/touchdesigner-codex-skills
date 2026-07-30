# Audio Tutorial Pattern Map

These tutorials supply reusable visual and mapping patterns. The packaged TOX remains the default signal source.

## Core Audio-Reactive Tutorials

| Tutorial | Main contribution | Suggested TOX use |
| --- | --- | --- |
| [Make Anything Audio Reactive](https://www.youtube.com/watch?v=rGoCbVmGtPE) | General audio-to-parameter mapping across many visual targets | Start with envelope; add triggers for discrete changes |
| [Audio-reactive psychedelic visuals](https://www.youtube.com/watch?v=Mt2hwb5cngA) | Math CHOP shaping and TOP modulation for psychedelic motion | Envelope or speed into TOP parameters |
| [Audio Reactive Visuals With TouchDesigner](https://www.youtube.com/watch?v=dkWwZ1CryYo) | Noise, translation, and beat-driven parameterization | Speed for motion; triggers for beat changes |
| [Audio-Reactive Visuals in TouchDesigner](https://www.youtube.com/watch?v=R7sAomk2vR4) | Audio analysis and beat detection | Triggers/count; extend manually for custom detection |
| [Audio Reactive Spectrum Visual](https://www.youtube.com/watch?v=jaXFcHgguq0) | Frequency spectrum and band mapping | Add a manual spectrum lane because the documented TOX contract has no primary spectrum output |

## Cross-Direction Tutorials

| Tutorial | Main contribution | Suggested handoff |
| --- | --- | --- |
| [Audioreactive Particle Cloud](https://www.youtube.com/watch?v=olhePB-r7I4) | Audio-driven particle cloud, ParticlesGPU, camera sequencing | Envelope to size/force; triggers to bursts; speed to camera/phase |
| [Audio Reactive 3D Point Clouds](https://www.youtube.com/watch?v=rlptcQpTMuo) | Audio-driven 3D point clouds and instancing | Envelope/bands to scale and displacement; triggers to state changes |
| [Audio Reactive & Motion Controlled Visuals](https://www.youtube.com/watch?v=qRTRJziqoJk) | Hybrid audio and body-tracking control | Keep audio and tracking buses separate; combine only at named visual parameters |

## Reusable Design Patterns

- Envelope -> brightness, scale, opacity, displacement, feedback gain.
- Speed -> rotation, translation, noise evolution, texture phase.
- Kick trigger -> flash, particle burst, camera punch, reset.
- Snare trigger -> cut, color inversion, alternate state.
- Count -> Switch index, progressive reveal, persistent variation.
- Bass/mid/high -> separate visual layers.
- Spectrum TOP -> bars, scanlines, mask, displacement, shader texture.

For combined effects, give each signal one readable role. Avoid connecting a single mixed audio value to every parameter.

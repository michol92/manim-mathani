---
title: Cameras
---

```mermaid
graph LR
* --> camera
camera --> MappingCamera
camera --> MovingCamera
MovingCamera --> MultiCamera
camera --> OldMultiCamera
OldMultiCamera --> SplitScreenCamera
camera --> ThreeDCamera
* --> BackgroundcoloredVMobjectDisplayer
```

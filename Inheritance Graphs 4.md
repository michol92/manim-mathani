---
title: Scenes
---

```mermaid
graph LR
* --> ScenefileWriter
* --> RerunSceneHandler
* --> Scene
Scene --> VectorScene
VectorScene --> LinearTransformationScene
Scene --> MovingCameraScene
MovingCameraScene --> ZoomedScene
Scene --> ThreeDScene
ThreeDScene --> SpecialThreeDScene
```

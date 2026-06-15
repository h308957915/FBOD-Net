Lightweight Multi-scale Feature Learning for Real-time Small Object Detection in Drone Imagery

[Lightweight Multi-scale Feature Learning for Real-time Small Object Detection in Drone Imagery] Jianli Hu, Tingting Song, Yichen Ye 
All experiments were conducted on an NVIDIA GeForce RTX 4060 Ti graphics card. The software configurations are as follows: Python 3.12.9, PyTorch 2.5.1 and CUDA 12.4. For model training, the batch size of input images was set to 16, while the initial learning rate and optimizer weight decay adopted default values. Stochastic Gradient Descent (SGD) was used as the optimizer.
abstract:
Drone-based visual perception requires object detectors that can recognise small, densely distributed and scale-varying targets while remaining deployable on resource-constrained aerial platforms. Existing real-time detectors have improved accuracy for aerial imagery, but many rely on heavier feature pyramids or detection heads that increase computational cost and limit practical onboard deployment. This study proposes FBOD-Net, a lightweight real-time object detection framework designed for drone imagery. The method introduces a multi-scale dilated convolution module that progressively enlarges the receptive field to capture fine target details, local structural cues and broader contextual information without substantially increasing model complexity. It further incorporates a slim dual-branch detection architecture that reduces redundant channels and simplifies the detection head while preserving multi-level feature fusion for small-object localisation. Experiments are conducted on three public drone-image benchmarks, VisDrone2019, AI-TOD and HIT-UAV, using comparisons with multiple YOLO-series and transformer-based real-time detectors. The results indicate that the proposed framework achieves a competitive balance between detection accuracy, parameter efficiency, model size and inference speed. On VisDrone2019, the lightweight variant improves mAP50 over the baseline while reducing model size, and the larger variant further improves precision and mAP while maintaining real-time performance. Experiments on AI-TOD and HIT-UAV demonstrate generalisation to tiny-object and infrared UAV scenarios. Ablation studies further show that channel reduction, the dual-branch design and the multi-scale dilated convolution module each contribute to the final trade-off between compactness and accuracy. The proposed approach offers a practical direction for efficient drone-image object detection and provides a basis for future work on more robust cross-scale feature modelling in complex aerial scenes.This code is available at https://github.com/h308957915/FBOD-Net.

Dataset:
Vistrone2019 (https://github.com/ultralytics/yolov5/releases/download/v1.0/VisDrone2019-DET-train.zip, https://github.com/ultralytics/yolov5/releases/download/v1.0/VisDrone2019-DET-val.zip, https://github.com/ultralytics/yolov5/releases/download/v1.0/VisDrone2019-DET-test-dev.zip)

Installation
conda virtual environment is recommended.
conda create -n FBOD-Net python=3.12
conda activate FBOD-Net
pip install -r requirements.txt
pip install -e .

Training
python train.py

Validation
python val.py

Citation
This paper submission is for the submission to the journal <<The Visual Computer>>.

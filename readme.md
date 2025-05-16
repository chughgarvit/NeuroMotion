# NeuroMotion: A Multi-Modal Dataset for Combined Activities

## About the Dataset
NeuroMotion is a dataset designed for research in human activity recognition and gesture analysis using wearable technology. It captures a wide range of single-labeled activities performed concurrently in diverse real-world scenarios.

![Illustration of activities collected. (a) Head gestures (facial and eye) IMU signatures are captured using an earable device, including specific eye movements and facial expressions. (b) Various scenarios where these activities were performed, such as driving, sitting as a passenger, running on a track, running on a treadmill, and running on a mountain hill.](dataset_images.png)

## Dataset Documentation and Intended Uses
The dataset can be used for developing robust recognition algorithms for healthcare, human-computer interaction, and other mobile applications.

## Access the Dataset
You can access the dataset and its metadata using the following links:
- [Dataset and Benchmark](https://github.com/chughgarvit/NeuroMotion/tree/main/code/imu/)

# Code Usage

## Notebook Files

The code usage can be found in the following notebook files:

- **Accuracy**:
  - [`./code/acc_112.ipynb`](./code/acc_112.ipynb)
  - [`./code/acc_gcc_118.ipynb`](./code/acc_gcc_118.ipynb)
  - [`./code/acc_gcc_224.ipynb`](./code/acc_gcc_224.ipynb)

- **MSE Benchmarking**:
  - [`./code/EE_Prep.ipynb`](./code/EE_Prep.ipynb)

## Other Files

The rest of the files are used for preprocessing and cleaning.

## Baseline Models and Results

### Baseline Models
We evaluated a range of model architectures to provide baseline performance on the NeuroMotion dataset. These models include:
- **Long Short-Term Memory (LSTM) Networks**
- **Support Vector Machine (SVM)**
- **Decision Tree (DT)**
- **Random Forest (RF)**
- **Recurrent Neural Networks (RNN)**
- **Gated Recurrent Unit (GRU)**
- **Co-training Setup of SVM and DT (CL)**

### Evaluation Metrics
The macro F1 score was used to evaluate classification performance due to the dataset's class imbalance. Mean Squared Error (MSE) was used to validate the prediction of IMU-based intensity detection with HRV from the smartwatch.

### Results
Below is a table summarizing the performance of different models under various protocols and settings.

| Protocol | P1 (F1 Score) | | | P2 (F1 Score) | | | P3 (F1 Score) | | | MSE (%) | | |
| -------- | ------------- | - | - | ------------- | - | - | ------------- | - | - | ------- | - | - |
| Setting  | S1            | S2 | S3 | S1            | S2 | S3 | S1            | S2 | S3 | R     | T | TM |
| LSTM     | 0.93          | 0.91 | 0.85 | 0.82 | 0.86 | 0.88 | 0.79 | 0.76 | 0.65 | 1.60 | 1.77 | 1.58 |
| SVM      | 0.91          | 0.87 | 0.90 | 0.93 | 0.89 | 0.90 | 0.81 | 0.71 | 0.73 | 1.67 | 2.14 | 1.89 |
| DT       | 0.80          | 0.82 | 0.76 | 0.88 | 0.82 | 0.89 | 0.75 | 0.74 | 0.79 | 1.80 | 1.91 | 2.18 |
| RF       | 0.91          | 0.88 | 0.87 | 0.78 | 0.74 | 0.76 | 0.86 | 0.82 | 0.83 | 0.89 | 1.16 | 1.12 |
| RNN      | 0.79          | 0.74 | 0.72 | 0.81 | 0.79 | 0.77 | 0.84 | 0.81 | 0.82 | 1.14 | 1.51 | 1.34 |
| GRU      | 0.85          | 0.81 | 0.84 | 0.88 | 0.83 | 0.79 | 0.71 | 0.74 | 0.70 | 1.63 | 1.81 | 1.76 |
| CL (SVM+DT) | 0.88       | 0.82 | 0.83 | 0.91 | 0.89 | 0.87 | 0.81 | 0.77 | 0.79 | 2.11 | 1.93 | 2.05 |

### Note on the Results
- **Protocol P1:** Includes 11 facial expressions (eye gestures).
- **Protocol P2:** Involves 5 fixed environments (car, road, track, treadmill).
- **Protocol P3:** Includes all 16 activities.
- **Setting S1:** Random Split.
- **Setting S2:** Cross-Subject Split.
- **Setting S3:** Cross-Environment Split.
- **MSE R:** Running.
- **MSE T:** Treadmill.
- **MSE TM:** Track.

## Acknowledgements
We thank the participants for their contributions. This work is funded by the project "Detecting Behavioral Health Disorders of Older Adults using Self-supervised Learning and Causal Reasoning" (Ref. No. S/TIH-ISI/SCB/20220090), sponsored by TIH at ISI Kolkata under the TIH-NSF joint research program, in collaboration with IIT Jodhpur (India), IIT Kharagpur (India), and UMBC (USA).

---

## Legal

NeuroMotion uses the Apache 2.0 license for code found on the associated GitHub repo and the Creative Commons Attribution 4.0 license. The [LICENSE file](https://github.com/chughgarvit/NeuroMotion/main/LICENSE) for the repo can be found in the top-level directory.

## Contact

For any questions or issues, please contact Garvit Chugh at [chugh.2@iitj.ac.in](mailto:chugh.2@iitj.ac.in).

&copy; 2024 NeuroMotion Dataset. All rights reserved.

# Text-to-Speech (TTS) System for OCR-Generated Text

## Introduction
- Reading challenges are common, especially for the visually impaired. Converting text to audio seamlessly is crucial to making information more accessible and inclusive.
- Text-to-Speech (TTS) System for OCR-Generated Text transforms printed or digital text into audio, addressing the need for quick and easy access to information.

## Hardware Evolution
- Initial Hardware Choice: Arduino Nano 33 BLEwith OV7675 camera module.
- Issue: Insufficient image resolution for ML model training.
- Midway Transition: Shifted to ESP32 CAM with OV2640 camera module.
- Challenge: RAM limitations hindered model deployment on ESP32.
- Optimal Solution: Finalized Raspberry Pi 4 for robust performance.
- Features: Raspberry Pi 4 offers ample RAM, processing power, and GPIO support, essential for efficient OCR implementation.

## Iterative Model Development
- Algorithm Training:Utilized synthetic data for initial training iterations.
- Challenges Encountered:Overcame dataset annotation issues and model performance drawbacks through iterative training.
- Optimization Strategies:Fine-tuned the model to achieve real-time OCR on Raspberry Pi 4.

## Results
- Performance Metrics: Achieved OCR accuracy rate of 74% with 'mjsynth' dataset on Raspberry Pi 4.
- Real-time Demonstration:Live showcase of text-to-audio conversion on Raspberry Pi 4, reinforcing practicality.

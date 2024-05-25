<h1 align="center">AIM (Aircraft Inspection and Monitoring)</h1>

### PROBLEM STATEMENT


<strong>AIM</strong> A Two-Level CRM and Aircraft Inspection and Monitoring Software with state-of-the-art damage detection models that take care of the entire lifecycle of Aircraft Maintenance, Inspection & Repair, providing insights to a persona at a different level. 



# Features 

- <strong> Image Segmentation & Object Detection with YoloV9</strong>:  machine learning algorithms to assess the severity and extent of damage on aircraft surfaces, now it can detect.
    
```commandline
  0: crack
  1: dent
  2: missing-head
  3: paint-off
  4: scratch
```

- <strong> RAG LLM Chatbot Model</strong>: Trained on Airbus data, to help operators & technicians find quick resolutions without reading the entire Airbus operating & maintenance manual.
- <strong> Image to Text</strong>: Using Google Gemini Pro, operators can upload a photo of an Aircraft Part that he is unaware of, and the LLM models will give them the details of that Aircraft Part.
- <strong> CRM Software</strong>: helps Airlines, MROs, and Airbus to maintain all customer-related data at one single place and drive their customer success journey through insightful analytics.


## 1. Project Architecture

<p align="center">
  <img src="data/architecture/AIM.png" />
</p> 

#### Chatbot Generative AI RAG (Retrieval Augment Generation) Architecture

<p align="center">
  <img src="data/architecture/RAG.png" />
</p> 


#### Database Entity–relationship Diagram

<p align="center">
  <img src="data/architecture/Airbus_ER_diagram.png" width="400"/>
  <img src="data/architecture/Postgres.png" width="400"/>
</p> 


## 2. Getting Started With The Fast API Application

```sh
$ git clone https://github.com/raj713335/AIM.git
$ cd AIM
$ pip install -r requirements.txt
$ pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
$ python main.py
```

Swagger UI `http://localhost:5000/docs`

Run `uvicorn main:app --reload`



## 3. Running the Test Cases

```sh
$ cd AIM
$ pytest --disable-warnings  
```

## 4. Run this project with docker locally

```sh
$ cd AIM
$ docker system prune 
$ docker-compose -f docker-compose.yml up -d --build
```



## 5. Getting Started With UI Application

```sh
$ git clone https://github.com/raj713335/AIM_UI.git
$ cd AIM_UI
$ npm i
```


## 6. Project Requirements

<h4>Languages</h4>
<ul>
  <li>KeyCloak 24.0.0</li>
  <li>Python 3.11.4</li>
</ul>




## 7. Application Screenshots / <a href="">Demo.</a>

<p align="center">
  <img src="data/screenshots/1.png" width="400"/>
</p>


## YoloV9 Object Segmentation & Detection Metrics

<br />
<p align="center">
  <img src="data/yoloV9/BoxF1_curve.png" width="200"/>
  <img src="data/yoloV9/BoxP_curve.png" width="200"/>
  <img src="data/yoloV9/BoxPR_curve.png" width="200"/>
  <img src="data/yoloV9/BoxR_curve.png" width="200"/>
  <img src="data/yoloV9/confusion_matrix.png" width="200"/>
  <img src="data/yoloV9/labels.jpg" width="200"/>
  <img src="data/yoloV9/labels_correlogram.jpg" width="200"/>
  <img src="data/yoloV9/MaskF1_curve.png" width="200"/>
  <img src="data/yoloV9/MaskP_curve.png" width="200"/>
  <img src="data/yoloV9/MaskPR_curve.png" width="200"/>
  <img src="data/yoloV9/MaskR_curve.png" width="200"/>
  <img src="data/yoloV9/results.png" width="200"/>
</p>
<br />

#### Train Batch/ Results 

<br />
<p align="center">
  <img src="data/yoloV9/train_batch0.jpg" width="200"/>
  <img src="data/yoloV9/train_batch1.jpg" width="200"/>
  <img src="data/yoloV9/train_batch2.jpg" width="200"/>
</p>
<br />

#### Validation Batch/ Results 

<br />
<p align="center">
  <img src="data/yoloV9/val_batch0_labels.jpg" width="200"/>
  <img src="data/yoloV9/val_batch0_pred.jpg" width="200"/>
  <img src="data/yoloV9/val_batch1_labels.jpg" width="200"/>
  <img src="data/yoloV9/val_batch1_pred.jpg" width="200"/>
  <img src="data/yoloV9/val_batch2_labels.jpg" width="200"/>
  <img src="data/yoloV9/val_batch2_pred.jpg" width="200"/>
</p>
<br />



## 8. Components to be built (Work In Progress)

* [x] API Enhancement.
* [x] API Optimization.
* [x] Connecting API with creo 3D Software.

<h1 align="center">AIM (Aircraft Inspection and Monitoring)</h1>

### PROBLEM STATEMENT


<strong>AIM</strong> Aircraft Inspection and Monitoring 


# Features 

- Aircraft Inspection and Monitoring.



## 1. Project Architecture

<p align="center">
  <img src="data/AIM.png" />
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



## 8. Components to be built (Work In Progress)

* [x] API Enhancement.


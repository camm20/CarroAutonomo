# Carro Autonomo
### Python3 + Raspberry Pi 3 B+ y OpenCV

See self-driving in action  

<a href="https://youtu.be/Xx6qgGh_JXU
" target="_blank"><img src="https://i9.ytimg.com/vi/Xx6qgGh_JXU/mqdefault.jpg?sqp=CLz2w6QG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGFsgWyhbMA8=&rs=AOn4CLBnsm2dZocVwf8ZpdSMihY4PrMWpw" width="360" height="240" border="10" /></a>


Este proyecto consiste en la construcción de un vehiculo autonomo, el cual debe de recorrer por una pista establecidad y detectar las señales de Stop y Semaforo ademas de recorrer de forma correcta por la pista dada, para ello se procede a realizar un entrenamiento guíado del recorrido de la pista y posteriormente se entrena la red neuronal para obtener los pesos de la pista.
  
### Para la realización de este proyecto se tomo como material de apoyo los siguintes repositorios.
  1. Repositorio GIT [`Repositorio de referencia para el proyexto`](https://github.com/hamuchiwa/AutoRCCar/tree/c5776aebff517361fb5473c36fd9918ae90a1a0b) 
  2. Conección de sensor ultrasonico a Raspberry Pi [`sensor ultrasonico con Raspberry Pi`](https://www.raspberrypi-spy.co.uk/2013/01/ultrasonic-distance-measurement-using-python-part-2/) 

  
### Acerca de los Archivos
**test/**  
  &emsp; &emsp; `rc_control_test.py`: Controla los motores por medio de la GPIO de la Raspberry Pi  
  &emsp; &emsp;  `stream_server_test.py`: transmisión de video desde Pi a la computadora
  &emsp; &emsp;  `ultrasonic_server_test.py`: transmisión de datos del sensor desde Pi a la computadora
  &emsp; &emsp;  **model_train_test/**  
      &emsp; &emsp;  &emsp; &emsp; `data_test.npz`: datos de muestra  
      &emsp; &emsp;  &emsp; &emsp; `train_predict_test.ipynb`: un cuaderno jupyter que pasa por el modelo de red neuronal en OpenCV  
  
**raspberryPi3B+/**    
  &emsp; &emsp;  `stream_client.py`:        transmite cuadros de video en formato jpeg a la computadora host  
  &emsp; &emsp;  `ultrasonicController.py`:    envía datos de distancia medidos por el sensor a la computadora host  
  &emsp; &emsp;  `motorController.py`:    librería creada para el control de los motors por medio de la GPIO
  &emsp; &emsp;  `socketMotores.py`:    socket server que recibe las señales enviadas por la computadora para accionar los motores.
  
**computer/**    
  &emsp; &emsp;  **cascade_xml/**  
      &emsp; &emsp;  &emsp; &emsp;  clasificadores en cascada entrenados  
  &emsp; &emsp;  **chess_board/**   
      &emsp; &emsp;  &emsp; &emsp;  imágenes para calibración, capturadas por cámara pi  
      
  &emsp; &emsp;  `picam_calibration.py`:     calibración de cámara pi  
  &emsp; &emsp;  `collect_training_data.py`: recopile imágenes en escala de grises, datos guardados como `*.npz`  
  &emsp; &emsp;  `model.py`:                 modelo de red neuronal  
  &emsp; &emsp;  `model_training.py`:        entrenamiento y validación de modelos  
  &emsp; &emsp;  `rc_driver_helper.py`:      clases/funciones auxiliares para `rc_driver.py`  
  &emsp; &emsp;  `rc_driver.py`:             recibir datos de raspberry pi y conducir el automóvil RC según la predicción del modelo  
  &emsp; &emsp;  `rc_driver_nn_only.py`:     simplificado `rc_driver.py` sin detección de objetos  
  
  
**Traffic_signal**  
  &emsp; &emsp;  Bosquejo de la señal de tráfico de aportado por [@geek111](https://github.com/geek1111)

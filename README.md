# **rosbridge**

#  Порядок запуска файлов

Запускаем контейнер с ROS Melodic:
```bash
docker run --name rosbridge -p 9090:9090 -it ros1-melodic-rosbridge /bin/bash
```

Запускаем в контейнере rosbridge:
```bash
roslaunch rosbridge_server rosbridge_websocket.launch

```

Далее открываем еще одно окно терминала и подключаемся к контейнеру:
```bash
docker exec -it rosbridge /bin/bash

```

В контейнере запускаем скрипт для чтения с вебсокета
```bash
source /opt/ros/melodic/setup.bash

python3 rosbridge_subscriber.py

```

На самом компьютере (ROS2 Humble) запускаем скрипт с издателем.
```bash
source /opt/ros/humble/setup.bash

python3 humble_rosbridge_publisher.py

```
А далее, с помощью вебсокета передаем данные с топика на ROS2 в топик на ROS

```bash
source /opt/ros/humble/setup.bash

python3 test.py

```
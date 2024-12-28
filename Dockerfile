FROM ros:melodic-ros-base

# Установка Python 3 и необходимых зависимостей
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-yaml \
    python3-zmq \
 && rm -rf /var/lib/apt/lists/*

# Установка rosbridge и других необходимых пакетов
RUN apt-get update && apt-get install -y \
    ros-melodic-rosbridge-server \
    && rm -rf /var/lib/apt/lists/*

# Установка websocket-client, PyZMQ, PyYAML и rospkg через pip3
RUN pip3 install websocket-client pyzmq PyYAML rospkg

# Копирование вашего скрипта в контейнер
COPY rosbridge_subscriber.py /rosbridge_subscriber.py

# Сделать скрипт исполняемым
RUN chmod +x /rosbridge_subscriber.py

# Опционально: Активация среды ROS при запуске контейнера
CMD ["/bin/bash"]

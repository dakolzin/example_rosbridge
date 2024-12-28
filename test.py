import websocket
import json
import time
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class LocalSubscriber(Node):
    def __init__(self, ws):
        super().__init__('local_subscriber')
        self.ws = ws
        self.subscription = self.create_subscription(
            String,
            'greeting',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        # Когда получаем сообщение, отправляем его через WebSocket
        pub_message = {
            "op": "publish",
            "topic": "/greeting",
            "msg": {
                "data": msg.data
            }
        }
        self.ws.send(json.dumps(pub_message))
        print(f"Sent message to /greeting via WebSocket: {msg.data}")

def on_open(ws):
    print("Connection opened")

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws_address = "ws://localhost:9090"
    ws = websocket.WebSocketApp(ws_address,
                                on_open=on_open)

    # Инициализируем ROS 2
    rclpy.init()
    local_subscriber = LocalSubscriber(ws)

    # Запускаем WebSocket в отдельном потоке
    import threading
    ws_thread = threading.Thread(target=ws.run_forever)
    ws_thread.start()

    # Запускаем ROS 2 спиннер
    try:
        rclpy.spin(local_subscriber)
    except KeyboardInterrupt:
        pass
    finally:
        # Очистка при закрытии
        local_subscriber.destroy_node()
        rclpy.shutdown()
        ws.close()

    # Дождаться завершения работы WebSocket
    ws_thread.join()

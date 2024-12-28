import rospy
from std_msgs.msg import String
import websocket
import json
import threading

def on_message(ws, message):
    print("Received WebSocket message:", message)
    data = json.loads(message)
    if 'msg' in data:
        rospy.loginfo("Received message from ROS 2: %s", data['msg']['data'])
    else:
        rospy.logwarn("Received message without 'msg' field")

def on_error(ws, error):
    rospy.logerr("Error: %s", error)

def on_close(ws):
    rospy.loginfo("### closed ###")

def on_open(ws):
    def run(*args):
        subscribe_message = {
            "op": "subscribe",
            "topic": "/greeting",
            "type": "std_msgs/String"
        }
        ws.send(json.dumps(subscribe_message))
    threading.Thread(target=run).start()

if __name__ == "__main__":
    rospy.init_node('ros1_websocket_client')
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:9090",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
